/**
function close(){
    window.location.href = 'MainPage.html';
};


document.getElementById("close").addEventListener("click", function() {
    window.location.href = 'MainPage.html';
});

document.getElementById("signup").addEventListener("click", function() {
    window.location.href = 'SignUp.html';
});


document.getElementById("submitLogin").addEventListener("click", function() {
  const email = document.getElementById("email").value
  const password =document.getElementById("pass").value
  if (email !== "" & password !== ""){
    //sendFormToServer(email, password)
  }
});

document.forms['loginForm'].addEventListener('submit', (event) => {
    event.preventDefault();
    // TODO do something here to show user that form is being submitted
    fetch(event.target.action, {
        method: 'POST',
        body: new URLSearchParams(new FormData(event.target)) // event.target is the form
    }).then((resp) => {
        alert(resp.json())
        return resp.json(); // or resp.text() or whatever the server sends
    }).then((body) => {
        alert("Body")
        // TODO handle body
    }).catch((error) => {
        alert("Error")
        alert(error)
        // TODO handle error
    });
});

  */

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

function sendFormToServer(email, password){

    var server = window.location.href
    var	http = new XMLHttpRequest();
    var params = 'email=' + email + "&pass=" + password;
    http.open("POST", server + "/login", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            alert(http.responseText);
        }
    }
    http.send(params)
}