---
layout: worksheet
permalink: /worksheet/j0
showsolution: False
---

# Worksheet: J0

Worksheets are self-guided activities that reinforce lectures. They are due Thursdays the week they are assigned.

## Setup

Create a new repo using all the steps in Lab 0 called `yourgitusername-worksheet-J0`. Then, add the following file to it:

Download the [UnitTestExample.java](https://cs2113-s23.github.io/labs/UnitTestExample.java)

Download the Junit jar file from the pinned post on Ed. Save it in the same directory as your java file (preserving the name `junit-platform-console-standalone-1.7.0-M1.jar`). This will allow you to run Junit tests through your terminal; there are also plugins for junit for text editors like VSCode if you want to google how to set that up.

Download the [CS1111_checks.xml](https://www2.seas.gwu.edu/~kinga/CS1111_S22/labs/CS1111_checks.xml) into the same directory.

Download the [checkstyle-9.2.1-all.jar](https://github.com/checkstyle/checkstyle/releases/download/checkstyle-9.2.1/checkstyle-9.2.1-all.jar
) into the same directory.

## Understanding unit tests

We will use unit tests throughout the semester to test your code; while we'll learn about them more formally later in the semester, the goal of this assignment is to make sure you're familiar enough with the basics. In addition, we sometimes use unit tests in an unusual way, to pipe the output of running `main` into a string that we compare to an expected output. 

Open the `UnitTestExample.java` file, and take a look at the three tests. The first one is comparing `Earth` to `Earth`, and should pass. The second one is comparing `Moon` to `moon`, and will fail because the two strings are not equal. 

The third test is running the Java Checkstyle command from the command line, and making sure that it reports no warnings. Right now, it also fails, because the file it is checking -- `UnitTestExample.java` -- doesn't have good coding style. We'll fix that and get it to pass in a minute.

## Running unit tests

To run your unit tests -- remember, two of them will fail for now -- compile and run your code with the following commands on the terminal (depending on your OS):

Windows:
`javac -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" UnitTestExample.java`
`java -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore UnitTestExample`

Mac/Linux:
`javac -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" UnitTestExample.java`
`java -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore UnitTestExample`

Your output should look something like:

```
JUnit version 4.13
..E.Starting audit...[WARN] C:\Users\Dr_Kinga\Documents\CS2113_S23\cs2113-s23.github.io\wrkshts\UnitTestExample.java:7:25: Member name 'n' must match pattern '^[a-z][a-z0-9][a-zA-Z0-9]*$'. [MemberName]Audit done.
E
Time: 2.406
There were 2 failures:
1) test2(UnitTestExample)
org.junit.ComparisonFailure: expected:<[M]oon> but was:<[m]oon>
        at org.junit.Assert.assertEquals(Assert.java:117)
        at org.junit.Assert.assertEquals(Assert.java:146)
        at UnitTestExample.test2(UnitTestExample.java:22)
2) test3(UnitTestExample)
org.junit.ComparisonFailure: expected:<Starting audit...[]Audit done.> but was:<Starting audit...[[WARN] C:\Users\Dr_Kinga\Documents\CS2113_S23\cs2113-s23.github.io\wrkshts\UnitTestExample.java:7:25: Member name 'n' must match pattern '^[a-z][a-z0-9][a-zA-Z0-9]*$'. [MemberName]]Audit done.>
        at org.junit.Assert.assertEquals(Assert.java:117)
        at org.junit.Assert.assertEquals(Assert.java:146)
        at UnitTestExample.test3(UnitTestExample.java:50)

FAILURES!!!
Tests run: 3,  Failures: 2
```

## Getting tests to pass

Next, modify your java file to 1) change the variable name `n` on line 7 to be something better so it passes the style checker; and 2) change the value of the variable `satellite` on line 9 so that it passes the test case. Looking at line 20 will show you what the expected value is for that second test case. Then, recompile and re-run your tests using the commands above.

When all your tests pass, you should see something like:

```
JUnit version 4.13
...Starting audit...Audit done.

Time: 0.918

OK (3 tests)
```

Please reach out to a TA for help if you need it.


# Grading rubric and submission

Create a tar file with your code by running the following command in the terminal:
`tar -cvf J0.tar UnitTestExample.java`

Then, upload this tarfile to the submitserver, and make sure you see 100/100 displayed there.

 You will be graded on the following:

|Item | Points |
|unit tests pass (33 points each) | 100 |

