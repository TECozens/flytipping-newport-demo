function myFunction() {
  // Get the checkbox
  var checkBox = document.getElementById("myCheck");
  // Get the output text
  var text = document.getElementById("text");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
    text.style.display = "none";
  }
}

function myFunction2() {
  // Get the checkbox
  var checkBox = document.getElementById("myCheck");
  // Get the output text
  var text = document.getElementById("text");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
    text.style.display = "none";
  }
}

function switchFunction() {
  // Get the checkbox
  var checkBox = document.getElementById("mySwitch");
  // Get the output text
  var addressF = document.getElementById("addressField");
  var mapF = document.getElementById("mapField");
  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    addressF.style.display = "block";
    mapF.style.display = "none";
  } else {
    addressF.style.display = "none";
    mapF.style.display = "block";
  }
}