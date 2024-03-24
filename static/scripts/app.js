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


/*========================*\
 * VIEWER / UPLOADER MODE *
\*========================*/

function toggleAnswerBlock() {
  const block = document.getElementById('uploaderMode');
  const showButton = document.getElementById('showButton');
  const hideButton = document.getElementById('hideButton');

  // Check if the block was previously hidden
  let isHidden = localStorage.getItem('isAnswerBlockHidden');
  if (isHidden === null) {
    isHidden = 'true';
  }

  if (isHidden === 'true') {
    if (block) {
      block.style.display = 'none';
    }
    showButton.style.display = 'inline-block';
    hideButton.style.display = 'none';
  } else {
    if (block) {
      block.style.display = 'block';
    }
    showButton.style.display = 'none';
    hideButton.style.display = 'inline-block';
  }

  showButton.addEventListener('click', function() {
    if (block) {
      block.style.display = 'block';
    }
    showButton.style.display = 'none';
    hideButton.style.display = 'inline-block';
    localStorage.setItem('isAnswerBlockHidden', 'false');
  });

  hideButton.addEventListener('click', function() {
    if (block) {
      block.style.display = 'none';
    }
    showButton.style.display = 'inline-block';
    hideButton.style.display = 'none';
    localStorage.setItem('isAnswerBlockHidden', 'true');
  });
}

document.addEventListener('DOMContentLoaded', toggleAnswerBlock);
