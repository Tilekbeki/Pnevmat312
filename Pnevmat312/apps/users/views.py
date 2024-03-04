from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from orders.models import Order, Cart

def profile(request):
    prof = Profile.objects.get(profile=request.user)
    orders = Order.objects.all()
    carts = []
    for order in orders:
            carts += Cart.objects.filter(id_order=order)
    if request.method == 'POST':
        if 'change_button' in request.POST:
            form = ChangeUserProfileForm(request.POST)
            if request.user.check_password(request.POST.get('password')):
                if request.POST.get('password_new') == request.POST.get('password_again'):
                    prof.profile.set_password(request.POST.get('password_new'))
                    prof.profile.save()
                    login(request, prof.profile)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Ошибка нового пароля')
            else:
                return HttpResponse('Ошибка старого пароля')

    initial_dict = {
        'username': request.user.username,
        'email': request.user.email
    }
    form = ChangeUserProfileForm(initial=initial_dict)
    return render(request, 'profile.html', {'form': form,'carts': carts, 'orders': orders, 'profile': prof})


def render_page(request, form_registration=UserForm(), form_authentication=UserLoginForm()):
    return render(request, 'auth.html', {'form_registration': form_registration,
                                         'form_authentication': form_authentication})

def chekmessage(request):
    return HttpResponse('Операция прошла успешно, проверьте почту')

def home(request):
    return HttpResponseRedirect('/')
def successmessage(request):
    return HttpResponse('Операция прошла успешно, зайдите под новым паролем')
def registration(request, form):
    def update_user_data(user):  # Создать профиль по user
        Profile.objects.update_or_create(profile=user)

    if form.is_valid():
        get_email = form.cleaned_data.get('email')
        get_user_emails = User.objects.values_list('email', flat=True)
        if get_email not in get_user_emails:
            user = form.save()
            user.refresh_from_db()
            user.save()
            update_user_data(user)
            login(request, user)
        else:
            form.add_error(None, "Такой пользователь уже существует")
            return render_page(request, form_registration=form)
        return HttpResponseRedirect("/")
    else:
        form.add_error(None, "Неверно введены данные (проверьте правильность введенного пароля)")
        return render_page(request, form_registration=form)


def authentication(request, form):  # Аутенфикация
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        try:
            login(request, user)
        except AttributeError:
            form.add_error(None, "Неверный пароль")
            return render_page(request, form_authentication=form)
        return HttpResponseRedirect('/')
    else:
        form.add_error(None, 'Неверно введены данные')
        return render_page(request, form_authentication=form)


def auth(request):
    if request.method == 'POST':
        if 'registration_button' in request.POST:
            form_registration = UserForm(request.POST)
            return registration(request, form_registration)
        if 'authentication_button' in request.POST:
            form_authentication = UserLoginForm(request.POST)
            return authentication(request, form_authentication)
    else:
        return render_page(request)

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')



class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'system/email/user_password_reset.html'
    success_url = reverse_lazy('chekmessage')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'system/email/password_subject_reset_mail.txt'
    email_template_name = 'system/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'system/email/user_password_set_new.html'
    success_url = reverse_lazy('successmessage')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'
               
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete_order()
    return HttpResponseRedirect('/user/profile/')