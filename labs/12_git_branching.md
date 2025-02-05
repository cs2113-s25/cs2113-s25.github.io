---
layout: default
permalink: /lab/12_git_branching
---

# Lab 12: Git branching and merging

## Setup

Use git, as discussed in Lab 0, to create a repo called `gitusername-lab12`, add the file above to it, and commit and push the changes to github. 

Create the following three new files, with filenames exactly as shown, in this repo after you have cloned it to your computer:

* `README` 
* `test.rb` 
* `LICENSE`
* `index.html`

Add some contents to these files -- this can be anything.

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


# Grading rubric and submission

Type the following command to generate a logfile in your repo, which you will submit to BB:
`git log --decorate --graph --all`


|Item | Points |
|Your logfile shows all the commands in the two tutorials above working and completed in order | 100 |


