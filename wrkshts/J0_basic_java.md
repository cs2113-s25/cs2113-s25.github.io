---
layout: worksheet
permalink: /worksheet/j0_basic_java
showsolution: false
---

# Worksheet: J0

Please submit your answers to the questions as comments in a `J0.txt` file you'll be writing in this lecture. 

# Grading rubric and submission

When you are done, submit your `J0.txt` file to BB.

 You will be graded on the following:

|Item | Points |
|Answers are correct | 100 |

## Questions

### q

Which of the following is an object and which is a basic type?

```java
int a;
double b;
int c[] = {1, 2, 3};
String s = "Hello World";
```

#### s
* In the first two lines, `int` and `double` are basic types.
* In the last two lines, array and `String` are both stored on the heap; technically, only `String` is a proper object from the base class `Object`.


### q

Two part question:

(A) What is a static method in Java?

(B) Why does the main method need to be a static method?

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("hello, world");
    }
}
```

#### s
* Static methods are called directly, or statically, without the need of an object instance.
* `main` methods need to be static because it needs to be called without instantiating an object of the class.


### q

What is the output of the following programs?

```java
/* Program 1 */
public static void main(final String args[]) {
    String choice = new String("A");
    if (choice == "A") {
        System.out.println("Correct");
    }
    else {
        System.out.println("Wrong");
    }
}
```

```java
/* Program 2 */
public static void main(final String args[]) {
    String choice = new String("A");
    if (choice.equals("A")) {
        System.out.println("Correct");
    }
    else {
        System.out.println("Wrong");
    }
}
```

#### s
* Program 1's output is `Wrong` and Program 2's output is `Correct`.
* Similar to the case in C, `String` is an object type where `String choice` will make `choice` have the address of the string on the heap. Thus, in Program 1, the if statement is comparing a memory address to a string; while in Program 2, the `.equals()` method will compare the content `choice` is pointing at to the string `"A"`.

### q

Does the below program change the season? Why, or why not?

```java
static void change_season(String str) {
    str = "Spring";
}

public static void main(final String args[]) {
    String season = "Winter";
    change_season(season);
    System.out.println("The current season is: " + season);
}
```

#### s
The program does not change the season, because the original season variable, which is a pointer to
`Winter` is reassigned to a new string, `Spring`, inside the method. That breaks the link with the original season in `main`.

### q

What is the output of the main method below? Please explain.

```java
public class Point {
    double x = 0;
    double y = 0;

    public Point(double x, double y) {
        x = x;
        y = y;
    }
}
```

```java
public static void main(final String args[]) {
    Point point = new Point(1, 2);
    System.out.println("X: " + point.x + " Y: " + point.y);
}
```

#### s
The output of the main method is `X: 0.0 Y: 0.0`. The reason is in the `Point` class, the constructor does not pass the parameters `x` and `y` onto `x` and `y` of the `Point` class.

### q

What principle of OOP does the `private` declaration for variable and functions achieve? Explain.

#### s
The principle of Information Hiding is achieved by `private` declaration of variable and functions. The reason is `private` variable and functions cannot be accessed by other objects outside the class.

### q

In the `Point` class below, how does Java choose between the two constructors?

```java
public class Point {

   private double x, y; 
   
   public Point(double x, double y) {
        this.x = x;
        this.y = y;
   }

   public Point(Point other) {
       this.x = other.getX();
       this.y = other.getY();
   }

}
```

#### s
Java chooses between the two constructors by checking the type of the argument passed in. When a new `Point` is called with two `double`s, it will use the constructor `public Point(double x, double y)`; in contrast, when a new `Point` is called with a `Point` passed in, it will use the constructor `public Point(Point other)`.

