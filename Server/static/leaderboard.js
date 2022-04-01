//example leaderboard
var leaderboardjson = {
  "totalpoints": 100,
  "ranking": [
      {"name": "Fatima", "points": 75, "pointsdifference": +10},
      {"name": "Bas", "points": 60, "pointsdifference": +5},
      {"name": "Judith", "points": 60, "pointsdifference": -10}
  ]
};
showrankings(leaderboardjson);

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

function startcountdown(number) {
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

function displayname(name) {
  document.getElementById("name").hidden = false;
  document.getElementById("nameinput").innerHTML = name;
  document.getElementById("namefooter").innerHTML = "It is your turn!"
}

function incorrectanswer(nextname) {
  document.body.style.backgroundColor = 'red';
  document.getElementById("namefooter").innerHTML = "Incorrect!"
  setTimeout(function () {
    document.body.style.backgroundColor = '#81ecec';
    displayname(nextname);
  }, 3000);
}

function correctanswer() {
  document.body.style.backgroundColor = '#4cd137';
  document.getElementById("namefooter").innerHTML = "Correct!"
  setTimeout(function () {
    document.body.style.backgroundColor = '#81ecec';
    document.getElementById("name").hidden = true;
  }, 3000);
}