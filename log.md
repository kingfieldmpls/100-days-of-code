# 100 Days Of Code - Log

### Day 1: July 28th, 2018 - Saturday

**Today's Progress** 
* Finished Coursera's University of Michigan Python Course - Course 2: Python Data Structures : Week 5

**Thoughts** 
* Still burning through what is basically review material. I learned about using dict.get(key,defaultValue) as an idiom for creating histograms without throwing a traceback if you look for a key that isn't in the dictionary yet. I felt a little strange reviewing basics that I've known for a long time, but clearly without coding regularly there are still a lot of methods and constructions that are new to me with some of the most common elements of the standard library.

**Link(s) to work**
* [Day 1 Exercises](exercises/day1.py)

### Day 2: July 29th, 2018 - Sunday

**Today's Progress** 
* Finished Coursera's University of Michigan Python Course - Course 2: Python Data Structures
* Started Courera's University of Michigan Python Course - Course 3: Using Python to Access the Web: Weeks 1 and 2

**Thoughts**
* Got a better sense of how and when to use a tuple. Also learned that a major feature of tuples is that they're much more memory efficient because they hardly support any methods. 
* Figured out the difference between list.sort() and sorted()
* Really enjoyed watching interviews with the creators of jQuery and C++ and the "discoverer" of JSON.
* Also learned about "greedy" and "non-greedy" regex statements
* This part of the tutorial is still feeling relatively easy, though it takes me a minute to complete the exercises, especially the "just for fun" exercise which involved list comprehensions. Amazing, but for some reason sort of mind bending.

**Questions** 
* Study up on list comprehensions
* Learn more about primitives in different languages
* Learn more about the history of AJAX in different languages

**Link(s) to work**
* [Day 2 Exercises](exercises/day2.py)
* [More Day 2 Exercises](exercises/day2a.py)

### Day 3: July 30th, 2018 - Monday

**Today's Progress** 
* Finished Coursera's University of Michigan Python Course - Course 3: Accessing the Web: Week 3

**Thoughts**
* Man was today a slow mover. Got stuck figuring out why set localecho doesn't work how I expect with the wonky Windows Telnet client, and then went down a Python documentation rabbit hole. 
* Networking still confuses the hell out of me. I think it's largely a vocabulary issue. I want to unlock the mysteries, but I also question the usefulness considering how many amazing shortcuts already exist to do the tasks we want to do.

**Questions**
* What's the simplest way to grab HTTP headers in Python? urllib? requests?

**Link(s) to work**
* [Day 3 Exercises](exercises/day3.py)

### Day 4: July 31st, 2018 - Tuesday

**Today's Progress** 
* Completed the lectures, quiz and one of the two activities for "Using Python to Access Web Data"
* I'll need to finish up the second example and then reviewing to take any other questions down and make sure I understand what it is I'm doing.

**Thoughts**
* Today was a long day, and it was hard to muster the gumption to put in the time starting shortly before 11pm. I think it was worth it? I mean, I enjoyed doing the activity, but morning comes at the same time regardless of when I go to bed.
* Things are starting to get really fun. Grabbing data from the web is such a practical and powerful skill. I can't wait to start using Beautiful Soup in my own projects.

**Questions** 
* What's the standard to deciding exactly how to import a library or module - especially when it just comes to how you'll call the module, no necessarily how many modules you're loading
* How many sites really have scraping policies? Where is that info kept? Is it ethical to write a spider to check for scraping policies?
* I didn't understand the import SSL bit from the example

**Link(s) to work**
* [Day 4 Exercises](exercises/day4.py)
* [More Day 4 Exercises](exercises/day4a.py)

### Day 5, August 1st, 2018 - Wednesday:
**Today's Progress** 
* Completed BeautifulSoup activities from "Using Python to Access Web Data"
* Completed the XML chapter from "Using Pything to Access Web Data"

**Thoughts**
* Still having lots of fun. It's really easy to stay up too late. BeautifulSoup is lots of fun and it was a sort of boring right turn to parsing XML. I've used Xpath in the path, so I see the use, but I'm excited to get to JSON tomorrow.
* I refactored my sample code using with and enumerate to shorten the code and be more Pythonic. That felt really good.

**Questions** 
* What is the full syntax is XPath? Is it a lot easier than just formally walking the whole tree?

**Link(s) to work**
* [Day 5 Exercises](exercises/day5.py)
* [More Day 5 Exercises](exercises/day5a.py)

### Day 6, August 2nd, 2018 - Thursday

**Today's Progress** 
* Finished course 3 "Using Python to Access Web Data" in the Coursera Python speciality. 

**Thoughts**
* Really similar exerises as yesterday, except working with JSON instead of XML. It makes a lots of sense traversing series of dictionaries and lists in the json.dumps() object if you can read the JSON somewhere. 
* This course definitely started to enter the realm of the practical. It seems like for most applications you really don't need to know all that much about the libraries - there are just a few key methods that do 90% of the work.
* Sleep continues to be a thing that there is less of. I'm really enjoying this time, but there wasn't really free time per se, so I'm just paying for this course in fewer hours slept.

**Questions**
* OOP is still a huge question in terms of how it actually shakes out in Python land. Also, how do I get enough practical experience without coding for my job to learn the nuance, norms and intrigue of the language?

**Link(s) to work**
* [Day 6 Exercises](exercises/day6.py)
* [More Day 6 Exercises](exercises/day6a.py)

### Day 7, August 3rd, 2018 - Friday:

**Today's Progress** 
* Completed chapter 1 and part of chapter 2 of "Using Databases with Pythong"

**Thoughts**
* I actually completed this chapter's month's ago. Dr. Chuck's 15 minute video explaining object oriented programming was an actual breakthrough for me the first time a watched it earlier this year. It was neat to revisit and reflect on how these concepts have crystallized over time, and how hard things become known things relatively quickly if you can avoid the frustration of not fully understanding each new concept you encounter right away.

**Questions** 
* There is still A LOT I don't understand about OOP from a practical, functional level.
* I also don't really understand namespaces or what __init__ ought to be used for when creating a class. I mean, I understand it, but my brain isn't naturally thinking like that yet.

**Link(s) to work**
* The code I wrote today was for work. I think that's technically against the rules? It was one of those things where I was very confident it would work how I expected. It didn't. There were all sorts of modules in this SDK I was using that weren't updated to the latest version of the API and they weren't helping matters much. In the end I got it to work but I don't really understand how. The agony. The ecstasy.

### Day 8, August 4th, 2018 - Saturday:

**Today's Progress** 
* Completed the "Basic SQL" portion of Coursera's "Python for Everybody".

**Thoughts**
* I honestly don't remember doing the exercise for this chapter, but apparently I did successfully complete it earlier this year. What's crazy is we have code exactly like this example in prodution at work now, and it's so interesting to come back with the context of seeing how this application actually get put to use in the real world. I've also learned more about SQL injection attacks since watching this video the first time, which helps explain some of the wildcard insertions. 

* I also feel like this chapter is a significant increase in difficulty compared to previous chapters. You're also not expected to really produce much original code. If you can read the example, you can fairly easily modify it to work. It's reinforcing spaghetti code, which isn't what I need right now. Ha!

**Questions**
* I want to come back and work through the Twitter spider example at some point in the future. It wasn't required for the course so I moved on.

**Link(s) to work**
* [Day 8 Exercises](exercises/day8.py)

### Day 9, August 5th, 2018 - Sunday:

**Today's Progress** 
* Completed the second SQL chapter from "Python for Everybody" - minus the db example.

**Thoughts**
* I've finally made it back to where I initially started. Definitely feel a little smarter than the first time around, but also have more questions.

**Questions** 
* When is a project so small where you shouldn't worry about duplcating strings?

**Link(s) to work**
* No Python to show, just some things in the DB Browser for SQLite.

### Day 10, August 6th, 2018 - Monday:

**Today's Progress** 
* Completed practical example for Coursera/Python/SQL. 

**Thoughts**
* Today's assignement more or less begged spaghetti code. It was much easier to make it work quickly that to put it together properly. It met me at a place where I was looking to complete more than put rigor against the process. Today was probably a low point. But we'll see where tomorrow ends up.

**Questions** 
Need to review the data validation rules for different SQL implementations in order to actually understand how to do this work. I'll need to review this chapter before completing the capstone, I think. One good idea, just redo the chapter 3 assignment, but write the code from scratch, and ignore the sample code.

**Link(s) to work**
* [Day 10 Exercises](exercises/day10.py)

### Day 11, August 8th, 2018 - Wednesday:

**Today's Progress** 
* Complete "Many to Many Relationships in SQL"

**Thoughts**
* For whatever reason these chapter assignments are getting easier and easier. Too much is already complete in the sample files, and so it's fairly trivial to get them to work to the point where you can satisfy the auto-grader. 

**Questions** 
* What are all of the SQL conn object commands that you should know? How different are these commands between SQLite and MySQL? Does MariaDB have it's own cursor?

**Link(s) to work**
* [Day 11 Exercises](exercises/day11.py)

