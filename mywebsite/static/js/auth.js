const loginForm  = document.getElementById('member-login');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const username = loginForm.elements['username-login'].value;
    const password = loginForm.elements['password-login'].value;

    $.post('/ingresar/', {username: username, password: password})
    .done(() => {
            $("#login-error-message").css({display: 'none'});
            window.location.reload();
        })
    .fail(() => {
            $("#login-error-message").css({display: 'inline'});
            console.log('Noooo!');
        })

});

const logoutButton  = document.getElementById('member-logout');

logoutButton.addEventListener('click', (e) => {

    console.log(e);

    e.preventDefault();

    $.post('/salir/', {})
    .done(() => {
            window.location.reload();
        })
    .fail(() => {
            console.log('Hubo un error!');
        })

})