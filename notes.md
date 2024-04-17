# Research
* Python shell vs zsh shell
* virtual environments and anaconda 
* operating systems
* how to go from learning Python to actually buildinf something
* look into the 4.12 exercises and try learning the math
* revisit base cases
* overflow in programming (applies to languages other than python)
* recursion depth limits: [why they're there, how to change them, when to change them, how to avoid them, and also the math/computer science behind them]

# Chapter Summaries/Take Aways/Notes

**Chapter 3:** explains the purpose of functions and how arguments are passed through them. answered my questions surrounding the purpose of parameters and how they can have different names in different places. touches on encapsulation e.g., a variable declared inside of a function does not exist outside of it. good practice problems.
* empty parenthesis after a function name indicate that it does not take any arguments.
* the name of the variable we pas as an argument (lucy) has nothing to do with the name of the parameter (meg). it does not matter what the value is called back home (in the caller); here in print_twice, we call everybody meg.
* '_ _main_ _' is a special name for the topmost frame. when you create a variable outside of any function, it belongs to 'underscore underscore main underscore underscore'.
* each parameter refers to the same value in as its corresponding argument. so part1 has the same value as line1, part2 has the same value as line2, and 'meg' has the same value as 'cat'.

**Chapter 4:** introduces loops and methods. also gives a mathematical but clear example of how functions work together and build on each other. expands the notion of parameters and arguments in functions. getting the turtle library up and running refreshed my memory for using virtual environments and stack overflow.

**Chapter 5:** deals with conditionals and their terminology. adds conditionals to functions and introduces user input. goes deeper into some mathematical examples. reminiscent of some of the ML algorithms. 
* each condition is checked in order. if more than one condition is true, only the first branch runs.
* avoid nested conditionals when possible for the sake of readability.
* recursion errors
* page 44: _ _main_ _ like the main branches in git?<br>
after working through stack diagram 10.5 in Chapter 10:<br>
_ _main_ _ is the first layer of a function. its empty in the stack diagram of countdown because there are no variables in the file (outside of the function) that get passed through it. "n" is created when the function is called so it shows up in the second layer of the diagram.

**Chapter 6:** functions thus far in the book have resulted in print statements and not returns. this chapter deals with fruitful functions or functions that yield return values. if you want to see what a fruitful function returns, you have to call it using a print statement otherwise there will be no output in the terminal. i'm guessing that this is the reason why the author chooses to introduce incremental development. incremental development involves testing a small amount of code at a time which cuts down on debugging and also ensures that you know if a fruitful function works should you call it later in your program.
* fruitful functions are functions with a return value. some void functions have return values. the difference is that in a fruitful function the return statement includes an expression.
* in a fruitful function, it is a good idea to ensure that every possible path through the program hits a return statement!!
* must use a print statement in order for fruitful functions to show in console when invoked. 
* without the print statement, could you then pass the return value of a function as an argument for another function?
* if you can write a recursive definition of something, you can write a python program to evaluate it. 

#### Key Aspects of Incremental Programming <br>
1) Start with a working program and make small incremental changes. At any point, if there is an error, you should have a good idea where it is.
2) Use variables to hold intermediate values so you can display and check them.
3) Once the program is working, you might want to remove some of the scaffolding or consolidate multiple statements into compound expressions, but only if it does not make the program difficult to read.

**Chapter 7:** shorter chapter that largely deals with algorithms using while loops. math heavy and somewhat difficult to understand. 
* recursion is a kind of iteration
* assignment and equality are not the same in programming. python scripts are interpreted as linear.
* the body of a while loop should should change the value of one or more variables so that the condition becomes false eventually and the loop terminates.
* loops beginning with "while True:" are always true so you have to tell it to break. always true bc the loop is the condition (page 66)
* debugging by bisection: find places in the program where there might be errors and place print statements (or something else that has a verifiable effect) in them before running the program again. if it is incorrect, then the problem is below it.

(starting again with chapter 8 after a month hiatus)<br>