### Day 12, August 9th, 2018 - Thursday:

**Today's Progress** 
* Completed course 4, "Using Databases with Python", which just leaves the capstone.

**Thoughts**
* The challenge level in course 4 was generally very low. I guess maybe there is some incentive to keep completion rates high? Most of the examples took very little tweaking to run properly to complete the assignment. I did try to understand the code by reading it, but it's really not the same as writing it yourself.

**Questions** 
* How to Redshift and Hadoop work?

**Link(s) to work**
* [Day 12 Exercises](exercises/day12)

### Day 13/14, August 10th/11th, 2018 - Friday/Saturday:

**Today's Progress** 
* Man, Fridays are a thing, eh? I crashed hard just after the one hour mark. Completed most of the lectures for the capstone project week 2. 

**Thoughts**
* Getting to some really interesting concepts with creating a page rank algorithm from scratch. Unfortunately, as has been the case with the last few weeks of classes, they don't really ask enough of the students. The passive feels easier and more passive then some of the much more foundational courses. Nevertheless, trying to read and understand the code did count for something.
* I was asked to identify my own data source for the optional (read interesting) part of this process. I chose the .gov website for monitoring the flow of the Minnehaha Creek as well as Open Weather API to try to combine data from these two sources and make both historical observations and a predictive model for the future.

**Questions** 
* I'd like to learn more about both the concept of convergence and graph theory.

**Link(s) to work**
* [Day 13/14 Exercises](exercises/day13)

### Day 15, August 12th, 2018 - Sunday:

**Today's Progress** 
* Ok, now we're starting to have fun. I did complete the "Spidering and Modeling Email Data" chapter, but who seriously cares? Way, way, way too passive. I'm still trying to glean what I can from reading the code and watching the walk through examples, but it's really not super helpful.
* Began in earnest on my Minnehaha Creek watershed app. This is going to be fun. I read all of the USGS documentation during nap time, and tonight successfully read in and parsed all of the info I need.

**Thoughts**
* Steps happen slowly, but they do continue to happen. I'm not really getting stuck on anything. The next steps is for me to write all of this data to a database to get ready to start analyzing.
* I'd also like to include weather forecast data and maybe historical weather data to try to model when conditions will be ideal.
* Finally, I'll need to visualize the output, so I guess it's back to frontend for me? It feels really weird to leave Python behind for even a moment when I've come this far. I'll have to figure that out as I get there. 
* I was checking out Treehouse again today, and it looks like there are some good data science tutorials. I think I'll walk through those along with the Google Machine Learning and Coursera Machine Learning courses next. Ah! So many directions to choose from, it's paralyzing.
* Using count % 50 == 0 is a brilliant way to count interations

**Questions** 
* Tell me more about Python context managers

**Link(s) to work**
* [Start of the Minnehaha Creek flow tracker app](exercises/creek)

### Day 16, August 13th, 2018 - Monday:

**Today's Progress**
* Now we're cooking with gas. Minnehaha Creek data from USGS is all plumbed up and writing to the database, and I think all of the functionality I want (pretty much) is there. The one addition might be to look at last updated for the runs. I also would consider refactoring into OOP just for funzies, not because it actually does any work for me.
* I also identified NOAA as the source of my weather data. It turns out NOAA is the data source behind the national service and they have a fairly robust API available for free. It took quite a bit of time to figure out which values I needed to grab, but I did eventually get it done. I need to work out how pagination is going to work and then I can write everything to the database.

**Thoughts**
* This shit is really, really fun and addicting.

**Questions**
* How am I going to run these scripts regularly?
* Need to figure out linting for PEP8

**Link(s) to work**
* [Added NOAA weather API data source](exercises/creek)

### Day 17, August 14th, 2018 - Tuesday:

**Today's Progress** 
* Got openweather api and dark sky api weather hooked up to the db
* Spent a lot of time reading about capabilities and different methodologies. It's obvious NOAA rules them all.

**Thoughts**
* I really need to get my datetimes matched up if I want the hourly data to make any sense
* Still need to figure out how to model expected rain in terms of what the flow rate will be
* I'm not sure how to measure snow melt just yet, and that seems to have the biggest impact on flow
* Mega rain events in MN are fascinating. That was a fun side project.
* Learned about the UNIX 2038 problem

**Questions** 
* When is the best time to handle DT conversions?
* When might I want to use the gzip header
* How specific should I be in my app headers?
* Curious about National Weather Service and Dark Sky for forecast data
* I haven't worked out which I end I want ot use Dark Sky for - I think I'd like to compare forecast data with National Weather Service

**Link(s) to work**
* [Added Dark Sky weather API data source](exercises/creek)

### Day 18, August 15th, 2018 - Wednesday:

**Today's Progress** 
* Did some prioritizing on the creek project
* Read more docs on weather APIs
* Read Beautiful Soup docs and tried desperately to quickly grab table data
* Realized Beautiful Soup doesn't load JavaScript, so I'll need Selenium to grab what I need to scrape
* Wand and ImageMagick

**Thoughts**
* Today I didn't really 'accomplish' anything, but I did put the time in. I learned a whole lot about the Beautiful Soup package and a little about Selenium.
* This whole thing is getting really addictive. There is still the crushing feeling of all of the things I don't know, but I'm getting closer to the point where I can do meaningful things relatively quickly, and basically know my resources for learning completely new things.
* We're getting pretty far afield here, I think it may be time to reset some of the goals and next steps

**Questions** 
* Learn how to use the Selenium package
* Learn more about Pandas dataframes for quickly making sense of tables

**Link(s) to work**
* [Couple of tweaks and some early thought starters](exercises/creek)

### Day 19, August 16th, 2018 - Thursday:

**Today's Progress** 
* Got Selenium up and running
* Scraped the data I was looking for

**Thoughts**
* I'm fascinated by what possibilities Selenium opens up from an automation standpoint
* It is really, really easy to hand Selenium objects off to Beautiful Soup

**Questions** 
* How can I get rid of ads and just generally speed up page loads?
* What's the default behavior for page load? Can I set a time for when I think the DOM element will be ready?
* I need ot spend more time with Selenium's documentation

**Link(s) to work**
* [Start of scraper](exercises/creek)

### Day 20, August 17th, 2018 - Friday:

**Today's Progress** 
* Successfully grabbed WU data from the website and wrote to the DB
* Did some datetime magic, and figured out how to use a Firefox profile with add-ons installed

**Thoughts**
* I'm getting some timeouts with Selenium at home, I'm not 100% sure how to address those
* I still don't feel like I have a good handle on Selenium's documentation
* Sometimes progress is still slow going, but I'm not really getting completely stuck on anything

**Questions** 
* When would I want to use generators?
* What does iter_tools do?
* I still don't have my mind wrapped around list comprehensions
* Other reserved words I don't use much [yield, assert, lambda
* Add timing into specific components of the script
* Move from procedural to OOP

**Link(s) to work**
* [Successful pulling and writing to DB](exercises/creek)

### Day 21, August 18th, 2018 - Saturday:

**Today's Progress** 
* Cooking with gas with the weather scraper. Grabbed a whole year with no crashes. Added some exception handling.
* Watched videos on lambda functions, map functions and history of recursion

**Thoughts**
* I'm already worried about what I'll be able to do in 100 days. What about front end? What about mastering OOP and wrting more Pythonic code? What about ML? What about general math and stats knowledge? What about pandas and numpy?

**Questions** 
* The meet ups are fine. How do I get more immersed in local community?

**Link(s) to work**
* [Scraper is procedural, but well tuned](exercises/creek)

### Day 22/23, August 19th/20th, 2018 - Sunday/Monday:

**Today's Progress** 
* Flask, Pyramid and Django examples and reading. I still like Flask
* Spent more time in Plotly and legit figured out where they store the JSON and Python. My goodness. Got a decent looking multiple axis chart together.
* Got WU updated since 2010
* Working on the best way to map JSON to a database
* Expanding NOAA dataset
* Got NWS pull pretty much put together, just need to finish plumbing into the DB
* Also did more research on discharge calculations and wrote those into the notes
* Learned that pushing to forked repos doesn't count for anything

**Thoughts**
* I'm actually just gathering data here, but it may have use at work on the near future
* Getting anxious to visualize and wrap up this part of the coursera program and move into data science, machine learning, better OOP practices and web frameworks

**Questions** 
* When exactly would you want to use collections.namedtuple and how is it used?
* Why ORMs? Isn't writing SQL statements using a connector way easier?
* Need to figure out git.ignore

**Link(s) to work**
* [NOAA and NWS updated](exercises/creek)

### Day 24/25, August 21st/22nd, 2018 - Tuesday/Wednesday:

**Today's Progress** 
* Finished plumbing NWS
* Learned about PHP role based access control
* Setup linting with Flake8
* Found out I can fire dumb logs into /nul/ of any folder to make it disappear
* Finally read PEP8 https://www.python.org/dev/peps/pep-0008/ (mostly)

