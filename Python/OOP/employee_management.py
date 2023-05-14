'''
Challenge
Complete the Employee class.

Class variables
Initialize the following class variables:

company_name set to "Dev.boot".
total_employees set to 0.
Constructor
The constructor should take the following parameters (in order) and set them to the corresponding instance variables:

first_name = first_name
last_name = last_name
id = id
position = position
salary = salary
Also, it should increment the total_employees class variable each time a new Employee is created.

Getter
Add a get_name method that returns the employee's full name as a string (e.g. "John Doe").
'''

class Employee:
    company_name = "Dev.boot"
    #class variable
    total_employees = 0 

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary

        Employee.total_employees += 1

    def get_name(self):
        return f"{self.first_name} {self.last_name}"
