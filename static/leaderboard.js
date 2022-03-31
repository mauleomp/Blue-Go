startcountdown(10);
document.getElementById("leaderboard").hidden = false;


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
