'use strict';

var submenu = document.getElementsByClassName('js-submenu')[0],
    resumeSections = document.getElementsByClassName('js-resume-section-headline');

submenu.addEventListener('touchend', activeMenuHandler);
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
    event.target.parentNode.classList.toggle('is-closed');
}

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-73903165-1', 'auto');
ga('send', 'pageview');
