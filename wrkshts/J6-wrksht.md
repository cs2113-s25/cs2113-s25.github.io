---
layout: worksheet
permalink: /worksheet/j6
showsolution: false
---

# Worksheet: J6

Submit a file called `worksheet-J6.md` to BB for this assignment. 

## Note

Attempt to answer these questions before running the code. This will improve your ability to analyize and reason about code without an IDE or compiler. This skill we be helpful on the exams.

## Questions

### q

Compile the two files below and run the main method in the `SimpleThreadExample`. 

```
$ javac *.java
$ java SimpleThreadExample
```

```java
/* SimpleThreadExample.java */
public class SimpleThreadExample {

    public static void main(String[] args) {
    
        
        Messages msg = new Messages();
        Thread morningThread = new GreetingsThread(msg, 0);
        Thread afternoonThread = new GreetingsThread(msg, 1);

        morningThread.start();
        afternoonThread.start();
        //MARK
        
    }
}
```

```java
/* Messages.java */
public class Messages {
    public String morning;
    public String afternoon;
    public String evening;
    public String night;

    public Messages() {
      morning = "Good morning!";
      afternoon = "Good afternnon!";
      evening = "Good evening!";
      night = "Good night!";
    }

    public String getMessage(int choice) {
      switch(choice) {
         case 0:
           return this.morning;
         case 1:
           return this.afternoon;
         case 3:
           return this.evening;
         case 4:
           return this.night;
         default:
           return "";        
      }
    }
 }
```

```java
/* GreetingsThread.java */
public class GreetingsThread extends Thread {

    private Messages msg;
    private int choice;
    public GreetingsThread(Messages msg, int choice) {
        this.msg = msg;
        this.choice = choice;
    }

    public void run() {
        System.out.println("Started the " + msg.getMessage(choice) + " thread...");
            
        //print 10 times
        for (int i = 0; i < 10; i++) {
            System.out.println(msg.getMessage(choice));
        }

        System.out.println("Exiting the " + msg.getMessage(choice) + " thread...");
    }
}
```

Then:
* Run the program a few times. Describe the output of this program. Is it consistent?
* Draw a memory diagram of the program at `MARK`

#### s
* The output of the program is not consistent.
* ```
  Stack
  
  .------------------------------------------------------------.
  |                                                            |
  |  main                   .------->morningThread -----.      '---->afternoonThread ---.
  | .-----------------.    |        .-------------.     |           .--------------.    |
  | | msg             |    |        | run()       |     |           | run()        |    |
  | | morningThread   |----'        | i           |     |           | i            |    |
  '-| afternoonThread |             | this        |     |           | this         |    |
    '-----------------'             '-------------'     |           '--------------'    |
                                                        |                               |
  ------------------------------------------------------+-------------------------------+--
  Heap                                                  |                               |
                                                        |                               |
     .--------------------------------------------------+--.                            |
     |  .-----------.             .-----------------.   |  |    .-----------------.     |
     '->| Messages  |<----.       | GreetingsThread |<--'  |    | GreetingsThread |<----'
        +-----------+     |       +-----------------+      |    +-----------------+
    .---| morning   |     '-------| msg             |      '----| msg             |
    | .-| afternoon |             | choice 0        |           | choice 1        |
    | | | evening   |-----------. '-----------------'           '-----------------'
    | | | night     |---------. |
    | | '-----------'         | |
    | |                       | |
    | |  .-----------------.  | |
    | |  | Good night!     |<-' |
    | |  '-----------------'    |
    | |                         |
    | |  .-----------------.    |
    | |  | Good evening!   |<---'
    | |  '-----------------'
    | | 
    | |  .-----------------.
    | '->| Good afternoon! |
    |    '-----------------'
    | 
    |    .-----------------.
    '--->| Good morning!   |
         '-----------------'
  ```

### q

Now let's modify `GreetingsThread` to add a `Thread.sleep()` in the `run()` method. Recompile the `GreetingsThread` class as below.

Run the program multiple times.  Does the output change in any way? Does one thread always finish first, or does the order change?


