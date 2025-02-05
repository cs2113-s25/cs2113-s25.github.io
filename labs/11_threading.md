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

## Running your code

To run your unit tests -- remember, you need to have the junit jar file in the same directory -- compile and run your code with the following commands on the terminal (depending on your OS):

### Windows
`javac -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" Lab11_Tests.java`
`java -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab11_Tests`

### Mac/Linux
`javac -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" Lab11_Tests.java`
`java -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab11_Tests`

All your tests should pass at home before submitti

# Grading rubric and submission

Type the following command to compress your files into the required submission format:
`tar -cvf lab11.tar Lab11_Tests.java`

Submit your code, as `lab11.tar` on the submitserver. 


|Item | Points |
|Your test suite passes all tests on a correct implementation of `Lab11_Thread` | 30 |
|Your test suite finds all the bugs in incorrect implementations of `Lab11_Thread` | 70 |
|TOTAL | 100 |

