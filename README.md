README.md<br/>

[Merriam-Webster Developer Center](https://dictionaryapi.com)<br/>
Registration:<br/>
E-mail: wenxuw@sfu.ca<br/>
Request API Key(1): Collegiate Dictionary<br/>
Request API Key(2): Collegiate Thesaurus<br/>

LOG:<br/>
20200221:<br/>

1. data.py: retrieve .json by using API;
2.index.html: date list of links to redirect to (date)-pages;
3. (date).html: button responding a click to play pronounce.

20200222:<br/>

1. Succeed in picking the "audio" key out from the json provided by the API;
2. fuction 'extr(word_id)' can return the url of audio file (.wav).

20200225:<br/>
1. The functions "playAudio" works, so all the buttons are able to use the this function to play the pronouciation of each distinctively;
2. Fix the url of the audio file in data.py.

20200226:<br/>
1. Extract the definitions and store them in a list;