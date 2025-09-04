# Age Checker Online
# age = int(input("Enter Your Age: "))
# if(age >= 18 and age < 65):
#   print("You are eligible")
# elif(age > 65):
#   print("You are too old for this position")
# else:
#   print("You are not eligible")
  
# Practice Set for If Elif Else 
# Q3 A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams. 
# w1="make a lot of money"
# w2="buy now"
# w3="subscribe this"
# w4="click this"

# string = input("Enter Keyword: ")
# if((w1 in string) or (w2 in string) or (w3 in string) or (w4 in string)):
#   print("This message is scam. If you trust this then check ✅ it")
  
# Q4 Write a program to find whether a given username contains less than 10 characters or not.
# username = input("Enter UserName: ")
# if(len(username)<=10):
#   print("Your username contains less than 10 characters")
# else:
#   print("Your username contains more than 10 characters")

# Q5 Write a program which finds out whether a given name is present in a list or not.
# list1 = ["Tehami", "Zayan", "Ubaid", "Mohaib"]
# nameU = input("Enter Your Name: ")

# if(nameU in list1):
#   print("You're invited, please proceed")
# else:
#   print("You're not invited") 

# Q6 Write a program to calculate the grade of a student from his marks from the following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 
number_of_subject = 3
m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))

total_marks = m1 + m2 + m3
percentage = (total_marks * 100)/(number_of_subject * 100)

if(percentage>=90 and percentage <=100):
  print("You got Ex grade with the percentage of:", percentage)
elif(percentage>=80 and percentage <90):
  print("You got A grade with the percentage of:", percentage)
elif(percentage>=70 and percentage <80):
  print("You got B grade with the percentage of:", percentage)
elif(percentage>=60 and percentage <70):
  print("You got C grade with the percentage of:", percentage)
elif(percentage>=50 and percentage <60):
  print("You got D grade with the percentage of:", percentage)
elif(percentage>=40 and percentage <50):
  print("You got E grade with the percentage of:", percentage)
else:
  print("You failed! Try again next year")
