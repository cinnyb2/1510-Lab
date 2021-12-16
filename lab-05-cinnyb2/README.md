# 1510-Lab-05

Every program needs a README.md

This is written in markdown. Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Your name:
Cindy Liu

## Your student number:
A1270988

## Your GitHub account:
https://github.com/cinnyb2

## Any important comments you'd like to make about your work:

## *** Step 2 ***
Step Into will go into a method and show exactly what is being executed line by line.
Step Over will go over the current line of code and take you to the next line, if the line contains a method, the method
will be executed with the results being returned without showing the line by line implementation of the method being 
called. Step Into will offer more details about exactly what your code is outputting at each line, which is useful to
find exactly which line within a method is causing errors. Step Over can provide a general overview of what your code is
doing, and allow you to quickly move through many lines of code and narrow down which method is giving an incorrect
output or an error.

## *** Step 4 ***
In step_04.py there is a long list of functions in the stack of function calls for fibonacci() because we are 
recursively calling fibonacci() the number of times specified in the main(), which is 30 in this case. 
A recursive function is a function that calls on itself. The structure of a recursive function can be broken down into 
two parts, the base case/s, which is the most atomic problem (n_term==0 and n_term==1), and the recursive step 
(fibonacci(n_term-1) + fibonacci(n_term-2)). Each call to this function will result in it calling itself
two more times in the recursive step, this doubling is increased exponentially as the number grows. The Fibonacci()
stack grows and shrinks repeatedly over the course of the execution because it grows to the maximum depth and then 
shrinks back to the answer. The base case allows the recursive step to transform into something smaller or else the 
recursive step will loop infinitely, which is why it is important for the function to grow and shrink.
The reason recursive fibonacci() takes so long to execute is because of its exponential growth, where it traverses 
through previous calls of itself (node), which it has already computed and thus waste exponential amount of time 
performing each repeated call. Recursive functions are elegant and easy to debug due to their short length, but they 
take a long time to execute due to their high time complexity.

