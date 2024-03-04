const anchors = document.querySelectorAll('a[href*="#"]')
for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()
    
    const blockID = anchor.getAttribute('href').substr(1)
    
    document.getElementById(blockID).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  })
}

new WOW().init();
const headerMenu = document.querySelector('.header__menu').querySelectorAll('a');
const footerMenu = document.querySelector('#footer-contacts').querySelectorAll('a');
if (document.querySelector('.offers__item')) {
  console.log(headerMenu);
} else {
  for (let i = 0; i < headerMenu.length; i++) {
    headerMenu[i].setAttribute('href', '/' + headerMenu[i].getAttribute('href'));
    headerMenu[i].setAttribute('target', '_blank');
    headerMenu[i].addEventListener('click', function(event) {
      event.preventDefault();
      history.pushState(null, null, `/`);
      
      history.pushState(null, null, `${headerMenu[i].href}`);
      location.reload();

      if (window.location.hash === headerMenu[i].href) {
        const catalogElement = document.querySelector(headerMenu[i].href);
        console.log(catalogElement)
        if (catalogElement) {
          catalogElement.scrollIntoView({ behavior: 'smooth' });
        }
      }
      

    });
  }
  
  for (let i = 0; i < footerMenu.length; i++) {
    footerMenu[i].setAttribute('href', '/' + footerMenu[i].getAttribute('href'));
    footerMenu[i].setAttribute('target', '_blank');
    footerMenu[i].addEventListener('click', function(event) {
      event.preventDefault();
      history.pushState(null, null, `/`);
      
      history.pushState(null, null, `${footerMenu[i].href}`);
      location.reload();
    });
  }

}