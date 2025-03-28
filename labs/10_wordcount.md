---
layout: default
permalink: /lab/10_wordcount
---

# Lab 10: Wordcount

## Setup

Download the [Lab10_Tester.java](./Lab10_Tester.java) file.

### Github setup

Use git, as discussed in Lab 0, to create a repo called `gitusername-lab10`, add the file above to it, and commit and push the changes to github. 

You will also need to create `WordCounter.java`, `EmptyFileException.java`, `InvalidStopwordException.java`, and `TooSmallText.java` files and add them to your repo for submission.

You will need to use this repo effectively to receive full credit on this assignment, even though you will be submitting it on the submitserver. See the grading rubric below.


## Word Count utilities

Being able to count the number of words in a piece of text is a common, often critical task required in the real world. For example, many web forms have word limits (such as when booking an appointment with a medical provider); other examples are word count limits on academic papers being considered for publication, professors asking for specific word counts on essays, or word count guidelines for different genres of fiction for authors. Counting the number of words in a file is available through text editors such as Microsoft Word, as well as command-line tools such as `wc` in the unix operating system.

### Using regular expressions

Conceptully, counting words is relatively simple; one can tokenize a document into words based on whitespace as a delimiter. Most of the time, these whitespaces would be the space characters, and perhaps tabs and newlines. However, sometimes multiple spaces are used between sentences. Punctuation (such as periods) can be ignored when counting the number of words in a document, as these are inside or adjacent to words (such as `'` or `!`). However, some punctuation such as `--` or ellipses (`...`) may occur between words with or without spaces in between. There may be all kinds of emojis or other characters in the text that someone doesn't want to include in the word count.

Wouldn't it be nice if there was a clean way to describe what "words" look like, and have an algorithm that scans an input stream looking for words (under the assumption that they are separated by non-words)?

It turns out, Java, and most other languages, have support for something called Regular Expressions. Loosely, regular expressions are a way to allow programmers to define what characters can define sub-groups within a string. Using [predefined character classes](https://docs.oracle.com/javase/tutorial/essential/regex/pre_char_classes.html) one could define, for example, an address as something that has a three digit street number, followed by a space, followed by a single English word, followed by a space, followed by a label, such as `800 Cherry Lane`:

`\d\d\d [a-zA-Z]+ (Lane|Street|Drive)`

The first three `\d`s allow one digit each. The character class between the brackets accepts one upper or lowercase letter and the `+` sign means at least one such character. The three options between parentheses separated by `|` allow one of these three labels only. Spaces are included as well. Obviously, the regular expression above is extremely restrictive in terms of real-world addresses, but hopefully you can get a feel for how programmers might use regular expressions for these kinds of tasks. We'll use regular expressions in this lab to define what words look like, and then pass them to some methods in Java that can help parse strings for such tokens.

Note: you may use the link above to examine and copy code from the Oracle documentation (for regular expressions only) for this assignment. All other code you submit must be code that you wrote yourself, that we have taught in classes you've taken here at GW. You may not use any outside resources (other than the link above) and you may not work with any other students on this assignment. Finally, you should not hard-code the expected output in your solutions; doing so will not receive credit (if you are pasting long strings of English text into your code, you're hard-coding the solution).

## Handling common exceptions in the right place

While using regular expressions to write a tool to count the number of words in a piece of text is helpful, it doesn't obviate all the issues one could entcounter while trying to complete this task. For example, if we're trying to count the number of words in a file, a missing file (because the user misspelled the filename) is something we'd like to communicate to the user and recover from. Alternatively, the file might exist, but it could be corrupted, or empty, or there could be some issue with its contents. 

We'd like a way to handle these different kinds of exceptions in the appropriate location in our code. For example, sometimes we could ask the user to choose a differnt file; other times, we could ask them if they want to proceed by just ignoring that error. 

Fortunately, Java's exception handling mechanisms allow us to catch different types of exception objects based on their class. Recall, these exceptions follow a class hierarchy, and `try-catch` statements allow us to place handling code in appropriate locations in our algorithms that can allow for graceful recovery from these unexpected situations. In this lab, we'll be defining our own exception classes to faciliate this kind of error handling.



## Task Requirements

In this lab, you'll write a driver in `WordCounter.java` that allows the user to provide text via the terminal, a file, or directly to a method. Then, your code will count the number of words in that text using regular expressions. If any errors are encountered, they are handled as described below.

This word count utility will not only allow users to get a total count of the number of words in a text, but also the count of the number of words until a specific stop-word (supplied by the user) is encountered.

Open a new file called `WordCounter.java` and copy and paste in the following code, and save the file.

```java
public class WordCounter {

}
```

Then, in three separate files, create classes for `EmptyFileException`, `InvalidStopwordException`, and `TooSmallText`. You will fill these out below.

### The `WordCounter` class

