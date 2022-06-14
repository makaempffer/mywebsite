var AbrirPopup = document.getElementById('abrir-popup'),
    overlay = document.getElementById('overlay'),
    popup = document.getElementById('popup'),
    btnCerrarPopup = document.getElementById('btn-cerrar-popup');

AbrirPopup.addEventListener('click', function(){
    console.log('!');
    overlay.classList.add('active');
    popup.classList.add('active');
});

btnCerrarPopup.addEventListener('click', function(){
    console.log('!');
    overlay.classList.remove('active');
    popup.classList.remove('active');
});


var AbrirPopupLogin = document.getElementById('abrir-popupLogin'),
    overlayLogin = document.getElementById('iniciarSesion'),
    popupLogin = document.getElementById('popup-login'),
    btnCerrarLogin = document.getElementById('btn-cerrar-login');

AbrirPopupLogin.addEventListener('click', function(){
    console.log('!');
    overlayLogin.classList.add('active');
    popupLogin.classList.add('active');
});

btnCerrarLogin.addEventListener('click', function(){
    console.log('!');
    overlayLogin.classList.remove('active');
    popupLogin.classList.remove('active');
});
