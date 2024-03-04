$('input[name=address]').mask("+996-(999)-999-999");

const inputOrders = $('.order__input');

inputOrders.each(function() {
    const value = $(this).val().trim();
    if (value === '') {
      console.log('Пустая');
      $('.order__items').css('display', 'none');
      $('.message').css('display', 'block');
    } else {
        console.log('что-то есть');
    }
  });