**Thoughts**
* My NWS forecast grid expired! Which makes it really hard to write the app, but nice to have the exception to reference
* Timer decorators
* \* unpacks tuples/lists (positional arguments) and \*\* unpacks dictionaries (keyword arguments)
* I should really ready this - https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control#ch01-getting-started

**Questions**
* Learn more about roles in Python web frameworks
* I think I'd like to tackle Flask soon, but ML and data science too! Ah!
* More functional programming: map, filter, itertools, functools, generators and decorators 
* Different types of imports - absolute v. explicit relative

**Link(s) to work**
* [NWS updated, numerous refinements and linted](exercises/creek)

### Day 26, August 24th, 2018 - Friday:

**Today's Progress** 
* Playing with refactoring some code
* Testing performance a couple of ways
* Learning some basics about importing, like how sys.path is resolved
*    It's looking in current dir first
*    There is a PYTHONPATH system variable that can be defined. Need to learn more about that.
* There is a difference between standard library and built-in modules
*    sys.builtin_module_names

**Thoughts**
* Turns out it would be a huge pain to turn my imperative statements into functions. Just for kicks I'd like to give it a try just to see how performance nets out.
* Man does an hour go by like nothing

**Questions** 
* I still don't really understand namespaces, packages and what the fine points of absolute, explicit and relative imports are.
* I think this is going to help me - https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
* tell me more about __init__.py
* How are import name conflicts resolved?

**Link(s) to work**
* [Minimal updates. Some linting](exercises/creek)

### Day 27, August 25th, 2018 - Saturday:

**Today's Progress** 
* Big lessoned learned, if you're calling a script directly, you can't traverse above it's current directly unless you've defined it in PYTHONPATH or sys.path. If you start something higher up the hierarchy and that file need to import back up the tree, you can do that, but it's best to use absolute imports and walk all the way back down the tree
* It seems so simple now, but running a file directly just imports it as "__main__". That's all.
* Flake8 throws a redefinition error if I reassign something I've imported from another module (function, variable, etc)

**Thoughts**
* You can just import any object, right?
* An hour really is nothing. The thought are all there, but apparently it takes me about an hour to start the engines and then any more time I would need after that to really rev the engines.
* Want to get back on Slack tomorrow

**Questions** 
* Tell me more about __package__ - it looks like you can set this variable to help figure out how to walk down the tree

**Link(s) to work**
[Some little sample files to figure out imports](exercises)


### Day 28-30, August 26th - 28th - Sunday - Tuesday:

**Today's Progress** 
* Reading up on generators, decorators and context managers - thanks PyCon AU 2018
* Using PIL and Tesseract
* Using help('string') is like being in the help interface and issuing a command - neat
* PIP names are often different from their actual module names you can import

**Thoughts**
* Really just need a lot more time practicing writing functions. My whole Coursera thing was great for a lot of reasons, but getting practice thinking about actual design and higher level objects wasn't a thing that happened.
* Positional arguments have to come before keyword arguments. If you provide defaults, the arguments are optional.

**Questions** 
* Where can you view help for functions and what arguments can be passed and if they're positional or keyword and if they're required or not from the command line?
* What are the finer points of keyword and positional arguments? If a KW arguments is None, can you just pass in arguments as if they were positional? If you set default arguments for keyword arguments, how do you overwrite those? 
* Can you have required keyword arguments? Yes, PEP 3102, use a *
* Read more about how docstrings work for individual lines in code, functions, methods within classes, etc.
* Using Vi or Vim
* Ghostscript, OpenVC, textract, Pandas, my god the list just keeps growing
* How do you install from tar.gz?

**Link(s) to work**

### Day 31, August 29th, Wednesday:

**Today's Progress** 
* Got the new version of Tesseract 4 running!
* Learned how to basically use GIMP
* Spent time in Wand and pytesseract learning more of the libraries
* Read quite a big about ImageMagick and OCR
* Going into OpenCV and Numpy - why not?!
* Finally got back to doing some work on the creek project - I really suck at object oriented programming

**Thoughts**
* Still need to figure out pre-processing of an image - how to do it efficiently
* Want to setup a config file for tesseract

**Questions** 
* What are the advantages to running Tesseract from the command line?
* How do you train tesseract?
* Is it weird to mix local and global scope of variables, or is it OK to initialize and then run with the new variable keeping track locally?

**Link(s) to work**
[Some progress back on creek, but I need to map logic again](exercises/creek/procedural)

### Day 32/33, August 30th/31st, Thursday/Friday:

**Today's Progress**
* Finally wrapped up turning all my imperative statements in one NOAA script into functions. It didn't actually add any performance, but it helped me get more practiced in this sort of design. My brain is coming around.

**Thoughts**
* Felt good to be back in the main project again. It's amazing how quickly you loose momentum if you change gears onto a different project.
* Still a bit daunted by all of the basics left to cover and getting anxious to move onto the next project, but dedicated to crossing the finish line on this one.

**Questions** 
* Time to put on the finishing touches:
 * Logging
 * Unit testing
 * Docstrings
 * Command line arguments

**Link(s) to work**
[Mostly completed refactoring one script](exercises/creek/procedural)

### Day 34/35, September 1st/2nd, Saturday/Sunday:

**Today's Progress** 
* Cory Schafer is just the absolute best. I watched both of his videos on logging 1+ times.
 * https://www.youtube.com/watch?v=jxmzY9soFXg
* Read the "Basic Python tutorial" and other major portions from Python.org documentation
 * https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
 * https://docs.python.org/3/library/logging.html#logging.Formatter
  * Esp. 16.6.7. LogRecord attributes
* Read the foundational PEP on docstrings, but it seems like the community has adopted a whole host of other conventoins by this point - https://www.python.org/dev/peps/pep-0257/
* Figured how how to handle exceptions with logging
 * Services like MySQL and Requests have methods built in to help you catch exceptions in real time without have to try too hard to identify them yourself

**Thoughts**
* Formatting logs uses the old style %s which is very annoying
 * Truncating and padding using -5.5s is confusing. Can you format adding timestaps with more modern string formatting, or even f strings?

**Questions**
* When do you want to use stdout v. a log file? Or both?
* What are good visualizations tools for log files?
* What's a goog Sublime course for Windows? It looks like Corey has a thing.
 * https://www.youtube.com/watch?v=9FPFogHkgOc
* Best ways to add timestamp formatting in logs?
* Where is rccron.log hanging out?
* It sounds like Google and NumPy have their own style of docstrings. What all is convention. Like when do you write about exceptions. And when do you mention if a parameter is required, or what a default value is? How verbose do you need to be when the output of the script is obvious?

**Link(s) to work**
[Docstrings complete](exercises/creek/procedural)

### Day 36/37/38, September 3rd/4th/5th, Monday/Tuesday/Wednesday:

**Today's Progress** 
* Learning about unittest
* Requires test_[moduleName]
* Read through pytest - seems better
* Finished converting NWS forecast to procedural
* Refactored USGS data sources - just WU remains

**Thoughts**
* Need to watch all of the Corey Schafer OOP vids
* Take a look at pytest for comparison
* Doing cleanup and maintenance takes a lot longer than just making something work
* Getting code "production ready" is really where the "work" comes in

**Questions** 
* what about PDB again?
* What are all of the Python command line arguments? -m for example
* How do I use the Sublime multi-cursor?
* from unittest.mock import patch seems important for simulating pulls from APIs
* Timing completion of each function call
* Creating progress bars in the command line

**Link(s) to work**
[USGS largely refactored](exercises/creek/procedural)

### Day 39, September 6th, Thursday:

**Today's Progress** 
* Ran the rest of the Creek daily
* Began refactoring WU historical

**Thoughts**
* Golf short game analogy is holding on strong. This is much less mentally taxing that writing the code in the first place. At least all of my code is still legible to me, but it takes a minute to remember what's what. That says something about writing imperative style code. 
* It's just about practicing in order to get faster and think more in a certain way. No doubt the code gets faster to maintain by the end.

**Questions**
* Getting really curious about the web server side of all of this. Where does the codebase run from? How does it inform a front end?

**Link(s) to work**
[WU refactoring in progress](exercises/creek/procedural)

### Day 40, September 8th, Saturday:

**Today's Progress** 
* Refactored last bit of the original code for WU
* Used urllib instead of Requests to encode URLs because I didn't actually want to make a GET request to the page, I just wanted to the encoded URLs

**Thoughts**
* Could keep doing cleanup forever - refactored function and variable names according to PEP8, that stuff actually isn't reported by the linter
* Actually do need to figure out how to report on the creek hourly data set so that I can do my analysis and close out that section of the Coursera journey
* I talked about PyBites, Talk Python to Me's course, Coursera's Machine Learning, Google's TensorFlow, more Treehouse training and then the whole wide world of front-end. Where do I go next?
* I want to keep pushing on this stuff forever, but it's hard to keep everything in balance. There are things I've missed during these last weeks already, but I'm really questioning where the time comes from

**Questions** 
* I'm questioning when to just jump back into front end web development. It's clear that so much of what's going to be useful to me exists in the space - such as really be proficient with the basic Chrome developer tools, understand web servers (especially Apache) and just applying my knowledge of OOP and coding paradigms to JavaScript again.

