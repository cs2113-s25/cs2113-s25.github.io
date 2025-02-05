---
layout: default
permalink: /lab/11_threading
---

# Lab 11: Threading debugging exercises

## Setup

Download the [Lab11_Tests.java](./Lab11_Tests.java) file.
Download the [Lab11_Thread.java](./Lab11_Thread.java) file.

Use git, as discussed in Lab 0, to create a repo called `gitusername-lab11`, add the file above to it, and commit and push the changes to github. Copy the file above into it and follow the comments in the code to write your unit tests.

## Writing test cases to find bugs

You will be writing unit tests that all pass against the correct implementation of `Lab11_Thread` above. Once your tests pass locally, you'll be uploading your code to the submitserver and see if you found all the bugs in buggy implementations there.

You may not modify (in spirit or in text) the existing code provided in the test case template, but you should, instead, add new lines of code.

Note: you must engineer your tests so that they run together in any arbitrary order and interleaving of statements. If your tests run fine individually, but don't run together (i.e. when you turn them all on) you'll need to think about why and figure out how to get around this problem in your test suite.

## Running your code

To run your unit tests -- remember, you need to have the junit jar file in the same directory -- compile and run your code with the following commands on the terminal (depending on your OS):

### Windows
`javac -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" *.java`
`java -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab11_Tests`

### Mac/Linux
`javac -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" *.java`
`java -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab11_Tests`

All your tests should pass at home before submitting to the submitserver.

# Grading rubric and submission

Type the following command to compress your files into the required submission format:
`tar -cvf lab11.tar Lab11_Tests.java`

Submit your code, as `lab11.tar` on the submitserver. 

Note: your tests cases must all pass at home in order to be eligible to earn points for finding bugs, similar to Lab3. You must also have meaningfully/usefully changed the test template provided with this lab in order to earn the 50 points below for passing all tests on a correct implementation.


|Item | Points |
|Your test suite passes all tests on a correct implementation of `Lab11_Thread` | 50 |
|Your test suite finds all the bugs in incorrect implementations of `Lab11_Thread` | 50 (25 pts each) |
|TOTAL | 100 |

