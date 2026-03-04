// Navigation: mobile menu toggle, products dropdown, sticky header
document.addEventListener('DOMContentLoaded', function() {
  // Mobile menu toggle
  var menuBtn = document.getElementById('mobile-menu-btn');
  var mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', function() {
      mobileMenu.classList.toggle('hidden');
      var expanded = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', !expanded);
    });
  }

  // Products dropdown (desktop)
  var dropdownBtn = document.getElementById('products-dropdown-btn');
  var dropdownMenu = document.getElementById('products-dropdown');
  if (dropdownBtn && dropdownMenu) {
    dropdownBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      dropdownMenu.classList.toggle('hidden');
    });
    // Close dropdown when clicking outside
    document.addEventListener('click', function(e) {
      if (!dropdownBtn.contains(e.target) && !dropdownMenu.contains(e.target)) {
        dropdownMenu.classList.add('hidden');
      }
    });
  }

  // Mobile products accordion
  var mobileProductsBtn = document.getElementById('mobile-products-btn');
  var mobileProductsMenu = document.getElementById('mobile-products-menu');
  if (mobileProductsBtn && mobileProductsMenu) {
    mobileProductsBtn.addEventListener('click', function() {
      mobileProductsMenu.classList.toggle('hidden');
      var arrow = mobileProductsBtn.querySelector('.dropdown-arrow');
      if (arrow) arrow.classList.toggle('rotate-180');
    });
  }

  // Close mobile menu on link click
  if (mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        mobileMenu.classList.add('hidden');
        if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }
});