```java
/* GreetingsThread.java */
public class GreetingsThread extends Thread {
    private Messages msg;
    private int choice;

    public GreetingsThread(Messages msg, int choice) {
        this.msg = msg;
        this.choice = choice;
    }

    public void run() {
        System.out.println("Started the " + msg.getMessage(choice) + " thread...");

        for (int i = 0; i < 10; i++) {
            System.out.println(msg.getMessage(choice));

            try {
                // Sleep for 1 second (1000 milliseconds)
                Thread.sleep(1000); 
            } catch (InterruptedException e) {
                System.out.println("Interrupted while sleeping...");
            }
        }

        System.out.println("Exiting the " + msg.getMessage(choice) + " thread...");
    }
}
```

#### s
Because each thread will sleep for 1 second after each print statement, the output changes in a way that two outputs are not clustered (e.g. more interleaving between the two messages). The order of two threads finish is still random.

### q

Now let's add a `System.out.println()` at the end of the main method. Recompile the program with this addition, continuing from above. Explain how it is possible that the main method is complete but the program is still producing output.


```java
/* SimpleThreadExample.java */
public class SimpleThreadExample {
    public static void main(String[] args) {
            
        Messages msg = new Messages();
        Thread morningThread = new GreetingsThread(msg, 0);
        Thread afternoonThread = new GreetingsThread(msg, 1);

        morningThread.start();
        afternoonThread.start();

        System.out.println("Main method exiting...");
    }
}
```

#### s
The main method acts as a 3rd thread where we have 3 different threads in total. Thus, the main thread completing has no effect on the `morningThread` and `afternoonThread`, which will both continue running.

### q

Finally let's add a `thread.join()` to join the `morningThread` for 5 seconds before starting the `afternoonThread`. Recompile and rerun. Then describe the output of this program. Explain how attempting to join the first thread for 5 seconds affects the output of this program.


```java
/* SimpleThreadExample.java */
public class SimpleThreadExample {
    public static void main(String[] args) {
        Messages msg = new Messages();
        Thread morningThread = new GreetingsThread(msg, 0);
        Thread afternoonThread = new GreetingsThread(msg, 1);

        morningThread.start();

        try {
            System.out.println("Joining the morning thread for 5 seconds...");
            morningThread.join(5000);
        } catch (InterruptedException e) {
            System.out.println("Interrupted while joining a thread...");
        }

        afternoonThread.start();

        System.out.println("Main method exiting...");
    }
}
```

#### s
The output becomes more consistent than previous implementations. The join for 5 seconds forces the `morningThread` to run for the first 5 seconds, resulting in 5 "Good morning" being printed out consecutively (thread sleeps for 1 second after each print). After that, the `afternoonThread` starts and the main thread exits which leads to interleaving messages between `morningThread` and `afternoonThread`. Finally, because `morningThread` started at least 5 seconds before `afternoonThread`, it finishes first leaving the `afternoonThread` printing out consecutive "Good afternoon!" messages.

### q

What does `join()` do compared to `join(10)`?

#### s
`join()` will make the current thread wait until the referenced thread terminates; it may wait 0 seconds (if the referenced thread already terminated), or infinitely long (if the referenced thread never terminates). `join(10)` will make the current thread wait for a maximum of 10 milliseconds.

### q

What are all the possible outputs of running the code below?

<div class="side-by-side">
<div class="side-by-side-a">
```java
import java.util.*;

public class Ex0 {
  public static void main(String[] args) {
    Thread t = new Foo();

    t.start();
    int x = 5 * 5;
    System.out.println(x);
  }
}
```
</div>
<div class="side-by-side-b">
```java
public class Foo extends Thread {
  public void run() {
    int x = 7 * 7;
    System.out.println(x);
  }
}
```
</div>
</div>

#### s

It could print out the 25 and 42 in any order.

### q

What is the output of the code below? Is it deterministic?

<div class="side-by-side">
<div class="side-by-side-a">
```java
import java.util.*;

public class Ex1 {
  public static Random rand = new Random();

  public static void printSlow(String s, String t) {
    for (int i = 0; i < s.length(); i++) {
      try {
        Thread.sleep(rand.nextInt(1000));
      } catch (Exception e) {}
      System.out.println(t + s.charAt(i));
    }
  }

  public static void main(String[] args) {
    String s = "Mississippi";
    Thread t = new Foo(s, "   ");

    t.start();
    printSlow(s, " ");
  }
}
```
</div>
<div class="side-by-side-b">
```java
public class Foo extends Thread {
  private String msg, tab;

  public Foo(String s, String t) {
    this.msg = s;
    this.tab = t;
  }

  public void run() {
    Ex1.printSlow(this.msg, this.tab);
  }
}
```
</div>
</div>

