

function signalCorrectAnswer(){

    var server = window.location.href
    var	http = new XMLHttpRequest();
    var params = 'temp=1';
    http.open("POST", server + "/signalCorrectAnswer", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            const response = JSON.parse(this.responseText);

            if ('confirmation' in response){
                  $('#ResponseModal').modal('show');
                  document.getElementById("ResponseModalLabel").innerText = "Action made successfully";
                  document.getElementById("serverMessage").innerText = response.confirmation[0].message;


            } else {
                $('#ResponseModal').modal('show');
                document.getElementById("ResponseModalLabel").innerText = "Error in action";
                document.getElementById("serverMessage").innerText = response.error[0].message;

            }
            return false;
        }
    }
    http.send(params);

}



function signalIncorrectAnswer(){

    var server = window.location.href
    var	http = new XMLHttpRequest();
    var params = 'temp=1';
    http.open("POST", server + "/signalIncorrectAnswer", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            const response = JSON.parse(this.responseText);

            if ('confirmation' in response){
                  $('#ResponseModal').modal('show');
                  document.getElementById("ResponseModalLabel").innerText = "Action made successfully";
                  document.getElementById("serverMessage").innerText = response.confirmation[0].message;


            } else {
                $('#ResponseModal').modal('show');
                document.getElementById("ResponseModalLabel").innerText = "Error in action";
                document.getElementById("serverMessage").innerText = response.error[0].message;

            }
            return false;
        }
    }
    http.send(params);

}


function signalNextQuestion(){

    var server = window.location.href
    var	http = new XMLHttpRequest();
    var params = 'temp=1';
    http.open("POST", server + "/signalNextQuestion", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            const response = JSON.parse(this.responseText);

            if ('confirmation' in response){
                  $('#ResponseModal').modal('show');
                  document.getElementById("ResponseModalLabel").innerText = "Action made successfully";
                  document.getElementById("serverMessage").innerText = response.confirmation[0].message;


            } else {
                $('#ResponseModal').modal('show');
                document.getElementById("ResponseModalLabel").innerText = "Error in action";
                document.getElementById("serverMessage").innerText = response.error[0].message;

            }
            return false;
        }
    }
    http.send(params);

}

function signalEndGame(){

    var server = window.location.href
    var	http = new XMLHttpRequest();
    var params = 'temp=1';
    http.open("POST", server + "/signalEndGame", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            const response = JSON.parse(this.responseText);

            if ('confirmation' in response){
                  $('#ResponseModal').modal('show');
                  document.getElementById("ResponseModalLabel").innerText = "Action made successfully";
                  document.getElementById("serverMessage").innerText = response.confirmation[0].message;


            } else {
                $('#ResponseModal').modal('show');
                document.getElementById("ResponseModalLabel").innerText = "Error in action";
                document.getElementById("serverMessage").innerText = response.error[0].message;

            }
            return false;
        }
    }
    http.send(params);

}