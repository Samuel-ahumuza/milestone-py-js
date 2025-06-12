print("welcome to the grading scale")
marks = int(input("please enter marks between 0 and 100"))
if marks >=91 and marks <= 100:
    print("A+")
elif marks >=81 and marks <= 90:
    print("A")
elif marks >=71 and marks <= 80:
    print("B+")
elif marks >=61 and marks <= 70:
    print("B")
elif marks >=51 and marks <= 60:
    print("C+")
elif marks >=41 and marks <= 50:
    print("C")
elif marks >=31 and marks <= 40:
    print("D+")
elif marks >=21 and marks <= 30:
    print("D")
elif marks >=0 and marks <= 20:
    print("F")
else:
    print("invalid, please enter a mark between 0 and 100")