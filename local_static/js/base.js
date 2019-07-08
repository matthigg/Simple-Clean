document.addEventListener('DOMContentLoaded', () => {

  const navbar = document.querySelector('.navbar');
  const navbar_stripe = document.querySelector('.navbar-stripe');
  const navbar_free_quote = document.querySelector('.navbar-free-quote');
  const navbar_offsetTop_initial = navbar.offsetTop;

  window.addEventListener('scroll', () => {
    if (window.scrollY > navbar_offsetTop_initial) {

      // "Minimize" the navbar
      navbar.classList.add('navbar-minimized-true');
      navbar.classList.remove('navbar-minimized-false');

      // Minimize the navbar stripe
      navbar_stripe.classList.add('navbar-stripe-minimized-true');
      navbar_stripe.classList.remove('navbar-stripe-minimized-false');

      // "Minimize" the 'free quote' button
      navbar_free_quote.classList.add('navbar-free-quote-minimized-true');
      navbar_free_quote.classList.remove('navbar-free-quote-minimized-false');
    } else {

      // "Maximize" the navbar
      navbar.classList.add('navbar-minimized-false');
      navbar.classList.remove('navbar-minimized-true');

      // Maximize the navbar stripe
      navbar_stripe.classList.add('navbar-stripe-minimized-false');
      navbar_stripe.classList.remove('navbar-stripe-minimized-true');

      // "Maximize" the 'free quote' button
      navbar_free_quote.classList.add('navbar-free-quote-minimized-false');
      navbar_free_quote.classList.remove('navbar-free-quote-minimized-true');
    }
  })
})