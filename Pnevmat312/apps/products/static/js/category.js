const products = document.querySelectorAll('.products__item');
const showMoreBtn = document.querySelector('.showMore');
const filtBtn = document.querySelector('.category__search-btn');
function warning(){
  const products = document.querySelectorAll('.products__item');
  const wrapper = document.querySelector('.category__products-list');
  if (products.length < 1) {
    if(!document.querySelector('.warning')) {
      let div = document.createElement('div');
      div.className = "warning";
      div.innerHTML=`
          <h1>Таких товаров еще нет, но это временно!</h1>
      `
      wrapper.append(div);
    } 
  }else {
    document.querySelector('.warning').remove();

  }
}

// Скрываем все товары при загрузке страницы
products.forEach(product => {
  product.style.display = 'none';
});

let visibleProducts = 0;

function showProducts(num) {
  let count = 0;
  
  while (count < num) {
    if (visibleProducts >= products.length) {
      visibleProducts = 0;
    }
    
    products[visibleProducts].style.display = 'block';
    visibleProducts++;
    count++;
  }
}
showMoreBtn.style.display = 'none'
// // Показываем первые 6 товаров
// products.length == 0 || products.length < 6 ? showMoreBtn.style.display = 'none' : showMoreBtn.style.display = 'block'; 
products.length == 0 ? showMoreBtn.style.display = 'none' : showProducts(6); 

setTimeout(warning,1000);

console.log(products.length)
showMoreBtn.addEventListener('click', () => {
  showProducts(visibleProducts+6)
});

//ajax фильтрация и поиск

const formInput = document.querySelector('.category__search').querySelector('form').querySelector('input'),
      searchBtn = document.querySelector('.category__search').querySelector('form').querySelector('button'),
      startPrice = document.querySelector('.fromPrice'),
      endPrice = document.querySelector('.toPrice'),
      categoryName = document.querySelector('.category__title');
let title,fromPrice,toPrice,filtrOption = '';


//функция на сортировку
const selectElement = document.querySelector('select');

function handleSelectChange(event) {
  const selectedValue = event.target.value;
  console.log('Выбрано значение:', selectedValue);
  title = formInput.value;
  fromPrice = startPrice.value ? startPrice.value : 1;
  toPrice = endPrice.value ? endPrice.value : 9999999;
  if(selectedValue == 'high-to-low'){
    const productss = document.querySelectorAll('.products__item')
    productss.forEach((item)=>{
      item.remove();
    });
    const wrapperr = document.querySelector('.category__products-list');
    highToLow=objectProducts.results.sort((a, b) => b.price - a.price);
    highToLow.forEach((item)=>{
      let div = document.createElement('div');
      div.className = "products__item";
      div.innerHTML=`
          <img src="../static/img/product.jpg" alt="product" class="products__item-cover">
          <div class="products__item-title">${item.name}</div>
          <div class="products__item-status">&#10004; в наличии</div>
          <div class="products__item-price">${item.price} сом</div>
          <a href="/products/${item.id}" class="products__item-moreBtn">
              <button>ПОДРОБНЕЕ</button>
          </a>
      `
      wrapperr.append(div);
    // Добавьте здесь свой код для обработки изменения выбранного значения
  });
  setTimeout(warning,1000);
  }
  if(selectedValue == 'low-to-high'){
    
    const productss = document.querySelectorAll('.products__item')
    productss.forEach((item)=>{
      item.remove();
    });
    const wrapperr = document.querySelector('.category__products-list');
    lowToHigh=objectProducts.results.sort((a, b) => a.price - b.price);
    lowToHigh.forEach((item)=>{
      let div = document.createElement('div');
      div.className = "products__item";
      div.innerHTML=`
          <img src="../static/img/product.jpg" alt="product" class="products__item-cover">
          <div class="products__item-title">${item.name}</div>
          <div class="products__item-status">&#10004; в наличии</div>
          <div class="products__item-price">${item.price} сом</div>
          <a href="/products/${item.id}" class="products__item-moreBtn">
              <button>ПОДРОБНЕЕ</button>
          </a>
      `
      wrapperr.append(div);
    // Добавьте здесь свой код для обработки изменения выбранного значения
  });
  setTimeout(warning,1000);
  }
  if (selectedValue === 'recommended') {
    const productss = document.querySelectorAll('.products__item')
    productss.forEach((item)=>{
      item.remove();
    });
    const wrapperr = document.querySelector('.category__products-list');
    recommendED = objectProducts.results.filter(item => item.type === 'RE');
    recommendED.forEach((item)=>{
      let div = document.createElement('div');
      div.className = "products__item";
      div.innerHTML=`
          <img src="../static/img/product.jpg" alt="product" class="products__item-cover">
          <div class="products__item-title">${item.name}</div>
          <div class="products__item-status">&#10004; в наличии</div>
          <div class="products__item-price">${item.price} сом</div>
          <a href="/products/${item.id}" class="products__item-moreBtn">
              <button>ПОДРОБНЕЕ</button>
          </a>
      `
      wrapperr.append(div);
    // Добавьте здесь свой код для обработки изменения выбранного значения
  });
  setTimeout(warning,1000);
  }
  
  if (selectedValue === 'discounted') {
    const productss = document.querySelectorAll('.products__item')
    productss.forEach((item)=>{
      item.remove();
    });
    const wrapperr = document.querySelector('.category__products-list');
    discountED = objectProducts.results.filter(item => item.type === 'SA');
    discountED.forEach((item)=>{
      let div = document.createElement('div');
      div.className = "products__item";
      div.innerHTML=`
          <img src="../static/img/product.jpg" alt="product" class="products__item-cover">
          <div class="products__item-title">${item.name}</div>
          <div class="products__item-status">&#10004; в наличии</div>
          <div class="products__item-price">${item.price} сом</div>
          <a href="/products/${item.id}" class="products__item-moreBtn">
              <button>ПОДРОБНЕЕ</button>
          </a>
      `
      wrapperr.append(div);
    // Добавьте здесь свой код для обработки изменения выбранного значения
  });
  }

  // Сюда код обновления элементов
  //возвращяю все элементы
 
  setTimeout(warning,1000);
}
//ajax

