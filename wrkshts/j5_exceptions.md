---
layout: worksheet
permalink: /worksheet/j5_exceptions
showsolution: false
---

# Worksheet: J5

Worksheets are self-guided activities that reinforce lectures. They are not graded for accuracy, only for completion. Submit a file called `J5.md` on BB for this assignment.

## Note

Attempt to answer these questions before running the code. This will improve your ability to analyize and reason about code without an IDE or compiler. This skill we be helpful on the exams.

## Questions

### q
What does the following code print to the terminal?

```java
int[] x = {};
int y = 0;
System.out.println(x[y]);
```

#### s
It will crash and print a stack trace to the terminal because an `ArithmeticException` was raised when doing `x[y]` 

### q
What does the following code print to the terminal?

```java
int[] x = {};
int y = 0;

try {
    System.out.println("before");
    System.out.println(x[y]);
    System.out.println("after");
} catch (Exception e){
    System.out.println("there was something wrong");
}
```

#### s
```
before
there was something wrong
```

### q
Does the following program crash? What gets printed to the terminal?

```java
int[] x = {};
int y = 0;

try {
    System.out.println("before");
    System.out.println(x[y]);
    System.out.println("after");
} catch (Exception e){
    System.out.println("there was something wrong");
    e.printStackTrace();
}
```

#### s
```
before
there was something wrong
java.lang.ArithmeticException: / by zero
    at [filename:line number]
```

### q
What does the following code print to the terminal?

```java
int[] x = {};
int y = 0;

try {
    System.out.println("before1");
    System.out.println(x[y]);
    System.out.println("after1");
} catch (ArithmeticException e){
    System.out.println("there was something wrong1");
}

try {
    System.out.println("before2");
    System.out.println(x[y]);
    System.out.println("after2");
} catch (Exception e){
    System.out.println("there was something wrong2");
} catch (ArithmeticException e){
    System.out.println("there was something wrong3");
}
```

#### s
```
before1
there was something wrong1
before2
there was something wrong2
```

### q
How do you manually raise an exception in Java? Why are you allowed to do this?

#### s
You can call the exception's constructor to create a new exception object, and then raise that exception with the `throw` keyword inside a method. This has the same behavior as a "naturally occuring" exception (such as a division by zero or a null pointer exception). 

When a method explicitly raises an exception like this (and it's not caught elsewhere in the method), the method signature should be annotated with a `throws` clause.

You're allowed to do this in Java because sometimes you'll want your own custom exception types (i.e. not "naturally occurring") to be raised and caught elsewhere in your code.

### q
What does the following code print to the terminal for the cases below? Assume the code compiles.

```java
public static void main(String[] args){

    int x = 3;
    String y = mystery();

    try {
        System.out.println("here 1");
        foo(x, y);
        System.out.println("here 2");
        int z = 3 / 0;
    } catch (Exception e){
        System.out.println("error 1");
    } catch (ArithmeticException e){
        System.out.println("error 2");
    }

    System.out.println("here 3");
}

public static void foo(int x, String y) throws ThingException{
    
   int y_int = -4;
   try{
         y_int = Integer.parseInt(y);
        check(y_int);
    }
    catch (Exception e){
        System.out.println("bad y");
        throw new ThingException();
    }

    System.out.println(y_int);
    int z = 4 / y_int;
    System.out.println(y_int);
}

public static void check(int y){
    if (y < 0)
        throw new ArithmeticException();
    System.out.println("in check");
    y = y / 0;
    System.out.println("end check");
}

```

Case 1: `mystery()` returns `"1"`
Case 2: `mystery()` returns `"0"`
Case 3: `mystery()` returns `"oops"`

#### s
Case 1:
```
here 1
in check
bad y
error 1
here 3
```

Case 2:
```
here 1
in check
bad y
error 1
here 3
```

Case 3:
```
here 1
bad y
error 1
here 3
```

### q
Give an example of when you would use exception handling over an if statement. 
#### s
An if statement only allows an error state to be handled locally. Exceptions allow error states to "bubble up" the call stack to be handled elsewhere.

For example, if you are trying to open a file that doesn't exist, the actual code that interfaces with the OS and file system to open the file is very low-level, deep in some library. If the filename is incorrect, it's not the place to ask the user to re-enter it; we don't know if the filename was typed in, came from a GUI, or was read from some other file -- we don't know where this filename came from. By raising an exception that can bubble up the call stack until it is caught, we have a chance to catch it in the location where the user actually specifies a file (whether by keyboard, command line, GUI window, or reading a file).

### q
Give a reason why it is not a good idea to only wrap your entire `main` method inside one `try-catch` block.

#### s
If you only have one `try-catch` block in `main` your code may never crash, but you also lose the ability to appropriately handle exceptions where they happen
 
### q
What is the difference between a *checked* versus an *unchecked* exception?

#### s
Unchecked exceptions are not required to be caught in a `try-catch` block (eventually). Checked exceptions must eventually be caught; this can be done locally, or the method that raises a checked exception must declare this exception type can be raised with a `throws` clause.

### q
How does the `Throwable` class inheritance hierarchy distinguish between checked and unchecked exceptions?

#### s
The hierarchy contains a *RuntimeException* class; any child class of this class is an unchecked exception:
```
                       Throwable
                       /      \
                      /        \
                   Error     Exception
                              /    \
                             /      \
                            /        \
               ** RuntimeException     IOException
```

### q
How is I/O (input/output) related to exception handling in Java?

#### s
Opening a file requires method calls that can raise checked exceptions; therefore, when calling these methods your call to open a file must be placed inside a `try-catch` block in order for the code to compile.

### q
Write code that opens a file called `data.txt` and prints out its contents, line by line.

#### s
```java
try {
    LineNumberReader reader = new LineNumberReader(new InputStreamReader(new FileInputStream("data.txt")));
    String line = reader.readLine();
    while( line != null ) {
      System.out.println(line);
      line = reader.readLine();  
    }
    reader.close();
} catch (IOException e){
    e.printStackTrace();
}
```

### q
Write code that prints `Hello World!` and `How are you?` on two separate lines of a file called `data.txt`

#### s
```java
try {
        PrintWriter pw = new PrintWriter(new File("output.txt")); 
        pw.println("Hello World!");
        pw.println("How are you?");
        pw.close(); 

} catch (IOException e){
    e.printStackTrace();
}
```

### q
What happens if you don't close an input/outputstream buffer in your code?

#### s
Usually, nothing, if your program is short and runs quickly; once the `main` method exits, all these resources are returned anyway...

However, if you are opening multiple buffers (and not closing them) in a loop that runs for a long time (this opening too many of these buffers) you can run out of memory and have other bad things happen (ask me how I know). It's good practice to always close the buffers you open. Newer versions of Java even do this automatically:

Old Java that uses a `finally` clause to wrap everything up at the end regardless if an exception was raised or not:
```java
static String readFirstLineFromFileWithFinallyBlock(String path) throws IOException {
   
    FileReader fr = new FileReader(path);
    BufferedReader br = new BufferedReader(fr);
    try {
        return br.readLine();
    } finally {
        br.close();
        fr.close();
    }
}
```

versus the newer version of Java that closes these resources automatically using a [*try-with-resources* statement](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html):
```java
static String readFirstLineFromFile(String path) throws IOException {
    try (FileReader fr = new FileReader(path);
        BufferedReader br = new BufferedReader(fr)) {
        return br.readLine();
    }
}   
```

# Grading rubric and submission

When you are done, submit your `J5.md` file to BB.

 You will be graded on the following:

|Item | Points |
|Answers are completed (for content)  | 100 |