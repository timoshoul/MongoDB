from pymongo import MongoClient
import json

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose InfoSys database
db = client['InfoSys']
students = db['Students']

def insert_student(name,email,year,gender):
    student = {
        "name": name, 
        "email": email, 
        "yearOfBirth": year, 
        "gender": gender
    }
    res = students.insert_one(student)
    print("Student inserted with id: ",res.inserted_id)

def get_all_students_after_1996():
    # Find all students after 1996
    iterable=students.find( { "yearOfBirth": { "$gt": 1996 } } ,{"_id":0})
    for student in iterable:
        print(student,"\n")

    # Print total count
    print("Total number of students: ", iterable.count())


def get_first_student_after_1996():
    # Find first student after 1996 
    res=students.find_one( { "yearOfBirth": { "$gt": 1996 } } ,{"_id":0})

    # Print 
    print("The first student after 1996:\n",res)

def get_all_females_before_1996():
    # Find all students after 1996  
    iterable=students.find( { "yearOfBirth": { "$lt": 1996 } },{"gender":"female"})

    # Print total count   
    print("Total number of females before 1996: ", iterable.count())



def find_student(name):
    student = students.find_one({"name": name},
                                {"_id":0})
    print(student)




insert_student('Timotheos Houliaros','timos009@hotmail.com',2000,'male')
find_student(name='Timotheos Houliaros')
get_all_students_after_1996()
get_first_student_after_1996()
get_all_females_before_1996()
