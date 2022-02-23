
function close(){
    window.location.href = 'MainPage.html';
};

document.getElementById("close").addEventListener("click", function() {
    window.location.href = 'MainPage.html';
});

document.getElementById("signup").addEventListener("click", function() {
    window.location.href = 'SignUp.html';
});

function show_password() {
  var x = document.getElementById("pass");
  var show_eye = document.getElementById("show");
  var hide_eye = document.getElementById("hide");
  hide_eye.classList.remove("d-none");
  if (x.type === "password") {
    x.type = "text";
    show_eye.style.display = "none";
    hide_eye.style.display = "block";
  } else {
    x.type = "password";
    show_eye.style.display = "block";
    hide_eye.style.display = "none";
  }
}