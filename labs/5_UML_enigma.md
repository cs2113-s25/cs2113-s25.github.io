---
layout: toc
permalink: lab/5_UML_enigma
---


# Lab 5: Creating a UML diagram for the Enigma lab

In this short lab, you will design your code for the upcoming Enigma lab using a UML diagram.

## Setup

Open the instructions for the [Engima lab](lab/6_enigma) in another tab and read over them, taking note of:

* The three classes you need to write and/or work with
* The contents of each (skeleton) class

## Drawing a UML diagram

Using the notes from class, draw a UML diagram for all the three classes associated with the Engima lab **using markdown**, described here. You'll be graded using the rubric below.

### Sketching a UML diagram by hand

First, draw a UML diagram by hand, and save it as UML.pdf

### Using Markdown to create UML

Take a look at this simple UML diagram:

 <pre class="mermaid">
classDiagram
    class Fish {
        - int age
        # String planet = "Earth"
        + Fish(int age)
        + String toString()
    }

    class Shark {
        - String food
        + Shark()
        + boolean eats()
    }

    Fish <|-- Shark
</pre>

    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    </script>

You can use the markdown code below to generate the UML diagram above. Modify this markdown code to generate a UML diagram for the Enigma lab.

```
classDiagram
    class Fish {
        - int age
        # String planet = "Earth"
        + Fish(int age)
        + String toString()
    }

    class Shark {
        - String food
        + Shark()
        + boolean eats()
    }

    Fish <|-- Shark

```

# Grading rubric and submission

Upload a PDF called lab5.pdf to BB to get graded.

You will be graded on the following:

|Item | Points |
|three classes are in the diagram as large rectangles | 2 |
|all methods, including constructors, appear in the diagram, with proper visibility, arguments, and return types | 72 (8 pts each) |
|all fields appear in the diagram, with proper visibility types | 16 (4 pts each) |
|correct relationship between classes drawn (including arrow direction) | 10 (5 pts each) |
|any extra fields, methods, or relationships | minus 5 pts each |
|TOTAL | 100 |

