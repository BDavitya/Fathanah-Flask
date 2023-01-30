$(document).ready(function(){
    $(".preloader").fadeOut();
})

var dropdown = document.getElementsByClassName("dropdown-btn");
var i;
for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
            this.classList.remove("active")
        } else {
            dropdownContent.style.display = "block";
            this.classList.add("active")
        }
    });
}

var modals = document.getElementById('profile');
window.onclick = function(event) {
    if (event.target == modals) {
        modals.style.display = "none";
    }
}

var modals = document.getElementById('about');
window.onclick = function(event) {
    if (event.target == modals) {
        modals.style.display = "none";
    }
}

var modal = document.getElementById('logout');
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}