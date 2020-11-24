# Less than/More than

Now that you know how to use logic you can really say that you can program in Python.  To summarise you can now do all of the three elements of computer programming:

1. You can use __variables__ to store data.
2. You can use __functions__ to change the data stored in __variables__.
3. You can use __logic__ and the data stored in __variables__ to choose what __functions__ to execute.

As we have pointed out multiple times that is pretty much all there is to computer programming.  The rest of the syntax you will learn will just make the programs you write shorter, which is a good thing as shorter programs contain fewer mistakes.

At this happy juncture, we will, in the next few tasks, extend your understanding of logic.  In this first task, we are going to consider what sort of logical propositions we can use.  

In the last exercise, the proposition we used was in this statement:

````
if data[i]==5 : filter[i] = 1
````

This command tells Python to set the ith element of the numpy array called `filter` equal to 1 if and only if the ith element of the numpy array called `data` is equal to 5.  Notice that the equals symbol is used in two distinct ways in this code.  The first time we use `==`, which is used to indicate that the proposition `data[i]==5` has a truth value of 1 if `data[i]` and 5 are equal and 0 if `data[i]` and 5 are not equal.  This command is distinct from the `=` in the statement `filter[i]=1`, which simply tells python to set the ith element of filter equal to 1. 

When we write an `=` sign in a mathematical derivation it is more like the `==` sign in Python than the `=` sign.  In a lot of the derivations that you will have encountered the fact that the truth value of a proposition such as ![](https://render.githubusercontent.com/render/math?math=x=1) is 1 is implicit.  When we write an equation such as ![](https://render.githubusercontent.com/render/math?math=P(X=1)),  however, it is understood that the proposition ![](https://render.githubusercontent.com/render/math?math=X=1) can have a truth value of 0 or 1.  In other words, in this proposition ![](https://render.githubusercontent.com/render/math?math=X=1) is itself a variable that can take two different values.

Some other examples of propositions that we can use in statements such as ![](https://render.githubusercontent.com/render/math?math=P(X=1)) are:

![](https://render.githubusercontent.com/render/math?math=P(X<1)\quad\P(X>1)\quad\P(X\le\1)\quad\P(X\ge\1))

i.e. less than, more than, less than or equal to and greater than or equal to.  It should come as no surprise to learn that we can all of these logical operations in the logical propositions that we might write in Python as shown below:

````
# Set b equal to 1 if a is less than 1
if a < 1 : b = 1
# Set b equal to 1 if a is greater than 2
if a > 2 : b = 1
# Set b equal to 1 if a is less than or equal to 3
if a <= 3 : b = 1
# Set b equal to 1 if a is greater than or equal to 4
if a >= 4 : b = 1
````

Your task is to use these logical operators to write a series of functions.  All of these functions will take in two arguments:

1. `data` - a numpy array containing a list of numbers
2. `n` - a single integer  

The four functions should then do the following:

1. `numberLessThan` -  should return the number of elements of `data` that are less than `n`
2. `numberMoreThan` - should return the number of elements of `data` that are greater than `n`
3. `numberLessThanOrEqualTo `- should return the number of elements of `data` that are less than or equal to `n`
4. `numberGreaterThanOrEqualTo` - should return the number of elements of `data` that are greater than or equal to `n`

The code at the bottom of the example should help you to see whether or not your functions are working correctly.

