#!/usr/bin/env python
# coding: utf-8

# In[77]:


# TBA = 2000 
# Bill = 0
# Units = int(input("Enter your bill : " ))
# #amount = 350
# if (Units <= 100):
#         print("No Charge")
# if Units >101 <= 200:
#       Paid_Bill = Bill+Units*5-TBA
# if Units >200 <= 350:
#         Paid_Bill = Bill+Units*10-TBA
# print("Total electricity bill is", Paid_Bill )


# In[11]:


#TBA = 2000 
Bill = 0
Units = int(input("Enter your bill : " ))
#amount = 350
if (Units <= 100):
        print("No Charge")
if Units > 100:
        Bill = Bill+100*5
if Units >=200 <=350:
        Bill = Bill+(Units-200)*10
        
print("Total electricity bill is", Bill )


# In[2]:


User = input ("Enter your percentage : ")

Marks = 100

if Marks>90:
    print("A")
    
elif (Marks >=80 <= 90):
    print("B")

elif (Marks >=60 <= 80):
    print("c")    

else:
    print("D")


# In[6]:


number = int (input("Enter the number : "))

x = abs(number) % 10 #last digit

if x % 3 == 0:
    print("Last digit is divisible by 3.")
else:
    print("Last digit is not divisible by 3.")


# In[10]:


# Accept ages from the user
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))
age4 = int(input("Enter the age of person 4: "))

# Use if-else to find the youngest
if age1 <= age2 and age1 <= age3 and age1 <= age4:
    youngest = age1
elif age2 <= age1 and age2 <= age3 and age2 <= age4:
    youngest = age2
elif age3 <= age1 and age3 <= age2 and age3 <= age4:
    youngest = age3
else:
    youngest = age4

# Display the youngest age
print(f"The youngest age is: {youngest}")


# In[33]:


User_Salary = float(input("Enter your salary: "))
User_YOS = float(input("Enter year of service: "))

if User_YOS > 10:
    Bonus = 0.10 * User_Salary
#     net_salary = User_Salary + Bonus
    
elif User_YOS >= 6 and User_YOS <= 10:
        Bonus = 0.08 * User_Salary
#         net_salary = User_Salary + Bonus
else:
    Bonus = 0.05*User_Salary
#     net_salary = User_Salary + Bonus
    

print("Net bonus amount is", Bonus )

# print("Net  net salary is",  net_salary )


# In[9]:


# Accept ages from the user
number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))
number3 = int(input("Enter the number 3: "))


# Use if-else to find the youngest
if number1 > number2 and number1 < number3: 
    Second_Largest = number1
    
elif number2 > number1 and number2 < number3:
    Second_Largest = number2
else:
    Second_Largest = number3

# Display the youngest age
print(f"The second_Largest number is: {Second_Largest}")


# In[10]:


# Accept marked price from the user
marked_price = float(input("Enter the marked price: "))

# Apply discount based on the marked price
if marked_price > 10000:
    discount = 0.20 * marked_price
elif marked_price > 7000 and marked_price <= 10000:
    discount = 0.15 * marked_price
else:  # marked_price <= 7000
    discount = 0.10 * marked_price

# Calculate net amount
net_amount = marked_price - discount

# Display the result
print(f"Discount: {discount}")
print(f"Net amount to pay: {net_amount}")


# In[17]:


# Accept marks from the user
english = int(input("Enter marks in English: "))
math = int(input("Enter marks in Math: "))
science = int(input("Enter marks in Science: "))
social_Studies = int(input("Enter marks in Social Studies: "))

# Determine stream based on conditions
if english > 80 and math > 80 and science > 80 and social_Studies > 80:
    print("Stream Allotted: Science Stream")
elif english > 80 and math > 50 and science > 50:
    print("Stream Allotted: Commerce Stream")
elif english > 80 and social_Studies > 80:
    print("Stream Allotted: Humanities Stream")
else:
    print("No stream allotted based on the given criteria.")


# In[33]:


# Accept number from the user
number = int(input("Enter the number: "))

if number % 5 == 0:
    print("Hello")
else:
    print ("Bye")


# In[3]:


number = int(input("Enter the number: "))

if 100 <= abs(number) <= 999:
    print("The number is a three digit number: ")
else:
    print("The number is not a three digit number: ") 


# In[ ]:





# In[ ]:





# In[ ]:




