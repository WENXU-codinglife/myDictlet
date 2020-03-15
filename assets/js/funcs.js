
function myAudioFunction(rcs){
    let aAudio = new Audio(rcs);
    aAudio.play();
}

function extr(word,action) {
    var request = new XMLHttpRequest()
    let rcs = '';
    // Open a new connection, using the GET request on the URL endpoint
    var app_key = 'c1f42caf-a67f-46b9-aba6-e14c23e777e5';
    request.open('GET', 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + app_key, true)

    request.onload = function() {
    // Begin accessing JSON data here
        var mydata = JSON.parse(this.responseText);
        //console.log(mydata);
        let audio = mydata[0].hwi.prs[0].sound.audio;
        rcs = "https://media.merriam-webster.com/soundc11/" + word[0] + "/" + audio + ".wav";
        if(action = 'audio'){
            myAudioFunction(rcs);
        }else{
            let htmlText = '';
            let index = 0;
            for(let i = 0; i < mydata.length; i++){
                index = i + 1;
                //console.log('Sense ' + index + '\n');
                htmlText +='<p>' + 'Sense ' + index + '</p>';
                let jj = 0;
                for(let j = 0; j < mydata[i].shortdef.length; j++){
                    //console.log(mydata[i].shortdef[j] + '\n');
                    jj = j+1;
                    htmlText +='<p>' + jj + '. ' +  mydata[i].shortdef[j] + '</p>';
                    document.getElementById("definition").innerHTML = htmlText;
                }
            }
        }
    }
    // Send request
    request.send()
    
}
