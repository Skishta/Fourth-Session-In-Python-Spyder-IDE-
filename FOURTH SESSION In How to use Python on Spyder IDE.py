'''بسم الله الرحمن الرحيم'''               
#اولا البايثون هي أحدث اللغات المستخدمة للبرمجة
#In this training program
#you will learn how to collect
#analyze and visualize any size of data
#Learn ٍsome-NOT ALL- Python basics.
#Learn simplest way in OOP (Object-Oriented Programming) and data structures in python
#Be able to implement some algorithms or program using python
#Learn the most needed data science algorithms

                '''FOURTH SESSION In How to use Python on Spyder IDE'''
#list & nested IF
#دلوقتى هنشتغل على الlist ونغير شوية ونكبر الlist
#هنشتغل دلوقتى على lists داخل list بحيث ان الlist الاولانية هتكون keys والتانية هتكون values
listx=[["Fname","Lname","Age","years",],["Ahmed","radwan","28","2019"],["00","55","88","99"]]
#to get specfic value from the list
#listx[numbering main index][numbering the sub index]
listx[2][0]
#to call specific element by index in a list
print("Your name is: " + listx[1][0] + " and your age is: " + listx[1][2]) 
#طيب لو انا عايز اطلب من اليوزرز يدخلوا اسمائهم والباسوورد بتاعهم واضيفوا فى list بأسماء المستخدمين والباسوورد بتاعهم
#to ask users to enter name and password and import it in list
#ask user to enter name and pass by input
username=input("plz enter UR name: ")
password=input("plz enter UR password: ")
#create list to import name and pass in
users=[[],[]]
#import name at index 0 in first list
users[0].append(username)
users[1].append(password)
#to use if condition in list
#So if the user have no ledal age he cannot enter name and password
#ask user to enter his age
age=int(input("plz enter UR age: "))
#make the condition for the user if he is older-than 22 he wll get in the loop
if age>22:
    username=input("plz enter UR name: ")
    password=input("plz enter UR password: ")
    users=[[],[]]
    users[0].append(username)
    users[1].append(password)
#if he is younger-than 22 it wll print statment saying sorry
elif age<22:
    print("plz sorry ur are too young")
#to make list of lists 
#each user will have his own list with sub-list of (keys and values) of his info
user_attr={"Ahmed":{"tall":78,"colour":"white","age":28,"weight":90},
           "Ali":{"tall":88,"colour":"black","age":38,"weight":100}}