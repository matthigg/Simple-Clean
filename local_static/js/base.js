document.addEventListener('DOMContentLoaded', () => {

  const navbar = document.querySelector('.navbar');
  const navbar_stripe_wrapper= document.querySelector('.navbar-stripe-wrapper');
  const navbar_stripe = document.querySelector('.navbar-stripe');
  const navbar_stripe_text = document.querySelector('.navbar-stripe-text');
  const navbar_free_quote = document.querySelector('.navbar-free-quote');
  const navbar_offsetTop_initial = navbar.offsetTop;

  window.addEventListener('scroll', () => {
    if (window.scrollY > navbar_offsetTop_initial) {

      // "Minimize" the navbar
      navbar.classList.add('navbar-minimized-true');
      navbar.classList.remove('navbar-minimized-false');

      // Minimize the navbar stripe wrapper
      navbar_stripe_wrapper.classList.add('navbar-stripe-minimized-true');
      navbar_stripe_wrapper.classList.remove('navbar-stripe-minimized-false');
      
      // Minimize the navbar stripe
      navbar_stripe.classList.add('navbar-stripe-minimized-true');
      // navbar_stripe.classList.remove('navbar-stripe-minimized-false');
      
      // Minimize the navbar stripe text
      navbar_stripe_text.classList.add('navbar-stripe-minimized-true');
      // navbar_stripe_text.classList.remove('navbar-stripe-minimized-false');

      // "Minimize" the 'free quote' button
      navbar_free_quote.classList.add('navbar-free-quote-minimized-true');
      navbar_free_quote.classList.remove('navbar-free-quote-minimized-false');
    } else {

      // "Maximize" the navbar
      navbar.classList.add('navbar-minimized-false');
      navbar.classList.remove('navbar-minimized-true');

      // Maximize the navbar stripe wrapper
      navbar_stripe_wrapper.classList.add('navbar-stripe-minimized-false');
      navbar_stripe_wrapper.classList.remove('navbar-stripe-minimized-true');
      
      // Maximize the navbar stripe
      // navbar_stripe.classList.add('navbar-stripe-minimized-false');
      navbar_stripe.classList.remove('navbar-stripe-minimized-true');
      
      // Maximize the navbar stripe text
      // navbar_stripe_text.classList.add('navbar-stripe-minimized-false');
      navbar_stripe_text.classList.remove('navbar-stripe-minimized-true');

      // "Maximize" the 'free quote' button
      navbar_free_quote.classList.add('navbar-free-quote-minimized-false');
      navbar_free_quote.classList.remove('navbar-free-quote-minimized-true');
    }
  })

  // Assign the .active class to the current page's nav-link
  if (document.querySelector('.container-fluid').classList.contains('index-page')) {
    document.querySelector('.nav-link-home').classList.add('active');
  } else if (document.querySelector('.container-fluid').classList.contains('services-page')) {
    document.querySelector('.nav-link-services').classList.add('active');
  } else if (document.querySelector('.container-fluid').classList.contains('work-page')) {
    document.querySelector('.nav-link-work').classList.add('active');
  } else if (document.querySelector('.container-fluid').classList.contains('reviews-page')) {
    document.querySelector('.nav-link-reviews').classList.add('active');
  } else if (document.querySelector('.container-fluid').classList.contains('contact-page')) {
    document.querySelector('.nav-link-contact').classList.add('active');
  }
})