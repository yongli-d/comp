# setting up
##command-line text editors
Being proficient with a text editor and being able to open it from the command line will both impress your friends and make your life as a programmer a whole lot easier. We at The Crimson love Sublime Text, and especially love the fact that it comes with a little command-line utility. Get set up with it like this:

1. Download [Sublime Text 3](http://www.sublimetext.com/3)
1. Be able to run it from the command line:

        $ sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/bin/subl

1. Use it to open files and folders:

        $ subl file.py
        $ subl directory/

Now you can open Sublime from your terminal. Get excited!

## pip
Lots of people have written a lot of really useful Python code, put it into Python packages, then put it online and made it free to use. pip lets you install and use them really easily. Let's install it and explore the magical wold of Python packages :D. Install it with

```
$ sudo easy_install pip
```

Now you have pip installed, and you can use it to install stuff! But wait! Don't do that yet! First we have to install...

## virtualenvwrapper
So pip is pretty sweet and all, but consider the following sticky situation. We at The Crimson haven't upgraded our version of Django in a while, so we're still stuck on Django 1.5. However, the hip new startup you're interning at is using the shiny new Django 1.7. You want to do work for both places, but how can you have two different versions of Django installed at the same time?

The answer, of course, is by using virtual environments! Generally, for each Python project you're working on, you'll have a different virtual environment. Each virtual environment has its own installation of Python and pip that are completely independent of each other. This means you can install Django 1.5 to your Crimson virtual environment and Django 1.7 to your hip startup's virtual environment and not have any conflicts.

### installation + setup
Ok, enough with all this high-level theory mumbo-jumbo. Let's install this thing and figure out how to use it! The basic virtual environment package is called virtualenv, but it's a bit of a pain to use, so we'll use a wrapper on it called virtualenvwrapper. Follow these steps to set it up:

1. Install virtualenvwrapper with

        $ sudo pip install virtualenvwrapper

1. Open up the file `~/.bash_profile` with Sublime by typing `subl ~/.bash_profile`. Add the following lines to `~/.bash_profile`:

        export WORKON_HOME=$HOME/virtualenvs
        source /usr/local/bin/virtualenvwrapper.sh

1. Actually make the directory specified by `WORKON_HOME` by running

        $ mkdir $HOME/virtualenvs

1. Finally, __close out of any open terminal windows__ and then open a new one. virtualenvwrapper is all set up and we're ready to rock and roll!

### usage
Ok, we've talked about what this thing does and we've set it up. Now let's see what this baby can do! Let's make our first virtual environment and call it `crimson_comp`. Create the virtual environment by running

```
$ mkvirtualenv crimson_comp
```

When you run this command, virtualenvwrapper will actually create new copies of Python and pip, and put them somewhere in a newly-created folder `~/virtualenvs/crimson_comp/`. If you use Python or pip while this virtual environment is activated, you will be using these new, separate copies of them. After you run the command, your prompt should look something like

```
(crimson_comp)$
```

The `(crimson_comp)` indicates that that the `crimson_comp` virtual environment is currently activated. Now that you have your virtual environment, let's actually use it!

1. Install your very first Python package!  [Pillow](https://pillow.readthedocs.org/) is a fun one; it's a library that makes it really easy to manipulate images. Plus it has a funny name. Install it with

        (crimson_comp)$ pip install Pillow

2. Actually use Pillow! Feel free to look at the documentation and play around with it, but the following should be sufficient to prove that we've installed it properly:

        (crimson_comp)$ python
        >>> from PIL import Image

3. If you didn't get any errors, you've successfully installed Pillow! Deactivate your virtual environment by running

        deactivate

4. Now that you've deactivated your virtual environment, the `(crimson_comp)` should have disappeared from your prompt, and you should no longer have access to any libraries you installed to that virtual environment. Verify that this is the case by re-running the code from step 2. If you get an error, then you're doing well!

5. Re-activate your virtual environment. If you've forgotten what you called it, you can run `lsvirtualenv` to see a list of all your virtual environments. Once you have the name of your virtual environment, you can re-activate it with `workon crimson_comp`

There you go! You're now ready to go off in the world and work on Python projects, never having to worry about conflicting libraries ever again :).
