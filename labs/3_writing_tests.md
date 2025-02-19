---
layout: toc
permalink: lab/3_writing_tests
---
# Lab 3: Writing your own unit tests

This lab will give you practice writing your own unit tests -- something you will need to do in industry. Today, we're going to be writing tests against the specification below.

You will be graded on whether or not your unit tests find the bug(s) in an implementation of this specification.

## Setup

Create a file called `Lab3.java` that contains a class by the same name in the file.

Next, add the Junit imports to the top of this file, and make sure you have the [Junit jarfile](https://cs2113-s25.github.io/labs/junit-platform-console-standalone-1.7.0-M1.jar) in the current directory.
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

The class and method you will be testing is as follows:

```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AmazonBackend{
    
    public static boolean checkCode(String code){
        Pattern pattern = Pattern.compile("^[1-9]\\d?\\d?\\.([A-Z][A-Za-z]* )+ *(\\d\\d\\d\\d\\d)?$");
        Matcher matcher = pattern.matcher(code);
        return matcher.find();
    }

}
```

Save the code above as `AmazonBackend.java` in the same directory as the rest of your files.

## Writing unit tests

Next, using the input domain partitioning skills you learned from lecture and the reading, write enough test cases for the `checkCode` method that find all the bugs. You'll be able to check how many bugs you found by running your code on the submitserver. Use the `assertEquals(x, y)` at least once in each of your test cases to call the `checkCode` method above with a specific input, and compare that to an expected boolean output.

You should continue to resubmit your code on the submitserver until you've found all the bugs.

This is an individual assignment (like all assignments in this class) and you may not share test cases (or talk about this lab) with other students. If you need help, see us in office hours and/or post to Ed.

## Checking for compilation

To run your unit tests – remember, you need to have the junit jar file in the same directory – compile and run your code with the following commands on the terminal (depending on your OS):

#### Windows
`javac -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" *.java`
`java -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab3`

#### Mac/Linux
`javac -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" *.java`
`java -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab3`

# Grading rubric and submission

Create a tar file with your code by running the following command in the terminal:
`tar -cvf lab3.tar Lab3.java`

Then, upload this tarfile to the submitserver to get graded.

**You have up to 15 submissions** on the submitserver to try to find the bug -- make sure you are thorough and thoughtful each time you upload your tests there in what you've added. Also, don't wait until the last minute to finish this lab -- the submitserver will take a long time to grade your work (and may timeout) if there are too many people trying to submit at once.

**Make sure you look at the autograder output** to figure out what went wrong with your submission. Post to Ed if you get stuck.

In order to earn up to 100 points, **you must first earn the 20 points for having your test suite pass all your tests at home**. Then, you will be eligible to earn up to 80 more points on the submitserver. 

**If your tests are not all passing at home, the score on the submitserver will be invalid**, as this also appears to the server like you're finding bugs, since tests are mismatched with expected values. In such cases we will be ignoring the submitserver scores. Please make sure your test suite passes on all your tests at home before submitting to the submitserver.

 You will be graded on the following:

|Item | Points |
|finds all the bugs (10 points each)  | 80 |
|all your tests pass on a correct implementation | 20 |

