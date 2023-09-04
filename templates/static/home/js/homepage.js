
let formLogin = null;
let formSignin = null;
let signInGroup = null;
let verticalBar = null;
let footerLogo = null;
var askLogin = null;

function login_to_signin() {

    formLogin = document.getElementById('id-login-form');
    formSignin = document.getElementById('id-signin-form');
    signInGroup = document.getElementById('id-signin-group');
    verticalBar = document.getElementById('id-vertical-bar');
    footerLogo = document.getElementById('id-footer-logo');



    if (window.getComputedStyle(formLogin).getPropertyValue('display') === 'block') {
        formLogin.style.display = 'none';
        formSignin.style.display = 'block';
    } else{
        formLogin.style.display = 'block';
        formSignin.style.display = 'none'; 
        console.log('tchau')
    }

    if (formLogin.style.display == 'none') {
        verticalBar.style.height = '700px';
        signInGroup.style.height = '900px';
        footerLogo.style.top = '140px';
    } else {
        verticalBar.style.height = '350px';
        signInGroup.style.height = '550px';
        footerLogo.style.top = '30px';
    }

}

function verifyCheckBox(index) {
    
    console.log(index);
    let sex_checkbox_f = document.getElementById('input-sex-f-signup');
    let sex_checkbox_m = document.getElementById('input-sex-m-signup');
    let sex_checkbox_o = document.getElementById('input-sex-o-signup');

    if (index == 1) {
        sex_checkbox_m.checked = false;
        sex_checkbox_o.checked = false;
    }

    if (index == 2) {
        sex_checkbox_f.checked = false;
        sex_checkbox_o.checked = false;
    } 

    if (index == 3) {
        sex_checkbox_f.checked = false;
        sex_checkbox_m.checked = false;
    }

}

function verifyPersonalInfo() {
    let input_name_signup = document.getElementById('input-name-signup');
    let input_email_sigup = document.getElementById('input-email-signup');
    let input_password_sigup = document.getElementById('input_password_sigup');
    let input_confirm_password_sigup = document.getElementById('input_confirm_password_sigup');
    let input_cpf_signup = document.getElementById('input_cpf_signup');
}

function scrollDown() {
    console.log('oi');
    let mid = document.getElementById('input-name-signup')
    return mid.scrollIntoView();
}

function main() { 
}

main();