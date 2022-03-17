
function submitForm() {
   var frm = document.forms["myForm"]["group_name"].value
   frm.submit(); // Submit
   frm.reset();  // Reset
   return false; // Prevent page refresh
}
