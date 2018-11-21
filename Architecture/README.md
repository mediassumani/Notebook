![alt text](https://cdn-images-1.medium.com/max/1200/1*M22DR3WPqbWXWidYIq2GwA.png)

## Software Architecture </br>

### Overview

This repository contains my notes and thoughts from Anand  Pillai's Software Architecture with Python book.

### Outline 

#### Chapter 1 - Principles of Software Architecture

#### Chapter 2 - Writting Modifiable and Readable Code

#### Chapter 3 - Testability - Writiing Testable Codes

#### Chapter 4 -

#### Chapter 5 - Writting Software that scales




# Tools

* Pylint - Gives informations about code smells
* Flake8 - Gives informations about broken conventions and code smells
* Pyflake - basic checker for that reports obvious syntax and logics errors



## CHP 2 - Writting Modifiable and Readable Code:

### Tips on refactoring codes

* Fix the complex code first - Improves code quality and reduces code smells
* Do an analysis check on the code -
* Fix code smells next - function/class/module
* Run checkers (pylint, Flake8, pyflake,etc...)
* Fix low hanging fruits - code style and conventions
* Perform final check using the tools above


## CHP 3 - Testability - Writiing Testable Codes

A software is testable if it gives up(exposes) its faults easily to the testers.

## CHP 4 -

## CHP 5 - Writting Software that scales

#### Scalability

 - Scale up : When a sytem scale by making better use of resource inside a compute node

#### Throughput


#### Latency


#### Concurency

Concurency referes to the amount of work that gets done simoultenously by a system, instead of sequentially.

* <i>Increating the concurency of a system often increases its scalability</i>

  - Multithreading: rewritting the applcation to perf
     - 
  - Multiprocessing: Running the app in multiple processes instead of one. A program that performs multiple CPU-Intensive computations would benefit more from Multiprocessing.
