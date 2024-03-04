document.addEventListener('DOMContentLoaded', function () {

//promo slider
let slider = tns({
    container: '.promo__slider',
    items: 1,
    slideBy: 'page',
    autoplay: true,//отключил autoplay
    controls: false,//выключил родные кнопки
    nav: true,//навигация выкл
    autoplayButton: false,
    autoplayButtonContainer: false,
    autoplayButtonOutput: false,
    touch: true,
    mouseDrag: true,
    swipeAngle: true
  });
//settings of nav

  let touched = false;
  const buttons = document.querySelectorAll(`[data-nav]`);
  buttons.forEach((item)=>{
    item.addEventListener('click', ()=>{
      setTimeout(()=>{
        slider.play(), 1500
      })
    })
  })

  //slider recomended

let sliderRec = tns({
    container: '.products-slider__recomended',
    items: 5,
    slideBy: 'page',
    autoplay: false,//отключил autoplay
    controls: false,//выключил родные кнопки
    nav: false,//навигация выкл
    arrowKeys:true,
    controlsContainer: '#Controls-rec',
    prevButton: '.rec-previous',
    nextButton: '.rec-next',
    autoplayButton: false,
    autoplayButtonContainer: false,
    autoplayButtonOutput: false,
    touch: true,
    mouseDrag: true,
    swipeAngle: true,
    responsive: {
      1: {
          edgePadding: 0,
          gutter: 0,
          items: 1,
          mouseDrag: true
      },
      700: {
          gutter: 0,
          items: 2,
          mouseDrag: true
      },
      900: {
        items: 4,
        mouseDrag: true
    }
  }
});

function arrows (slider,prev,next) {
  // Навешиваем событие на кнопку "Предыдущий слайд"
document.querySelector(prev).addEventListener('click', () => {
  slider.goTo('prev');
});

// Навешиваем событие на кнопку "Следующий слайд"
document.querySelector(next).addEventListener('click', () => {
  slider.goTo('next');
});
  
}

arrows(sliderRec,'.rec-previous','.rec-next');

// slider new
let sliderNew = tns({
  container: '.products-slider__new ',
  items: 5,
  slideBy: 'page',
  autoplay: false,//отключил autoplay
  controls: false,//выключил родные кнопки
  nav: false,//навигация выкл
  arrowKeys:true,
  controlsContainer: '#Controls-new',
  prevButton: '.new-previous',
  nextButton: '.new-next',
  autoplayButton: false,
  autoplayButtonContainer: false,
  autoplayButtonOutput: false,
  touch: true,
  mouseDrag: true,
  swipeAngle: true,
  responsive: {
    1: {
        edgePadding: 0,
        gutter: 0,
        items: 1,
        mouseDrag: true
    },
    700: {
        gutter: 0,
        items: 2,
        mouseDrag: true
    },
    900: {
      items: 4,
      mouseDrag: true
  }
}
});
arrows(sliderNew,'.new-previous','.new-next');

//slider saleon
let sliderSaleon = tns({
  container: '.products-slider__saleon',
  items: 5,
  slideBy: 'page',
  autoplay: false,//отключил autoplay
  controls: false,//выключил родные кнопки
  nav: false,//навигация выкл
  arrowKeys:true,
  controlsContainer: '#Controls-saleon',
  prevButton: '.saleon-previous',
  nextButton: '.saleon-next',
  autoplayButton: false,
  autoplayButtonContainer: false,
  autoplayButtonOutput: false,
  touch: true,
  mouseDrag: true,
  swipeAngle: true,
  responsive: {
    1: {
        edgePadding: 0,
        gutter: 0,
        items: 1,
        mouseDrag: true
    },
    700: {
      gutter: 0,
      items: 2,
      mouseDrag: true
  },
  900: {
    items: 4,
    mouseDrag: true
}
}
});


arrows(sliderSaleon,'.saleon-previous','.saleon-next');
//slider actions
//slider saleon
let sliderActions = tns({
  container: '.actions__slider',
  items: 4,
  slideBy: 'page',
  autoplay: false,//отключил autoplay
  controls: false,//выключил родные кнопки
  nav: false,//навигация выкл
  arrowKeys:true,
  controlsContainer: '#Controls-action',
  prevButton: '.action-previous',
  nextButton: '.action-next',
  autoplayButton: false,
  autoplayButtonContainer: false,
  autoplayButtonOutput: false,
  touch: true,
  mouseDrag: true,
  swipeAngle: true,
  responsive: {
    1: {
        edgePadding: 0,
        gutter: 0,
        items: 4,
        mouseDrag: true
    },
    300: {
      gutter: 0,
      mouseDrag: true,
      items:1
  },
    400: {
      gutter: 0,
      mouseDrag: true,
      items:1
  },
    500: {
      gutter: 0,
      mouseDrag: true,
      items:1
  },
    600: {
      gutter: 0,
      mouseDrag: true,
      items:1
  },
    700: {
        gutter: 0,
        mouseDrag: true,
        items:1
    },
    900: {
      items: 4,
      mouseDrag: true
  }
}
});

arrows(sliderActions,'.action-previous','.action-next');
//сокращение названий у товара
if(document.querySelectorAll('.products__item-title')) {
  document.querySelectorAll('.products__item-title').forEach((item)=>{
    if (item.textContent.length>13) {
      item.textContent= item.textContent.slice(0,13) + '...';
    }
    console.log('eee')
  })
}
//сокращение дат и описаний
if(document.querySelectorAll('.actions__item-title')) {
  document.querySelectorAll('.actions__item-title').forEach((item)=>{
    if (item.textContent.length>26) {
      item.textContent= item.textContent.slice(0, 26) + '...';
    }
  })
}

if(document.querySelectorAll('.actions__item-descr')) {
  document.querySelectorAll('.actions__item-descr').forEach((item)=>{
    if (item.textContent.length>78) {
      item.textContent= item.textContent.slice(0, 78) + '...';
    }
  })
}



//табы

const tabs = document.querySelector('.products-promo__titles').querySelectorAll('li');
const  tabsContent= document.querySelector('.products-promo__wrapper').querySelectorAll('.tabs_content');
console.log(tabsContent);
tabs.forEach((tab,i)=>{
  tab.addEventListener('click', ()=>{
    tabs.forEach(item=>item.classList.remove('active'))
    tab.classList.add('active');
    console.log(i);
    tabsContent.forEach(content=>content.classList.remove('tabs_content-active'));
    tabsContent[i].classList.add('tabs_content-active')
  })
})


//переход по странице
const headerMenu = document.querySelector('.header__menu').querySelectorAll('a');
const footerMenu = document.querySelector('#footer-contacts').querySelectorAll('a');
const actionBlock = document.querySelector('#actions');
const catalogBlock = document.querySelector('#catalog');
const aboutBlock = document.querySelector('#about');
const contactsBlock = document.querySelector('#contacts');


console.log(window.location.href)

headerMenu.forEach((item,i)=>{
  console.log(item.getAttribute('href'));
  if (window.location.href === item.href && item.getAttribute('href') == '#catalog') {
      catalogBlock.scrollIntoView({ behavior: 'smooth' });
  }
  if (window.location.href === item.href && item.getAttribute('href') == '#actions') {
    actionBlock.scrollIntoView({ behavior: 'smooth' });
  }
  if (window.location.href === item.href && item.getAttribute('href') == '#about') {
    aboutBlock.scrollIntoView({ behavior: 'smooth' });
  }
  if (window.location.href === item.href && item.getAttribute('href') == '#contacts') {
    contactsBlock.scrollIntoView({ behavior: 'smooth' });
  }
});

footerMenu.forEach((item,i)=>{
  console.log(item.getAttribute('href'));
  if (window.location.href === item.href && item.getAttribute('href') == '#catalog') {
      catalogBlock.scrollIntoView({ behavior: 'smooth' });
  }
  if (window.location.href === item.href && item.getAttribute('href') == '#actions') {
    actionBlock.scrollIntoView({ behavior: 'smooth' });
  }
  if (window.location.href === item.href && item.getAttribute('href') == '#about') {
    aboutBlock.scrollIntoView({ behavior: 'smooth' });
  }
  if (window.location.href === item.href && item.getAttribute('href') == '#contacts') {
    contactsBlock.scrollIntoView({ behavior: 'smooth' });
  }
})


});