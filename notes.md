# Research
* Python shell vs zsh shell
* look into the 4.12 exercises and try learning the math

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

**Chapter 6:** 
* fruitful functions are functions with a return value. some void functions have return values. the difference is that in a fruitful function the return statement includes an expression.
* in a fruitful function, it is a good idea to ensure that every possible path through the program hits a return statement!!
* must use a print statement in order for fruitful functions to show in console when invoked. 
* without the print statement, could you then pass the return value of a function as an argument for another function?

#### Key Aspects of Incremental Programming <br>
1) Start with a working program and make small incremental changes. At any point, if there is an error, you should have a good idea where it is.
2) Use variables to hold intermediate values so you can display and check them.
3) Once the program is working, you might want to remove some of the scaffolding or consolidate multiple statements into compound expressions, but only if it does not make the program difficult to read.