class Student:
    def __init__(self, name, age, address, qualification):
        self.name = name
        self.age = age
        self.address = address
        self.qualification = qualification

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Qualification: {self.qualification}"

s1 = Student("Rahul", 20, "Mumbai", "BSc")
s2 = Student("Anita", 21, "Pune", "BTech")
s3 = Student("Ravi", 22, "Nashik", "BA")
s4 = Student("Priya", 19, "Nagpur", "BCA")

students = {
    1: s1,
    2: s2,
    3: s3,
    4: s4
}

roll = int(input("Enter roll number: "))

if roll in students:
    print("Student Details:", students[roll])
else:
    print("Student not found")