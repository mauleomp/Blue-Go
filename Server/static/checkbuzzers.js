var examplejson = {
  buzzers: [
        { "buzzerID": 0,
          "teamConnected": true,
          "teamName": "Team0"},
        { "buzzerID": 1,
          "teamConnected": true,
          "teamName": "Team1"},
        { "buzzerID": 2,
          "teamConnected": false,
          "teamName": undefined}
    ]
};

loadbuttons(examplejson);
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
