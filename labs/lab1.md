---
layout: toc
permalink: lab/1
---

# Lab 1: Debugging with print statements

In this assignment you will practice tracing through code using print statements in order to find and fix a fault. This is one of the most common (if not the most common) activities software engineers spend their time on in the real world. Also, it's not something that an LLM like ChatGPT can help with, so you'll need to master this skill in order to do well in your career.

Fortunately, debugging using print statements is *extremely easy*, once you get the hang of it! You'll learn you can debug *anything*, if you're able to print things out for code that you're running. To illustrate this point, **this exercise is in python**, but you don't need to have seen python before in order to complete it. In fact, you will certainly have to teach yourself at least one new programming language in the future -- knowing how to use print statements to figure out what's going on is more than half the battle :-)

## Setup

Before you get started,

1. Make sure you have python installed. Try running `python` and then `python3` in your terminal. If both of these give an error that the program can't be found, google how to install python for your operating system, install it, and **open a new terminal window** to see if the installation worked.
2. Download [this zip folder](./lab1_starter.zip) of all the files you will need for this project.

## Problem description

We're working on an [advising tool frontend](https://faculty.cs.gwu.edu/goldfrank/advisingtool/) in the CS department (**it's not ready yet, so beware!**) to populate valid list of courses that meet each of the degree requirements. While we were writing this code, we had a bug: in the **NTT (non-tech track) requirement for the 2019-2021 Bachelor of Science (ancient, I know!) the attached code incorrectly generates duplicates into that list. Specifically, each of the three NTT options shows the course, `CSCI 2501` (which we also no longer offer) as listed twice. This is a bug!** There should be no duplicate courses in this or any of the lists for entries in the `possible_courses` dictionary.

In particular, these NTT electives cannot be lower-level courses required for the CS major (such as this class); higher-level courses such as `CSCI 2501` should be allowed towards this requirement (but they should *not* appear twice in this list, as they do now -- the bug).

This is a (slightly modified) example of a real bug we encountered while writing this code. Note that the codebase is imperfect and realistic for a library you might find online or inherit: comments are sparse because the developer was in a rush and/or writing the code for themselves, functions are expected to be understood by looking at their contents, and the JSON files are enormous and virtually illegible due to their size. However, when this bug was live, we were able to isolate it and fix it in less than five minutes (though, to be fair, we were familiar with the codebase having written it ourselves). However, it may take you much longer if you're learning how to use print statements to debug.

## Part 1: Understanding what went wrong

Take a minute to write down, in your own words in English, what the bug is -- if you're not sure (after trying), ask a neighbor for help. Make sure you can conceptualize what's wrong, using the description above, before you proceed. Ask the TA if you still need help.

### Reproducing the bug

Next, we're going to ensure that we can re-create the bug by running the code. You'll notice there are a lot of files for this assignment, but the test case that shows the duplicate entries in `possible_courses` is in the file called `BS_2019_courses_buggy.py`.

You can run this file with `python BS_2019_courses_buggy.py` in the terminal to generate the JSON file `possible_courses_BS_2019.json`; in this file, the possible courses for `elective_1`, `elective_2` `elective_3`, and `elective_4` all contain the bug above where `CSCI 2501` appears more than once in the lists associated with those keys. **Running the python file will show you the duplicates at the bottom** -- this is effectively our test case to see if you fixed the bug or not, since the JSON file is huge and unwieldy. 

**Make sure you can run the file and you can see the `2` at the bottom of the terminal** before moving on.

### Find the failing test case

Next, let's find the failing test case in the python file. Take a look at line 78:

```python
print(possible_courses["elective_1"].count("CSCI 2501#Ethical Issues in Computing"))
```
You may not know any python, but what do you think this statement is doing? How did it print out the number `2` a moment ago? Verify with your neighbor that you understand what that line of code is doing conceptually, even if you don't know the details. Ask the TA if you're still unsure.

### Working backwards to understand the code

Next, add the following line (you will comment it out in a bit) to the bottom of that file:

```python
print(possible_courses["elective_1"])
```

