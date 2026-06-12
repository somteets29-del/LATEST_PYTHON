print("Welcome! to our fast CGPA calculation platform\n")

#ask for details
name= str(input("Enter your name: "))
Department= str(input("Enter your department: "))
Registration_number = int(input("Enter your reg no: "))
print()

#input number of courses
course_number = int(input("How many courses did you offer this semester: "))
print()

print("Enter only" , course_number, "courses")

total_points = 0
total_credits = 0

#set up the loop
i=0
while i < course_number:
    
    course_name= str(input("Course: "))
    load = int(input("Credit unit: "))
    grade = str(input("Grade: ")).strip() .upper()
    
    
    if grade == "A":
        abe = load * 5
        print ("Total of" ,abe, "points")
        print()
        total_points += abe
        total_credits += load
        
    elif grade == "B":
        tt = load * 4
        print ("Total of" ,tt, "points")
        print()
        total_points += tt
        total_credits += load
    
    elif grade == "C" :
        rd = load * 3
        print ("Total of" ,rd, "points")
        print()
        total_points += rd
        total_credits += load
        
    elif grade == "D" :
        _h = load * 2
        print ("Total of", _h, "points")
        print()
        total_points += _h
        total_credits += load
        
    elif grade == "E" :
        h = load * 1
        print ("Total of", h, "points")
        print()
        total_points += h
        total_credits += load
        
    elif grade == "F" :
        th = load * 0
        print ("Total of", th, "points")
        print()
        total_points += th
        total_credits += load
  
    else: 
        print ("Invalid Grade")
    i += 1
    cgpa = 0.0
if total_credits > 0:
    cgpa = total_points / total_credits
    print("Your CGPA is:", round(cgpa, 2))
else:
    print("No courses entered")
    
    # Save to file
filename = "cgpa_result.txt"
with open("cgpa_result.txt", "w") as file:

    file.write("CGPA RESULT\n")
    file.write("===================\n")
    file.write("Name: " + name + "\n")
    file.write("Department: " + Department + "\n")
    file.write("Reg No: " + str(Registration_number) + "\n")
    file.write("Courses: " + str(course_number) + "\n")
    file.write("Total Points: " + str(total_points) + "\n")
    file.write("Total Credits: " + str(total_credits) + "\n")
    file.write("CGPA: " + str(round(cgpa, 2)) + "\n")

print("Dear" , name, "your result has been saved to cgpa_result.txt")