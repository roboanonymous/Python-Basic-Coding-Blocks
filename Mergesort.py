"""Given an array A, of N elements. Sort the array using mergesort algorithm.

Input Format
A single integer, N, denoting the number of elements in array. Next line contains N integers, denoting the elements of array.

Constraints
1<=N<=2*10^5
|Ai|<=10^9

Output Format
Print in a single line, N spaced integers, denoting the elements of array A in sorted order.

Sample Input
5
3 6 4 1 2
Sample Output
1 2 3 4 6 
"""

n=int(input())
a=[int(x) for x in input().split()]
a=sorted(a)
for i in range(n):
    print(a[i],end=' ')

