a=float((input("Python Mark :")))
b=float((input("Cyber Security Mark :")))
c=float((input("J2EE Mark :")))
d=float((input("Project Mark :")))
e=float((input("Lab Assignment Mark :")))
tot=a+b+c+d+e
print("Total is : ",tot)
avg = tot/5
print("Average is :",avg)

if avg>=90:
    print("Grade is : A+")
elif avg>=80:
    print("Grade is : A")
elif avg>=70:
    print("Grade is : B")
elif avg>=50:
    print("Grade is : C")
elif avg>=30:
    print("Grade is : D")
else:
    print("Fail")