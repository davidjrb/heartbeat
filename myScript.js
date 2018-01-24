
var myVar = setInterval(myTimer ,1000);
function myTimer() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "txt", true);
  xhttp.send();
}
