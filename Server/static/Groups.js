
function submitForm() {
   var frm = document.forms["myForm"]["group_name"].value
   window.alert("A group with name " + frm + " has been added.");
   frm.submit(); // Submit
   frm.reset();  // Reset
   return false; // Prevent page refresh
}
