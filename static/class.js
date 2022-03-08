
document.getElementById("icon").addEventListener("click", function() {
    window.location.href = 'TeacherSide.html';
});

$(document).on('click', '.delete', function (event) {
    event.preventDefault();
    $(this).closest('tr').remove();
});