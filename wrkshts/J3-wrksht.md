---
layout: worksheet
permalink: /worksheet/j3
showsolution: false
---

# Worksheet: J3


Worksheets are self-guided activities that reinforce lectures. They are due Thursdays the week they are assigned.

Please submit your answers to the questions as comments in a `J3.md` markdown file you'll be writing in this lab. To render your file, create a github repo and upload your file there -- it can be viewed in your web browser.

# Grading rubric and submission

When you are done, submit your `J3.md` file to BB.

 You will be graded on the following:

|Item | Points |
|Answers are completed (for content)  | 100 |


## Note

Attempt to answer these questions before running the code. This will improve your ability to analyze and reason about code without an IDE or compiler. This skill we be helpful on the exams.

## Questions


### q
Define **polymorphism** in the context of Java and provide one example where it is valuable. 

#### s

**Polymorphism** in Java allows multiple implementation of the same interface. One example will be the `Point` and `CustomPoint` classes we implementated in class where we can have a `toString()` method in both `Point` and `CustomPoint` that prints out different information.


### q

Consider the following program from the class notes

```java
public class Ex3 {
  public static void main(String[] args) {
    Random   rand = new Random(System.currentTimeMillis());
    Point    v    = new Point(3, 4);
    LabPoint w    = new LabPoint(5, 2, "A");
    String   x    = "I'm a string";
    Scanner  y    = new Scanner(System.in);

    Object u;
    int i = rand.nextInt(4);

    if( i == 0 )
      u = v;
    else if( i == 1 )
      u = w;
    else if( i == 2 )
      u = x;
    else
      u = y;
    System.out.println(u.toString()); //<--
  }
}
```

Explain how polymorphism makes this program possible. 

#### s
Since every class that does not have the `extends` keyword implicitly extends the `Object` class, the `Object u` declaration makes `u` capable of "morphing" into any of the 4 variables `v, w, x, y`.

### q
What is the output of this program? You should be able to do this without running the program!

```java
class A {
    public String toString(){
        return "A";
    }
}

class B extends A{
    public String toString() {
        return "B";
    }
}

class C extends A {
    public String toString() {
        return super.toString();
    }
}

class D extends C {
    public String toString() {
        return super.toString();
    }
}

public class tmp {
    public static void main(final String args[]) {
        D d = new D();
        System.out.println(d.toString());
    }
}
```

#### s
The output is `A` because `class D` extends `class C` and `class C` extends `class A` where both classes `C, D` have their `toString()` function return `super.toString()` and the `toString()` method of `class A` returns a single character `A`.

### q
What is the output of this program? You should be able to do this without running the program!

```java
class A {
    public String toString() {
        return "A";
    }
    
    public String fancyToString() {
        return "~~A~~";
    }
}

class B extends A {
    public String toString() {
        A letterA = this;
        return letterA.fancyToString();
    }
    public String fancyToString() {
        return "~~B~~";
    }
}

public class LetterPrinter {
    public static void main(final String args[]) {
        B letterB = new B();
        System.out.print(letterB.toString() + " ");
        
        A letterA = letterB;
        System.out.println(letterA.toString());
    }
}
```

#### s
* The output of the program is `~~B~~ ~~B~~`.
* With polymorphism, `letterB.toString()` will make `letterA` of `A letterA = this;` in `class B` to `class B`, which results in `letterA.fancyToString();` return `~~B~~`. Similarly, in the main function, when `A letterA = letterB`, it is morphed into `class B` rather than `class A`, resulting in `letterA.toString()` give the same output as the first print statement `~~B~~`.

### q
What is the output of this program? You should be able to do this without running the program!

```java
class A {
    public String toString() {
        return "A";
    }
    
    public String fancyToString() {
        return "~~A~~";
    }
}

class B extends A {
    public String fancyToString(){
        return "~~B~~";
    }
}

public class LetterPrinter {
    public static void main(final String args[]) {
        B letterB = new B();
        System.out.print(letterB.toString() + " ");
        
        A letterA = letterB;
        System.out.println(letterA.toString());
    }
}
```

#### s
* The output of this program is `A A`.
* Note that `class B` does not have a `toString()` method, which means calling `letterB.toString()` will result in the `toString()` method of `class A` since `class B extends A`. Similarly, although `A letterA = letterB` morphed `letterA` to `class B`, it still uses the `toString()` method of `class A`.


### q
What is the output of this program? You should do this without running the program.

```java
class A {
    public String toString() {
        return "A";
    }
}

class B extends A {
    public String toString() {
        return "B";
    }
}

public class PolymorphicOverload {
    public void foo(B letterB1, B letterB2) {
        // 2
        System.out.println("foo2: " + letterB1 + " " + letterB2);
    }

    public void foo(A letterA1, A letterA2) {
        // 1
        System.out.println("foo1: " + letterA1 + " " + letterA2);
    }
    public static void main(String args[]) {
        PolymorphicOverload f = new PolymorphicOverload();
        B letterB = new B();
        A letterA = (A) new B();
        f.foo(letterB, letterA);
    }
}
```