**Link(s) to work**
[WU refactoring largely complete](exercises/creek/procedural)

### Days 41-43, September 9th-11th, Sunday-Tuesday:

**Today's Progress** 
* Tried to figure out a command line progress bar - minimal progress
* Compacted the database
* Did some creek hourly clean-up
* Built the progress bar
* A bunch of clean-up and fixing shit in creek hourly
* Some last minute work database management. Loaded a model, which made sense and felt good.

**Thoughts**

**Questions** 

**Link(s) to work**
[DB work and progress bar sort of installed](exercises/creek/procedural)

### Day 44, September 12th, Wednesday:

**Today's Progress**
* Going through Corey Schafer's OOP tutorials. Helpful!
* Important info on using super(). to extend classes but keep the code DRY and reuse parent code
 * Python OOP Tutorial 4: Inheritance - Creating Subclasses

**Thoughts**
* Class.method(instance) is the same as instance.method()

**Questions** 
* Learn about PR etiquette - what's the proper way to comment, submit, merge from master, merge into master, how do you handle situations where the codebase has changed since the PR and has to be remerged? How do you submit one little tweak?

**Link(s) to work**

### Day 45, September 13th, Thursday:

**Today's Progress**
* Attended Python Meet-up at Buzzfeed
 
**Thoughts**
* It's can be a very awkward community
* Talks included:
 * Writing cleaner code. It was a really great marker of time for how far I've come already. I knew almost all of the tools and best practices discussed. I marked "Eradicate" as a potential useful linting tool to check out.
 * Talk on using Python to do data modeling with ARIMA. There was a whole lot of vocabulary I was hearing for the first time, so it was pretty hard to intimately follow. Learned about errors in time series and data bias. That was interesting.
 * Using Geopandas and Follium for GIS. That was pretty interesting. The speaker appeared to be a U grad student. His demo showed using publicaly available GIS data (like parks and neighborhoods) to calculate the neighborhoods with the most parks, then visualized in a choropleth. Also a good demo of jupyter notebooks. 

**Questions** 
**Link(s) to work**

### Day 46, September 15th, Saturday:

**Today's Progress**
* Tough to fit in much with a busy start to the weekend and a show that night, but I got an hour of Corey Schafer and configuring my Sublime environment.

**Thoughts**
**Questions** 
**Link(s) to work**

### Day 47, September 16th, Sunday:

**Today's Progress**
* Had to setup my Macbook since I left my laptop at work. Not too painful, and good to see how quickly I could apply what I learned to the Mac OS.
 * In the process of setting up the Mac I learned about soft links and what python v. python3 and pip v. pip3 are things
 * Setup new builds in Sublime text
* Watched Kenneth Reitz's PyCon 2018 talk on pipenv - which was also a helpful history of package management in Python in general.

**Thoughts**
**Questions** 
**Link(s) to work**

### Day 48, September 17th, Monday:

**Today's Progress**
* I did it. I finished the Coursera course. Heck yes.
* Fired Plot.ly back up and man oh man have they improved Chart Studio
* Drummed up a quick script to write some SQL into a new table after doing some transformation
* Learned about datetime functions in SQL

**Thoughts**
* I spent pretty much 30 days on the capstone project in self-directed study. That was a really fun thread to pull. I think I'll hop back into something more structured for a bit until the next logical project jumps out.
* As I put a bow on the Coursera work, it was amazing how my ability to understand Charles' code as well as my impression of its quality changed over time.
* I'm excited for the point that the project is at now to be a jumping off point for applying new knowledge at a later point in this journey.

**Questions** 

**Link(s) to work**
[More or less the final version for now](exercises/creek/procedural)

### Day 49, September 18th, 2018 - Tuesday:

**Today's Progress**
* Reflecting and gearing up for the second half

**Thoughts**
* Wrestling a little bit with where to go from here. I think I'll take a little break from Coursera. Here are the things I said I'd like to learn in my intial Tweet:
  * Goals: 
   1. Gird loins - CHECK
   2. Complete Coursera University of Michigan Python course (currently Course 2: Week 5) - CHECK
   3. Complete 100 Days course from @pybites and @TalkPython (I’m getting a running start) 
   4. Discover 20 new (to me) libraries - I should try to list these out, I bet I'm getting somewhat close. Ok, actually I need a new goal. I've just completely blown that one out of the water. Here's the list so far - plus a wrote a script to keep checking on my progress:
    1. import bs4
    1. import codecs
    1. import csv
    1. import datetime
    1. import dateutil
    1. import json
    1. import logging
    1. import math
    1. import pathlib
    1. import os
    1. import re
    1. import requests
    1. import socket
    1. import sqlite3
    1. import ssl
    1. import string
    1. import sys
    1. import time
    1. import unittest
    1. import urllib
    1. import webdriver
    1. import xml
    1. import zlib
   * Of the above, I think I have some depth (relative) of knowledge about 9
 * Taking a hot minute to re-orient for the back half of the challenge
* Other things on the bucket list:
 * This University of Michigan Data Science Course
  * https://www.coursera.org/specializations/data-science-python#courses
 * This IBM Data Science Course
  * https://www.coursera.org/specializations/ibm-data-science-professional-certificate
 * Picking up where I left off with Treehouse
  * Flask course - https://teamtreehouse.com/library/type:course/q:python
 * Google TensorFlow thing
  * https://developers.google.com/machine-learning/crash-course/
 * Setting up a Python development environment
  * https://www.youtube.com/watch?v=xFciV6Ew5r4

**Questions** 

**Link(s) to work**

### Day 50, September 19th, 2018 - Wednesday:

**Today's Progress**
* Pulled the trigger on Talk Python to Me's 100 days of code program
* Learned about os.walk and then immediately decided pathlib is much, much easier to understand and use
* Creating a script to look at every library I import to help answer some of the above questions
* You can use list(dictionary or generator) to create a list from that object.
* Reviewed list comprehensions ... again
* Using pipenv to try and manage dependencies for this TPTM course
* Learning about the Mac terminal and alias to simplify python3 and pip3
* Got homebrew all setup
* Basically just learning more about using my mac at a high level

**Thoughts**
* So excited to dive into Jupyter notebooks
* Still want to review the PSF Python tutorials
* I really hope this course offers enough challenge and hammers home a lot of things I've been working on and techincally understand, but haven't worked with enough to really have reinforced
* Add PyBites slack

**Questions**
* Really curious to learn a lot more about homebrew
* learn more about sudo and chmod
* learn move about unix command line in general, like how > dumps the contents of something into something else
* why did homebrew just install python again? Now do I have 3 version of python on my machine? What the hell is going on here?
* Oh man, this mystery Python 3.7 is confusing
* Ok, I found the cellar, and updates the .bash_profile to set usr/local/bin, but I'm still so confused
* Need to learn more about homebrew link and the flags - that's what eventually did it for python
* Why does launch terminal in folder not follow my terminal preferences?
* Is there still a sneaky version of python 3.6 somewhere on my mac?
* Did I mention wanting to learn more about mac shell yet?

**Link(s) to work**

### Day 51, September 20th, 2018 - Thursday:

**Today's Progress**
* Completed days 1-3 of Talk Python course

**Thoughts**
* The .seconds attribute in a timedelta object only refers to the hours value and not the days value. Interesting.
* There's really only a few attribute in datetime, date and timedelta objects. You have to keep track of which positional arguments are where when dealing with the input and output.
* Actually really happy with this approach so far. 
* There is a difference between readline() and readlines()
* This list comprehension solve for Bite 7 - so good!
* Really happy with the level of challenge

**Questions** 
* Set Sublime default to 4 spaces
* Global and local scope in functions. How come I can append to a global list but change re-assign a global variable without first invoking the global keyword?

**Link(s) to work**
Not sure how to link to a different repo - I'll figure it out

### Day 52, September 21st, 2018 - Friday:

**Today's Progress**
* Basically lots of no progress on pomodoro
* I wrote 160 lines of code, but it's not fully functioning because I kept changing my mind on how to structure the functions and also kept add features.

**Thoughts**
* Figure out what's in a function and what's in what function is super confusing for me. That thoughts process can be interminable, but also interesting and challening.
* I need to move on to the next day and come back to pomodoro, but I hope I'm not creating a back log for myself.

**Questions** 

**Link(s) to work**
Link to Pomodoro once I figure that out

### Day 53, September 22nd, 2018 - Saturday:

**Today's Progress**
* Back into day 4 - going to have to come back to pomodoro
* New vocabulary
 * Things from the Collections module
  * NamedTuple - It's sort of like a dictionary with key value pairs, except they're tuples and you can reference the values using dot notation on the keys. It's like defining a class without methods.
  * DefaultDict - Build up a nested data structure and avoid key errors - key ares initialized before appending values
  * Counter - My god, it just takes an iterable, there are probably multiple methods, the one we saw is "most_common" and then you pass an argument for how many results you want
  * Deque - Inserts at both ends of a list - most performant than a normal list
  * timeit - IPython and Python module for timing small bits of code
