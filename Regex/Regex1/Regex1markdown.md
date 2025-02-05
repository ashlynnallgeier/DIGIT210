# Regex Steps for Converting Movie Data From a tab-separated text file to XML

*Before beginning, think about how to do these assignments. It might be helpful to run a separate (free) Markdown editor to keep
your step recording in a different software window than oXygen, where you'll be writing your Find and Replace operations.
You want to be able to copy and paste your expressions into your markdown file to record them. 
I'm going to use Macdown (a nice markdown editor for Mac). Windows has Typora or reMarkable, etc.*


First step is ALWAYS to search for characters that will disrupt XML encoding: 
`&`, `<`, `>`. 
XML is not allowed to contain raw ampersand characters `&`. 
So I needed to find:

```
&
```
and replace with the special escape characters for ampersands:
```
&amp;
```
I searched for `<` and `>` and did not find them. 


Moving on, we can begin the "autotagging" find and replace process.
I wanted to wrap elements around whole lines. 

I used the following expression to find. 
I made sure that *dot matches all* was NOT set so that
the dot matches on any character but only inside each line. 
This expression matches on the beginning of each line, 
and *one ore more characters on that line*.

```
^.+
```
I set this to replace:
```
<movie>\0</movie>
```

Second step I matched this and set capturing groups so I could tag the titles:

Find: 
```
(<movie>)(.+?)(\t)
```



I set this to replace, so I could keep the first tag, and then add a new pair of tags for the title elements:
```
\1<title>\2</title>\3
```
At the very end of class, I manually set a root element around the entire document 
```
<xml>
   <movie>...</movie>
   <movie>....</movie>
    <!--yada yada yada more code -->   
</xml>
```

And I saved the file as movieData.xml.
And I closed it.
And I opened my new movieData.xml and saw that I had a green square in oXygen, indicating 
that the document is well-formed. Yay!

I can continue doing more regex find and replace operations to tag the dates, locations, and time durations inside each of these movie elements. 



Ashlynn Allgeier - Regex Assingment Movie Data

I used this to find all the movie titles
```
(<movie>)(.+?)(\t)
```.

I then replaced it with ```\1<title>\2</title>\3 ``` so that the title element was inside each movie element, and ended before the tab after each movie title.

My next step was to put date elements around each of the years that each movie. To do so, I searched for 4 digits after a tab element: ```(\t)(\d{4})```.

Then I replaced it with ```\1<date>\2</date>``` so that the date element would start after the tab and end after the 4 digits.

The next step was to identify the country in each line and wrap it in a ```<country>``` element. To do this, I searched for ```(\t)([A-Za-z, ]+) ```. This allowed for it to search after a tab, as well as searching for all characters and multiple words.

I then replaced those with ```\1<country>\2</country> ``` to add the country element.

The last step was to create the runtime element. I searched for ```(\d+)\s*(min)```, which searches for digits with the unit of minutes after them.

I then replaced it with ```<runTime unit="min">\1 \2</runTime>```. This wrapped the time in the runtime element, while also adding the unit attribute.