const request = new XMLHttpRequest();


function getInfo(title,fromPrice,toPrice){
  let req = new XMLHttpRequest();
  const url = `/test/?title=${title}&catName=Ножи&fromPrice=${fromPrice}&toPrice=${toPrice}`;
  const selectV = document.querySelector('.category__selection');
  req.open("GET", url);
  req.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
  req.addEventListener("readystatechange", () => {
    if (req.readyState ===4 && req.status === 200) {
      console.log(JSON.parse(req.responseText));
      objectProducts = JSON.parse(req.responseText);
      const wrapper = document.querySelector('.category__products-list');
      // Сюда код обновления элементов
      //возвращяю все элементы
      objectProducts.results.sort((a, b) => a.price - b.price);
      objectProducts.results.forEach((item)=>{
        let div = document.createElement('div');
        div.className = "products__item";
        div.innerHTML=`
            <img src="../static/img/product.jpg" alt="product" class="products__item-cover">
            <div class="products__item-title">${item.name}</div>
            <div class="products__item-status">&#10004; в наличии</div>
            <div class="products__item-price">${item.price} сом</div>
            <a href="/products/${item.id}" class="products__item-moreBtn">
                <button>ПОДРОБНЕЕ</button>
            </a>
        `
        wrapper.append(div)
      });
      selectV.style.display='block';
      selectV.style.opacity='1';
    }

    //удаляю все объекты
    products.forEach((item)=>{
      item.remove();
    });
    

  });
  req.send();
  setTimeout(warning,1000)
}



filtBtn.addEventListener('click', (e)=>{
  const productss = document.querySelectorAll('.products__item')
    productss.forEach((item)=>{
      item.remove();
    });
  title = formInput.value;
  fromPrice = startPrice.value ? startPrice.value : 1;
  toPrice = endPrice.value ? endPrice.value : 9999999;
      

  getInfo(title,fromPrice,toPrice);

  
  e.preventDefault();
})


searchBtn.addEventListener('click', (e)=>{
    const productss = document.querySelectorAll('.products__item')
    productss.forEach((item)=>{
      item.remove();
    });
    title = formInput.value;
    fromPrice = startPrice.value ? startPrice.value : 1;
    toPrice = endPrice.value ? endPrice.value : 9999999;
        

    getInfo(title,fromPrice,toPrice);

    
    e.preventDefault();
    setTimeout(warning,1000)
})
let objectProducts=''

console.log(`${title} - ${fromPrice} - ${toPrice}`);
formInput.addEventListener('keypress', function (e) {
  const productss = document.querySelectorAll('.products__item')
    productss.forEach((item)=>{
      item.remove();
    });
  if (e.key === 'Enter') {
    
    title = formInput.value;
    fromPrice = startPrice.value ? startPrice.value : 1;
    toPrice = endPrice.value ? endPrice.value : 9999999;
        

    getInfo(title,fromPrice,toPrice);

    
    e.preventDefault();
    setTimeout(warning,1000)
  }
});

selectElement.addEventListener('change', handleSelectChange);




