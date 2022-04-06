//Displays rankings based on JSON input, formatting can be seen in example JSON.
//Python still must determine how long the rankings are displayed.
//Animation of the leaderboard takes 3s, so take that into account.
function showrankings(input) {
  document.getElementById("leaderboard").hidden = false;
  document.getElementById("ranking").innerHTML = "";
  // var json = JSON.parse(input);
  var json = input;
  for (let i = 0; i < json.ranking.length; i++) {
    var barpercentage = json.ranking[i].points / json.totalpoints * 100;
    var pointsdifference = json.ranking[i].pointsdifference < 0 ? json.ranking[i].pointsdifference : "+" + json.ranking[i].pointsdifference;
    let entry = '<dt class="text-center">' + json.ranking[i].name + '</dt>'
    + '<dd><div class="progress"><span class="progress-bar" style="width: ' + barpercentage + '%;">' + pointsdifference +'</span></div></dd>';
    document.getElementById("ranking").innerHTML += entry;
  }
}

//used by other functions to first close rankingsboard
function closerankings() {
  document.getElementById("leaderboard").hidden = true;
}

//Countdown from parameter number.
//Python needs to set a sleep function of the same amount of seconds before calling next function.
function startcountdown(number) {
  closerankings();
  document.getElementById("countdown").hidden = false;
  var i = number;
  var interval = setInterval(function () {
    document.getElementById("countdownnumber").innerHTML = i;
    i--;
    if (i < 0) {
      clearInterval(interval);
      document.getElementById("countdown").hidden = true;
      return false;
    }
  }, 1000);
}

//Can be used in classic gamemode.
function waitforpress(questionnumber) {
  closerankings();
  document.getElementById("name").hidden = false;
  document.getElementById("nameinput").innerHTML = "Question " + questionnumber;
  document.getElementById("namefooter").innerHTML = "Waiting for button press...";
}

//Display a name
function displayname(name) {
  closerankings();
  document.getElementById("name").hidden = false;
  document.getElementById("nameinput").innerHTML = name;
  document.getElementById("namefooter").innerHTML = "It is your turn!"
}

//Answer of current student was wrong.
//Give name of next turn, then next name will automatically be displayed after the animation
//Animation takes 3s
function incorrectanswer(nextname) {
  document.body.style.backgroundColor = 'red';
  document.getElementById("namefooter").innerHTML = "Incorrect!"
  setTimeout(function () {
    document.body.style.backgroundColor = '#81ecec';
    displayname(nextname);
  }, 3000);
}

//Answer was correct
//Animation takes 3s
//Next move needs to be called by Python
function correctanswer() {
  document.body.style.backgroundColor = '#4cd137';
  document.getElementById("namefooter").innerHTML = "Correct!"
  setTimeout(function () {
    document.body.style.backgroundColor = '#81ecec';
    document.getElementById("name").hidden = true;
  }, 3000);
}

//---------------------------------------------------------------------------------------------------------------------

//example leaderboard
var leaderboardjson = {
  "totalpoints": 100,
  "ranking": [
      {"name": "Fatima", "points": 75, "pointsdifference": +10},
      {"name": "Bas", "points": 60, "pointsdifference": +5},
      {"name": "Judith", "points": 60, "pointsdifference": -10}
  ]
};

//example game sequence
displayname("Fatima");
setTimeout(function () {
  incorrectanswer("Bas");
}, 2000);
setTimeout(function () {
  correctanswer();
}, 8000);
setTimeout(function () {
  showrankings(leaderboardjson);
}, 12000);
setTimeout(function () {
  displayname("Judith");;
}, 17000);
