function changeText(){
    var x = document.getElementById("where-to-find-me")
    var y = document.getElementById("emails")
    if(x.style.display === "none"){
        x.style.display = "block";
        y.style.display = "none";
    } else{
        x.style.display = "none";
        y.style.display = "block";
    }
}