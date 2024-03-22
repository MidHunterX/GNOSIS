/*================*\
 * THEME SWITCHER *
\*================*/

const themeToggle = document.getElementById('themeToggle');
const htmlTag = document.querySelector('html');
const currentTheme = localStorage.getItem('theme') || 'light';

if (currentTheme === 'dark') {
    htmlTag.setAttribute('data-bs-theme', 'dark');
    themeToggle.classList.add('fa-sun');
} else {
    htmlTag.setAttribute('data-bs-theme', 'light');
    themeToggle.classList.add('fa-moon');
}

themeToggle.addEventListener('click', function() {
    const currentTheme = htmlTag.getAttribute('data-bs-theme');

    if (currentTheme === 'dark') {
        htmlTag.setAttribute('data-bs-theme', 'light');
        localStorage.setItem('theme', 'light');
        themeToggle.classList.remove('fa-sun');
        themeToggle.classList.add('fa-moon');
    } else {
        htmlTag.setAttribute('data-bs-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        themeToggle.classList.remove('fa-moon');
        themeToggle.classList.add('fa-sun');
    }
});
