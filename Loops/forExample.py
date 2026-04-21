#Print numbers from 1 to 29
for i in range(1,30):
    print(i)

#Print even numbers from 1 to 20
for i in range(1, 21):
    if i%2==0:
        print(i)


#print each character of a string in a new line
name=input("Enter student name: ")
for i in name:
    print(i)   

#Calculate the sum of first 100 natural numbers
sum=0
for i in range(1,101):
   sum=sum+i
print(sum)

#Calculate the number of vowels in a string
vowels="aeiouAEIOU"
name="Anushka"
count=0
for n in name:
    for v in vowels:
        if v==n:
         count=count+1
print(count)

#collect student data and print it
students=[]
for i in range(3):
    name=input("Enter student name: ")
    age=int(input("Enter student age: "))
    students.append([name,age])
print("Student data:")
for student in students:
    print(student)  
