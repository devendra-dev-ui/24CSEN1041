hours = int(input("enter number of hours: "))

if hours<=8:
    gross = hours*200
else:
    gross = 8*200+(hours-8) *300
    
if gross>5000:
    tax = gross *0.05
else:
    tax = 0
net = gross - tax

print(gross, tax, net)

#output
enter number of hours: 5
1000 0 1000


#2question
x = float(input("enter the marks of subject1: "))
y = float(input("enter the marks of subject2: "))
z = float(input("enter the marks of subject2: "))
average=(x+y+z)/3
    print("average")
if average>=90 and average<=100:
    print("grade is o")
elif average>=80 and average<=89:
    print("grade is A+")
elif average>=70 and average<=79:
    print("grade is A")
elif average>=60 and average<=69:
    print("grade is B+")
elif average>=50 and average<=59:
    print("grade is B")
elif average>=49 and average<=45:
    print("grade is C")
elif average>=44 and average<=40:
    print("grade is P")
else:
    print("grade is F")

#output
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 5
    print("average")
IndentationError: unexpected indent

#if i remove that print average then the output looks like this 
#output
enter the marks of subject1: 99
enter the marks of subject2: 99
enter the marks of subject2: 99
grade is o

=== Code Execution Successful ===