* Getting a few more glimpes inside Jupyter notebooks

**Thoughts**


**Questions** 
* What does a sorted dictionary output?
* Don't fully grok "key=lambda x: x[1]"
 * https://dbader.org/blog/python-lambda-functions
 * Ok, thank god, this make sense now I can sleep - https://docs.python.org/3/howto/sorting.html

**Link(s) to work**

### Day 54, September 23nd, 2018 - Sunday:

**Today's Progress**
* Working on PyBites Challenge 13. Cheating quite a bit, but still doing it myself and learning. Reading the docs but also referencing the Jupyter notebok.
* csv.DictReader uses the first line of a CSV by default to set the keys so you don't have to work about referencing those each time. Seroiusly helpful.

**Thoughts**


**Questions** 


**Link(s) to work**

### Day 55, September 24th, 2018 - Monday:

**Today's Progress**
* You can pass lots of objects into a named tuple, not just a string of keys with spaces between them. You can pass a tuple, a list, etc. Direct quote from PSF 
 * "The field_names are a sequence of strings such as ['x', 'y']. Alternatively, field_names can be a single string with each fieldname separated by whitespace and/or commas, for example 'x y' or 'x, y'."
 * Packing and unpacking tuples now makes sense too:
```
    >>> b = ("Bob", 19, "CS")    # tuple packing
    In tuple unpacking, the values in a tuple on the right are ‘unpacked’ into the variables/names on the right:
    >>> b = ("Bob", 19, "CS")
    >>> (name, age, studies) = b    # tuple unpacking
    >>> name
    'Bob'
    >>> age
    19
    >>> studies
    'CS'
    >>> for director in d:
    ...     for item in d[director]:
    ...         print(item.score)
```

**Thoughts**
* Fail at getting my lists separate for calculating mean


**Questions** 


**Link(s) to work**


### Day 56, September 25th, 2018 - Tuesday:

**Today's Progress**
* Just putting time against understanding directors.py solution as well as defaultdict, namedtuple and counter. Deque is sort of falling my the wayside here.

**Thoughts**
* Talk Python to Me is really the greatest challenge yet. I thought I was going to breeze through the early days, but really by the time I get to the practical stuff there is a lot of reading the PSF docs, rewatching the tutorials, checking out the PyBites challenge repo and experimenting in the command line that takes place to facilitate something that feels like learning.

**Questions**
* I don't totally understand the square bracket notation for counter:
```
    # Counter w/ helper function
            cnt = Counter()
            for director, movies in directors.items():
                if len(movies) >= MIN_MOVIES:
                    cnt[director] += _calc_mean(movies)
```
* I don't really understand anything about this string formatting mini langauge
 * https://docs.python.org/3/library/string.html#formatstrings

**Link(s) to work**
* Link to directors.py, again once I figure out how markdown works cross-repo


### Day 57, September 26th, 2018 - Wednesday:

**Today's Progress**
* Completed the directors PyBite challenge. Just a little formatting to round things out. It's not totally polished, but that can be a task for another day. I'm excited to keep on expanding those horizons in the near future.
* Did my Day 6 task which was just to pracice counter, defaultdict and namedtuple on my own. Still a little hazy on how to thing of these collections first, but definitely have a handle on using them from a technical perspective.

**Thoughts**
* Deque can just be used instead of a list.

**Questions** 


**Link(s) to work**

### Day 58, September 27th, 2018 - Thursday:

**Today's Progress**
* Finished days 4-6 vids. Meh.

**Thoughts**
* What in the world were the Python data structures vids doing? If you can make it through Days 1-3 in collections, you can't possible have use for days 4-6. I'm sure the challenges will be challenge, but holy uneven.
* Assigning a list sort to a variable isn't going to work out well
* The sorted method is really awesome and better than list.sort() and accept lots of amazing helper functions for the keys such as len and lambda
 * https://docs.python.org/3/howto/sorting.html
 * https://docs.python.org/3/library/functions.html#sorted

**Questions** 
* Memorize how slicers are exclusive v. indexes are zero. The whole OBOE thing is real.


**Link(s) to work**

### Day 59, September 29th, 2018 - Saturday :

**Today's Progress**
* Just watched the pytest vids

**Thoughts**
* There was A LOT of stuff I didn't recognize, and the days 2 and 3 challenges are a bit more open ended. This is going to be a hard segment.
* Seeing all of the examples in vim and not really being familiar with vim also hindered mental dexterity

**Questions** 


**Link(s) to work**

### Day 60, September 30th, 2018 - Sunday:

**Today's Progress**
* Setup the challenges repo
* Installed pytest and pytest-cov
* I'm going to get totally stuck just figuring out packaging - I should just dump in the same directory and start to figure out the basic pytest syntax
* Ok, so what I've done is import packages in the Python interpreter in "interactive" mode. It sounds like there is a lot more to package in terms of what's installed and what's on path - like putting a package somewhere on PATH is going to matter lots and lots
* Ran a VERY simple pytest using just a single script without any imports

**Thoughts**
* This resource already saved me - how to stucture your app so pytest works how you expect
 * https://docs.pytest.org/en/latest/goodpractices.html#test-discovery
* Possibly also helpful
 * https://realpython.com/python-modules-packages/


**Questions** 
* What does "installing code" mean for the pidly shit I'm running? Apparently this can be done with virtualenv (probably pipenv) and pip as well. This allows some sort of access to imports that currently have to get hacked together with sys.path stitching and other tom-foolery
* How is PATH setup on the Linux box, since CodePros is using explicit relative imports
* Why do you ever need to refer to the current directory using . instead of just using an absolute import?
* What's the deal with using tox to automate testing?
* What's a good way to just structure testing, or is it best just to execute from the command line?

**Link(s) to work**

### Day 61, October 1st, 2018 - Monday:

**Today's Progress**

**Thoughts**
* Using absolute imports going down directories is fine, but moving up directories using explicit relative imports is much much harder to me
 * https://realpython.com/python-application-layouts/
* Real Python is being real helpful again. This is a guide on writing unittests for scripts that read from APIs
 * https://realpython.com/testing-third-party-apis-with-mocks/
  * Ok, this article is very good and I'm making progress, but I'm not going to make it to Bob's article on fixtures tonight, which means I'm going to fall behind on my 100 days with Talk Python schedule.
* My goal is to finish test_noaa_historical, which will require using fixtures. I feel like there is no way I can complete that task tomorrow
* Looking ahead to some future days, it looks like there is a lot more familiar territory ahead (and some totally new stuff as well). I'm starting to lose hope in actually wrapping this project in 100 days, but I think I will be able to crawl back somewhat.

**Questions** 

**Link(s) to work**
* Link to my pytests

### Day 62, October 2nd, 2018 - Tuesday:

**Today's Progress**
* Tests are supposed to be independent so you can run them in any order
* I got a fixture working!
* Watched classes vods and fixed game so you can actually win

**Thoughts**
* I honestly need to watch Corey Schafer's OOP vods again

**Questions** 

**Link(s) to work**

### Day 63, October 3rd, 2018 - Wednesday:

**Today's Progress**
* Finished the rock, paper, scissors game. It totally works, but there is still so much functionality to you could add, it all just seems like a pain in the ass when I'm not really learning anything new by doing it. 
* I extended the intial class to accomodate 15 way rock paper scissors, and that seemed to work pretty well
* Videos for list comprehensions and generators
* The lesson learned with generators is basically that anything you create an empty list and then you're appending items to that list one by one, you could just create a generator. Generators are also way faster over across massive data sets.
* Completed day 2 activities
* Completed by 5 and 26

**Thoughts**
* Try to do the same thing I just did writing this 15 way dict by hand just using Python to create the output.
 * It was easy to get an ordered dict, but the logic wouldn't have worked the same way, so I still would have needed to write more code to get the same exact output
 * It would be great to try to force myself to think in terms of lambda functions

**Questions** 
* Challege 11 is about the UNIX pipeline, which I think I'll skip for now. It's relevant, it just represents a rabbit hole I don't want to go down at this exact moment. What's funny, is that I already built basically this exact same script earlier
 * https://en.wikipedia.org/wiki/Pipeline_(Unix)
 * https://pybit.es/generators.html
* Ok, I'm changing my mind. Maybe I should rewrite my 100libraries.py now based on using generators and comprehensions, plus I could also add in the logic about the different syntax you can use for importing
* Ok FINE I'll come back to challenge 11 before moving on - and I'll read the damn article

**Link(s) to work**

### Day 64, October 4th, 2018 - Thursday:

**Today's Progress**
* After doing some wacky things to my GitHub repo due to large file sizes, it's clear I need to upgrade my Git knowlege.
 * Commands beyond add, commit and push
 * Using .gitignore
* Read generator articles from PyBites - also read an itertools article linked from the generators article

**Thoughts**

**Questions** 

**Link(s) to work**

### Day 65, October 6th, 2018 - Saturday:

