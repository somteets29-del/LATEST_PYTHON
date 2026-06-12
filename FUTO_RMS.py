print("WELCOME TO THE FUTO STUDENTS RESULT MANAGEMENT SYSTEM" "\n")

#Ask for details
print("Enter your details below" "\n")
name = str(input("Name: "))
reg_no = int(input("Registration number: "))
department = str(input("Department: "))
print()

#number of courses
course_num = int(input("Courses Offered: "))
print("Enter only", course_num, "courses")
print()

if course_num > 20:
    jj = "Exceeded Minimum number of Courses\nEnter only 20 courses"
    print(jj)
    exit()

#counters
total_points=0
total_credits=0
a_count=0
b_count=0
c_count=0
d_count=0
e_count=0
fail_count=0
courses = []

#set the loop
i=0
while i < course_num:
    course_name= str(input("Course: "))
    courses.append(course_name)
    
    load = int(input("Credit unit: "))
    grade = str(input("Grade: ")).strip() .upper()  
      
    #grading system
    if grade == "A":
        abe = load * 5
        print ("Total of" ,abe, "points")
        print()
        total_points += abe
        total_credits += load
        a_count +=1
        
    elif grade == "B":
        tt = load * 4
        print ("Total of" ,tt, "points")
        print()
        total_points += tt
        total_credits += load
        b_count +=1
    
    elif grade == "C" :
        rd = load * 3
        print ("Total of" ,rd, "points")
        print()
        total_points += rd
        total_credits += load
        c_count +=1
        
    elif grade == "D" :
        _h = load * 2
        print ("Total of", _h, "points")
        print()
        total_points += _h
        total_credits += load
        d_count +=1
        
    elif grade == "E" :
        h = load * 1
        print ("Total of", h, "points")
        print()
        total_points += h
        total_credits += load
        e_count +=1
        
    elif grade == "F" :
        th = load * 0
        print ("Total of", th, "points")
        print()
        total_points += th
        total_credits += load
        fail_count +=1
  
    else: 
        print ("Invalid Grade")
        i -= 1
    i += 1
    
#result summary
print("====================")
print("Result Summary")
print("====================")
print("Your results details are: ")
print("\nCourses Offered:")

for course in courses:
    print(course)
    
print()
print("Total Credits is",total_credits)
print("Total Points is" ,total_points)

print("Number Of A's:", a_count)
print("Number Of B's:", b_count)
print("You failed", fail_count, "courses")

#cgpa calculation
cgpa = 0.0

    
if total_credits > 0:
    cgpa = total_points / total_credits
    print("Your CGPA is:", round(cgpa, 2))
    print()
    
if cgpa >= 4.50 :
    print("Congratulations! You are a First Class Student")
elif 4.00 <= cgpa < 4.50:
    print("Second Class Upper")
elif 3.50 <= cgpa < 4.00:
    print("Second Class Lower")
elif 3.00 <= cgpa < 3.50:
    print ("Third Class")
elif cgpa < 3.00:
    print ("Fail")
else:
        print("No courses entered")
filename = "results.txt"
with open ("results.txt" , "w") as file:
    file.write ("Semester Results\n")
    file.write ("================\n")
    file.write ("Name: " + name + "\n")
    file.write ("Department: "+ department + "\n")
    file.write ("Registration Number: " +str(reg_no) + "\n")
print("You results have been saved in Calcul.txt to ")