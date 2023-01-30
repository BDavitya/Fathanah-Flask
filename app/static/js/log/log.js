function showPassword() {
    var x = document.getElementById("input-pw");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}