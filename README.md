# Boolean Interpreter

## Description

This is an interpreter that evaluates boolean expressions. 

To use the interpreter:

    -Clone or Download the project 
    
    -On your machine, navigate to the project directory and open terminal
    
    -Run `python home.py` command

Installation of python3 is a prerequisite to running the application.   

## Syntax specifications.

`T v T ` --> Read and Interpreted as True or True

`T ^ T` --> Read and Interpreted as True and True

`F v F ` --> Read and Interpreted as False or False

`T v T ^ F` -->  True **or** True **and** False

`(T v F ) = F` --> True **or** False **Equals** False

`F = T` --> False **Equals** True 

This interpreter is case sensitive, `f v f` as input will result to an error

Input expression can only start with either ` T , F , or (`,  you cannot have `v`,`)` or  `v` starting in an input expression.

Two operators cannot follow each other concurrently, eg. `F v ^ F` would result to an error.
    

## Features not implemented

 1. Interpreter doesn't handle variables input, any variable input would result to an error.

 2. -- not-- operator has not implemented since variables handling was not implemented.  


## Credits
Credits to [Ruslan's blog, Let's build a simple interpreter](https://ruslanspivak.com/lsbasi-part1/)
that helped to guide and understand interpreter and concepts. 
