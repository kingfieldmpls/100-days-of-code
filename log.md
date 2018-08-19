# 100 Days Of Code - Log

### Day 1: July 28th, 2018 - Saturday

**Today's Progress** 
* Finished Coursera's University of Michigan Python Course - Course 2: Python Data Structures : Week 5

**Thoughts** 
* Still burning through what is basically review material. I learned about using dict.get(key,defaultValue) as an idiom for creating histograms without throwing a traceback if you look for a key that isn't in the dictionary yet. I felt a little strange reviewing basics that I've known for a long time, but clearly without coding regularly there are still a lot of methods and constructions that are new to me with some of the most common elements of the standard library.

**Link(s) to work**
* [Day 1 Exercises](exercises/day1.py)

### Day 2: July 29th, 2018 - Sunday

**Today's Progress**: 
* Finished Coursera's University of Michigan Python Course - Course 2: Python Data Structures
* Started Courera's University of Michigan Python Course - Course 3: Using Python to Access the Web: Weeks 1 and 2

**Thoughts**
* Got a better sense of how and when to use a tuple. Also learned that a major feature of tuples is that they're much more memory efficient because they hardle support any methods. 
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

**Today's Progress**: 
* Finished Coursera's University of Michigan Python Course - Course 3: Accessing the Web: Week 3

**Thoughts**
* Man was today a slow mover. Got stuck figuring out why set localecho doesn't work how I expect with the wonky Windows Telnet client, and then went down a Python documentation rabbit how. 
* Networking still confuses the hell out of me. I think it's largely a vocabulary issue. I want to unlock the mysteries, but I also question the usefulness considering how many amazing shortcuts already exist to do the tasks we want to do.

**Questions**
* What's the simplest way to grab HTTP headers in Python? urllib? requests?

**Link(s) to work**
* [Day 3 Exercises](exercises/day3.py)

### Day 4: July 31st, 2018 - Tuesday

**Today's Progress**: 
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
**Today's Progress**: 
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

**Today's Progress**: 
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

**Today's Progress**: 
* Completed chapter 1 and part of chapter 2 of "Using Databases with Pythong"

**Thoughts**
* I actually completed this chapter's month's ago. Dr. Chuck's 15 minute video explaining object oriented programming was an actual breakthrough for me the first time a watched it earlier this year. It was neat to revisit and reflect on how these concepts have crystallized over time, and how hard things become known things relatively quickly if you can avoid the frustration of not fully understanding each new concept you encounter right away.

**Questions** 
* There is still A LOT I don't understand about OOP from a practical, functional level.
* I also don't really understand namespaces or what __init__ ought to be used for when creating a class. I mean, I understand it, but my brain isn't naturally thinking like that yet.

**Link(s) to work**
* The code I wrote today was for work. I think that's technically against the rules? It was one of those things where I was very confident it would work how I expected. It didn't. There were all sorts of modules in this SDK I was using that weren't updated to the latest version of the API and they weren't helping matters much. In the end I got it to work but I don't really understand how. The agony. The ecstasy.

### Day 8, August 4th, 2018 - Saturday:

**Today's Progress**: 
* Completed the "Basic SQL" portion of Coursera's "Python for Everybody".

**Thoughts**
* I honestly don't remember doing the exercise for this chapter, but apparently I did successfully complete it earlier this year. What's crazy is we have code exactly like this example in prodution at work now, and it's so interesting to come back with the context of seeing how this application actually get put to use in the real world. I've also learned more about SQL injection attacks since watching this video the first time, which helps explain some of the wildcard insertions. 

* I also feel like this chapter is a significant increase in difficulty compared to previous chapters. You're also not expected to really produce much original code. If you can read the example, you can fairly easily modify it to work. It's reinforcing spaghetti code, which isn't what I need right now. Ha!

**Questions**
* I want to come back and work through the Twitter spider example at some point in the future. It wasn't required for the course so I moved on.

**Link(s) to work**
* [Day 8 Exercises](exercises/day8.py)

### Day 9, August 5th, 2018 - Sunday:

**Today's Progress**: 
* Completed the second SQL chapter from "Python for Everybody" - minus the db example.

**Thoughts**
* I've finally made it back to where I initially started. Definitely feel a little smarter than the first time around, but also have more questions.

**Questions** 
* When is a project so small where you shouldn't worry about duplcating strings?

**Link(s) to work**
* No Python to show, just some things in the DB Browser for SQLite.

### Day 10, August 6th, 2018 - Monday:

