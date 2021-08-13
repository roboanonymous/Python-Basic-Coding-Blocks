"""Given an integer 'n'. Print all the possible pairs of 'n' balanced parentheses.
The output strings should be printed in the sorted order considering '(' has higher value than ')'.

Input Format
Single line containing an integral value 'n'.

Constraints
1<=n<=11

Output Format
Print the balanced parentheses strings with every possible solution on new line.

Sample Input
2
Sample Output
()()
(()) """



def parenthesis(opened,closed,n,s=[]):
    if closed==n:
        print(''.join(s))
        return
    if closed<opened:
        s.append(')')
        parenthesis(opened,closed+1,n,s)
        s.pop()
    if opened<n:
        s.append('(')
        parenthesis(opened+1,closed,n,s)
        s.pop()

n=int(input())
parenthesis(0,0,n)
