'use strict';

var submenu = document.getElementsByClassName('js-submenu')[0],
    resumeSections = document.getElementsByClassName('js-resume-section-headline');

submenu.addEventListener('click', activeMenuHandler);
for (var i = 0; i < resumeSections.length; i++) {
    resumeSections[i].addEventListener('click', toggleResumeSection);
}

function activeMenuHandler(event) {
    if (event.target.classList.contains('active')) {
        event.stopPropagation();
        event.preventDefault();
        submenu.classList.toggle('open');
    }
}

function toggleResumeSection(event) {
    event.stopPropagation();
    event.preventDefault();
    console.log(event);
    event.target.parentNode.classList.toggle('is-closed');
}