#### s

See the notes for an example output; it is not deterministic.

### q

When adding into a linked list with the code below, why is a race condition possible here?

```java
      tail.next = new Node(s, null);
      tail = tail.next;
```

#### s

Each thread may call the constructor to create a new node. Then, one of the threads overwrites the old `tail.next` with this new node. Then, the other thread may also overwrite the current value of `tail.next` (which was a new node) with the other new node, losing one of the new nodes. This second thread then updates `tail` by setting it to the new node in `tail.next`, which is fine. However, the first thread then also tries to update `tail` by setting it to `tail.next`, but `tail.next` is `null`. Therefore, not only did we lose adding a node, but our `tail` now points to `null`, which will likely crash our code at some point.

### q

How do you solve the problem above?

#### s

Wrap the code/method that contains those two lines with the `synchronized` keyword. This will make the code above *atomic*, that is, the lines cannot be interleaved across two different threads. Once one thread starts to try to add the new node, it will block all other threads from trying to run the same lines.


### q

Why is the `synchronized` keyword necessary in the method below to avoid race conditions? The method is only one line of code, but the `value` is shared amongst multiple threads.

```java
    public void increment() {
        value++;
```

#### s

`value++` is actually doing the following two calculations:

```
temp = value + 1
value = temp
```

Let's imagine value is currently 10 in memory, before the code above runs. Two threads read this `value`, both setting `temp` to be 11. This is already wrong, because we want `temp` to be 12 at this point. Both threads will then set `value` to 11.

Making the method `sychronized` will ensure `value++;` is an atomic transaction and avoids the race condition.

```java
    public synchronized void increment() {
        value++;
```

### q

The `Singleton` class below implements the `Singleton` pattern.  The singleton pattern is a software engineering design pattern that restricts the instantiating of a class to a single instance. Review the `Singleton` class code below.  Is it possible to create more than one instance of the `Singleton` class if two threads attempt to call the `getInstance()` method at the same time?


```java
// Java program to create a Singleton class.
public class Singleton {
    // This is a private member variable so that the singletonInstance
    // can only be accessed through the getInstance() method.
    private static Singleton singletonInstance;

    // Private constructor forces the class to be instantiated 
    // via the getInstance method.
    private Singleton() {
        // private constructor.
    }

    // Method to get an instance of this class.
    public static Singleton getInstance() {
        // If this singleton instance is null, 
        // then construct a new instance.
        // Otherwise return the existing instance.
        if (singletonInstance == null) {
            singletonInstance = new Singleton();
        }

        return singletonInstance;
    }
}
```

#### s
Theoretically, it is possible to create more than 1 instance of the `Singleton` class if 2 threads attempts to call `getInstance()` method at the same time in the above code. The reason it is only "theoretical" is two threads need to call `getInstance()` at almost exact same time so that one `getInstance()` is not complete before the other thread executes `getInstance()`. See the example below on how this issue is resolved.

### q

Review the modified thread safe Singleton class code below.  Is it possible to create more than one instance of the `Singleton` class if two threads attempt to call the `getInstance()` method at the same time? How does the synchronized keyword affect the attempts to call the `getInstance` method from multiple threads at the same time?


```java
// Java program to create thread safe Singleton class.
public class Singleton {
    // This is a private member variable so that the singletonInstance
    // can only be accessed through the getInstance() method.
    private static Singleton singletonInstance;

    // Private constructor forces the class to be instantiated 
    // via the getInstance method.
    private Singleton() {
        // private constructor.
    }

    // Synchronized method to control simultaneous access 
    // to the getInstance method.
    synchronized public static Singleton getInstance() {
        // If this singleton instance is null, 
        // then construct a new instance.
        // Otherwise return the existing instance.
        if (singletonInstance == null) {
            singletonInstance = new Singleton();
        }

        return singletonInstance;
    }
}
```

#### s
It is not possible for multiple threads to create more than one instance of the `Singleton` class if more than one threads attempt to call the `getInstance()` method at the same time with the synchronized keyword added to the `getInstance()` method.


