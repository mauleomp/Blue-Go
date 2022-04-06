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