What does it print out? What can you now saw about the `possible_courses` variable contents? Verify with your neighbor that you understand what's being stored there.

#### Using print statements in python 

As you just saw, in python there is a function called `print()` that can print out anything. The only trick, which is different than Java, is if you want to label your print statements (which you will need to do below), you need to convert everything in the expression into a string:

```python
print("DEBUG 1: possible_courses[elective_1]: " + str(possible_courses["elective_1"]))
```

Notice the `str()` function wrapping the dictionary value with a string before concatenating it with the string `"DEBUG 1: possible_courses[elective_1]: "`

Now you know how to use print statements to debug in python :-)

# Part 2: Fault localization

Now that we re-ran the test case and saw the error (printing `2` instead of `1` there), let's check our understanding:
1. What does the `2` mean there? What should its value be if this test case would have passed?
2. How are we getting the `2` there? What does `2` represent? What is being counted?
3. What should the contents of `possible_courses` look like in order for there to be a `1` printed for that test case?

If you can't answer these questions, review the instructions above and check in with your neighbor or a TA for help. 

Delete the print statement printing out `possible_courses`, because it's output makes it difficult to read the rest of the test cases and program output.
 
## Where was the variable most recently changed?

Okay, now that we understand what's going on with that test case, it's time to find where the incorrect data was placed into `possible_courses`. A lot of the time, students try to *think hard* and take a look at the code to try to see what went wrong, **but this is unnecessary**. 

All you need to typically do to fix a bug like this is work your way backward from the last place that variable was touched until you can find the line number where the incorrect value was assigned. You technically don't even need to know what the rest of the code does; you don't even have to look at the whole file to start. It doesn't matter -- what matters is following the trail of where `possible_courses` got its values until you can see the incorrect data being placed into it.

So, where was the last time we could have possibly updated `possible_courses`? It's last used on line 62 as an argument to a function `reformatForFrontEnd`. Copy the following print statement right before that line so we can see if `reformatForFrontEnd` modified the variable:
```python
print("DEBUG 1: possible_courses[elective_1] count: " + str(possible_courses["elective_1"].count("CSCI 2501#Ethical Issues in Computing")))
```

Was `possible_courses` correct *before* that function call? If yes, then we know `reformatForFrontEnd` must be where the bug is.

In this case, it turns out `possible_courses` was wrong even before that function call, so the issue is not with that function. **Where is the next line where this variable was potentially modified**?

It's *used* on line 58, but only to be assigned to something else. You could have put a print statement here to check we didn't change it, but we'll skip this.

Looking at lines 44-55, we can see the variable is definitely modified there! In particular, on line 52 we see that `possible_courses["elective_1"]` -- which is the thing we specifically care about -- is set to a variable called `electives`. **This means that we now need to trace backwards to see where `electives` was incorrectly modified** in order to find the bug. Place the following print statement on line 51 to convince yourself of this (notice how we are now printing out the `electives` variable):
```python
print("DEBUG 2: electives count: " + str(electives.count("CSCI 2501#Ethical Issues in Computing")))
```

### Continuing to work backwards

Now, we're going to **repeat these steps going backwards to see the most recent place `electives` was modified**.

If you go through the rest of the file, it turns out `electives` was not actually updated anywhere in there. However, there are two `import` statements at the top -- in python these copy the entire contents of the file into the current file. Go ahead and open up `utils_buggy.py` and see if `electives` is modified in there, starting at the bottom of the file and working your way up.

It turns out that `utils_buggy.py` is full of utility functions, with a call to one of them at the bottom (`record_year_for_hss()`). The variable `electives` is not updated in this file, at least not directly. It may be passed into one of the many functions we see, but we can't rely on variable names for local arguments like that to be sure. So, let's put this file aside for now, because it's not responsible for making the decision to modify `electives`.

Let's open the other file, `course_list_imports_buggy.py`, and work from the bottom to try to find where `electives` was last modified.

