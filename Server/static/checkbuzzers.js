var buzzers = [];

document.addEventListener("DOMContentLoaded", function(){

    // Update Functions: obtain and replace html input with server response
    getBuzzers();

});

function getBuzzers(){
    var server = window.location.href;
    var http = new XMLHttpRequest();
    var txt = "", x;
    http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            buzzers = JSON.parse(this.responseText);

            loadbuttons(buzzers)

            setTimeout(function(){
                getBuzzers()
            }, 3000);
        }
    };
    const link = server + "/getConnectedBuzzers"
    http.open("GET", link, true);
    http.send();
}


function loadbuttons(input) {
  var list = input.buzzers;
  generatebuttons(list.length);
  for (let i = 0; i < list.length; i++) {
    if (list[i].teamConnected) {
      document.getElementById(i).style.backgroundColor = '#4cd137';
    }
  }
}

function generatebuttons(number) {
  var row = "";
  for (let i = 0; i < number; i++) {
    if ( i%6 === 0) {
      row += '<div class="row">';
    }

    //creates button with number and id equal to the number
    row += '<div class="col-2"><div id="' + i + '" class="card buzzer">' + i + '</div></div>';

    if ( i%6 === 5) {
      row += '</div>';
    }
  }
  document.getElementById("buzzercontainer").innerHTML = row;
}
