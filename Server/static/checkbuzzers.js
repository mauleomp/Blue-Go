var buzzers = [];
var counter = 1;

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
                getBuzzers();
                textAnimation();
            }, 3000);
        }
    };
    const link = server + "/getConnectedBuzzers"
    http.open("GET", link, true);
    http.send();
}

function submitStartGame(){

    var server = window.location.href
    var	http = new XMLHttpRequest();
    http.open("POST", server + "/start_game", true);
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            const response = JSON.parse(this.responseText);
            if ('confirmation' in response){
                window.location.href = "leaderboard"
            } else {
                $('#ResponseModal').modal('show');
                document.getElementById("serverMessage").innerText = response.error[0].message;
            }
        }
    }
    http.send()
}

function textAnimation(){
    var points = '';
    for (let i = 0; i < counter; i++){
        points += '.';
    }
    counter += 1;
    if (counter >= 4){
        counter = 0;
    }
    document.getElementById("text").innerText = "Connecting with the buzzers" + points
}


function loadbuttons(input) {
  var list = input.buzzers;
  generatebuttons(list);
  for (let i = 0; i < list.length; i++) {
    if (list[i].teamConnected) {
      document.getElementById("b_" + i).style.backgroundColor = '#4cd137';
    }
  }
}

function generatebuttons(list) {
  var row = "";

  for (let i = 0; i < list.length; i++) {
    if ( i%6 === 0) {
      row += '<div class="row">';
    }

    const teamname = list[i].teamName

    //creates button with number and id equal to the number
    row += '<div class="col-2 container">' +
        '      <div id="b_' + i + '" class="card buzzer text-center" style="margin-bottom: 10px">' +
        '          <div class="card-body">' +
        '             <p class="card-text">' + i + '</p>' +
        '          </div>' +
        '      </div>' +
        '      <div style="padding-left: 38px; padding-bottom: 20px">' +
        '          <label style="text-align: center" for="b_' + i + '">' + teamname + '</label>' +
        '      </div>' +
        '   </div>\n';

    if ( i%6 === 5) {
      row += '</div>';
    }
  }
  document.getElementById("buzzercontainer").innerHTML = row;
}