You can see on line 75, `electives` is set to the result of a function call, `beautifyElectives()` (in python a function can return more than one item which is what you're seeing there). `electives` is also used as an argument to the function. This seems like a promising place to check, so let's find out if this function call is responsible for the bug. Place the following print statement on line 74:
```python
print("DEBUG 3: electives count: " + str(electives.count("CSCI 2501#Ethical Issues in Computing")))
```
Okay, progress! We see that `electives` was correct before this function call, but it's wrong after. Let's go inside the function. Where is `beautifyElectives` defined? If we scroll up, it's not in this file. So, it must come from the `utils_buggy.py` because that file is imported at the top here.

Looking inside `utils_buggy.py` again, we see this function defined on line 122. On line 133, we can confirm the return statement is returning what `electives` will get assigned to: a local variable called `elec`. Where is that variable most recently modified? Looking up, there is an `if-else` on lines 129-132 where `elec` *must* be modified (since we have to take one of those two branches).

# Part 3: Isolating and fixing the fault

We can be sure that the bug is in this function; `electives`/`elec` has the correct value before the function (you can even use a print statement on line 123 to verify this), but by the return statement, it is incorrect (again, you could use a print statement to verify). That means the bug has to be inside that `if-else`.

But which branch is it in? Here, we need to dive a little deeper, finally, and understand what this code block is doing.

Use print statements to print out all the relevant variables on the line after they are created, *making sure you label what you're printing out*:

* `all_courses`
* `course`
* `cs_name`
* `cs_num`

For example, you might have:
```python
print("DEBUG 4: cs_num: " + str(cs_num))
```
to legibly print out `cs_num` with a label so you know which variable you're looking at.

What are all these variables doing, based on what they are storing? Make sure you can explain each one in your own words -- if you're stuck, ask a neighbor or a TA for help. Once you understand what these variables are storing, feel free to comment out those print statements if there is too much output to be legible.

Now, take a look at the `if-else` where we know the problem lies. What variable does it depend on? `cs_num[:4]` -- print this out to see what's in there:
```python
print("DEBUG 5: cs_num[:4]: " + str(cs_num[:4]))
```

So it's using the course number (i.e. `2113` or `1112`) to decide to either append the course, or remove it. 

In our failing test case, the course number is `2501`. Will it get into the `if` or the `else`?

## Fixing the fault

Based on the course number, we should be entering the `if`. It's also literally adding a duplicate there. Do we need that line? See if you can fix the fault without changing the meaning of the rest of the code. 

You'll know you fixed it if/when you re-run your code and it prints out `1` instead of `2`.

# Part 4: Checking your work

It seems like we fixed the fault, but can we be sure that we didn't accidentally break the rest of the code? Normally, we'd have a robust test suite that could verify no new test cases fail when we fix a different one. 

Let's go back in and add this missing test case to the bottom of our `BS_2019_courses_buggy.py` file and add in this test case, which checks to make sure required CS courses (such as CS1111) are *not* in the electives (this was a rule for those degree requirements):
```python
print("TEST2: " + str(possible_courses["elective_1"].count("CSCI 1111#Introduction to Software Development")))
```

We want the line above to print 0 when we run our fixed code. Does it? If not, go back and take a look at how you fixed your bug and see if you can modify that code so that it prints out 1 for our original test case and 0 for this one.


# Requirements, submission, and grading

## Submission

Tar up everything in the zip folder you downloaded with `tar -cvf lab1.tar *.*` and submit this to BB before the deadline in class. 

## Grading

You should be using print statements that are properly labelled, as shown above, to **tell a story** of how you ran these individually as you traced through your code to find and fix the bug. 

You should be running the lab on your own machine with your own code, even if you chatted with a neighbor to verify some of the conceptual components. You should be writing your own print statements in your own file.

If you are working on this assignment outside of lab, you may *NOT* consult other students: only refer to the TAs and Ed for help. 

Also, be careful **not to hardcode** the bug fix for this lab; your solution must work for any CSCI class that should/should not be a part of the electives, including future classes that are not currently captured in any of the files.

|Item | Points |
|submission tells a story of how the bug was discovered | 75 |
|bug was fixed without modifying the behavior of the rest of the code | 25 |
| TOTAL | 100 |

