
var profileDetails = [];
var settingsData = [];


function getProfileDetails(){
    var server = window.location.href;
    var http = new XMLHttpRequest();
    var txt = "", x;
    http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Response with all the students in a JSON array
            profileDetails = JSON.parse(this.responseText);

            // Fill the inputs of the Profile form
            fillProfileInfo();
        }
    };
    const link = server + "/getProfileData"
    http.open("GET", link, true);
    http.send();
}

function fillProfileInfo(){
    document.forms["profileDetailsForm"].first_name.value = profileDetails.first_name;
    document.forms["profileDetailsForm"].last_name.value = profileDetails.last_name;
    document.forms["profileDetailsForm"].email.value = profileDetails.email;
    document.forms["profileDetailsForm"].university.value = profileDetails.university;
    document.forms["profileDetailsForm"].password.value = profileDetails.password;
    document.forms["profileDetailsForm"].n_password.value = '';
    document.forms["profileDetailsForm"].c_password.value = '';
}

function updateProfileDetails(){

    const first_name = document.forms["profileDetailsForm"].first_name.value;
    const lastname = document.forms["profileDetailsForm"].last_name.value;
    const email = document.forms["profileDetailsForm"].email.value;
    const university = document.forms["profileDetailsForm"].university.value;
    const current_password = document.forms["profileDetailsForm"].password.value;
    const new_password = document.forms["profileDetailsForm"].n_password.value;
    const repeat_passwrod = document.forms["profileDetailsForm"].c_password.value;

    const c_pass = 'GET from DATABASE';

    if (new_password === repeat_passwrod){
        var server = window.location.href
        var	http = new XMLHttpRequest();
        var params = "first_name=" + first_name + "&lastname=" + lastname + "&email=" + email
            + "&university=" + university + "&new_password=" + new_password;
        http.open("POST", server + "/updateProfileDetails", true);
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
                    document.getElementById("modalButtonClose").removeAttribute("href");
                    return false;
                }
            }
        }
        http.send(params);
    } else {
        $('#ResponseModal').modal('show');
        document.getElementById("ResponseModalLabel").innerText = "Error in action";
        document.getElementById("serverMessage").innerText = "Passwords do not match.";
        document.getElementById("modalButtonClose").removeAttribute("href");
        return false;
    }


}

function resetProfileDetails(){

    document.forms["profileDetailsForm"].first_name.value = profileDetails.first_name;
    document.forms["profileDetailsForm"].last_name.value = profileDetails.last_name;
    document.forms["profileDetailsForm"].email.value = profileDetails.email;
    document.forms["profileDetailsForm"].university.value = profileDetails.university;
    document.forms["profileDetailsForm"].password.value = profileDetails.password;
    document.forms["profileDetailsForm"].n_password.value = '';
    document.forms["profileDetailsForm"].c_password.value = '';

}

function getSettings(){
    var server = window.location.href;
    var http = new XMLHttpRequest();
    var txt = "", x;
    http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Response with all the students in a JSON array
            settingsData = JSON.parse(this.responseText);

            // Fill the inputs of the Settings form
            fillSettingsData();
        }
    };
    const link = server + "/getSettingsData"
    http.open("GET", link, true);
    http.send();
}

function fillSettingsData(){
    const temp = settingsData.login;
    if (tempX === 'true'){
        document.getElementById("flexCheckLogIn")
    }
}

function updateSettings(){

}

function resetSettings(){

}

function submitContactForm(){

}