**Today's Progress**
* Read the Pipeline (Unix) Wikipedia article.
* Reviewed challenge 11 - changed my mind again, but I know basically how I would use a generator in the future
* Watched itertools videos
* Played with zip
* Generators only play through once, then they're exhausted
* Any object with a __iter__ magic method is iterable, check out dir(object)
* There's also an iter() method built into Python to call this method
* cycle just creates an infinite loop of an iterable
* product is cartesian product
 * https://en.wikipedia.org/wiki/Cartesian_product
 * It's positional, so it doesn't dedupe
* Permutations and combinations seems like something I should have used recently. Combinations is just all of the possible combinations, regardless of order, and permutations is every posssible combination in all possible orders.


**Thoughts**

**Questions** 

**Link(s) to work**


### Day 66, October 7th, 2018 - Sunday:

**Today's Progress**
* Cracked 2 itertools bites, that were rather easy
* Got stuck on the 3rd after referencing the tests. Once again, I built something that I think actually works, but didn't pass the tests. Sometimes the instructions aren't perfectly clear. After reading the tests, now I know that I need to generate words from any length within a given string. I think I could actually do this with regex, but I believe the bite wants me to solve it with product. Got tired, so starting here tomorrow.

**Thoughts**

**Questions** 

**Link(s) to work**

### Day 67, October 8th, 2018 - Monday:

**Today's Progress**
* Basically just beat my head against bite 65 all night, trying to take a list of letters and see what words from the dictionary are contained in those letters rearranged in any combination
* I had lots of false starts using product, and even found a couple of solutions which sort of worked, but either took a long time to process and overflowed the stack
* Ultimately, I remembered that permutations takes a second argument that lets you specify how many items from the original set to run permutations on.
* I'm a little salty that the ultimate sample solution harded coded the number of items in the string, that's kind of cheating
* One thing from the final answer which I thought was really elegant was using set & set to just get the shared members of the dictionary and the permutations. That's a smart solution that I never would have thought of.
* Overall, this was easily the most challenging bite so far.

**Thoughts**
* I still don't really have my head wrapped around generators being passed to other functions and just running. I need to do more of that hands on to understand.
 * Think I got it. You trade a for loop now for a for loop later.

**Questions** 

**Link(s) to work**

### Day 68, October 10th, 2018 - Wednesday:

**Today's Progress**
@wraps makes sure that if you are putting a decorator on a function, you still get the wrapped function's docstrings back, otherwise you'd get the decortors docstrings(?) since that's the function that is be instantiated first.
* Watched decorator vids
* Completed Bite 22
* Read these articles:
 * https://pybit.es/decorators-by-example.html
 * https://pybit.es/decorator-optional-argument.html
 * https://realpython.com/primer-on-python-decorators/

**Thoughts**

**Questions** 

**Link(s) to work**

### Day 69, October 12th, 2018 - Friday:

**Today's Progress**
* Back at decorators article from Real Python
* This snippet
 * Three conversion flags are currently supported: '!s' which calls str() on the value, '!r' which calls repr() and '!a' which calls ascii().
 * https://docs.python.org/3.7/library/string.html?highlight=string#module-string
* Holy, just realized "unsigned" means positive because it means it is un (positive or negative) signed.
* Also curious to play more with Format Specification Mini-Language - which is the formatting syntax that starts with ":"
* You can enforce this with the special * syntax, which means that all following parameters are keyword-only:

**Thoughts**

**Questions** 

**Link(s) to work**

### Day 70, October 13th, 2018 - Saturday:

**Today's Progress**
* Wrote a decorator of highly questionable value, it checks if a database table exists each time it runs. It would actually be better to decorate the "main" function with this decorator it just occurred to me. Anyway, it works and I have some basic concepts down so I'm moving on.

**Thoughts**
* This TalkPython course is going to take me well past 100 days. I think I'll keep on but then turn down the accountability piece a bit. I want to re-orient myself in all of my notes and set a plan forward for my next actual project.
* So, came across pathlib again yesterday. So weird. It's only been a couple of weeks since I spent an hour figuring it out, I recognized the library name, but didn't really remember how to do anything. I'm sure it would come back to me, but is this survey still moving too fast? Do I actually just need to use one thing at a time long enough to regard it as an old friend before moving on?


**Questions**
* What are my "triggers" for "this would be a good place to write a decorator"?

**Link(s) to work**
wu_historical

### Day 71, October 14th, 2018 - Sunday:

**Today's Progress**
* Using try/except on NOAA scripts. I think I figured out basic Requests exception handling. I also saw that it's relatively easy to just figure out eveything that might break. 
* There seems to be a try block where the exception isn't being caught by except just naked and I really have no idea why. It doesn't actually make any sense to me
* This article is helping:
 * https://realpython.com/python-exceptions/

**Thoughts**
* ZOMG, I didn't realize that the try catch was working, but logging.exception was doing something different than I thought. Sometimes I'm still a real dumb dumb

**Questions** 

**Link(s) to work**

### Day 72, October 16th, 2018 - Tuesday:

**Today's Progress**
* Finished getting stuff in NOAA historical properly setup for catching exceptions
* This section of requests was super helpful, but I still needed a trusty example for SO to totally understand what the raise_for_status() method was up to - http://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions
* I generally feel comfortable using try/except, but I don't really have a clear framework in my mind for where to put all of the blocks.
* You can throw a "raise" at the end of an except block to re-raise and exception after you've done some other stuff to deal with the exception
* "else" runs code after except if try didn't raise and exception
* "finally" performs the clean up bit and just run regardless of whether an exception was thrown or not - if you re-run the exception, finally just first before the exception - which makes sense

**Thoughts**
* logging.exception pastes the message along with the element - https://docs.python.org/3/library/logging.html

**Questions** 
* At what level to folks typically log their exceptions? You can use "exception" but then it writes the whole damn Traceback. I'm using error now, which seems good.

**Link(s) to work**

### Day 73, October 17th, 2018 - Wednesday:

**Today's Progress**
* Watched regex videos
* Search and match
 * Match needs to match a whole string
 * Search can match a substring
* Always use rawstrings so you don't have to escape as much junk
* Using () or (?) will set capturing and non-capturing sets
* re.compile lets you save a statement object into a variable, and then you can just operate on the variable
* re.VERBOSE is a flag that ignores comments and spaces so you can split out the whole regex and add comments for readability, because they can get very complicated.


**Thoughts**
* String methods like "startswith", "endswith", "contains" and even just good old "in" cna be used in a lot of situations, so don't forget dir(str) methods

**Questions** 

**Link(s) to work**


### Day 74, October 18th, 2018 - Thursday:

**Today's Progress**
* Read https://pybit.es/mastering-regex.html
* Watched Al Sweigart's PyCon talk
 * https://www.youtube.com/watch?v=abrcJ9MpF60&feature=player_embedded
  * Compile -> Search -> Do something with group method
  * The basic regex syntax is pattern => qty
  * Video is a really solid foundation
  * No ? for greedy, ? for not greedy

**Thoughts**

**Questions** 

**Link(s) to work**

### Day 75, October 20th, 2018 - Saturday:

**Today's Progress**

**Thoughts**
* findall still seems like the most useful thing to every use. Match makes sense if you're looking at well defined strings. Search returns a search object, which then you need to do something with whereas findall just gives you everything.
 * Oh yeah, use group, just like the awesome YouTube PyCon talk above suggests
* This is a clever piece of engineering
 * >>> tweet = 'New PyBites article: Module of the Week - Requests-cache for Repeated API Calls - http://pybit.es/requests-cache.html … #python #APIs'
 >>> re.findall(r'((?:#|http)\S+)', tweet)
 ['http://pybit.es/requests-cache.html', '#python', '#APIs']

**Questions** 
* I wanted to pass something like [0].ul.li.li - the end part of a beautiful soup index/method, but store that stuff in a dictionary and tack it onto the end at a later date. I can definitely store the whole object in the dictionary as a string and then just run eval() on it when I'm ready to use it. I'm pretty sure the answer is just something like, you should never try to store that kind of information in a dictionary, but I'm still just curious how you would do that if you absolutely had to. Maybe store the rest of the first part of the object as a string too and then concatenate the whole thing and then evalute that? Probably easier just to think of a different way to solve the problem - like write a function that handles returning the beautiful soup object - or even the response.

**Link(s) to work**

### Day 76, October 21st, 2018 - Sunday:

**Today's Progress**
* Completed challenge 42
* Made an honest effort at understanding both sub and backreferences, with progress
* Read a decent portion of the HOWTO article
* Executed PyTests without needing to lookup how to do it!

**Thoughts**
* More useful than the regular docs
 * https://docs.python.org/3/howto/regex.html
* I finally realized that sub is not at all like search or findall in terms of how it returns a string. It's going to return the whole string no matter what, it's just going to also replace something that matches a pattern. Adding in period asterix dollar sign (not sure what those were destroying my markdown) just means capture the rest of the string, whatever it is, and then replace the whole thing with whatever I want. Makes sense for this code challenge. I also have a better understanding now for why backreferences and subs are the one-two punch for making changes in a text.

