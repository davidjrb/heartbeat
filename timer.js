var myVar = setInterval(myTimer ,1000);
function myTimer() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    {
      document.getElementById("refresh").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "txt.xml", true);
  xhttp.send();
}