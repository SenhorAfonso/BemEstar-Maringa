

function verifyCheckBox(index) {
    
    console.log(index);
    var sex_checkbox_f = document.getElementById('input-sex-f-signup');
    var sex_checkbox_m = document.getElementById('input-sex-m-signup');
    var sex_checkbox_o = document.getElementById('input-sex-o-signup');

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
    var input_name_signup = document.getElementById('input-name-signup');
    var input_email_sigup = document.getElementById('input-email-signup');
    var input_password_sigup = document.getElementById('input_password_sigup');
    var input_confirm_password_sigup = document.getElementById('input_confirm_password_sigup');
    var input_cpf_signup = document.getElementById('input_cpf_signup');
}

function scrollDown() {
    console.log('oi');
    var mid = document.getElementById('input-name-signup')
    return mid.scrollIntoView();
}

function main() { 
}

main();