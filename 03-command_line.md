# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd : shows current working directory path  
> > mkdir : creates a new directory  
> > rm -r : deletes a directory and all contained files  
> > touch : create a file
> > rm : delete a file
> > ls -a : list all files including hidden ones  
> > mv [file1] [file2]: move file1 to file2

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls : lists files  
> > ls -a : lists all files, including hidden ones
> > ls -l : long list format
> > ls -lh : lists file size in a more readable format  
> > ls -lah : lists all files, including hidden ones, with sizes in a readable format  
> > ls -t : lists files sorted by last modified  
> > ls -glp : displays list in long format, excluding owner names. Shows a backslash after directories  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > -C : Displays files in a columnar format (default)  
> > -r : Displays files in reverse order.  
> > -R : Displays subdirectories as well.  
> > -t : Displays newest files first. (based on timestamp)  
> > -u : Displays files by the file access time.  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs allows you to construct and execute command lines using standard input.  
> > Example: find -name "*.txt" | xargs grep "abc"

 

