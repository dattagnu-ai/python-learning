#C1. तुझं नाव, वय आणि height store कर literals वापरून आणि print कर.


'''name=" dattu "
age = 20
height = 6.01

print ("Name =",name)
print ("age =",age)
print ("height = ",height)'''

# C2 हे complete कर:
'''city = "pune"       
temperature = 36.5
is_raining = False
population = 5000000


print ("City = ",city)
print ("Temprature = ",temperature)
print ("is raining = ",is_raining)
print ("Population = ",population)'''



# तुझं पूर्ण नाव, शहर, वय, weight आणि is_engineer
# स्वतः variables बनव आणि values दे!


'''name=" Dattu"
city = "Alapalli"
age = 20
weight = 87
is_engineer= True

print ("Name = ",name)
print ("City = ",city)
print ("Age  = ",age)
print ("Weight = ",weight,"kg")
print ("You are Engineer = ",is_engineer)'''



# एकाच line मध्ये a, b, c ला 10, 20, 30 assign कर
# आणि तिन्ही print कर

'''a=b=c=100

print (a,b,c)


age = 10

my_name = "Dattu"

height = 6.0

print(age)

print(my_name)

print(height)'''



# name, age, height, is_student, marks_list
# स्वतः values दे आणि type() print कर!


'''name="Dattu"
age = 20
height = 6.01
is_student = True
marks_list = 450

print (type(name))
print (type(age))
print (type(height))
print (type(is_student))
print (type(marks_list))'''



'''# हे run कर आणि output सांग:
x = 10
y = 10.0
z = "10"

print(type(x))
print(type(y))
print(type(z))
print(x == y)
print(type(x) == type(y))'''



# 1) D print कर → Positive index वापर
# 2) u print कर → Negative index वापर
# 3) att print कर → Slicing वापर


"""name="Dattu"

print(name[0])
print(name[-1])
print(name[1:4])"""



# 1) पहिले 4 letters print कर
# 2) शेवटचे 3 letters print कर
# 3) "pal" print कर → slicing वापर
# 


"""
name = "Alapalli"

print(name[0:4])
print(name[5:])
print(name[3:6])"""



# 1) पहिला mark print कर
# 2) शेवटचा mark print कर
# 3) पहिले 3 marks print कर


'''marks = [85, 90, 95, 78, 102]

print (marks[0])
print (marks[4])
print (marks[0:3])'''

# 1) "100" → int मध्ये convert कर आणि 50 add कर
# 2) 75 → float मध्ये convert कर
# 3) 3.99 → int मध्ये convert कर — काय होतं बघ!

"""number="100"
flt=75
integer= 3.99

print(int(number)+50)
print(float(flt))
print(int(integer))"""


# z चा type काय असेल? print करून दाखव!

"""x = 10
y = 3.14
z = x + y

print(type(z))"""




"""print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Dattu"))
print(bool(None))"""



# 1) Addition print कर
# 2) Modulus print कर
# 3) Floor Division print कर
# 4) Exponentiation print कर (a ** b)


"""a = 20
b = 6

print (a+b)
print (a%b)
print (a//b)
print (a**b)"""


'''a = 15
b = 10

print(a > b)
print(a == b)
print(a > 5 and b > 5)
print(a < 5 or b > 5)
print(not(a == b))'''

"""weight=87
height=6

print(f"weight :{weight}")
print(f"BMI calc :{weight}/({height}*{height})")
print("sum:",10+20)"""

name = "Dattu"
age = 20
weight = 85
height = "6ft"
goal = "AI/ML Engineer"
year = 2027

print("=" * 30)
print(f"  Name   : {name}")
print(f"  Age    : {age}")
print(f"  Weight : {weight}kg")
print(f"  Height : {height}")
print(f"  Goal   : {goal}")
print(f"  Target : Job by {year}")
print("=" * 30)