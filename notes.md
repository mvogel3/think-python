# Research
* Python shell vs zsh shell
* virtual environments and anaconda 
* operating systems
* how to go from learning Python to actually buildinf something
* look into the 4.12 exercises and try learning the math
* revisit base cases
* overflow in programming (applies to languages other than python)

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