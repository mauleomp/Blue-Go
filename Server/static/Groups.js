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

function addAllCourseHtml() {

    innerHTML = ""

    console.log(all_courses)

    for (x in all_courses['courses']) {
        temp_course_name = all_courses['courses'][x].name.toString()
        temp_course_code = all_courses['courses'][x].code.toString()

        console.log("#" + temp_course_code + "#")

        const course_HTML = "" +
            "<div class=\"col\">\n" +
            "     <div class=\"card position-relative\" id=\"class\">\n" +
            "          <img src=\"https://images.unsplash.com/photo-1627637819848-7074cb1565e8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80\" class=\"card-img\" alt=\"...\">\n" +
            "          <div class=\"card-img-overlay text-end\" style=\"margin-top: -1rem; margin-right: -1rem;\">\n" +
            "               <button class=\"btn btn-link\" style=\"color:black\" data-bs-toggle=\"dropdown\">\n" +
            "                   <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" fill=\"currentColor\" class=\"bi bi-three-dots-vertical\" viewBox=\"0 0 16 16\">\n" +
            "                      <path d=\"M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z\"/>\n" +
            "                   </svg>\n" +
            "               </button>\n" +
            "               <ul class=\"dropdown-menu dropdown-menu-end\">\n" +
            "                   <li><a class=\"dropdown-item\" href=\"#\">Add to favourites</a></li>\n" +
            "                   <li><a class=\"dropdown-item\" href=\"#\">Rename</a></li>\n" +
            "                   <div class=\"dropdown-divider\"></div>\n" +
            "                   <li><a class=\"dropdown-item\" href=\"#\">Delete</a></li>\n" +
            "               </ul>\n" +
            "           </div>\n" +
            "           <div class=\"card-body\" style=\"transform: rotate(0);\">\n" +
            "               <a href=\"/groups/class/" + temp_course_code +  "\" class=\"stretched-link text-decoration-none\" style=\"color:black;\">\n" +
            "                   <h5 class=\"card-title\"></h5>" + temp_course_name + "</a>\n" +
            "           </div>\n" +
            "      </div>\n" +
            "</div>\n"

        innerHTML = innerHTML + course_HTML
    }

    document.getElementById("groups").innerHTML = document.getElementById("groups").innerHTML + innerHTML

}