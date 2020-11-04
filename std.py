
students=[]
for num in range(1):
    x=input("Enter name of students: ")
    students.append(x)
n=int(input("enter number of subjects"))
marks=[]
for num in range(0,n):
    m=int(input("Enter marks of students:"))
    marks.append(m)
    print(m)
print("sum of subjects")
s=sum(marks)
print(s)
avg=sum(marks)/n
print("average of marks")
print(avg)
print(marks)
    
