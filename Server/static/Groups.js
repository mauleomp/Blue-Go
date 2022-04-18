var all_courses = []
var courses_names = []
var courses_codes = []

document.addEventListener("DOMContentLoaded", function(){
    getAllCourses()

});

function submitForm() {
   var frm = document.forms["myForm"]["group_name"].value
   frm.submit(); // Submit
   frm.reset();  // Reset
   return false; // Prevent page refresh
}

function getAllCourses(){
   var server = window.location.href;
   var http = new XMLHttpRequest();
   var txt = "", x;
   http.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
           console.log(this.responseText)
           all_courses = JSON.parse(this.responseText);
           for (x in all_courses['courses']){
               courses_names.push(all_courses['courses'][x].name.toString());
               courses_codes.push(all_courses['courses'][x].code.toString());
           }
           addAllCourseHtml()
       }
   };
   const link = server + "/getAllCourses"
   http.open("GET", link, true);
   http.send();
}

function updateCourseName(course_code, course_name){
    var server = window.location.href
    var	http = new XMLHttpRequest();
    var params = 'course_name=' + course_name + "&course_code=" + course_code;
    http.open("POST", server + "/updateCourseName", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            alert(http.responseText);
        }
    }
    http.send(params)
}

function submitRenameForm(form){
    var course_name = document.forms[form].course_name.value
    var course_code = form.split('_')[1]
    updateCourseName(course_code, course_name)
}

function removeFromFavourites(course_code){

}

function addToFavourites(course_code){

    document.getElementById("favourites").innerHTML = document.getElementById("favourites").innerHTML + innerHTML
}

function deleteCourse(course_code){

}

function addAllCourseHtml() {

    innerHTML = ""

    for (x in all_courses['courses']) {
        temp_course_name = all_courses['courses'][x].name.toString()
        temp_course_code = all_courses['courses'][x].code.toString()

        const course_HTML = "" +
            "<div class=\"col\">\n" +
            "     <div class=\"card position-relative\" id=\"class\">\n" +
            "          <img src=\"https://images.unsplash.com/photo-1627637819848-7074cb1565e8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80\" class=\"card-img\" alt=\"...\">\n" +
            "          <div class=\"card-img-overlay text-end\" style=\"margin-top: -1rem; margin-right: -1rem;\">\n" +
            "               <button class=\"btn btn-link\" style=\"color:white\" data-bs-toggle=\"dropdown\">\n" +
            "                   <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" fill=\"currentColor\" class=\"bi bi-three-dots-vertical\" viewBox=\"0 0 16 16\">\n" +
            "                      <path d=\"M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z\"/>\n" +
            "                   </svg>\n" +
            "               </button>\n" +
            "               <ul class=\"dropdown-menu dropdown-menu-end\">\n" +
            "                   <li><button class=\"dropdown-item\" onclick=\"addToFavourites('" + temp_course_code +  "')\">Add to favourites</button></li>\n" +
            "                   <li><button class=\"dropdown-item\" data-bs-toggle=\"modal\" data-bs-target=\"#rename_" + temp_course_code +  "\">Rename</button></li>\n" +
            "                   <div class=\"dropdown-divider\"></div>\n" +
            "                   <li><button class=\"dropdown-item\" onclick=\"deleteCourse('" + temp_course_code +  "')\">Delete</button></li>\n" +
            "               </ul>\n" +
            "           </div>\n" +
            "           <div class=\"card-body\" style=\"transform: rotate(0);\">\n" +
            "               <a href=\"/courses/class/" + temp_course_code +  "\" class=\"stretched-link text-decoration-none\" style=\"color:black;\">\n" +
            "                   <h5 class=\"card-title\"></h5>" + temp_course_name + "</a>\n" +
            "           </div>\n" +
            "      </div>\n" +
            "</div>\n" +
            "\n" +
            "<!-- Rename Modal -->\n" +
            "                <div class=\"modal fade\" id=\"rename_" + temp_course_code +  "\" tabindex=\"-1\" aria-labelledby=\"renameLabel_" + temp_course_code +  "\" aria-hidden=\"true\">\n" +
            "                    <div class=\"modal-dialog  modal-dialog-centered\">\n" +
            "                        <div class=\"modal-content\">\n" +
            "                            <div class=\"modal-header justify-content-end\" style=\"background-color: #5bc0de; height: 3rem;\">\n" +
            "                                <button type=\"button\" class=\"btn\" data-bs-dismiss=\"modal\" aria-label=\"Close\">\n" +
            "                                    <script src=\"https://cdn.lordicon.com/lusqsztk.js\"></script>\n" +
            "                                    <lord-icon\n" +
            "                                        src=\"https://cdn.lordicon.com/fdzomkrp.json\"\n" +
            "                                        trigger=\"loop-on-hover\"\n" +
            "                                        colors=\"white\"\n" +
            "                                        style=\"width:30px;height:30px\">\n" +
            "                                    </lord-icon>\n" +
            "                                </button>\n" +
            "                            </div>\n" +
            "                            <div class=\"modal-body\">\n" +
            "                                <h4 class=\"modal-title text-center\" id=\"renameLabel_" + temp_course_code +  "\"> Rename course</h4>\n" +
            "                                <br>\n" +
            "                                <form id=\"renameForm_" + temp_course_code +  "\" name=\"newCourseForm_" + temp_course_code +  "\">\n" +
            "                                    <div class=\"mb-3\">\n" +
            "                                        <label for=\"rename_name_" + temp_course_code +  "\" class=\"form-label\" style=\"color:darkgrey; font-size: x-small;\"> COURSE NAME </label>\n" +
            "                                        <input id=\"rename_name_" + temp_course_code +  "\" name=\"course_name\" type=\"text\" class=\"form-control\" placeholder=\"Example group name\" value=\"" + temp_course_name + "\">\n" +
            "                                    </div>\n" +
            "                                    <div> <p id=\"rename_confirmation_" + temp_course_code +  "\"></p> </div>\n" +
            "                                </form>\n" +
            "                            </div>\n" +
            "                            <div class=\"modal-footer justify-content-center\">\n" +
            "                                <button id=\"submit_form_" + temp_course_code +  "\" onclick=\"submitRenameForm('renameForm_" + temp_course_code +  "')\" type=\"button\" class=\"btn rounded-pill\" style=\"background-color: #5bc0de; color: white\">Save changes</button>\n" +
            "                            </div>\n" +
            "                        </div>\n" +
            "                    </div>\n" +
            "                </div>"

        innerHTML = innerHTML + course_HTML
    }

    document.getElementById("groups").innerHTML = document.getElementById("groups").innerHTML + innerHTML

}