**Questions** 

**Link(s) to work**

### Day 77, October 22nd, 2018 - Monday:

**Today's Progress**
* Watched logging videos
* Introduced to logbook library, created by creator of Flask - so that's a positive

**Thoughts**
* Still don't totally understand the diffrence between print and stdout. When does print not write to stdout?
* Funny that MK uses the "TRACE" level which is in logbook but not in the standard library logging module. Just seems kind of strange, especially without some sort of explanation.

**Questions** 
* I'll need to read the logbook documentation to feel like I got something out of this series of days.
 * https://logbook.readthedocs.io/en/stable/index.html
* What's my default stderr handler?
* Why am I not seeing Trace in the documentation?

**Link(s) to work**

https://docs.python.org/3/library/typing.html

### Day 78, October 23rd, 2018 - Tuesday:

**Today's Progress**
* Working on replacing my existing logger with logbook in the canoe app
* I need to set bubble=True to use multiple handlers - just a different flow than the stdlib

**Thoughts**
* Maybe logbook makes a lot of sense for if you really know what the hell you're doing with logging, it certainly isn't easier to setup than Python's standard logging with the provide documentation
* Just adding multiple loggers is quite confusing
* Examples are helpful to me, and there aren't the sorts of examples present that really get me off the ground
* There are type hints in this example function MK writes, but that isn't explained and the colons in the parameters were super confusing. After taking a moment to orient myself to type hints, they actually seem pretty great, it's just, a little heads up pls.
 * https://docs.python.org/3/library/typing.html
* Ok, I figured it out. I learned some stuff. I do trust the core developer, but also standard logging still sort of makes more sense to me. I'm sure logbook is more performant, but if I don't really understand how it works, I'm not that sure how it helps me.

**Questions**
* How can you format the timestamp that comes out of logbook?
 * https://logbook.readthedocs.io/en/stable/api/utilities.html
* How can you add multiple handlers?
 * Yes, you have to use the bubble flag

**Link(s) to work**

### Day 79, October 29th, 2018 - Monday:

**Today's Progress**
* Watched Refactoring/Pythonic Code videos
 * It was pretty comforting that most everything today was review. Not that the most Python solution always comes straight away, but it was great to reiterate that I do actually know how to do some stuff in the most efficient way

**Thoughts**
* Ok, that was BY FAR the longest gap I've ever had in days. I'm going to forgive myself and move on. There were a couple of opportunities, for sure, but also a string of not being able to work at night, which has been my practice and preference. The one bright spot is that I've had more time - especially last Thursday and Friday to solve real problems at work using Python. I've been submitting pull requests, adding logging and handling exceptions as well as working with parent/child class over-riding and super() methods. So it's been good, but now it's time to get back at it.

**Questions** 
* I need to practice writing lambda functions
* Still need to read PEP8 end to end
 * PEP8.org sounds like a thing worth checking out - written by Kenneth Reitz!
* Ok, it basically sounds like if you don't have an __init__.py file then you need to add your scripts to PATH

**Link(s) to work**

### Day 80, October 30th, 2018 - Tuesday:

**Today's Progress**
* Pretty much just read a bunch of the resources of the Jupyter notebook on refactoring and then stared at NOAA for a while without really making many changes. I got stuck on questions like "where should a make my db connection" and "why does RC's manager.py code just live in one massive chunk?"

**Thoughts**
* Read 
 * https://realpython.com/python-logging/
 * https://pybit.es/python-packaging.html
 * https://realpython.com/python-modules-packages/
 * https://pybit.es/beautiful-python.html 11:11
 * https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application/193181#193181
 * https://realpython.com/python-application-layouts/
 * https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826


**Questions** 

**Link(s) to work**

### Day 81, November 2nd, 2018 - Friday:

**Today's Progress**
* Watched 'Using CSV Data' videos
* The use of dictreader + namedtuple to handle CSV files seems clever

**Thoughts**
* I'm really falling off of the wagon here. I have been spending more time at work coding, which has been nice, but spending much less time, less frequently working on my #100days projects. I also sort of gave up on day 3 of refactoring because I was feeling overwhelmed by sort of starting creek.py from scratch. I want to come back to these lessons when I'm at that point. I think I sort of got the points I needed to get but didn't take the time to really put them into practice.

**Questions**
* I don't really understand the utility of type hinting if you're not using PyCharm or some other IDE that makes sense of that input
* Are there easier ways to convert CSV strings into data types than manually assigning one at a time?

**Link(s) to work**

### Day 82, November 3rd, 2018 - Saturday:

**Today's Progress**
* Grabbed a Star Wars data set from 538
* Learning lots:
 * Needed to bring in the codecs library to open the Star Wars data set because of some funky, not UTF-8 characters
 * The Python docs tell you this, but you should add newline='' is csv readers and writers when working with an actual file in memory
* Progress upon progress - I used namedtuples, list unpacking, and a list comprehension to do what I wanted to do succinctly, correctly and in a Pythonic way. I was actually able to logic myself from beginning to end on that one.

**Thoughts**

**Questions**
* Why is it so hard for me to find the actual list of params the csv objects take?

**Link(s) to work**

### Day 83, November 5th, 2018 - Monday:

**Today's Progress**
* Used itertools.chain (eventually removed)
* Turned counter objects into dicts and used those dicts to write the f strings to present the final info
* Wrote fairly eloquent functions to handle the output across any data set

**Thoughts**
* OMFG getattr() is the way to solve my beautiful soup problem and hand in attributes dynamically
 * https://docs.python.org/3.7/library/functions.html#getattr

**Questions** 

**Link(s) to work*** 
* Completed my 538 data analysis project

### Day 84, November 7th, 2018 - Wednesday:

**Today's Progress**
* Watched JSON in Python videos

**Thoughts**

**Questions** 

**Link(s) to work**

### Day 85, November 10th, 2018 - Saturday:

**Today's Progress**
* Listened to Talk Python to Me Podcast
* Read this Real Python article
 * https://realpython.com/python-json/
* Started day 3 of JSON work for #100days, working with the PageSpeed Insights API
 * https://developers.google.com/speed/docs/insights/v4/first-app

**Thoughts**
* More practice with collections.defaultdict for adding values to keys that don't exist
* Need to ingrain lambdas for sorting keys

**Questions** 
* How do you run a script in interactive mode? What does the -i flag do?

**Link(s) to work**

### Day 86, November 11th, 2018 - Sunday:

**Today's Progress**
* Listened to several Talk Python to Me and several Python Bites podcasts. I listen to stuff and read news all of the time and don't usually count it toward my daily effort, since it's largely passive, but we were headed home from South Dakota today and it felt like I moderately productive thing for me to do.
* Read a bunch of the Google API client libraries documentation
* Successfully setup PageSpeed Insights API

**Thoughts**

**Questions** 
* Where's the documentation on following my API key's usage when building the service object?

**Link(s) to work**



### Day 87, November 18th, 2018 - Sunday:

**Today's Progress**
* Finished properly parsing my PageSpeedsInsights API data. I think I have a better sense of dump v dumps and load v loads now, but I find adding all of the [] when you get into deeply nested responses is always a bit awkward.
* Watched JSON APIs and Search
* Successfully put a namedtuple on top of some complicated JSON responses. It would take some work, and you're screwed if anything ever changes, but it's a pretty neat way to deal with data in a more OO feeling way.
* Read some stuff about Kenneth Reitz controversy with pipenv and his response including some extremely candid info about his mental health struggles.

**Thoughts**
* Between travel, a back injury, business and Sarah's schedule and general lack of discipline, it was really easy to fall off the wagon. I'm sure I'll still finish. I don't doubt any of the value, but you just realize that you make a lot of progress when you do something every day, and time passes very quickly when you think you'll do something and don't.
* Cool resource from an interview in "Talk Python to Me" - interesting blog from someone who I kind of identify with. Learning code because it solves a problem, but not being satisfied not knowing how things work. http://alpopkes.com
* Read about type annotations https://www.python.org/dev/peps/pep-3107/
* NamedTuples for dictionary parsing seems promising
* You can also chop slices off of layers of dictionaries (if there are multiple nested dictionaries) by putting a level that you want to access in a variable and then parsing from there.
* pipes is a solution for viewing all of your pipenv environments
 * lsvirtualenv does this with virtualenvwrapper

**Questions**
* Would creating namedTuples from the JSON response make parsing easier? 

**Link(s) to work**


### Day 88, November 20th, 2018 - Tuesday:

**Today's Progress**
* Finished up days 2 and 3 of JSON APIs and search. Pretty simple stuff, but spending more time with namedtuples never hurts.
* Got the web browser working. Searching Talk Python episodes by topic and then opening a web browser is actually useful. Holy goodness.

**Thoughts**

**Questions** 

**Link(s) to work**

### Day 89, November 23rd, 2018 - Friday:

**Today's Progress**
* My big purchase for today was buying a PyBites subscriptions. That and some Hue lightbulbs
* Watching the Web Scraping with BS4 vids. This one should be a breeze.
* Created a Netflix db scraper
* Messing with Requests-HTML to try to render Javascript without using Selenium
 * Also pretty curious about using the auto pagination
