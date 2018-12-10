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

function checknumber(){
  var phone = document.getElementById('phonenum').value;
  console.log(phone);

  if (phone.length != 11){
    document.getElementById("numerror").innerHTML = "enter valid number";
    document.getElementById("numerror").style.color = "red";
    return false;
  } else{
    console.log("valid")
    document.getElementById("numerror").innerHTML = "valid";
    document.getElementById("numerror").style.color = "green";
    return true;
  }

}
function checkemail(){
  console.log("test")
  var emailentr = document.getElementById('emailentr').value;
  console.log(emailentr);
  if (emailentr.length == 1){
    document.getElementById("emailerror").innerHTML = "invalid";
    document.getElementById("emailerror").style.color = "red";
    return false;
  } else if(emailentr.length == 5){
    document.getElementById("emailerror").innerHTML = "test";
    document.getElementById("emailerror").style.color = "red";
  } else{
    document.getElementById("emailerror").innerHTML = "valid";
    document.getElementById("emailerror").style.color = "green";
  }
//
//   if (email.length == 0) {
//     document.getElementById("emailerror").innerHTML = "invalid";
//     document.getElementById("emailerror").style.color = "red";;
//     // return false;
//
//   } else{
//     document.getElementById("emailerror").innerHTML = "valid";
//     document.getElementById("emailerror").style.color = "green";
//     // return true;
//   }

  // if (!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)) {
  //
  //   document.getElementById("emailerror").innerHTML = "invalid";
  //   document.getElementById("emailerror").style.color = "red";
  //   return false;
  //
  }
