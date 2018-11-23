![alt text](https://cdn-images-1.medium.com/max/1200/1*M22DR3WPqbWXWidYIq2GwA.png)

# Software Architecture </br>

## Overview

This repository contains my notes and thoughts from Anand  Pillai's Software Architecture with Python book.

## Table of Contents 


* [Chapter 1 - Principles of Software Architecture](#ch1)
* [Chapter 2 - Writting Modifiable and Readable Code](#ch2)
* [Chapter 3 - Testability - Writiing Testable Codes](#ch3)
* [Chapter 4 - ](#ch4)
* [Chapter 5 - Writting Software that scales](#ch5)

### Tools

* Pylint - Gives informations about code smells
* Flake8 - Gives informations about broken conventions and code smells
* Pyflake - basic checker for that reports obvious syntax and logics errors
* time - put in front of python3 file_name.py to get timing of your program

[Back to top ^](#)


### CHP 2 - Writting Modifiable and Readable Code:

*  **Tips on refactoring codes**

   - Fix the complex code first - Improves code quality and reduces code smells
   - Do an analysis check on the code -
   - Fix code smells next - function/class/module
   - Run checkers (pylint, Flake8, pyflake,etc...)
   - Fix low hanging fruits - code style and conventions
   - Perform final check using the tools above


## CHP 3 - Testability - Writiing Testable Codes

A software is testable if it gives up(exposes) its faults easily to the testers.

## CHP 4 -

## CHP 5 - Writting Software that scales

#### Scalability

 - Scale up : When a sytem scale by making better use of resource inside a compute node

#### Throughput
 The 


#### Latency

#### Concurency and Parallelism

Concurency referes to the amount of work that gets done simoultenously by a system, instead of sequentially.

* <i>Increating the concurency of a system often increases its scalability</i>

  - Multithreading: rewritting the applcation to perform parallel tasks in different threads.
   - Thread : A simple seqeunce of programming instruction that is performed by a CPU
   
  - Multiprocessing: Running the app in multiple processes instead of one. A program that performs multiple CPU-Intensive computations would benefit more from Multiprocessing.
  - Example : A financial institution processing multiple transactions at the same time.
  
  - Asynchronous Processing : Operrations are performed asynchronously with no specific order of tasks with respect of time.
   * -- Async process works by grabbing a task from the task queue, schedule it to perfom in the future, and expect a callback
    - Example : Node.js' 
