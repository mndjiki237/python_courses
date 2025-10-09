"""
 write a python program to get subject marks from the user 
 and calculate tital avarage of that marks. And display to user   
"""


while True:

    marks = input("Enter all your marks: ")

    marks = marks.split(", ")
    marks_interger = []
    for mark in marks:
        if not mark.isdigit():
            print("Enter numbers only")
            continue
            
        else:
            marks_interger.append(int(mark))
    if marks_interger:

        average = sum(marks_interger)/len(marks_interger)
        print(f"the mark average is {average}")
        break
