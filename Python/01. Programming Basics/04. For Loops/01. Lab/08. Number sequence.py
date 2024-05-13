# https://judge.softuni.org/Contests/Compete/Index/2417#7
a = int(input())
b = int(input()) #! This variable captures the first input value separately, ensuring the loop starts from the second input for comparisons
c = b                       
d = b                  
#! b --> (c, d)
for i in range(1, a):
    '''
#! range(a): This generates a sequence of numbers from '0' up to, but not including, 'a'. For example, range(5) would generate '0, 1, 2, 3, 4'.

#! range(1, a): This generates a sequence of numbers from '1' up to, but not including, 'a'. For instance, range(1, 5) would generate '1, 2, 3, 4'.
    '''
    e = int(input())
    if e > c:
        c = e
    elif e < d:
        d = e

print(f'Max number: {c}')
print(f'Min number: {d}')

'''
This code effectively finds the maximum and minimum values entered by the user among a series of inputs (a defines how many inputs will be given).
Each input value (e) is compared to the current maximum (c) and minimum (d) values, updating them accordingly as the loop progresses.

B:

ChatGPT
https://python-book.softuni.bg/chapter-05-loops.html

'''