//Scroll navbar

window.addEventListener('scroll', function () {
    const nav = document.getElementById('mainNavbar');
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  });


document.querySelectorAll('.capital-card-1').forEach(card => {
    card.addEventListener('mouseenter', function() {
        const tab = new bootstrap.Tab(this);
        tab.show();
    });
});