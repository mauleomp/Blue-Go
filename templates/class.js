
$(document).on('click', '.delete', function (event) {
    event.preventDefault();
    $(this).closest('tr').remove();
});