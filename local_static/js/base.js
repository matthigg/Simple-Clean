document.addEventListener('DOMContentLoaded', () => {

  const navbar = document.querySelector('.navbar');
  const navbar_offsetTop_initial = navbar.offsetTop;
  const navbar_stripe = document.querySelector('.navbar-stripe')

  window.addEventListener('scroll', () => {
    if (window.scrollY > navbar_offsetTop_initial) {
      navbar.classList.add('navbar-minimized-true');
      navbar.classList.remove('navbar-minimized-false');
      navbar_stripe.classList.add('navbar-stripe-minimized-true');
      navbar_stripe.classList.remove('navbar-stripe-minimized-false');
    } else {
      navbar.classList.add('navbar-minimized-false');
      navbar.classList.remove('navbar-minimized-true');
      navbar_stripe.classList.add('navbar-stripe-minimized-false');
      navbar_stripe.classList.remove('navbar-stripe-minimized-true');
    }
  })
})