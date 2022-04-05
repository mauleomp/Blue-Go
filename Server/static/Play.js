var selectedGroup;
var selectedGamemode;

function selectgroup(id) {
  if (typeof selectedGroup !== "undefined") {
    document.getElementById(selectedGroup).style.backgroundColor = "rgba(255, 255, 255, 0.9)";
  }
  document.getElementById(id).style.backgroundColor = "orange";
  selectedGroup = id;
  checkstart();
  return false;
}

function selectGamemode(id) {
    if (typeof selectedGamemode !== "undefined") {
      document.getElementById(selectedGamemode).style.backgroundColor = "rgba(255, 255, 255, 0.9)";
    }
    document.getElementById(id).style.backgroundColor = "orange";
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

    var res = "";
    for (let i = 0; i < json.list.length; i++) {
        if (i === 0) {
            res +=  '<div class="carousel-item active text-center" style="top: 0px">\n' +
                        '<div class="row row-cols-3 text-center" style="width: 70%; margin: auto;">\n';
            addcarouselindicator(i/3);
            // res += initialcard;
        } else if (i%3 === 0) {
            res +=  '<div class="carousel-item text-center" style="top: 0px">\n' +
                        '<div class="row row-cols-3 text-center" style="width: 70%; margin: auto;">\n';
            addcarouselindicator(i/3)
        }
        res += createcoursecard(i, json.list[i].name, json.list[i].img);
        if (i%3 === 2 || i === json.list.length-1) {
            res +=      '</div>\n' +
                    '</div>\n';
        }
    }
    document.getElementById("courses").innerHTML += res;
}

function createcoursecard(id, name, img) {
    var res = '' +
        '<div class="col">\n' +
            '<div id="' + id + '" class="card">\n' +
                '<img src="' + img + '" class="card-img-top" alt="...">\n' +
                '<div class="card-body" style="transform: rotate(0);">\n' +
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

{
    let initialcard =
        '                  <div class="col">\n' +
        '                    <div id="anonymous" class="select d-flex flex-column rounded" style="background-color: rgba(255,255,255,0.9);">\n' +
        '                      <button type="button" class="btn" onclick="selectgroup(\'anonymous\');" id="anonymous" style="height:50%;">\n' +
        '                        <div class="row">\n' +
        '                          <div class="col-3"></div>\n' +
        '                          <div class="col-6 d-flex align-items-end justify-content-center">Play anonymously</div>\n' +
        '                          <div class="col-3 text-start">\n' +
        '                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-question-square" viewBox="0 0 16 16">\n' +
        '                              <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>\n' +
        '                              <path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/>\n' +
        '                            </svg>\n' +
        '                          </div>\n' +
        '                        </div>\n' +
        '                      </button>\n' +
        '                      <button type="button" class="btn btn-info" style="height:50%;">\n' +
        '                        <div class="row">\n' +
        '                          <div class="col-3"></div>\n' +
        '                          <div class="col-6 d-flex align-items-start justify-content-center">Add a course</div>\n' +
        '                          <div class="col-3 text-start">\n' +
        '                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square" viewBox="0 0 16 16">\n' +
        '                              <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>\n' +
        '                              <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>\n' +
        '                            </svg>\n' +
        '                          </div>\n' +
        '                        </div>\n' +
        '                      </button>\n' +
        '                    </div>\n' +
        '                  </div>'
}

function resetForm(form) {
    document.forms[form].reset();
}
