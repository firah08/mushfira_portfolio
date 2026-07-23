/* ── NAVBAR SCROLL EFFECT ──────────────────────────────────────────────────── */
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
  if (window.scrollY > 40) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
}, { passive: true });

/* ── MOBILE MENU TOGGLE ────────────────────────────────────────────────────── */
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  mobileMenu.classList.toggle('open');
});

// Close mobile menu on link click
mobileMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('open');
    mobileMenu.classList.remove('open');
  });
});

/* ── SMOOTH SCROLL ─────────────────────────────────────────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));

    if (target) {
      e.preventDefault();
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

/* ── CARD HOVER LIFT ───────────────────────────────────────────────────────── */

/* ── INTERSECTION OBSERVER: fade-in on scroll ──────────────────────────────── */
const observerOptions = {
  threshold: 0.12,
  rootMargin: '0px 0px -40px 0px',
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.card, .event-card, .role-card').forEach((el, i) => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(18px)';
  el.style.transition = `opacity 0.55s ease ${i * 60}ms, transform 0.55s ease ${i * 60}ms`;
  observer.observe(el);
});

/* ── ACTIVE NAV LINK HIGHLIGHT ─────────────────────────────────────────────── */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a, .mobile-menu a[href^="#"]');

const activeSectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          link.style.color = '';

          if (link.getAttribute('href') === `#${entry.target.id}`) {
            link.style.color = 'var(--gold)';
          }
        });
      }
    });
  },
  { threshold: 0.4 }
);

sections.forEach(section => activeSectionObserver.observe(section));

/* ── ABOUT CAROUSEL ────────────────────────────────────────────────────────── */

const slides = document.querySelectorAll('.slide');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

if (slides.length > 0) {

  let currentSlide = 0;

  function showSlide(index) {

    slides.forEach(slide => slide.classList.remove('active'));

    if (index >= slides.length) {
      currentSlide = 0;
    } else if (index < 0) {
      currentSlide = slides.length - 1;
    } else {
      currentSlide = index;
    }

    slides[currentSlide].classList.add('active');
  }

  nextBtn.addEventListener('click', () => {
    showSlide(currentSlide + 1);
  });

  prevBtn.addEventListener('click', () => {
    showSlide(currentSlide - 1);
  });

  // Auto slide every 7 seconds
  setInterval(() => {
    showSlide(currentSlide + 1);
  }, 70000);

}

/* ── CURRENT YEAR ──────────────────────────────────────────────────────────── */
const yearEl = document.getElementById('year');

if (yearEl) {
  yearEl.textContent = new Date().getFullYear();
}