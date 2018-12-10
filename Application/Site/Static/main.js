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

function checknumber(){
  console.log("test")
  var phone = document.getElementById('phonenum').value;
  console.log(phone);

  if (phone.length != 12){
    console.log("invalid")
    document.getElementById("numerror").innerHTML = "enter valid number";
    document.getElementById("numerror").style.color = "red";
  } else{
    console.log("valid")
    document.getElementById("numerror").innerHTML = "valid";
        document.getElementById("numerror").style.color = "green";
  }

}

function makerequired(){
  console.log("makerequired");
  // document.getElementById("phonenum").required = true;
  if (document.getElementById("phonenum").required == true){
    phonenum.removeAttribute("required");
  } else{
    document.getElementById("phonenum").required = true;
  }
}


function twofunctions(){
  myFunction2();
  makerequired();
}
