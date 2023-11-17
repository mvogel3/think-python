# Research
* Python shell vs zsh shell
* look into the 4.12 exercises and try learning the math
* revisit base cases

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
* _ _main_ _ like the main branches in git?

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