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
    // ICON
    themeToggle.classList.remove('fa-sun');
    themeToggle.classList.add('fa-moon');
    // ICON COLOR
    themeToggle.classList.remove('text-secondary-emphasis');
    themeToggle.classList.add('text-warning');
  } else {
    bodyTag.setAttribute('data-bs-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    // ICON
    themeToggle.classList.remove('fa-moon');
    themeToggle.classList.add('fa-sun');
    // ICON COLOR
    themeToggle.classList.remove('text-warning');
    themeToggle.classList.add('text-secondary-emphasis');

  }
});


/*=================================*\
 * VIEWER / UPLOADER TOGGLE BUTTON * -> [DEPRECATED]
\*=================================*/

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

// document.addEventListener('DOMContentLoaded', toggleAnswerBlock);



/*=============================*\
 * SPLIT SCREEN SELECTION MODE *
\*=============================*/

function splitscreenSelectMode() {
  const uploaderMode = document.getElementById('uploaderMode');
  // INSIDE MODAL
  const viewModeButton = document.getElementById('viewMode');
  const uploadModeButton = document.getElementById('uploadMode');
  // ON NAVBAR
  const showButton = document.getElementById('showButton');
  const hideButton = document.getElementById('hideButton');

  // Check if the uploaderMode was previously hidden
  let isHidden = localStorage.getItem('isHidden');

  // Default Mode [true=Viewer, false=Uploader]
  if (isHidden === null) {
    isHidden = 'true';
  }

  function updateUploaderModeVisibility(hidden) {
    if (hidden === 'true') {
      // console.log("Hidden")
      localStorage.setItem('isHidden', 'true');
      if (uploaderMode) {
        uploaderMode.style.display = 'none';
      }
      showButton.style.display = 'inline-block';
      hideButton.style.display = 'none';
    } else {
      // console.log("Not Hidden")
      localStorage.setItem('isHidden', 'false');
      if (uploaderMode) {
        uploaderMode.style.display = 'block';
      }
      showButton.style.display = 'none';
      hideButton.style.display = 'inline-block';
    }
  }

  // Initialize visibility based on local storage
  updateUploaderModeVisibility(isHidden);

  viewModeButton.addEventListener('click', function() {
    updateUploaderModeVisibility('true');
  });

  uploadModeButton.addEventListener('click', function() {
    updateUploaderModeVisibility('false');
  });
}

document.addEventListener('DOMContentLoaded', splitscreenSelectMode);
