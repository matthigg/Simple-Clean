document.addEventListener('DOMContentLoaded', () => {

  const navbar = document.querySelector('.navbar');
  const navbar_brand = document.querySelector('.navbar-brand');
  const navbar_offsetTop_initial = navbar.offsetTop;

  window.addEventListener('scroll', () => {
    if (window.scrollY > navbar_offsetTop_initial) {
      navbar.classList.add('navbar-minimized-true');
      navbar.classList.remove('navbar-minimized-false');

      // navbar_brand.style.fontSize = '2vw';
    } else {
      navbar.classList.add('navbar-minimized-false');
      navbar.classList.remove('navbar-minimized-true');

      // navbar_brand.style.fontSize = '3vw';
    }
  })
})