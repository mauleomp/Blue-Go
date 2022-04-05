//example of 9 buttons with 1, 3 and 6 being connected
generatebuttons(9);
connectedbutton(1);
connectedbutton(3);
connectedbutton(6);

function generatebuttons(number) {

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
}
