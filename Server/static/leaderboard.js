//example leaderboard
var leaderboardjson = {
  "totalpoints": 100,
  "ranking": [
      {"name": "Fatima", "points": 75, "pointsdifference": +10},
      {"name": "Bas", "points": 60, "pointsdifference": +5},
      {"name": "Judith", "points": 60, "pointsdifference": -10}
  ]
};

//--------------------
//Global variables
let countdowntime;
let roundcount = 1;
//---------------------

// showrankings();
playrandom(5);

//Starts a classic game, who has 3 second countdowns as default
function playclassic() {
    countdowntime = 3;
    playround(3);
}

//Starts a classic game, with a custom countdown time
function playrandom(time) {
    countdowntime = time;
    playround();
}

//Play one round of classic or random gamemode. This means, play with one question until it is answered correctly.
//Only difference in front end is that classic always plays with a 3 second countdown, while random countdown timer can be changed in the settings
//After the question is answered correctly, waits for a response to either end or continue the game.
//If next round is chosen, the function increases the roundcount and calls itself again.
async function playround() {

      closerankings();
      //Await countdown before starting the round
      await(new Promise((resolve, reject) => {
        startcountdown(countdowntime);
        setTimeout(() => resolve(), 1000*(countdowntime+1));
      }));
      waitforpress(roundcount);

      var currentplayer;
      //Keep looping until answer is correct
      var loop = setInterval(async function () {
        getIsCorrect().then(async function(json) {

          //   example json: {"iscorrect": true}
          //   or:      {"iscorrect": false, "nextname":"Fatima"}
          if (json.iscorrect) {

            endround();

            //End the loop
            clearInterval(loop);

          } else if (typeof currentplayer === "undefined") {
            //Displaying name of first presser. There was no incorrect answer yet
            currentplayer = json.nextname;
            displayname(json.nextname);
            //Go again

          } else if (json.nextname !== currentplayer) {
            //Await incorrect answer animation
            //Give turn to the next player in line
            currentplayer = json.nextname;
            await(new Promise((resolve, reject) => {
              incorrectanswer(json.nextname);
              setTimeout(() => resolve(), 3000);
            }));
            //Go again

          } else {
            //No new value. Go again...
          }
        })
      }, 1000);
}

//Is called when correct answer is given and the round ends.
//Does the correct answer and leaderboard animation, and then calls playnextround();
async function endround() {
    //Await correct answer animation
    await(new Promise((resolve, reject) => {
      correctanswer();
      setTimeout(() => resolve(), 3000);
    }));

    getRanking().then(function(json) {
        console.log(json);
        showrankings(json);
        playnextround();
     });
}

//Waits for input on whether to continue playing, or to stop the game.
async function playnextround() {
    var loop = setInterval(async function() {
        console.log("1");
        getStatus().then(function(json) {
            if (json.status === "endgame") {
                closerankings();
                clearInterval(loop);
                //Game has ended, what now?
            } else if (json.questionnumber >= roundcount && json.status === "nextround") {
                roundcount++;
                playround();
                clearInterval(loop);
            }
        });
    }, 1000);
}



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
      document.getElementById("countdownnumber").innerHTML = '';
      return true;
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

function signalNotification(text){
  // Notification
      (async () => {
          // create and show the notification
          const showNotification = () => {
              // create a new notification
              const notification = new Notification('Blue&GO!', {
                  //The body is the text that will go inside the notification
                  icon: "/images/logo",
                  body: text
              });

              // close the notification after 10 seconds
              setTimeout(() => {
                  notification.close();
              }, 10 * 1000);

              // navigate to a URL when clicked
              notification.addEventListener('click', () => {

                  window.parent.parent.focus();
              });
          }

          // show an error message
          const showError = () => {
              const error = document.querySelector('.error');
              error.style.display = 'block';
              error.textContent = 'You blocked the notifications';
          }

          // check notification permission
          let granted = false;

          if (Notification.permission === 'granted') {
              granted = true;
          } else if (Notification.permission !== 'denied') {
              let permission = await Notification.requestPermission();
              granted = permission === 'granted' ? true : false;
          }

          // show notification or error
          granted ? showNotification() : showError();

      })();
}


function getIsCorrect() {
    return new Promise(function(resolve, reject) {
        // The URL of the server
        var server = window.location.href;

        // GET request
        var http = new XMLHttpRequest();
        http.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                // Response containing a JSON object
                //   example: {"iscorrect": true}
                //   or:      {"iscorrect": false, "nextname":"Fatima"}

                var response = JSON.parse(this.responseText);
                console.log(response);

                // After just received the data, return the json as a resolved promise
                resolve(response);
            }
        };
        // URL route that is stored in server
        const link = server + "/isCorrect" // If parameters, then append them here

        // Send the http GET request
        http.open("GET", link, true);
        http.send();
    });
}

function getRanking() {

    return new Promise(function(resolve, reject) {
        // The URL of the server
        var server = window.location.href;

        // GET request
        var http = new XMLHttpRequest();
        http.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                // Response containing a JSON object with ranking
                // example:
                // {
                //   "totalpoints": 100,
                //   "ranking": [
                //       {"name": "Fatima", "points": 75, "pointsdifference": +10},
                //       {"name": "Bas", "points": 60, "pointsdifference": +5},
                //       {"name": "Judith", "points": 60, "pointsdifference": -10}
                //   ]
                // };

                var response = JSON.parse(this.responseText);

                // After just received the data, return the json as a resolved promise
                resolve(response);
            }
        };
        // URL route that is stored in server
        const link = server + "/ranking" // If parameters, then append them here

        // Send the http GET request
        http.open("GET", link, true);
        http.send();
    });
}

function getStatus() {

    return new Promise(function(resolve, reject) {
        // The URL of the server
        var server = window.location.href;

        // GET request
        var http = new XMLHttpRequest();
        http.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                // Response containing a json with status on how to continue and current questionnumber
                // {questionnumber": 1, "status": "nextround"}
                // or    {questionnumber": 1, "status": "endgame"}

                var response = JSON.parse(this.responseText);

                // After just received the data, return the json as a resolved promise
                resolve(response);
            }
        };
        // URL route that is stored in server
        const link = server + "/status" // If parameters, then append them here

        // Send the http GET request
        http.open("GET", link, true);
        http.send();
    });
}

document.getElementById("nextroundbutton").addEventListener('click', function() {
    postJSON({"questionnumber": roundcount, "status": "nextround"}, "/status");
})

document.getElementById("endgamebutton").addEventListener('click', function() {
    postJSON({"status": "endgame"}, "/status")
})

function postJSON(json, address) {
    return new Promise(function(resolve, reject) {
        // The URL of the server
        var server = window.location.href

        // POST request
        var http = new XMLHttpRequest();
        http.open("POST", server + address, true);
        http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        http.onreadystatechange = function () {
            // If the server responded with a response OK
            if (http.readyState == 4 && http.status == 200) {
                console.log(http.responseText);
                resolve();
            }
        }
        // Send the http POST request with a form
        http.send(json);
    });
}


//---------------------------------------------------------------------------------------------------------------------

//example game sequence
// displayname("Fatima");
// setTimeout(function () {
//   incorrectanswer("Bas");
// }, 2000);
// setTimeout(function () {
//   correctanswer();
// }, 8000);
// setTimeout(function () {
//   showrankings(leaderboardjson);
// }, 12000);
// setTimeout(function () {
//   displayname("Judith");;
// }, 17000);
