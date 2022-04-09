var selectedCourse;
var selectedGamemode;
var game_settings;
var all_courses = [];

var classic_settings = ["1", "2"];
var random_settings = ["1", "1", "10"];
var lifelines_settings = ["10", "1", "3", "10"];

document.addEventListener("DOMContentLoaded", function(){

    // Update Functions: obtain and replace html input with server response
    getAllCourses();

});

function getAllCourses(){
    var server = window.location.href;
    var http = new XMLHttpRequest();
    var txt = "", x;
    http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            all_courses = JSON.parse(this.responseText);

            generatecourses(all_courses)
        }
    };
    const link = server + "/getAllCourses"
    http.open("GET", link, true);
    http.send();
}

function submitGamePreferences(){

    var server = window.location.href
    var	http = new XMLHttpRequest();
    var params = 'course_code=' + selectedCourse.toString()
        + "&game_mode=" + selectedGamemode
        + "&game_settings=" + game_settings;
    http.open("POST", server + "/save_game_preferences", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            const response = JSON.parse(this.responseText);
            if ('confirmation' in response){
                window.location.href = "buzzers"
            } else {
                $('#ResponseModal').modal('show');
                document.getElementById("serverMessage").innerText = response.error[0].message;
            }
        }
    }
    http.send(params)
}

function selectgroup(id) {
  if (typeof selectedCourse !== "undefined") {
    document.getElementById(selectedCourse).style.backgroundColor = "rgba(255, 255, 255, 0.9)";
  }
  document.getElementById(id).style.backgroundColor = "#eeca66";
  selectedCourse = id;
  checkstart();
  return false;
}

function selectGamemode(id) {
    if (typeof selectedGamemode !== "undefined" && selectedGamemode !== "Anonymously") {
        document.getElementById(selectedGamemode).style.backgroundColor = "rgba(255, 255, 255, 0.9)";

    } else if (id !== "Anonymously") {
        document.getElementById("Anonymously").style.backgroundColor = '#31C1D6';

    }

    document.getElementById(id).style.backgroundColor = '#eeca66';
    // document.getElementById("Anonymously").style.backgroundColor = '#eeca66';
    document.getElementById("anonymoustext").innerHTML = "Playing " + id;
    selectedGamemode = id;
    if (id === 'Classic'){
        game_settings = classic_settings;
    } else if (id === 'Random') {
        game_settings = random_settings;
    } else if (id === 'Lifelines') {
        game_settings = lifelines_settings;
    }
    checkstart();
    return false;
}

function submitFormMode(id){
    if (id === 'classic'){
        classic_settings[0] = document.getElementById("sumPointsC").value.toString();
        classic_settings[1] = document.getElementById("deductPointsC").value.toString();
    } else if (id === 'random') {
        random_settings[0] = document.getElementById("sumPointsR").value.toString();
        random_settings[1] = document.getElementById("deductPointsR").value.toString();
        random_settings[2] = document.getElementById("timerR").value.toString();
    } else if (id === 'lifelines') {
        lifelines_settings[0] = document.getElementById("lifesL").value.toString();
        lifelines_settings[1] = document.getElementById("deductLifes1L").value.toString();
        lifelines_settings[2] = document.getElementById("deductLifes2L").value.toString();
        lifelines_settings[3] = document.getElementById("timerL").value.toString();
    }
}

function checkstart() {
    if (typeof selectedCourse !== "undefined" && typeof selectedGamemode !== "undefined") {
        document.getElementById("startbutton").disabled = false;
    }
}

function generatecourses(input) {
    // var json = JSON.parse(input);
    var json = input;
    console.log(json)

    var res = '<div class="carousel-item active text-center" style="top: 0px">\n' +
            '<div class="row row-cols-3 text-center" style="width: 70%; margin: auto;">\n';
    res += getaddcoursecard();
    addcarouselindicator(0);
    for (let i = 0; i < json.courses.length; i++) {

        if ((i+1)%3 === 0) {
            res +=  '<div class="carousel-item text-center" style="top: 0px">\n' +
                        '<div class="row row-cols-3 text-center" style="width: 70%; margin: auto;">\n';
            addcarouselindicator((i+1)/3)
        }
        const id = json.courses[i].code
        res += createcoursecard(id, json.courses[i].name, json.courses[i].img);
        if ((i+1)%3 === 2 || i === json.courses.length-1) {
            res +=      '</div>\n' +
                    '</div>\n';
        }
    }
    document.getElementById("courses").innerHTML += res;
}

function createcoursecard(id, name, img) {
    var res = '' +
        '<div class="col">\n' +
            '<div id="' + id + '" class="card coursecard">\n' +
                '<img src="' + img + '" class="card-img-top" alt="...">\n' +
                '<div class="card-body">\n' +
                    '<h5 class="card-title" style="color:black;">' + name + '</h5>\n' +
                '</div>\n' +
                '<a onclick="selectgroup(\'' + id + '\');" class="stretched-link"></a>' +
            '</div>\n' +
        '</div>\n';
    return res;
}


function addcarouselindicator(number) {
    var res;
    if (number === 0) {
        res = '<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="' + number + '" class="active" aria-current="true"></button>';
    } else {
        res = '<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="' + number + '"></button>';
    }
    document.getElementById("carouselindicators").innerHTML += res;
}

function resetForm(form) {
    document.forms[form].reset();

    if(form === 'classic'){
        classic_settings = ["1", "2"];
    } else if (form === 'random'){
        random_settings = ["1", "1", "10"];
    } else if (form === 'lifelines'){
        lifelines_settings = ["10", "1", "3", "10"];
    }
}

function getaddcoursecard() {
    let addcoursecard = '                    <div class="col">\n' +
        '                        <div id="0" class="card addcoursecard"  style="height:100%;">\n' +
        '                            <div class="card-body">\n' +
        '                            <h5 class="card-title" style="color:black;">Add a course</h5>\n' +
        '                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-plus-square icon" viewBox="0 0 16 16">\n' +
        '                                  <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>\n' +
        '                                  <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>\n' +
        '                                </svg>\n' +
        '                            </div>\n' +
        '                            <a onclick="" class="stretched-link"></a>\n' +
        '                        </div>\n' +
        '                    </div>';
    return addcoursecard;
}
