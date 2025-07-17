m = int(input("Markes in Mathes: "))
s = int(input("Markes in Science: "))
e = int(input("Markes in English: "))
total_marks = m+s+e
average = total_marks/3
percentage = (total_marks/300)*100
grade = ""
if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage <=90:
    grade = "B"
elif percentage > 70 and percentage <=80:
    grade = "C"
elif percentage > 60 and percentage <=70:
    grade = "D"
elif percentage > 50 and percentage <=60:
    grade = "E"
else:
    grade = "P"
print(f"Total Marks: {total_marks} \nAverage Marks: {average} \nGrade: {grade}")
