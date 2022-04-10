var selectedGroup;
var selectedGamemode;

function selectgroup(id) {
  if (selectedGroup === "Anonymously") {
    document.getElementById(selectedGroup).style.backgroundColor = "#6c757d";
  }
  else if (typeof selectedGroup !== "undefined") {
    document.getElementById(selectedGroup).style.backgroundColor = "rgba(255, 255, 255, 0.9)";
  }
  document.getElementById(id).style.backgroundColor = "#eeca66";
  selectedGroup = id;
  checkstart();
  return false;
}

function selectGamemode(id) {
    if (typeof selectedGamemode !== "undefined" && selectedGamemode !== "Anonymously") {
      document.getElementById(selectedGamemode).style.backgroundColor = "rgba(255, 255, 255, 0.9)";
    }
    document.getElementById(id).style.backgroundColor = '#eeca66';
    selectedGamemode = id;
    checkstart();
    return false;
}

function checkstart() {
    if (typeof selectedGroup !== "undefined" && typeof selectedGamemode !== "undefined") {
        document.getElementById("startbutton").disabled = false;
    }
}

var coursesjson =
    {
        "list": [
            {"name": "TCS 3", "img": "https://images.unsplash.com/photo-1639815189096-f75717eaecfe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80"},
            {"name": "TCS 3", "img": "https://images.unsplash.com/photo-1642698166111-1e736132b0ee?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80"},
            {"name": "TCS 3", "img": "https://images.unsplash.com/photo-1627637819848-7074cb1565e8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80"},
            {"name": "TCS 3", "img": "https://images.unsplash.com/photo-1639815189096-f75717eaecfe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80"},
            {"name": "TCS 3", "img": "https://images.unsplash.com/photo-1639815189096-f75717eaecfe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80"},
        ]
    };

generatecourses(coursesjson);
function generatecourses(input) {
    // var json = JSON.parse(input);
    var json = input;

    var res = '<div class="carousel-item active text-center" style="top: 0px">\n' +
            '<div class="row row-cols-3 text-center" style="width: 70%; margin: auto;">\n';
    res += getaddcoursecard();
    addcarouselindicator(0);
    for (let i = 0; i < json.list.length; i++) {

        if ((i+1)%3 === 0) {
            res +=  '<div class="carousel-item text-center" style="top: 0px">\n' +
                        '<div class="row row-cols-3 text-center" style="width: 70%; margin: auto;">\n';
            addcarouselindicator((i+1)/3)
        }
        res += createcoursecard(i, json.list[i].name, json.list[i].img);
        if ((i+1)%3 === 2 || i === json.list.length-1) {
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
}

function getaddcoursecard() {
    let addcoursecard = '                    <div class="col">\n' +
        '                        <div class="card addcoursecard"  style="height:100%;">\n' +
        '                            <div class="card-body">\n' +
        '                            <h5 class="card-title" style="color:black;">Add a course</h5>\n' +
        '                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-plus-square icon" viewBox="0 0 16 16">\n' +
        '                                  <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>\n' +
        '                                  <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>\n' +
        '                                </svg>\n' +
        '                            </div>\n' +
        '                            <a data-bs-toggle="modal" data-bs-target="#addcourse" class="stretched-link"></a>\n' +
        '                        </div>\n' +
        '                    </div>';
    return addcoursecard;
}
