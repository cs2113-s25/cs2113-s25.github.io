---
layout: worksheet
permalink: /worksheet/j2
showsolution: false
---

# Worksheet: J2

Please submit your answers to the questions as comments in a `J2.md` markdown file you'll be writing in this lab. To render your file, create a github repo and upload your file there -- it can be viewed in your web browser.

# Grading rubric and submission

When you are done, submit your `J2.md` file to BB.

 You will be graded on the following:

|Item | Points |
|Answers are correct  | 100 |

## Questions

### q

How are `private`, `public`, and `protected` visibility modifiers handled when fields/methods with these different visibilities are inherited from a parent class?

From a grandparent class?

How do classes outside the class inheritance hierarchy see (or not see) fields/methods with these different modifiers?

#### s

Any class anywhere can see `public` fields/methods. Any child classes in the inheritance hierarchy can see anything `protected`, but other classes outside the hierarchy cannot see these items. Only the class itself can see anything `private`.


### q

For the below questions, when the class `Point` is referenced, we are talking about the below class, which you can assume is fully implemented and working as described:

```java
public class Point {
   private double x,y; //the x,y fields
   public Point(double x,double y); //construct a point from an x,y
   public Point(Point other); //construct a point from another point
   public double getX(); //return the x component
   public double getY(); //return the y component
   public double setXY(double x, double y); //sets the x and y fields
   public String toString(); //return the string representation
   private double sum_x_y(); // Returns the sum of X and Y
}

```


Say we want to make a class that extends `Point` with a method that can reflect a point across the X and Y axis:

```java
public class CustomPoint extends Point {
    public void reflect(); // Reflects point
}
```

Which of the following implementations achieves this?

```java
    // Option 1
    public void reflect() {
        x = -x;
        y = -y;
    }

    // Option 2
    public void reflect() {
        this.x = -this.x;
        this.y = -this.y;
    }

    // Option 3
    public void reflect() {
        this = Point(-x,-y);
    }
    
    // Option 4
    public void reflect() {
        double x = -this.getX();
        double y =-this.getY();
        this.setXY(x,y);
    }
    
    // Option 5
    public void reflect() {
        x = -this.getX();
        y = -this.getY();
    }
```

Explain why. 

#### s
Option 4 achieves the goal of reflecting the point. None of the other options compiles because `x` and `y` in `CustomPoint` is inheritted from `Point` and cannot be read/written to directly in `CustomPoint` since they are declared private in `Point`.

### q

If we add this constructor to `CustomPoint`:

```java
    public CustomPoint() {
        setXY(10, 10); // Line 1
        super(0, 0); // Line 2
    }
```

...and then run this program,  what is the output?

```java
    public static void main(final String args[]) {
        CustomPoint p = new CustomPoint();
        System.out.println(p.toString());
    }
```

#### s
The program does not compile because the constructor call on `Line 2` must be called before anything else inside the constructor for `CustomPoint`.


### q

What if we switch line 1 and 2 in the previous question?

#### s
Now the program compiles and the output is `(10.0, 10.0)`.

### q

If we want to override `sum_x_y` in our custom point, but first reflect the point before returning the sum, which of the following implementations are valid? (Note: assume that `reflect` has a valid implementation)

```java
    //Option 1
    public double sum_x_y() {
        this.reflect();
        return super.sum_x_y();
    }

    //Option 2
    public double sum_x_y() {
        this.reflect();
        return this.getX() + this.getY();
    }

    //Option 3
    public double custom_sum_x_y() {
        this.reflect();
        return super.sum_x_y();
    }

    //Option 4
    public double custom_sum_x_y() {
        this.reflect();
        return this.getX() + this.getY();
    }

```

Explain your answer.

#### s
Option 2 is valid. Option 1 and 3 does not compile because `sum_x_y()` is a private method that cannot be accessed by `CustomPoint` class. Option 4 has the correct implementation of the method but does not override `sum_x_y` as it has a different function name.

### q

What is the point of the `protected` modifier? Why do we have it and how does it work in terms of inheritance?

#### s
The `protected` modifier allows all child (and grand-child, etc) classes to see the variable or method within the inheritance hierachy. Otherwise, like `private`, other classes cannot see these items. It's meant to obviate the need for child classes to use public getters and setters to access these items, especially when we don't actually want them to be fully public to the rest of the world.

### q

Consider the following class

```java

public class Racecar {

    private int number; 
    private Driver driver; //assume implemented properly
    protected String sponsor = null;
    public Racecar(int n, Driver d) {
        number = n;
        driver = d;
    }

    public String toString() {
        return "Car #" + number + " Driver: " + driver;
    }
    
    protected addSponsor(String sp) {
        sponsor = sp;
    }
}
```

Suppose we want to extend this to a `FormulaOne` class which has a make, e.g., Mercedes. Complete the constructor and `toString()` method.

```java

public class FormulaOne extends Racecar {
    private String make;

    //TODO
}
```

#### s
```java

public class FormulaOne extends Racecar {

    private String make;
    public FormulaOne( int n, Driver name, String car_make) {
        super(n, name);
        make = car_make;

    }

    @Override
    public String toString() {
        return super.toString() +" Make: " + this.make;
    }
    
}

```

### q 

Using the `Racecar` and `FormulaOne` classes above, if we had a main method **in a different class than either of those**,

```java

public static void main(String args[]) {


   Racecar r = new Racecar(/* ... some args .. */);
   r.addSponsor("Home Depot"); //<--A

   FormulaOne f1 = new FormulaOne(/* ... some args .. */);
   f1.addSponsor("Home Depot"); //<--B
     
}
```

Does the code work at mark `A` or mark `B` or neither? Explain.

#### s
The code works at both marks. Each mark is adding a sponsor to two different objects, so there is not a conflict of overwriting the other. Since `F1` inherits from `Racecar`, it also has access to the `addSponsor` function even though it was not explicitly defined in the F1 class.


### q

Consider the UML diagram from the notes. Expand this to include an **intern**. An **intern** is like an employee, has a manager, unit, but has an expiration on their employment. How does this fit into the UML diagram?


Include your UML diagram and explanation below in this markdown file.

#### s

The intern should have Employee as its parent class, with an additional `Date` field called `employmentExpiration`.

Additional type left as an exercise to the reader.


