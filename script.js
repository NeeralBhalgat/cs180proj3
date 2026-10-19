// Open result images at full resolution.
const viewer = document.querySelector('#viewer');
const viewerImage = viewer.querySelector('img');
const viewerCaption = viewer.querySelector('p');

for (const link of document.querySelectorAll('a.zoom')) {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    viewerImage.src = link.href;
    viewerImage.alt = link.querySelector('img').alt;
    viewerCaption.textContent = link.closest('figure')
      .querySelector('figcaption').textContent;
    viewer.showModal();
  });
}

document.querySelector('#close').addEventListener('click', () => {
  viewer.close();
});

viewer.addEventListener('click', (event) => {
  if (event.target === viewer) viewer.close();
});

// Highlight the section currently visible in the page.
const observer = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    if (!entry.isIntersecting) continue;

    for (const link of document.querySelectorAll('nav a')) {
      const active = link.hash === '#' + entry.target.id;
      link.classList.toggle('active', active);

      if (active) {
        link.setAttribute('aria-current', 'location');
      } else {
        link.removeAttribute('aria-current');
      }
    }
  }
}, {
  rootMargin: '-10% 0px -65% 0px',
});

document.querySelectorAll('section[id]').forEach((section) => {
  observer.observe(section);
});
