var selectedGroup;
var selectedGamemode;

function selectgroup(id) {
  if (typeof selectedGroup !== "undefined") {
    document.getElementById(selectedGroup).style.backgroundColor = "white";
  }
  document.getElementById(id).style.backgroundColor = "orange";
  selectedGroup = id;
  return false;
}

function selectGamemode(id) {
    if (typeof selectedGamemode !== "undefined") {
      document.getElementById(selectedGamemode).style.backgroundColor = "rgba(255, 255, 255, 0.8)";
    }
    document.getElementById(id).style.backgroundColor = "orange";
    selectedGamemode = id;
    return false;
}
