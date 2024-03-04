const minus = document.querySelector('.minus'),
      plus = document.querySelector('.plus'),
      valueHTML = document.querySelector('.counter');
let num = +valueHTML.value;

minus.addEventListener('click', ()=>{
    if(num==1) {
        return num;
    } else {
        num--;
    }
    valueHTML.value = num;
})

plus.addEventListener('click', ()=>{
    num++;

    valueHTML.value = num;
})

valueHTML.addEventListener('input', ()=>{
    if(valueHTML.value<1) {
        valueHTML.value = valueHTML.value.slice(1,valueHTML.length)
    }

})


//слайдер
let productPhoto = tns({
    "container": "#customize",
    "items": 1,
    "controlsContainer": "#customize-controls",
    "navContainer": "#customize-thumbnails",
    "navAsThumbnails": true,
    "autoplay": false,
    "autoplayButton": "#customize-toggle",
    controls: false,//выключил родные кнопки
    nav: true,//навигация выкл
    autoplayButtonContainer: false,
    autoplayButtonOutput: false,
    touch: true,
    mouseDrag: true,
    swipeAngle: true
});


const feedbacks = document.querySelectorAll('.product__feedbacks-person');
console.log(feedbacks.length);
if (feedbacks.length<1) {
    document.querySelector('.message').style.display = 'block';
}