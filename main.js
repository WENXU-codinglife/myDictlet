var btn = document.getElementById("btn");
var app_key = 'c1f42caf-a67f-46b9-aba6-e14c23e777e5';
/*
function extr(word) {
    var url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + app_key;
    var myrequest = new XMLHttpRequest();
    myrequest.onreadystatechange = function(){
        if(this.status == 200){
            console.log(this.responseText[0]);
            return this.responseText;
        }
    }
    myrequest.open("GET", url, true);
    myrequest.send;
}
*/
/*
var output = '1';
fetch("./anomaly.json")
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        output = data;
        console.log(output);
    });
*/
var newword = document.getElementById("new_word").textContent;

btn.addEventListener("click", function(){
    console.log('newword');
    //document.getElementById("demo").innerHTML = extr(newword);
});

/*    
function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "./anomaly.json", true);
    xhttp.send();
    
}*/