* Created a parser to just grab ingredients from Food Network
* Really took the long way around trying to figure our how to just get up to date info on Netflix catalog, and trying to do some Javascript rendering with Request-HTML and also reading more into the underlying package - pypetteer

**Thoughts**

**Questions** 
* There are a lot of BS4 commands I'm confused about. Like when to use "text" v. "content" and "select" v. "find"

**Link(s) to work**


### Day 90, November 24th, 2018 - Saturday:

**Today's Progress**
* Watched Measuring Performance videos
* cProfile from command line
 * python -m cProfile -s cumtime myprogram.py
* API by importing the profiler
 * Only enable and disable the profiler around where you want to measure

**Thoughts**

**Questions**

**Link(s) to work**


### Day 91, November 25th, 2018 - Sunday:

**Today's Progress**
* Running cProfile as both a command line module and using the imported funtion. All of Creek stuff is the most complex, but also relies on timing of receiving information from the web APIs as well as the time to write to the database, so I'll be curious to see what comes back.
* Before    NumCall                 CumTime
               1    0.003    0.003    0.956    0.956 noaa_historical.py:136(send_to_database)
              98    0.793    0.008    0.793    0.008 {method 'commit' of 'sqlite3.Connection' objects}
               1    0.000    0.000    0.547    0.547 noaa_historical.py:59(setup_request)
* After     NumCall                 CumTime
               1    0.000    0.000    0.015    0.015 noaa_historical_speed.py:136(send_to_database)
               1    0.009    0.009    0.009    0.009 {method 'commit' of 'sqlite3.Connection' objects}                     
               1    0.000    0.000    0.553    0.553 noaa_historical_speed.py:59(setup_request)


**Thoughts**

**Questions**
* There are a lot of underlying processes that I can't control, like api.py and session.py that are only called once and control the underlying sessions (assuming these are from Requests). Is there a convenient way to just look at filename = __file__ ? Is that good design?

**Link(s) to work**


### Day 92, November 28th, 2018 - Wednesday:

**Today's Progress**
* Watched parsing RSS feeds with Feedparser
* Read the feedparser documentation, did the activities and pulled down a Netflix release RSS feed parser

**Thoughts**
* It would be cool to put together a database of show we like or are interested in and then get notifications when a show we like has relevant news

**Questions** 
* I'm closing down all of the windows, so here is a link dump
 * PyBites article on packaging https://pybit.es/python-packaging.html
 * Pipenv and virtual environments
  * https://docs.python-guide.org/dev/virtualenvs/
 * Books
  * https://www.amazon.com/dp/1775093301/
  * https://www.amazon.com/dp/1491946008/
  * https://www.amazon.com/dp/1491919531/
  * https://www.amazon.com/dp/1491939362/

**Link(s) to work**

### Day 93, November 29th, 2018 - Thursday:

**Today's Progress**
* Finished up reading FeedParser documentation and playing around a bit more with yesterday's app
* Watched "Structured API Clients with Uplink"
* Read some of the uplink documentation

**Thoughts**
* Most challening module in a while
* This video use type annotation and type checking. Those things make sense in the context of PyCharm, but I'm unsure of how they really work otherwise
* I could still use a crash course on the format specification mini language
 * https://docs.python.org/3/library/string.html?highlight=format%20specification%20mini%20language#formatspec

**Questions** 

**Link(s) to work**

**Link(s) to work**


### Day 94, December 2nd, 2018 - Sunday:

**Today's Progress**
* Reading all of the gory Uplink documentation
* Reading this Python article on typing (a thing that Uplink does and I don't really know about)
 * https://docs.python.org/3/library/typing.htm
l* Found this nifty Real Python article on 3.7 which includes a solid section on typing
 * https://realpython.com/python37-new-features/#typing-enhancements

**Thoughts**

**Questions** 

**Link(s) to work**


### Day 94 Part 2, December 5th, 2018 - Wednesday:

**Today's Progress**
* This day took about an hour, but was sort of a follow up to a partial effort on Sunday. I was able to finish days 2 and 3 of the Uplink module, easily the hardest module I've encountered in weeks. I had to learn about type hinting and type annotations just to understand the Uplink documents. I needed to go back and rewatch some of the videos as well as poke through the example source code. When it was all said and done I still ended up making a lot of errors before I could make it run - mostly from still being fairly uncomfortable with OOP and not putting () where I should be putting (). Still, it was good and I think I was able to basically logic my way through it. The output is rough and could be improved upon, but the program does technically work.

**Thoughts**
* Really fun to have a challening module again. I feel good about my learning, comprehension and output.

**Questions** 

**Link(s) to work**


### Day 95, December 6th, 2018 - Thursday:

**Today's Progress**
* Watched "Twitter Data Analysis with Python"
* Learned about using .env files for environment variables to automatically be loaded into pipenv
* Picked a challenge for the rest of this module - built a Twitter APi web app

**Thoughts**

**Questions** 

**Link(s) to work**


### Day 96, December 10th, 2018 - Monday:

**Today's Progress**
* Going to get started on building this web app with the Twitter user of my choice
 * The account I chose was - Netflix US
 * Installing Postgres

**Thoughts**

**Questions** 

**Link(s) to work**


### Day 97, December 17th, 2018 - Monday:

**Today's Progress**
* So listen, I have been doing stuff, but it's also been a crazy period. Primarily because Barb's house closed permanently last Tuesday. I've been listening to a lot of Python podcasts on the way to skiing, I've been continuing to read articles and poke around on stuff at work. It took me basically two days to get PostgreSQL up and running locally.
* For today I'm going to consume a bunch of packaging articles and then make some progress on the Twitter web app, with the goal of completing that project on day 100.
 * https://www.youtube.com/watch?v=CqvZ3vGoGs0
 * https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
 * https://realpython.com/absolute-vs-relative-python-imports/
 * https://realpython.com/python-modules-packages/
 * https://realpython.com/python-application-layouts/

**Thoughts**
* Some goals for beyond 100 days
 * Finish Talk Python course
 * Data science course from University of Michigan
 * Flask app course with Treehouse
 * All the PyBites stuff
 * Working through my Python books
 * Back to FreeCodeCamp
 * Working through TensorFlow tutorial hosted by Google
 * The PSF Python Tutorial FFS

* Starting my thank you list:
 * Kenneth Love
 * Dr. Chuck
 * Michael Kennedy
 * Bob Belderbos
 * Julian Sequira
 * Guido Van Rossum
 * The PSF
 * Corey Schafer
 * Real Python
 * Stack Overflow

**Questions** 

**Link(s) to work**


### Day 98, December 22nd, 2018 - Saturday:

**Today's Progress**
* Cloned the pytip repo and currently just setting everything up to run. I'm going to make minimal changes at first, and then get into how it all works - changing the Tweepy target, Bottle template and figuring out a little SQLAlchemy and PostgreSQL along the way.

**Thoughts**
* Got everything into the database, time to learn more about pytest
 * https://realpython.com/python-testing/
* Not able to get the tests to work, but I dunno
 * I think it's because I hadn't installed pytest in the pipenv environment
 * Yep, that did it

**Questions** 

**Link(s) to work**


### Day 99, December 25th, 2018 - Tuesday:

**Today's Progress**
* Watched videos "Using the Github API with Python"
* You can run python -m pydoc [name of something] in the terminal to read documentation about that thing
* When you're not sure what an API returns, you can use pdb to pause the response and inspect it - brilliant
 * https://pybit.es/pdb-debugger.html

**Thoughts**
* Listening to Talk Python to Me
* Reading "Hello World"
* I'd like to get a little PDB training tomorrow
* Ideas for last day
 * Complete the GitHub module
 * Do a PyBite or two
 * Send out a long ass Tweet
 * Drink a beer


**Questions** 

**Link(s) to work**


### Day 100, December 26th, 2018 - Wednesday:

**Today's Progress**
* The Plan
 * Figure out pipenv builds on Sublime
  * Watching this vid cause Google failed me - https://www.youtube.com/watch?reload=9&v=xFciV6Ew5r4
  * And this https://www.youtube.com/watch?v=xqcTfplzr7c
  * Fuckety fuck fuck fuck. I never got it to run, and I'm stuck and frustrated. I just Tweeted and called it a night. Fuck.
 * Play with pdb
 * Write something silly with GitHub api
 * Do a PyBite or 2
 * Write a long ass thank you Tweet

**Thoughts**
* Holy fucking shit. I still don't want to be done. Although in some ways I feel like I finished whenever I stopped trying to go daily and everything since then has been "normal"? There are so many challenges left to face, and I still have produced nearly what I would like to even for starters. I still feel like a total noob, but a newb who can find answers.
* Mint seems like a good Linux distro

**Questions** 

**Link(s) to work**


https://itnext.io/become-a-git-pro-in-just-one-blog-a-thorough-guide-to-git-architecture-and-command-line-interface-93fbe9bdb395



