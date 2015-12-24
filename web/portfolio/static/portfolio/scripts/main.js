'use strict';

var submenu = document.getElementsByClassName('js-submenu')[0];

function activeMenuHandler(event) {
    event.stopPropagation();
    event.preventDefault();
    submenu.classList.toggle('open');
}


submenu.addEventListener('click', activeMenuHandler);
