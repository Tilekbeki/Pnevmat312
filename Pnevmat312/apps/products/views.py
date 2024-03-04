from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Q

def action(request, id_action):
    act = Action.objects.get(id=id_action)
    return render(request,'action.html', {'action': act})


def main_page(request):
    products = Product.objects.all()
    images = MainPageSliders.objects.all()
    products_images = list(Sliders.objects.all())
    im = []
    for product in products:
        for img in products_images:
            if (img.id_product==product):
                im.append(img)
                break
    print(im)


    categories = Category.objects.all()
    actions = Action.objects.all()
    return render(request, 'main_page.html', {'products': products, 'im': im,'images': images,
                                              'categories':categories, 'actions': actions})

def category(request):
    category = request.GET.get('category')
    cat = Category.objects.all()
    allcat = cat
    products = Product.objects.all()
    if category is not None and category != '':
        cat = Category.objects.get(name=category)
        products = Product.objects.filter(id_category=cat)
    return render(request, 'category.html', {'category': cat,  'products': products, 'allcat': allcat })

def test(request):
    query_dict = request.GET
    category_name = query_dict.get('catName') 
    product_name = query_dict.get('title')
    min_price = query_dict.get('fromPrice')
    max_price = query_dict.get('toPrice')
    if (min_price and max_price):
        min_price = query_dict.get('fromPrice')
        max_price = query_dict.get('toPrice')
    if (min_price is None or max_price is None or min_price > max_price):
        # Если значения не заданы или min_price > max_price, устанавливаем значения по умолчанию
        min_price = 1
        max_price = 999999
    # получаем объекты категории и товаров, удовлетворяющие заданным условиям
    category = Category.objects.filter(name__icontains=category_name).first()
    products = Product.objects.filter(name__icontains=product_name, id_category=category.id, price__gte=min_price, price__lte=max_price)
    # формируем список результатов
    results = []
    for product in products:
        images = Sliders.objects.filter(id_product=product)
        if images:
            img_url = images[0].image.url
        else:
            img_url = "Нету картинки"
        results.append({
        'id':product.id,
        'name': product.name,
        'price': product.price,
        'img':img_url,
        'type': product.type
        })
            
            

    # возвращаем результаты в виде JSON-ответа
    return JsonResponse({'results': results})

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    images = Sliders.objects.filter(id_product=product)
    feedbacks = FeedBacks.objects.filter(id_product=product)
    properties = Property.objects.all()
    brand = Brand.objects.all()

    avg_rating = []

    for feedback in feedbacks:
        avg_rating.append(feedback.rating)

    try: 
        avg_rating = int(round(sum(avg_rating) / len(avg_rating),1))
    except:
        avg_rating = '-'
    print(images)
    if request.method == 'POST':
        if 'buy_button' in request.POST:
            try:
                Profile = apps.get_model('users.Profile')
                get_profile = Profile.objects.get(profile=request.user)
                quantity = request.POST.get('counter')
                user_order = check_order(request.user)[0]
                Cart = apps.get_model('orders.Cart')
                print(user_order)
                print(Cart)
                print(quantity)
                print(get_profile)
                
                Cart.objects.create(id_order=user_order, id_product=product, quantity=quantity)
            except TypeError:
                print(Profile)
                print('asdasdasds')
                return HttpResponse('Похоже вы не вошли, попробуйте войти или перезагрузить страницу...')
                
            # return HttpResponseRedirect('/orders')
        if  'feedback' in request.POST:
            try:
                Profile = apps.get_model('users.Profile')
                get_profile = Profile.objects.get(profile=request.user)
                description = request.POST.get('description')
                rating = request.POST.get('rating')
                new_feedback = FeedBacks.objects.create(id_user=get_profile, id_product=product, rating=rating, description=description)
                new_feedback.save()
            except TypeError:
                print(Profile)
                print('asdasdasds')
                return HttpResponse('Походу вы не вошли,чтобы оставить коментарий, попробуйте войти или перезагрузить страницу...')
    return render(request, 'product.html', {'product': product, 'images': images, 
    'feedbacks': feedbacks, 'avg_rating': avg_rating, 'properties': properties, 'brand':brand})


def check_order(user):
    Profile = apps.get_model('users.Profile')
    get_profile = Profile.objects.get(profile=user)
    Order = apps.get_model('orders.Order')
    try:
        user_orders = Order.objects.filter(id_user=get_profile, placed=False)
    except ObjectDoesNotExist:
        user_orders = Order.objects.create(id_user=get_profile)

    if not user_orders:
        user_orders = Order.objects.create(id_user=get_profile)
    return user_orders

def fabricators(request):
    fabricators = Brand.objects.all()
    return render(request,'fabricators.html', {'fabricators': fabricators})

def pay(request):
    return render(request, 'pay.html')
def guarantees(request):
    return render(request, 'guarantees.html')