You will write this class which is responsible for:
* a method called `processText` that expects a `StringBuffer` as argument (the text), and a `String` stopword, and counts the number of words in that text through that stopword. If the stopword is not found the text, the method will raise an `InvalidStopwordException`. If the stopword is `null`, your method will count all words in the file. The methods returns the integer word count, unless the count was less than five, it which case it raises a `TooSmallText` exception (regardless of whether or not it found the stopword). For example, if there are only three words in the text, your code will raise the exception.
* a method called `processFile` that expects a `String` path as an argument, and converts the contents of the file to a `StringBuffer`, which it returns. If the file cannot be opened, it should prompt the user to re-enter the filename until they enter a file that can be opened. If the file is empty, this method should raise an `EmptyFileException` that contains the file's path in its message.
* a `main` method that asks the user to choose to process a file with option `1`, or text with option `2`. If the user enters an invalid option, allow them to choose again until they have a correct option. Both of these items will be available as the first command line argument. It then checks to see if there is a second command line argument specifying a stopword. The method then calls the methods above to process the text, and outputs the number of words it counted. If the file was empty, this method will display the message of the exception raised (which includes the path of the file), and then continue processing with an empty string in place of the contents of the file (note that this will raise a `TooSmallText` exception later). Note that the path of the empty file may not be the same path that was specified in the command line by the time this exception is raised. If the stopword wasn't found in the text, allow the user one chance to re-specify the stopword and try to process the text again. If they enter another stopword that can't be found, report that to the user.

Your `processText` method should use regular expressions to define what a word is; for this lab, we'll limit words to only alphanumeric characters with single quotes, that is, a-z, A-Z, 0-9, and `'`. We'll also define a word as needing to be at least one character long. The code below allows you to specify a regular expression, and then use it to keep searching for the next word in a piece of text:

```
Pattern regex = Pattern.compile("your regular expression here");
Matcher regexMatcher = regex.matcher(text);
while (regexMatcher.find()) {
    System.out.println("I just found the word: " + regexMatcher.group());
} 
```

A number of things can go wrong in the methods above; you will need to wisely place `try-catch` blocks in your code in the appropriate places in order to handle these exceptions in a way that recovery is elegant. Don't just include a single `try-catch` block that contains all of `main`. In particular, you'll want to raise and handle the exceptions below; they should all be public classes outside your `WordCounter` class.

### The `EmptyFileException` class

Extend Java's `IOException` class to be this `EmptyFileException` class. An exception of this type should be raised when the contents of the file to be parsed are empty. You should pass in a string to its constructor, which passes that string to the parent's constructor. This string will be what is printed when your other code does something like:

```
catch (TooSmallText e){
    System.out.println(e); // will print whatever string you passed to the constructor
}
```

because `.toString()` will be called on the exception object there.

### The `InvalidStopwordException` class

Extend Java's `Exception` class to be this exception that is raised when the stopword is not found in the text.

### The `TooSmallText` class

Extend Java's `Exception` class to be this exception that is raised when the length of the text is less than five words.

## Running your program

You can run your code to open a file with the following commands (assuming you've created the file or use the ones in the unit tests):

```
java WordCounter myFile.txt stopword
java WordCounter myFile.txt
```
and select option `1`.

You can also place a string between double quotes for processing with option `2`:

```
java WordCounter "Please process this sentence for me I want to know its length!"
```

## Junit testing

First, take a look at the Junit file provided and make sure you understand/appreciate the exception handling an heavy reliance on input streams in that file. For example, in `test9` we re-route the keyboard input to come from a buffer we designed and filled; `System` doesn't care, and your code executes the same way in your `main` method as if you were typing in input via the keyboard. Also observe how the unit tests expect to catch certain exceptions raised by your non-`main` methods, including `catch` blocks with multiple checks. Finally, the unit tests are great because you can re-run them with a single stroke; you'll need to test your `main` method manually, however, and you'll realize what a pain that is by comparison.

To run your unit tests -- remember, you need to have the junit jar file in the same directory -- compile and run your code with the following commands on the terminal (depending on your OS):

### Windows
`javac -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" Lab10_Tester.java`
`java -classpath ".;junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab10_Tester`

### Mac/Linux
`javac -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" Lab10_Tester.java`
`java -classpath ".:junit-platform-console-standalone-1.7.0-M1.jar" org.junit.runner.JUnitCore Lab10_Tester`


# Grading rubric and submission

In your github repo, type the following command to pipe your log to a text file:
`git log > log_file.txt`

Next, type the following command to compress your files into the required submission format:
`tar -cvf lab10.tar WordCounter.java TooSmallText.java InvalidStopwordException.java EmptyFileException.java log_file.txt`

Submit your code, as `lab10.tar` on the submitserver. 

Use git, as discussed in lab zero, to submit your work in a repo called `gitusername-lab10`. You will be graded on the following:

|Item | Points |
|your git logs show comments that helpfully and meaningfully describe what updates you were committing | 2 |
|your git logs show evidence that you committed code at least once during the WordCounter lab | 1 |
|your git logs show at least five commits that are all at least ten minutes apart | 1 |
|the test cases pass (6 points each) | 84 |
|`main` prompts the user to re-enter an option until a correct choice is made | 3 |
|`main` asks the user to re-enter a stopword when a bad stopword is provided for a file| 3 |
|`main` prints out the correct number of words when the user chooses to process command line text that is long enough| 3 |
|`main` prints a warning when the user chooses to process command line text that is too short| 3 |
|TOTAL | 100 |

<font color=red>Note: hard-coding unit tests (by copying in the expected value into your code) will not receive points.</font>
