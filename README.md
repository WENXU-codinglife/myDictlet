README.md<br/>
myDictlet: [clickme](https://mydictlet-0.herokuapp.com/)<br/>
This is a personal project that mainly make use of Python, HTML, JS, CSS, Heroku and PostgreSQL.<br/>

I have been working on this project, because, as an non-native English speaker, I have to keep learning and praticing English each single day. However, I have found that it is an obstale that I am used to memorizing English words by 'seeing' rather than 'hearing'. That is, sometimes I am able to recognize a word immediately when seeing it, but not when merely hearing it, even for those are quite commom like 'economic' or 'privilege'. So, I decided to make this handy tool to help me building vocabulary be directly connecting the pronoucation and definition without prioritizing the spelling. The new words are stored by the date and could reviewed anytime to check.<br/>

This is an easy-going web application deployed on Heroku so that it is accessable with any devices as long as the Internet is available. And the words are stored and managed with PostgreSQL as an Add-on in Heroku.<br/>
As I am self-taugth developing the entire project, I feel so excited and proud, even though it is not huge.<br/>

In next step, I plan to add registration module and provide individual 'vocabulary-base' for more English learners like me who are in need of it. Really hope it could help more people.<br/>

API: [Merriam-Webster Developer Center](https://dictionaryapi.com)<br/>
Registration:<br/>
E-mail: wenxuw@sfu.ca<br/>
Request API Key(1): Collegiate Dictionary<br/>
Request API Key(2): Collegiate Thesaurus<br/>

DevLog:<br/>
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

20200317:<br/>
1. Add favicon.
2. Vanish the "navPanel->undefined" in a dumb way.
3. Add some elements and styles, such as background image, demonstration box, copyright, "fold" button, etc..

20200319:<br/>
1. Add the error message, avoiding adding words which have already been added.

20200324:<br/>
1. 'CORS error', when using another API to add a new component---'Daily Quotes'.

20200409:<br/>
1. Fix the 'CORS error' in an easy way that I'd like to summarize later.
2. So the addtion of 'dailyquote' works well.

20200414:<br/>
1. Add a new div called 'Archive' with links redirecting to the previous words categorized by month;
2. So now the main 'flashcard' div only shows this month's words.

 <mark>RELEVANT STUFFS TO LEARN:</mark>
- [ ] Google for 'handlebar.js';
- [x] (20200301) Try to use javascript to realize fetching json from API; 
- [x] (20200302) Deploy on a web server;
- [ ] Clearify the concepts, modules, etc. of Heroku: [Procfile](https://devcenter.heroku.com/articles/procfile), [gunicorn](https://gunicorn.org/);
- [ ] Learn about: [pgAdmin](https://www.pgadmin.org/),[postgresql](https://www.postgresql.org/);
- [ ] Figure out what the "navPanel" is and where it is from;
- [x] [3 Ways to Fix the CORS Error](https://medium.com/@dtkatz/3-ways-to-fix-the-cors-error-and-how-access-control-allow-origin-works-d97d55946d9);