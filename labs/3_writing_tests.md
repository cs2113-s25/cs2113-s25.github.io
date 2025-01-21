---
layout: toc
permalink: lab/3_writing_tests
---
# Lab 3: Writing your own unit tests

This lab will give you practice writing your own unit tests -- something you will need to do in industry. Today, we're going to be writing tests against the specification below.

You will be graded on whether or not your unit tests find the bug(s) in an implementation of this specification.

## Setup

Create a file called `Lab3.java` that contains a class by the same name in the file.

Next, add the Junit imports to the top of this file, and make sure you have this [junit jar file](./junit-platform-console-standalone-1.7.0-M1.jar) in your current directory.
```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;
```

## Software specification

We're going to be writing unit tests to verify a method called `checkCode`, which will check if a string entered by the user is a valid item code or not in the Amazon database we're building a backend for. 

A valid item code will have the following characteristics:

* It will start with an integer between 1 and 999 (without preceding zeros).
* Next, a period will appear.
* One or more words composed of letters, separated by spaces, will appear. Each word must be capitalized.
* The last word is followed by one or more spaces.
* Finally, the code will end with an optional five digit number.


# Grading rubric and submission

Create a tar file with your code by running the following command in the terminal:
`tar -cvf lab2.tar UnitTestExample.java`

Then, upload this tarfile to the submitserver, and make sure you see 100/100 displayed there.

 You will be graded on the following:

|Item | Points |
|unit tests pass (33 points each) | 100 |

