# Midpoint Pt. 1 - learning to read and write (code)
Diving into the codebase. Oh boy.

![oh boy](https://raw.githubusercontent.com/harvard-crimson/comp/master/midpoint/part1/ohboy.gif)

This week, we're going to ask you get set up on Vagrant and begin to go through our codebase and figure out some of the working parts.

## Overview

- **First, setup (github, vagrant).** The hope is that you'll have your own mini-version of thecrimson.com on your computer.
- **Second, answer questions in a text file.** Send this text file to kyle.kwong@thecrimson.com and haotian.wu@thecrimson.com. Note that these don't actually require you to have vagrant set up.

## Setup

### Github
1. If you haven't gotten permission to access the codebase, send us your github username.
2. Grab the link on the GitHub page for `crimsononline` under "SSH clone URL".
3. Clone the `crimsononline` repo to your computer via

        git clone <link here>

Now you should have a directory called `crimsononline` on your computer! It's not perfect out of the box, though, so let's tinker with some additional things (we only have to do this once).

### Fiddling with the Repo

1. Activate your virtual env (we'll be installing some things). 
2. `cd` into the new `crimsononline` repository.
3. Copy over everything from `sample_local_settings.py` into `local_settings.py`.

Why all this "local_settings" nonsense? `local_settings.py` is gitignored. 
This is because (for example) Kyle's  `local_settings.py` may have secrets (such as AWS ke.ys) that we don't want to store on Github

### Vagrant
Follow the instructions [here](https://github.com/harvard-crimson/crimsononline/blob/master/PROVISIONING.md#getting-started) under **Getting Started** and **Bootstrapping a Local VM**,  ignoring the AWS keys bit.

### Does it work?
In order to check that it works, visit [http://local.thecrimson.com](http://local.thecrimson.com). If you see something that looks like thecrimson.com, you're ready to go!

## Questions 
[Here is a template](https://raw.githubusercontent.com/harvard-crimson/comp/master/midpoint/part1/answer_template.txt) for your text file! Remember to put your name in the provided space. We'll be instructing you to poke through various aspects of the website, like tags, articles, the base template, and searching. 

Actual searching will be implemented in Midpoint Pt. 2. 

Let's get into it!

## Tags
Check out [this tag page](http://www.thecrimson.com/tag/editorials/). Play around a little with the section and type filter, and take a look at `urls.py` in crimsononline. (Here's [Django documentation on urls.py](https://docs.djangoproject.com/en/1.8/topics/http/urls/) if you get confused!) 

**TODO 1:** Briefly explain what a "tag" is. What is the name of the URL pattern that handles requests for the tag page? 

Now check out `views.py` in `crimsononline/content/`. 

**TODO 2:** What view handles the tag page?

**TODO 3:** Say I wanted the page for the just the tag “Editorials.” What parameter(s) would be passed from the url to the view, and what would their value(s) be?

**TODO 4:** Now say I wanted only the articles with the tag “Editorials” in the “Opinion” section. What parameter(s) would be passed from url to view now, and what would their value(s) be? 

## Articles
Check out [this piece](http://www.thecrimson.com/article/2014/2/20/harvard-odyssey-dogecoin/). It’s a standard non-feature article. 

**TODO 5:** What url pattern handles this? What view handles it?      
...having trouble finding it in urls.py? (it’s kind of tricky!) _**Hint:** check out `generic_patterns`, know that “article” is what we call a “content type,” and pay particular attention to the patterns (think regex) in the url of the piece!_

Go to the view you identified in TODO 5.

**TODO 6:** What type of object (i.e. what class / model) is the variable “c” in this view? _**Hint:** Notice the model methods that are called by “c” in the view, particularly the method used to return a rendered page._

Check out the model/class you just identified in TODO 6 in the appropriate`models.py` file.

Notice how complex it is! Take a look at the methods and how they interact and call upon other methods in the class. Keeping in mind what was returned by the view in TODO 6, answer: 

**TODO 7:** Which method is ultimately responsible for rendering the article? 
_**Hint:**  If stuck, this Django documentation on [requests/responses](https://docs.djangoproject.com/en/1.8/ref/request-response/), especially the section about HttpRequest objects, may be helpful._

For a standard non-feature piece like our example, the template is called `page.html`. Find this file.

**TODO 8:** What is its file path? _**Hint:** check the models folder—what type of content is this news piece?_

**TODO 9:** Find the div with the id “article-tags” in the template. Explain what is happening in this div. Also take a look at this div via Inspect element on the actual article. 

## Base Template and Search
Now let's visit something we call the base template, or `__base.html`, which this, as well as many other (read: most) pages extend. 

Find it in the codebase, and using Inspect element to compare divs, ids, etc. on the website to help you figure things out, answer the following:

**TODO 10:** What is the purpose of this particular template? 

**TODO 11:** What are some parts of the website that are defined in `__base.html`? 

Find the search box in `__base.html`. The actual search is powered by Google, and our template simply displays the search results. Read up a little on HTML forms if needed, particularly the action attribute. 

**TODO 12:** What is the url pattern that handles search? _**Hint:** there are two relevant urls.py files._

Notice how Google’s JavaScript handles all of the search functionality, and our template is basically just a shell to display what Google does for us. 

**TODO 13:** Describe at a high level how we might implement our own search functionality, say, that searched specifically just Content with specific Tags. 

### That's all, folks! Stay tuned for next time :D
