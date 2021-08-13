"""Take as input N, a number. Print the pattern as given in output section for corresponding input.

Input Format
Enter value of N

Constraints
Output Format
All numbers and stars are Space separated

Sample Input
5
Sample Output
1 2 3 4 5
1 2 3 4 * 
1 2 3 * * *
1 2 * * * * *
1 * * * * * * *
Explanation
Catch the pattern for the corresponding input and print them accordingly."""



n=int(input())
for i in range(n):
    for j in range(n-i):
        print(int(j+1),end=' ')
    for j in range((i-1)*2+1):
        print('*',end=' ')
    print('')
