README.md<br/>
myDictlet: [clickme](https://limitless-retreat-15223.herokuapp.com/)<br/>

API: [Merriam-Webster Developer Center](https://dictionaryapi.com)<br/>
Registration:<br/>
E-mail: wenxuw@sfu.ca<br/>
Request API Key(1): Collegiate Dictionary<br/>
Request API Key(2): Collegiate Thesaurus<br/>

LOG:<br/>
20200221:<br/>

1. data.py: retrieve .json by using API;
2. index.html: date list of links to redirect to (date)-pages;
3. (date).html: button responding a click to play pronounce.

20200222:<br/>

1. Succeed in picking the "audio" key out from the json provided by the API;
2. fuction 'extr(word_id)' can return the url of audio file (.wav).

20200225:<br/>
1. The functions "playAudio" works, so all the buttons are able to use the this function to play the pronouciation of each distinctively;
2. Fix the url of the audio file in data.py.

20200226:<br/>
1. Extract the definitions and store them in a list;

20200229:<br/>
1. Run the Server.py and activate the local web server;
2. Load the content from a local json file by 'onclick' which makes a 'GET' request.

20200301:<br/>
1. Use javascript to realize fetching json from API;
2. finish the definition-presentation and sound-play on the index page.

20200302:<br/>
1. Deploy the app to Heroku.

20200306:<br/>
1. Switch the deployment source from Heroku git to github.

20200309:<br/>
1. Postgres.app has been installed locally.
2. Database has been created for 'mydicelet-0' and works. **(BUT VALUES OF 'DATE' ATTRIBUTE SEEM WRONG)**
3. Store and retrieve data on and from database.
4. Generate the flashcard list on 'index.html' automatically, which redirect to 'flashcard.html', according to the data passed from backend.

20200313:<br/>
1. Redirect from the links on 'index.html' to 'flashcard.html', passing the 'date' as parameter.
2. By loading page 'flashcard.html', the words can show up, accociated with 'edifier.svg' and 'lookup.button'.

20200314:<br/>
1. Basically, all functions designed have been realized. **(NEXT STEP: OPTIMIZAZTION/MODIFICATION/UI DESIGN)**
2. It is PI Day today!
3. COVID-19 is spreading, as well as panic and nonsense!

 <mark>RELEVANT STUFFS TO LEARN:</mark>
- [ ] Google for 'handlebar.js';
- [x] (20200301) Try to use javascript to realize fetching json from API; 
- [x] (20200302) Deploy on a web server;
- [ ] Clearify the concepts, modules, etc. of Heroku: [Procfile](https://devcenter.heroku.com/articles/procfile), [gunicorn](https://gunicorn.org/);
- [ ] Learn about: [pgAdmin](https://www.pgadmin.org/),[postgresql](https://www.postgresql.org/);