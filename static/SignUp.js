
document.getElementById("close").addEventListener("click", function() {
    window.location.href = 'MainPage.html';
});

document.getElementById("login").addEventListener("click", function() {
    window.location.href = 'Login.html';
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

function show_password2() {
  var x = document.getElementById("pass2");
  var show_eye = document.getElementById("show2");
  var hide_eye = document.getElementById("hide2");
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

var check = function() {
  if (document.getElementById('pass').value == document.getElementById('pass2').value) {
      document.getElementById('pass2').classList.remove("is-invalid");

  } else {
    document.getElementById('pass2').classList.add("is-invalid");
    document.getElementById('pass2').classList.remove("is-valid");
    document.getElementById('message').innerHTML = 'Passwords are not matching';
    document.getElementById('message').style.color = 'red';
  }
}

// If any button has class is-invalid, disable the sign up button.
// Make sure all elements are filled in. Else mark as in-valid
// Make sure email address has '@' on it.

/*
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

document.getElementById("submit").addEventListener("click", function() {
    window.location.href = 'Login.html';
});
*/