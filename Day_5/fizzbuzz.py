'''
Exercise 4 of day 5 for 100 Days of Python

In this exercise we have to solve the famous FizzBuzz problem.

I have written the solution in 1 line, though, either for loop or a while loop may also be used
'''

print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1,101)))