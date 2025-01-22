---
layout: toc
permalink: lab/4_debugging_with_tests
---
# Lab 4: Writing your own unit tests

In this short lab, you will use *print statement debugging* as we learned about earlier to find and fix a fault that is failing the unit tests below in the attached codebase.

## Setup

Copy the following four files into a folder on your computer:
* [Lab4_Tester.java](./Lab4_Tester.java)
* [Person.java](./Person.java)
* [Address.java](./Address.java)
* [junit jarfile](./junit-platform-console-standalone-1.7.0-M1.jar)

To run your unit tests – remember, you need to have the junit jar file in the same directory – compile and run your code with the following commands on the terminal (depending on your OS):

#### Windows
`javac -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" *.java
java -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab4_Tester`

#### Mac/Linux
`javac -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" *.java
java -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab4_Tester`

## Finding and fixing the bugs

There are a handful of bugs in `Person.java` and `Address.java` as reflected in the unit tests. Use print statements, like in Lab 1, to work your way backwards from the test cases and figure out what's wrong, and fix it.

Remember that you can add print statements anywhere, including the Junit test file itself, to print out pieces of code. For example, you can print out what the `toString()` methods for both `Person` and `Address` are returning for a specific person to help you debug.

**You will need to have meaningful print statements that tell a story** in order to recieve credit for this lab. Even if you figured out the bug "in your head," use print statements to show how you could have otherwise deduced what the bug was.

# Grading rubric and submission

Create a tar file with your code by running the following command in the terminal:
`tar -cvf lab4.tar *.java`

Then, upload this tarfile to the submitserver to get graded.


 You will be graded on the following:

|Item | Points |
|all test cases pass (without hardcoding) | 100 |
|missing meaningful print statements | up to -100 |

