var all_students = []
var s_ranking = []
var c_ranking = []

document.addEventListener("DOMContentLoaded", function(){
    getAllStudents()
    getCourseRanking()
    getTeamRanking()

});

document.getElementById("icon").addEventListener("click", function() {
    window.location.href = 'TeacherSide.html';
});

$(document).on('click', '.delete', function (event) {
    event.preventDefault();
    $(this).closest('tr').remove();
});


function getAllStudents(){
   var server = window.location.href;
   var http = new XMLHttpRequest();
   var txt = "", x;
   http.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
           all_students = JSON.parse(this.responseText);

           console.log(all_students)

           addStudentsInTable()

       }
   };
   const link = server + "/getStudents"
   http.open("GET", link, true);
   http.send();
}

function getCourseRanking(){
   var server = window.location.href;
   var http = new XMLHttpRequest();
   var txt = "", x;
   http.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
           s_ranking = JSON.parse(this.responseText);

           console.log(s_ranking)

           addStudentRankInTable()
       }
   };
   const link = server + "/getStudentsRanking"
   http.open("GET", link, true);
   http.send();
}

function getTeamRanking(){
   var server = window.location.href;
   var http = new XMLHttpRequest();
   var txt = "", x;
   http.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
           c_ranking = JSON.parse(this.responseText);

           console.log(c_ranking)

           addCourseRankInTable()


       }
   };
   const link = server + "/getTeamsRanking"
   http.open("GET", link, true);
   http.send();
}

function addStudentsInTable(){

    table = document.getElementById("tableBody")

    table.innerHTML = ""

    tableHTML = ""

    for (x in all_students['students']){

        s_number = all_students['students'][x].s_number
        s_name = all_students['students'][x].s_name
        s_lastname = all_students['students'][x].s_lastname
        t_teams = all_students['students'][x].t_teams

        const html = "" +
            "<tr>\n" +
            "    <th scope=\"row\">" + s_number + "</th>\n" +
            "    <td>" + s_name + "</td>\n" +
            "    <td>" + s_lastname + "</td>\n" +
            "    <td>\n" +
            "        <button class=\"btn btn-light rounded-pill\"> " + t_teams + " </button>\n" +
            "    </td>\n" +
            "    <td>\n" +
            "        <button type=\"button\" class=\"btn btn-success\">\n" +
            "            <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" fill=\"currentColor\" class=\"bi bi-pencil-square\" viewBox=\"0 0 16 16\">\n" +
            "                <path d=\"M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z\"/>\n" +
            "                <path fill-rule=\"evenodd\" d=\"M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z\"/>\n" +
            "            </svg>\n" +
            "        </button>\n" +
            "        <button type=\"button\" class=\"btn btn-danger delete\">\n" +
            "            <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" fill=\"currentColor\" class=\"bi bi-trash3\" viewBox=\"0 0 16 16\">\n" +
            "                <path d=\"M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z\"/>\n" +
            "            </svg>\n" +
            "        </button>\n" +
            "    </td>\n" +
            "</tr>\n"


        tableHTML = tableHTML + html
    }

    table.innerHTML = tableHTML
}


function addStudentRankInTable() {

    table = document.getElementById("studentRankingTableBody")

    table.innerHTML = ""

    tableHTML = ""

    var index = 1

    for (x in s_ranking['s_ranking']) {

        s_name = s_ranking['s_ranking'][x].s_name
        s_lastname = s_ranking['s_ranking'][x].s_lastname
        s_rank = s_ranking['s_ranking'][x].s_rank

        const html = "" +
            "<tr>\n" +
            "    <th scope=\"row\">" + index + "</th>\n" +
            "    <td> " + s_name + " <br> " + s_lastname + "</td>\n" +
            "    <td></td>\n" +
            "    <td> " + s_rank + " </td>\n" +
            "</tr>\n"

        tableHTML = tableHTML + html

    }

    table.innerHTML = tableHTML
    index = index + 1

}

function addCourseRankInTable() {

    table = document.getElementById("courseRankingTableBody")

    table.innerHTML = ""

    tableHTML = ""

    var index = 1

    for (x in c_ranking['c_ranking']) {

        c_name = c_ranking['c_ranking'][x].c_name
        c_rank = c_ranking['c_ranking'][x].c_rank

        const html = "" +
            "<tr>\n" +
            "    <th scope=\"row\">" + index + "</th>\n" +
            "    <td> " + c_name + " </td>\n" +
            "    <td></td>\n" +
            "    <td> " + c_rank + " </td>\n" +
            "</tr>\n"

        tableHTML = tableHTML + html

        index = index + 1

    }

    table.innerHTML = tableHTML

}