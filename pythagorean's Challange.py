""" Given a non negative integer A, print all the pairs of integers(a,b) such that

a and b are positive integers

a<=b and

a^2 + b^2 = A

0 <= A

Input Format
First line contains T , number of test cases. Next T lines contain a single integer A each.

Constraints
A<=1000

Output Format
T lines each containing a pair (a,b) in sorted order.

Sample Input
3
1
9
25
Sample Output
(0,1)
(0,3)
(0,5) (3,4) """





t=int(input())
for k in range(t):
    n=int(input())
    i=0
    while(i<=n):
        j=i
        while((j*j)<=n):
            if((i*i + j*j)==n):
                print('',end='(')
                print(i,end=',')
                print(j,end=')')
                print('',end=' ')
            j+=1
        i+=1
    print('')
