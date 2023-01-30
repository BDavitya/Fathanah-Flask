function showPassword1() {
    var x = document.getElementById("oldPassword");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function showPassword2() {
    var x = document.getElementById("newPassword");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function showPassword3() {
    var x = document.getElementById("confirmNewPassword");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}