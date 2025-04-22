---
layout: default
permalink: /lab/12_git_branching
---

# Lab 12: Git branching and merging

**As an exception for this lab only**, this lab assignment is groupwork. However, the logfile you turn in must be of your own git repo.

## Setup

Use git, as discussed in Lab 0, to create a repo called `gitusername-lab12`. 

Create the following four new files, with filenames exactly as shown, in this repo after you have cloned it to your computer:

* `README` 
* `test.rb` 
* `LICENSE`
* `index.html`

Add some contents to these files -- this can be anything.

### Meet your team

In the rows in the classroom, find 2-5 other students to work with: this will be your team for this lab. In the last part of the assignment, we're going to practice working on a shared piece of code and how that translates into using `git` collaboratively.

## Using official documentation and tutorials

Git is an industry-standard version control tool that is most useful when working with groups of developers. In this lab, we're going to walk through a tutorial from git itself to understand how branching and merging work.

While these same topics are covered in numerous videos and websites, it's hard to know, especially if you are totally new to what you're doing, what's a high-quality video/resource versus one that is misleading, incorrect, or inefficient. Videos in particular can be a huge time sink and/or waste of time because it's difficult to skim them and/or see a summary.

### Creating and using branches in git

**Branches** are used in version control systems like git to help developers organize and limit changes they are making to a (shared) codebase when fixing a bug or making other small, incremental updates. They are a way for these folks to isolate the updates they are working on to a specific *branch* of the repo, that is, a branch that they create specifically for this purpose. Once they fix their bug, for example, the goal is then to merge this branch back to the main branch of the repository so that other developers can see those updates with `git pull`.

Next, read and complete the tutorial at the following link: [https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

Note: github has [changed the name](https://github.com/github/renaming) of the default branch from `master` to `main`. When you come to this step in the tutorial instructions, **remember to replace `master` with `main`**. (github is just a hosting service for git; github is not the same thing as git)

### Merging branches in git

Now that you understand why and how to creates branches in git, we can learn about how to merge them. For example, when you've made a bug fix on some part of your code, reran the test suite to make sure the bug is fixed (and no other tests are broken), you'll want to **merge** your changes back with the main git repository so that other people can see these changes.

One issue that might pop up is what happens when two people are updating the same part of their code in their respective branches? Well, first, this is fine and kind of the point of everyone using branches anyway! But sometimes developers will end up with conflicts between different branches for the same piece of code that they might have both updated. *Merging* branches in git allows us to identify and resolve these conflicts.

Next, read and complete the tutorial at the following link: [https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

### Working in a group with git

Now that you know to do branches and merges in git, you're ready to try this out with your group!

First, have one group member create a new repo called `lab12_group` and add all your team members to this repo using github's web interface. You can find a menu to search for people to add to your repo under the settings menu within your repository. Once you've created the repo and added your team, have everyone check out the repo -- you will all have a local copy of the empty main branch.

Next, have a different team member create a file called `HelloWorld.java` that prints out Hello World! to the terminal, and add that to their repo, commit, and push. The rest of the team should do a `git pull` to then get a local copy of that file. Then, each team member should create a branch of the repo with the name of their choosing.

Now, each team member should: 1) add a new, additional line to that file and 2) change the message from Hello World! to say something else that includes their first name. 

Once you have all edited the file, try to merge the branch and resolve the conflicts until a satisfactory version of the file is committed to the main branch and all teammates are able to pull that same file from the repo.

# Grading rubric and submission

Type the following command to generate a logfile in your repo, which you will submit to BB:
`git log --decorate --graph --all >logfile.txt`


|Item | Points |
|Your logfile shows all the commands in the two tutorials above working and completed in order | 100 |


