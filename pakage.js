    function addNumbers() {
    var num1 = document.getElementById("num1").value;
    var num2 = document.getElementById("num2").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    var result = JSON.parse(this.responseText).result;
    document.getElementById("result").innerHTML = result;
}
};
    xhttp.open("GET", "/add-numbers/" + num1 + "/" + num2, true);
    xhttp.send();
}