**Chapter 8:** deals with indexes, sting comparisons, and for loops. 
* for obvious reasons, the index value has to be an integer.
* line 7 in strings.py --> the reason last = fruit[length-1] is because length equals 6 and the index of fruit is 0 to 5
* the operator [n:m] for string slices includes the n but excludes m.
* strings are immutable so the best you can do is create a new string that is a variation of the original.
* count not figure out the three parameter function in 8.7. what is the difference btwn using a string traversal vs the index?
* the debugging section in this chapter may be useful later on

[string methods in python](https://docs.python.org/3/library/stdtypes.html#string-methods)

*8.4*
1. the first function is designed to test if any letter in the word is lowercase but it ends if the first letter is not lowecase. so if the first letter is uppercase it returns False. the function runs as intended if the else: statement is removed.
2. the second function runs as intended but the making the iterator a string before calling the method confuses me.
3. function returns nothing as is even with a print statement. needs a conditional 


(starting again with chapter 9 after a month hiatus)<br>

**Chapter 9:** case study involving solving word puzzles using word properties. I was able to find the txt file from another repo. the file is not a csv which makes it easier to read in i'm guessing.<br>

for some reason I could not print the results of two functions both acting on fin. they both can exist in the file without error but i can't print the two lists at the same time. I'm assuming this is because the functions are changing the variable and so two changes can't happen at once but i've never come across this before. does fin need to be named a global variable?

stackoverflow advised against using global variables so I opened words.txt as a local variable in each function and that seemed to fix the problem. 

this chapter allowed me to realize that although I'm able to solve a few coding problems at this point, it takes me a very long time to come up with the solution and that solution is often lengthy and doesn't adhere to best practices. after completing this textbook, I'll need to practice more leetcode/interview style problems. 

*9.7*
1. wrote a function that returned true for any three sets of double letters. (three_doubles_works)
2. tried to edit that function to recognized consecutives. that didn't work so I moved on to a recursion function. 
3. recognized that 3 consecutive doubles is 3 index pairs and we're looking for one set of 6 letters.recursion function works on its own(doubles_recursion).
4. created a new function that takes words.txt as the object for doubles_recursion. this runs with an index error. 
5. called three_doubles_works and appended the True values to a new list. ran that list through doubles_recursion and it worked! however, I'm guessing this isn't the most optimal solution so I'll keep working on the string index out of range error from before.
6. tested 'forget' on doubles_recursion and got the same index error (special case).
7. used print statements for debugging. appened the "wrong" words to a list, printed the length of that list, and then used the len number as an index on the word list. the 164th word in word_list is 'abjectness' which has a double letter at the end. another special case. 
8. amended the first conditional in doubles_recursion so that if the word ever gets to be less than 6 characters, the return is false. IT WORKS!

*9.9*
I needed to look at a solution for the age palendrome function. I plan to go back and see if I can understand it and go about the problem a different (albeit less optimal) way.

**Chapter 10:** This chapter deals with lists.
after skimming the glossary section, I realized that this chapter teaches many of the techniques I was using 

### <u>Notes</u>
* the elements of a list do not have to be the same type
* lists are mutable. 
* the syntax for accessing list elements is the same as strings. uses []. <br>
any integer expression can be used as an index. <br>
if you try to read or write an element that does not exist, you will get an index error. <br>
if an index error has a negative value, it counts backwards from the end of the list. <br>
* the most common way to traverse a list is a for loop. but if you want to write or update a list, you need to use indices. usually done by combining len and range.
* the nested list counts as a single element (i.e. the list inside of a list counts as 1)
* if you omit the first index in slicing, the slice starts at the beginning. if you omit the second index, the slicee goes to the end. if you omit both, the slice is a copy of the whole list. 
* a slice operator on the left side of an assignment can update multiple elements.
* total += x is the same as total = total + x
* most list operations are some combination of map, filter, and reduce.
* a list of characters does not a string make
* calling a built-in method requires dot notation. why?<br>

(ins tag needed in order for underline to show on github)

(as an aside, I wanted to make a word doc for my notes as I was reading this chapter but I realized that since markdown files recognize html, I'd have more flexibility with this file and I'd learn more about HTML as well.)

### <ins>10.10 - Objects</ins> 
a = 'banana'
b = 'banana'

a and b are two different OBJECTS but those objects have the same value.

an object has a value. an object is not a value.

<mark>if two objects are identical, they are also equivalent. but if they are equivalent, they are NOT necessarily identical.</mark>

### <ins>10.11 - Aliasing</ins> 
* the association of an object with a variable is called a <b>reference</b>.
* an object with more than one reference has more than one name, so we say that object is <b>aliased</b>.
* if the aliased object is mutable(e.g. a string), changes made with one alias affect the other. but this is prone to error so its best not to alias with mutable objects.
* "even with  mutable objects, it almost never makes a difference whether a and b refer to the same string or not." why? what is the use case for aliasing? like .copy() in pandas?

### <ins>10.12 - List Arguments</ins> 
* When you pass a list to a function, the function gets a reference to the list. If the function modifies the list, the caller sees the change. 
* an example of aliasing is in _delete_head(t)_. both _t_ and _letters_ refer to the same object. 
* .append() modifies a list
* the + operator (to join two lists) creates a new list. 
* the _bad_delete_head(t)_ function shows how t and letters have the same object at the beginning but by the end, t is a new list and letters remains unchanged.

### <ins>Tips For Working With Lists</ins> 
1. Read the documentation carefully and test list methods in interactive more. <br>
(most list methods modify the argument and return None. which is the opposite of string methods.)
e.g. t = t.sort() will return None so working with t in a following operation is likely to result in an error or nothing.
2. Pick an idiom and stick with it.<br>
e.g. del or pop or + 
3. Make copies to avoid aliasing.<br>
e.g. t = [3, 2, 1]<br>
t2 = t[:] 

*Exercise 10.1* <br>
I had this idea that if I could compare the index numbers of the nests to the index numbers of the entire list and extend the list if the numbers matched. 
Then I realized that I had wasted hours because the whole function could be solved with one for loop. the answer is in _nested_sum_2_.

*Exercise 10.8* <br>
learned a new git command: git reset (used to unadd a file if git commit has not been run)

*Exercise 10.10* <br>
look into using if name = main and what the significance of that is. 

* learned floor division for this function. // drops the decimal instead of using the round function. 
* watched a video on binary search algorithms. the author brought up the possibility of overflow in languages other than python. said that mid could be written as _mid = lo + (hi-lo)//2_ to avoid this problem. <br>
[Here is the video](https://www.youtube.com/watch?v=tgVSkMA8joQ/ "Binary Search - A Different Perspective | Python Algorithms")
* using the algorithm from the above video, hi is always going to equal lo at the end. 
* since lo = hi, either is the index of the word being passed through or it is the index of the next word in alphabetical order (if the word isn't in the list). therefore, if the argument does not equal the word at that index, the function returns None.

*Exercise 10.11* <br>
* extend creates one cohesive list, appending a list to a list creates a nested list which made more sense for a function that returns pairs.
* this for look took forever to run. could possibly use bisection again but I'm not sure. 
* is using variables always the way to go for loops? the function works whether I assign half the list to a variable or not but I'm not sure what the best practice is.

(decided to skip exercise 12. could not figure it out)

returning to this textbook after about a month.

**Chapter 11:** this chapter deals with dictionaries. I've worked with dictionaries before in data analysis but lists were far more common. this chapter allowed me to understand the many other uses of dictionaries and encouraged me to get creative with them which I enjoyed. it also touched on hashabile data types as well as global variables. <br>
(as an aside, I do love how each chapter in this book has exercises that require or would be improved with topics not yet touched on. its comforting that said topics will be explained later in the book with more context.)

### <u>Notes</u>
* the author explains dictionaries as lists with less specific indicies. e.g. the indices of a list need to be integers but in a dictionary, they can be almost any data type. 
* the indices of a dictionary are called keys.
* each key "maps" to a value. 
* the order of a dictionary is unpredictable but this is not an issue bc we make the keys. (could use sorted in certain occasions)
* the len function returns the number of key-value pairs.
* the in operator tells you whether something appears as a KEY in a dictionary (will not work for a value). 
* using a for statement on a dictionary only traverses the keys.
* dictionaries can have more than one key that maps to a value. (i.e. not all keys are unique)

### <ins>11.4 - Reverse Lookup</ins> 
Two problems with finding a key from a value:<br> 
1. there might be more than one key that maps to the value. depending on the application, you might be able to pick one, or you have to make a list that contains all of them.
2. there is no simple syntax to do a reverse look up; you have to search.

reverse lookups are much slower than straightforward lookups. if you have to use them often, or the dictionary gets too big, the performance of the program will suffer.

### <ins>11.5 - Dictionaries and Lists</ins> 
* lists can be values in a dictionary but they canNOT be keys. dictionaries can also be values in a dictionary but NOT keys.
* lists are not hashable because they are mutable.
* tuples can be keys because they are immutable.

### <ins>11.6 - Memos</ins>
a memo is a previously computed value stored for later use. <br>
in this case, known is a dictionary that tracks the fibonacci numbers we already know. <br>
if the argument is not in known, the function will calculate the fibonacci number for n and all the previous integers.

### <ins>11.7 - Global Variables</ins>
* to reassign a global variable inside a function, you have to declare the global variable before you use it. (this is called a global statement)
* if a global variable refers to a mutable value, you can modify the value without declaring the variable.<br>
e.g.<br>
known = {0:0, 1:1}<br>
def example(): <br>
known[2] = 1
* you can add, remove, and replace elemements of a global list or dictionary, but if you want to reassign a variable, you have to declare it.<br>
e.g.<br>
def example2():<br>
global known<br>
known = dict()

global variables can be useful, but if you have a lot of them, and you modify them frequently, they can make programs hard to debug.

*Exercise 11.1* <br>
cannot raise a KeyError with a custom message without using try & except

*Exercise 11.2* <br>
I am so proud of myself for this one!!! using stackoverflow, I learned that I would need to append all the keys/new values to an empty list otherwise the function would return a TypeError. This can be written in one line of code instead of 5 which makes the function more concise. it also controls for times when there are repeat values in the dictionary to be inverted.
[StackOverflow Link](https://stackoverflow.com/questions/34815461/append-to-list-in-a-dictionary-after-setdefault "Append to list in a dictionary after setdefault [duplicate]")

<!-- i just learned you can comment on markdown! -->

you can comment on markdown using the same keyboard command for python files.

*Exercise 11.3* <br>
I realized that in order to "memoize" a function with two arguments and one output, I'd need to make a nested dictionary. I used the m values as the first keys and then the n values as a value/secondary key with the return value as the secondary value. using w3 schools I learned how to traverse nested dictionaries using square brackets and that allowed me to access the return value I needed.<br>
as I tested this function with larger numbers, I get a RecursionError if m is greater than 3 and n is greater than 6. using stack overflow, I found that these errors occur when the functioin hits a recursion depth limit. using the built-in python library "sys", i was able to check that my current limit is set to 1000. 
[RecursionError Link (StackOverflow)](https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-and-how-to-increase-it "What is the maximum recursion depth, and how to increase it?") <br>
the same stack overflow page also discussed using memos to decrease the recursion stack size. not fully sure what that means or how it would work but it felt relevant. <br>

why do dictionaries not have to be declared global in functions?<br>
Answer: because dictionaries are mutable<br>

was getting a KeyError when passing arguments not in memo_ack. i realized that I need to account for the cases when m exists as a key and n does not. this was done using an "and" statement as well as using the .keys() built-method. Geeks for geeks also had a good page for this. 
[StackOverflow Link for iterating over nested dictionaries](https://stackoverflow.com/questions/64980051/python-accessing-specific-items-from-a-nested-dictionary?rq=3 "Python - Accessing specific items from a nested dictionary")

*Exercise 11.5* <br>
* findng all the rotate pairs i'm assuming is referring to all the words that can be rotated any which way (-10, 1, 13, etc.) for simplicity, i'm starting with ROT13. the function will start as a list comparison where I run the words.txt file against itself and make key-value pairs of the original and rotated words. i started with part of the txt file and then tried the whole file which took forever to run so I think im going to try adding a bisect search to this exercise. if I use a bisect search and also randomize the integers I'm rotating by, I should be able to make a mini program. 
* tried to using the bisect search and the regular list search both resulted in 94 key-value pairs so to my knowledge it works!
* adding random integers to rotate by and then memoizing with a nested dictionary. 
* (confused by the concept of seeding a psuedo random number generater.)
* using a random integer generator for 0-10 (will expand later). the function is currently working so now I'm going to add a dictionary outside the program to memoize and record the outputs each time the function is run. (is it possible to run the program using all the possible integers instead of using a random generator and running it multiple times?)
* using range(1-10) in a nested for loop means that each is being rotated a different way. but even then the program isn't working correctly because "aa" rotated 0 times is "aa" and that doesn't show up in the return dictionary. I'm going to go back to using random numbers and try to figure out ranges later.
* using the random integer did work even when the integer was 0
* it does's make sense to memoize this function since it takes no arguments. i think im going to leave it for now until I have a better idea.

* finally got it to work!!! (3/25)

*Exercise 11.6* <br>
[CMU Pronounciation Dictionary Link](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
* downloaded the CMU pronunciation dictionary from github. adding it to my git ignore bc my github can't handle a file that large. 
* pip installed pronouncing library but disovered it only works for python 2 and I'm not sure how to make a separate environment for that nor do i think it is worth it 
* leaving 11.6 alone for now.

**Chapter 12:** deals with the last built-in Python type: tuples. explains how all the built-in types work together. 

### <u>Notes</u>
* the values in a tupe can be any type and they are indexed by integers (like lists)
* Tuples Are Immutable
* the syntax for a tuple is a comma-separated list of values. (it is common practice to enclose the values in parentheses)
* most list operators work on tuples. E.g. brackets, slice, etc. 
* you cannot modify the elements of a tuple, but you can replace one tuple with another.
* how relational operators work with tuples: Python starts by comparing the first element from each sequence. If they are equal, it goes on to the next elements, until it finds elements that differ. subsequent elements are not considered (even if they are really big).

### <ins>12.2 - Tuple Assignment</ins>
a, b = b, a

### <ins>12.4 - Variable-Length Argument Tuples</ins>
* a parameter name that begins with "*" gathers arguments into a tuple. 
* the same is true for scatter. parameters that begin with * will be passed through as multiple arguments. 

### <ins>12.5 - Lists and Tuples</ins>
* Iterators are similar to lists in some ways, but unlike lists, you cant an index to select an element from an iterator. 
* the result from the built-in function enumerate is an 'enumerate object' which iterates a sequence of pairs; each pair contains an index (starting from 0) and an element from the given sequence. (page 119)

### <ins>12.6 - Dictionaries and Tuples</ins>
* Dictionaries have a built-in method called "items" that returns a sequence of tuples where each tuple is a key-value pair. <br>
The result is a "dict_items" object which is an iterator that iterates the key-value pairs.
* can make a dictionary by zipping a string and a range of numbers.
* the dictionary method "update" adds a list of tuples as key-value pairs to an exisiting dictionary.

### <ins>12.7 - Sequences of Sequences</ins>
#### Reasons to Use Tuples Over Lists <br>
1. In some contexts, like a return statement, it is syntactically simpler to create a tuple than a list.
2. If you want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or string.
3. If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.

### <u>Notes</u>
* Still lost on methods vs functions. <br>
E.g. tuples don't have the methods "sort" and "reverse". instead they have _the functions_ "sorted" and "reversed".
* interesting to note that for 12.8 (Debugging), I found the file online and copied the code to my computer in a new file. <br>
In order to import and use it as a module, I had to run the structshape.py file on my machine before referencing it in tuples.py

*Exercise 12.1* <br>