**Today's Progress**: 
* Completed practical example for Coursera/Python/SQL. 

**Thoughts**
* Today's assignement more or less begged spaghetti code. It was much easier to make it work quickly that to put it together properly. It met me at a place where I was looking to complete more than put rigor against the process. Today was probably a low point. But we'll see where tomorrow ends up.

**Questions** 
Need to review the data validation rules for different SQL implementations in order to actually understand how to do this work. I'll need to review this chapter before completing the capstone, I think. One good idea, just redo the chapter 3 assignment, but write the code from scratch, and ignore the sample code.

**Link(s) to work**
* [Day 10 Exercises](exercises/day10.py)

### Day 11, August 8th, 2018 - Wednesday:

**Today's Progress**: 
* Complete "Many to Many Relationships in SQL"

**Thoughts**
* For whatever reason these chapter assignments are getting easier and easier. Too much is already complete in the sample files, and so it's fairly trivial to get them to work to the point where you can satisfy the auto-grader. 

**Questions** 
* What are all of the SQL conn object commands that you should know? How different are these commands between SQLite and MySQL? Does MariaDB have it's own cursor?

**Link(s) to work**
* [Day 11 Exercises](exercises/day11.py)

### Day 12, August 9th, 2018 - Thursday:

**Today's Progress**: 
* Completed course 4, "Using Databases with Python", which just leaves the capstone.

**Thoughts**
* The challenge level in course 4 was generally very low. I guess maybe there is some incentive to keep completion rates high? Most of the examples took very little tweaking to run properly to complete the assignment. I did try to understand the code by reading it, but it's really not the same as writing it yourself.

**Questions** 
* How to Redshift and Hadoop work?

**Link(s) to work**
* [Day 12 Exercises](exercises/day12)

### Day 13/14, August 10th/11th, 2018 - Friday/Saturday:

**Today's Progress**: 
* Man, Fridays are a thing, eh? I crashed hard just after the one hour mark. Completed most of the lectures for the capstone project week 2. 

**Thoughts**
* Getting to some really interesting concepts with creating a page rank algorithm from scratch. Unfortunately, as has been the case with the last few weeks of classes, they don't really ask enough of the students. The passive feels easier and more passive then some of the much more foundational courses. Nevertheless, trying to read and understand the code did count for something.
* I was asked to identify my own data source for the optional (read interesting) part of this process. I chose the .gov website for monitoring the flow of the Minnehaha Creek as well as Open Weather API to try to combine data from these two sources and make both historical observations and a predictive model for the future.

**Questions** 
* I'd like to learn more about both the concept of convergence and graph theory.

**Link(s) to work**
* [Day 13/14 Exercises](exercises/day13)

### Day 15, August 12th, 2018 - Sunday:

**Today's Progress**: 
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

**Today's Progress**:
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

**Today's Progress**: 
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

**Today's Progress**: 
* Did some prioritizing on the creek project
* Read more docs on weather APIs
* Read Beautiful Soup docs and tried desperately to quickly grab table data
* Realized Beautiful Soup doesn't load JavaScript, so I'll need Selenium to grab what I need to scrape

**Thoughts**
* Today I didn't really 'accomplish' anything, but I did put the time in. I learned a whole lot about the Beautiful Soup package and a little about Selenium.
* This whole thing is getting really addictive. There is still the crushing feeling of all of the things I don't know, but I'm getting closer to the point where I can do meaningful things relatively quickly, and basically know my resources for learning completely new things.

**Questions** 
* Learn how to use the Selenium package
* Learn more about Pandas dataframes for quickly making sense of tables

**Link(s) to work**
* [Couple of tweaks and some early thought starters](exercises/creek)

### Day 19, August 16th, 2018 - Thursday:

**Today's Progress**: 
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

**Today's Progress**: 
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

**Today's Progress**: 
* Cooking with gas with the weather scraper. Grabbed a whole year with no crashes. Added some exception handling.
* Watched videos on lambda functions, map functions and history of recursion

**Thoughts**
* I'm already worried about what I'll be able to do in 100 days. What about front end? What about mastering OOP and wrting more Pythonic code? What about ML? What about general math and stats knowledge? What about pandas and numpy?

**Questions** 
* The meet ups are fine. How do I get more immersed in local community?

**Link(s) to work**
* [Scraper is proceduarl, but well tuned](exercises/creek)

### Day X:

**Today's Progress**: 
**Thoughts**
**Questions** 
**Link(s) to work**