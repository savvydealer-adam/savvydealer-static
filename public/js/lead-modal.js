// Global lead form modal
// Triggered by elements with data-lead-form attribute
document.addEventListener('DOMContentLoaded', function() {
  var modal = document.getElementById('lead-modal');
  if (!modal) return;

  var overlay = modal.querySelector('.modal-overlay');
  var closeBtn = modal.querySelector('.modal-close');

  function openModal() {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }

  // Open triggers
  document.querySelectorAll('[data-lead-form]').forEach(function(el) {
    el.addEventListener('click', function(e) {
      e.preventDefault();
      openModal();
    });
  });

  // Close triggers
  if (overlay) overlay.addEventListener('click', closeModal);
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeModal();
  });
});
