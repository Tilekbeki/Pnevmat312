const tabs = document.querySelector('.profile__tabs').querySelector('ul').querySelectorAll('li');
const  tabsContent= document.querySelectorAll('.profile__tab-content');
console.log(tabsContent);
tabs.forEach((tab,i)=>{
  tab.addEventListener('click', ()=>{
    tabs.forEach(item=>item.classList.remove('active'))
    tab.classList.add('active');
    console.log(i);
    tabsContent.forEach(content=>content.classList.remove('profile__tab-content_active'));
    tabsContent[i].classList.add('profile__tab-content_active')
  })
})

const ordersBtn = document.querySelectorAll('.profile__order-more');

ordersBtn.forEach((item)=>{
  item.addEventListener('click', ()=>{
    const detailElement = item.parentElement.parentElement.querySelector('.profile__order-details');
    detailElement.classList.toggle('profile__order-details_active')
  })
})


