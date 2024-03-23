/*================*\
 * THEME SWITCHER *
\*================*/

const themeToggle = document.getElementById('themeToggle');
const bodyTag = document.querySelector('body');
const currentTheme = localStorage.getItem('theme') || 'light';

if (currentTheme === 'dark') {
    bodyTag.setAttribute('data-bs-theme', 'dark');
    themeToggle.classList.add('fa-sun');
} else {
    bodyTag.setAttribute('data-bs-theme', 'light');
    themeToggle.classList.add('fa-moon');
}

themeToggle.addEventListener('click', function() {
    const currentTheme = bodyTag.getAttribute('data-bs-theme');

    if (currentTheme === 'dark') {
        bodyTag.setAttribute('data-bs-theme', 'light');
        localStorage.setItem('theme', 'light');
        themeToggle.classList.remove('fa-sun');
        themeToggle.classList.add('fa-moon');
    } else {
        bodyTag.setAttribute('data-bs-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        themeToggle.classList.remove('fa-moon');
        themeToggle.classList.add('fa-sun');
    }
});
