#Program to find golden ratio
print("This is a program to compute the golden ratio\n")
      
n = int(input("Enter limit of fibonacci series: "))

#Initialising fibonacci list and first,second term
fbseries = [0,1]
a = 0
b = 1

#Generate fibonacci series
for i in range(n-2):
    c = a + b
    a = b
    b = c
    fbseries.append(c)
print("The generated fibonacci series upto",n,"terms is: ",fbseries)

#Compute golden ratio for each pair of terms of fibonacci series

for i in range(2,n):
    gratio = fbseries[i]/fbseries[i-1]
    print(fbseries[i-1],fbseries[i],gratio,sep = "\t")
print("We find that the Golden ratio is ",'%0.1f'%(gratio))

"""OUTPUT:
This is a program to compute the golden ratio

Enter limit of fibonacci series: 10
The generated fibonacci series upto 10 terms is:  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
1	1	1.0
1	2	2.0
2	3	1.5
3	5	1.6666666666666667
5	8	1.6
8	13	1.625
13	21	1.6153846153846154
21	34	1.619047619047619
"""

