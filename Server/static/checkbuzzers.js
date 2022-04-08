//example of 9 buttons with 1, 3 and 6 being connected
generatebuttons(3);
connectedbutton(1);
connectedbutton(2);
connectedbutton(3);
setTimeout(function () {
  connectedplayer(1);
  connectedplayer(2);
}, 2000);
setTimeout(function () {
  connectedplayer(3);
}, 3000);



var buttonmap;
var loginmap;
function generatebuttons(number) {
  buttonmap = new Map();
  loginmap = new Map();
  for (let i = 0; i < number; i++) {
    buttonmap.set(i+1, false);
    loginmap.set(i+1, false);
  }

  var row = "";
  for (let i = 0; i < number; i++) {
    if ( i%6 === 0) {
      row += '<div class="row">';
    }

    //creates button with number and id equal to the number
    row += '<div class="col-2"><div id="' + (i+1) + '" class="card buzzer">' + (i+1) + '</div></div>';

    if ( i%6 === 5) {
      row += '</div>';
    }
  }
  document.getElementById("buzzercontainer").innerHTML = row;
}

function connectedbutton(id) {
  document.getElementById(id).style.backgroundColor = '#4cd137';
  buttonmap.set(id, true);
  checkallbuttons();
}

function disconnectedbutton(id){
  document.getElementById(id).style.backgroundColor = 'white';
  buttonmap.set(id, false);
  checkallbuttons();
}

function connectedplayer(id) {
  document.getElementById(id).style.backgroundColor = '#31C1D6';
  loginmap.set(id, true);
  checkalllogin();
}

function disconnectedplayer(id){
  document.getElementById(id).style.backgroundColor = '#4cd137';
  loginmap.set(id, false);
  checkalllogin();
}

//check if all buttons are connected
//On screen text is adjusted accordingly
function checkallbuttons() {
  var keys = [...buttonmap.keys()];
  for (let i = 0; i < keys.length; i++) {
    if (!buttonmap.get(keys[i])) {
      document.getElementById("text").innerHTML = "Connecting with the buzzers..."
      return false;
    }
  }
  document.getElementById("text").innerHTML = "All buzzers are connected! Waiting for all players to join..."
  return true;
}

//check if all players are connected
//On screen text is adjusted accordingly
function checkalllogin() {
  var keys = [...loginmap.keys()];
  for (let i = 0; i < keys.length; i++) {
    if (!loginmap.get(keys[i])) {
      checkallbuttons();
      return false;
    }
  }
  document.getElementById("text").innerHTML = "All buzzers are connected and all teams are logged in!"
  return true;
}
