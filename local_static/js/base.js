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

  // Assign the .active class to the current page's nav-link & display the
  // 'Free Quote' button if needed
  if (document.querySelector('.container-fluid').classList.contains('index-page')) {
    document.querySelector('.nav-link-home').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('services-page')) {
    document.querySelector('.nav-link-services').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('ourwork-page')) {
    document.querySelector('.nav-link-ourwork').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('reviews-page')) {
    document.querySelector('.nav-link-reviews').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('contact-page')) {
    document.querySelector('.nav-link-contact').classList.add('active');
  }

  // Modals
  //
  // When a <div> .section-1-baap-group element or any of its children (all of 
  // which are located in ourwork.html and together represent a 'before & after'
  // picture group) are clicked, search/scrounge for the appropriate data-id
  // attribute's value, which identifies that particular 'before & after' picture
  // group. This data-id value is then used to construct the before & after <img>
  // src attributes in the re-usable Bootstrap modal HTML markup located in 
  // ourwork-modals.html. 
  //
  // Additionally, this JavaScript will scrounge for the relative static img path 
  // (ie. /static/img/...) which is stored as data-src in the same HTML element 
  // as the data-id, and the data-src attribute's value, together with the data-id 
  // attribute's value is then used to construct a path to the before & after 
  // images that we're looking for.
  const baap_groups = document.querySelectorAll('.section-1-baap-group');
  baap_groups.forEach((baap_group) => {
    baap_group.addEventListener('click', (event) => {
      let element = event.target;
      if (element.dataset.id === undefined) {
        while (element.parentNode) {
          element = element.parentNode;
          if (element.dataset.id) {
            const img_src_before = element.dataset.src + '/' + element.dataset.id + '-before.jpg';
            const img_src_after = element.dataset.src + '/' + element.dataset.id + '-after.jpg';            
            document.querySelector('.modal-baap-group-img-before').src = img_src_before;
            document.querySelector('.modal-baap-group-img-after').src = img_src_after;
            return
          } 
        }
      } else {
        console.log('element: ', element.dataset.id);
      }
    })
  })  
})