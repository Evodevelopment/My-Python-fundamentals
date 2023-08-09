The if…elif…else statement used in Python helps automate that decision making process.

if condition
The if condition is considered the simplest of the three and makes a decision based on whether the condition is true or not. If the condition is true, it prints out the indented expression. If the condition is false, it skips printing the indented expression.

if condition
Example of if
Suppose you have a variable z, equal to 4. If the value is 'even', you will print z is 'even'. You will use modulo operator 2, which will return 0 if z is 'even'. As soon as you run the below code, Python will check if the condition holds. If True, the corresponding code will be executed.

example of if
Example of multiple lines inside if statement
It is perfectly fine to have more lines inside the if statement, as shown in the below example. The script will return two lines when you run it. If the condition is not passed, the expression is not executed.

example of multiple lines inside if
Example of a False if statement
Let's change the value of z to be odd. You will notice that the code will not print anything since the condition will not be passed, i.e., False.

example of a false if condition
if-else condition
The if-else condition adds an additional step in the decision-making process compared to the simple if statement. The beginning of an if-else statement operates similar to a simple if statement; however, if the condition is false, instead of printing nothing, the indented expression under else will be printed.

if-else condition
Example of if-else
Continuing our previous example, what if you want to print 'z is odd' when the if condition is false? In this case, you can simply add another condition, which is the else condition. If you run it with z equal to 5, the condition is not true, so the expression for the else statement gets printed out.

example of if-else condition
if-elif-else condition
The most complex of these conditions is the if-elif-else condition. When you run into a situation where you have several conditions, you can place as many elif conditions as necessary between the if condition and the else condition.

if-elif-else condition
Example one of if-elif-else condition
Below is an example of where you want different printouts for numbers that are divisible by 2 and 3.

Here, since z equals 3, the first condition is False, so it goes over to the next condition. The next condition does hold True. Hence, the corresponding print statement is executed.

example of if-elif-else condition