#### s
* The output of the program is `foo1: B B`.
* While `letterB` and `letterA` are both `class B`, the declaration makes `f.foo(letterB, letterA)` look for the best method to fit `f.foo(class B, class A)` due to the static declaration of `letterA` being `class A`. This means the method `public void foo(A letterA1, A letterA2)` is called in the main function because it is the best fitting method where both parameters passed in can be `class A` (remember `B` extends `A`). Therefore, the output is `foo1: B B`.


### q
Suppose you had the following class structures


```java
public class Species {
    String genus;
    String species;
    public Species(String g, String s) {
        genus = g;
        species = s;
    }
    
    public Species(Species s) {
        genus = s.genus;
        species = s.species;
    }
    
    public String toString() {
        return genus + " " + species;
    }
}

public class Breed extends Species {
    protected String breed;

    public Breed(String b, String g, String s) {
        super(g, s);
        breed = b;
    }

    public Breed(String b, Species s) {
        super(s);
        breed = b;
    }

    public String toString() {
        return super.toString() + "(" + breed + ")";
    }
}

public class Pet {
    String name;
    Species species;

    public Pet(String n, Species s) {
       name = n;
       species = s;
    }

    public String toString() {
        String ret = "Name: " + name + "\n";
        ret += "Species: " + species;
        retunr ret;
    }       
}
```


What is the output of the following snippet of code? If there is an ERROR, describe the error. **You should not need to run the code to determine the output**.

```java
    
   Species dog = new Species("Canis","Familaris");
   Breed shorthair = new Breed("shorthair", new Species("Felis","Catus"));
   Pet fluffy = new Pet("fluffy", new Breed("pomeranian", dog));
   Pet george = new Pet("george", dog);
   Pet brutus = new Pet("brutus", (Species) shorthair);
   
   System.out.println(fluffy);
   System.out.println(george);
   System.out.println(brutus);
```


#### s
```
Name: fluffy
Species: Canis Familaris(pomeranian)
Name: george
Species: Canis Familaris
Name: brutus
Species: Felis Catus(shorthair)
```


### q

Consider the following classes

```java
public class A {
    public int foo() {
        return 42;
    }

    public int bar() {
        return foo() + 8;
    }
}

public class B extends C {
    public int foo() {
        return 41;
    }

    public char baz() {
        return "y";
    }
}

public class C extends A {
    public char baz() {
        return "x";
    }
}

public class D extends A {
    public int bar() {
        return 7;
    }
}

public class E extends C {
    public int bar() {
        return foo() + 20;
    }
}

```

Consider a mystery function that returns a object of the given class.  **You do not know the definition of the mystery function, other than it compiles properly and returns an object of the class.** For each of the following method calls marked below, indicate the value of the output, if the output cannot be determined, or if there is an error.

```java

A a = mysteryA(); //<-- mystery function, this line compiles (the below may not!)
System.out.println(a.foo()); //<-- Mark A.1
System.out.println(a.bar()); //<-- Mark A.2
System.out.println(a.baz()); //<-- Mark A.3


B b = mysteryB(); //<-- mystery function, this line compiles (the below may not!)
System.out.println(b.foo()); //<-- Mark B.1
System.out.println(b.bar()); //<-- Mark B.2
System.out.println(b.baz()); //<-- Mark B.3

D d = mysteryD(); //<-- mystery function, this line compiles (the below may not!)
System.out.println(d.foo()); //<-- Mark D.1
System.out.println(d.bar()); //<-- Mark D.2
System.out.println(d.baz()); //<-- Mark D.3
```

#### s

```
A.1 : Compiles, Output not deterministic
A.2 : Compiles, Output not deterministic
A.3 : Doesn't Compile, No output

B.1 : Compiles, Output is 41
B.2 : Compiles, Output is 49
B.3 : Compiles, Output is y

D.1 : Compiles, Output is 42
D.2 : Compiles, Output is 7
D.3 : Doesn't Compile, No output
```

### q

What is the difference between a `class` and an `abstract class`? From a software engineering perspective, why would you ever want to use an abstract class instead of a regular class?

#### s

An `abstract class` can only be inherited by another class and can not be directly instantiated. A `class` can be instantiated in most contexts, and still inherited by other classes as well. `abstract class`es must also be implemented before code will compile.

You would prefer an abstract class when you want to enforce that the abstract class' constructor can/should never be called. 


### q

If you were to create an abstract class for a `Car` -- what features could be defined in the implemented class vs. what could be defined in the abstract class? Provide justifications for your design.

#### s

Features such as car brand, model, year, and other attributes that would be highly variable would be defined in the class implmentation. Other functions that would be mostly fixed and more deterministic across different class definitions, such as `toString` and functions that get or set values would be defined in the `abstact` class.

