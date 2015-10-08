# regular expressions: anything but regular

Ok, fine, regular expressions are pretty standard stuff, but I was really struggling to come up with a clever title. Anyways, yeah, read this page and maybe you'll learn things about regular expressions!

## introduction
A regular expression is basically just a string with some special syntax that represents a pattern. You can use regular expressions to

1. **test** if strings **match the pattern** represented by the regex
    * Is it a phone number or an email address?
    * Does the string contain any numbers?

2. **extract information** from that string
    * What's the area code of this phone number?
    * What's this person's last name?

## basic syntax
What's that? All that jazz about patterns is cool and all, but you want to know how to actually code one of these things up? Ok hold your metaphorical horses and metaphorically listen up; ima tell you everything you need to know in order to write some sweet, sweet regxes. Feel free to (i.e. definitely, definitely) follow along using [rubular](http://rubular.com/), a Ruby-based regular expression engine.  

### super-duper simple regex
The simplest possible regex just tests to see whether a test string contains a substring. Here's an example:

**regex:** `milk`<br>
**explanation:** the string "milk"<br>
**test strings:**

1. **"milk"** (matches)
2. "the cow mooed when I **milk**ed her" (matches)
3. "go vegan!" (no match)

### character sets
A character set (using syntax like `[abc]`) is a placeholder for any one of the characters in that set. You can also use hyphens, so `[a-c]` is equivalent to `[abc]`. Some examples:

**regex:** `li[vf]e`<br>
**explanation:** li[v OR f]e<br>
**test strings:** 

1. **"live"** (matches)
2. **"life"** (matches)
3. "livfe" (no match)
4. "line" (no match)

**regex:** `#[0-9]`<br>
**explanation:** # followed by exactly 1 digit<br>
**test strings:**

1. "You are #**1**! :D" (matches)
2. "Michael Jordan: #**2**3" (matches)
3. "I'll have 3 french fries, please :)" (no match)

**regex:** `[a-zA-Z0-9][0-9]`<br>
**explanation:** exactly 1 letter or digit followed by exactly 1 digit<br>
**test strings:** 

1. "**A4** paper is the bomb!" (matches)
2. "**96** paper is not a real paper size" (matches)
3. "EL paper is also made up :(" (no match)")"

### shortcuts
Apparently brackets are really hard to type, so regular expressions also has shortcuts for common character groups. On the real though, using these shortcuts makes your regexes easier to write and more readable for others. Here are some useful ones:

**digit:** `\d` = `[0-9]`<br>
**word:** `\w` = `[A-Za-z0-9_]`<br>
**whitespace:** `\s` = `[ \t\r\n]`<br>
A dot (`.`) **matches literally anything** - use sparingly

## repeating sets
Enclose any regex you want to repeat in parentheses. For example, 
`(versace ){4}` matches `versace versace versace versace `
If you want a variable number of matches, you can use

- `(versace)*` for any number (including 0) of repetitions of `versace`
- `(versace)+` for 1 or more repetitions of `versace`

You can also match repeating sets of individual character sets! For example:

**regex:** `[a-zA-Z]+`<br>
**explanation:** One or more uppercase/lowercase letters<br>
**test strings:** 

1. **mPqrzzzzN** (matches)
2. 847 404-8821 (no letters, no match)

## anchors
You make sure that a string starts or ends with a particular pattern! Check out some examples:

**regex:** `^[A-Z]`<br>
**explanation:** Must start with a capital letter<br>
**test strings:** 

1. **H**ello, world! (matches)
2. my name is Josh. (doesn't start with a capital letter, no match)

**regex:** `amazing$`<br>
**explanation:** must end with the word amazing<br>
**test strings:** 

1. Josh's google forms are **amazing** (matches) (obviously)
2. Tiffany's google forms are amazing too!!! (doesn't match. also obviously untrue >:D hahaha JOSH WUZ HERE)

