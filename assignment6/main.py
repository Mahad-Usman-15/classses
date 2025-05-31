
# class Student:
#     def __init__(self, name="Mahad Usman", marks=100):
#         self.name = name
#         self.marks = marks

#     def Display(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print(f"The Student name is {self.name} and marks gained is {self.marks}.")

# # Create an object
# student = Student()

# # Call the method
# student.Display("Mahad", 100)



# class Car:
#     def __init__(self,brand="BMW",model="2006"):
#         self.brand=brand
#         self.model=model
#     def Display(self,brand,model):
#         self.brand=brand
#         self.model=model
#         print(f"The Car is {self.brand} with {self.model}.")  


# car=Car()
# car.Display("Toyota",100)    



# class Counter:
#     count:int=0
#     def __init__(self):
#      Counter.count+=1

#     @classmethod
#     def displayCount(cls):
#         print(f"The total count is {cls.count}")


# object1=Counter() 
# object2=Counter()   
# object3=Counter()   
# object4=Counter()      


# Counter.displayCount()
        

# class Car:
#     brand="BMW"
#     def __init__(self,brand):
#         self.brand=brand
#     def start(self,brand,voice):
#         self.brand=brand 
#         self.voice=voice
#         print(f"The car with brand {self.brand} when starts roars like a {self.voice}")


# car=Car("BMW")
# car.start("Toyota","Ratata")



# class Bank:
#     bank_name="Meezan"
#     @classmethod
#     def changebankname(cls,name):
#         cls.bank_name=name
      
# bankname=Bank()     

# print("bankname:",bankname.bank_name)  


# bankname.changebankname("AlHabib")

# print("bankname:",bankname.bank_name) 


# class Mathutils:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     @staticmethod
#     def subtract(a,b):
#         return a-b
#     @staticmethod
#     def Multiply(a,b):
#         return a*b
#     @staticmethod
#     def Divide(a,b):
#         return a/b


# input1=int(input("Enter the number"))
# input2=int(input("Enter the number"))
# print("1.Add")
# print("2.Subtract")
# print("3.Divide")
# print("4.Multiply")

# choice=int(input("Enter the choice (1-4):"))
# if choice==1:
#     result=Mathutils.add(input1,input2)
#     print(result)
# elif choice==2:
#     result=Mathutils.subtract(input1,input2)
#     print(result)
# elif choice==3:
#     try:
#      result=Mathutils.Divide(input1,input2)
#      print(result)
#     except ZeroDivisionError:
#         print(f"The divident cant be zero")
    
# elif choice==4:
#     result=Mathutils.Multiply(input1,input2)
#     print(result) 
# else:
#     print("Invalide choice")    
# class Todo:
#     tasks = []

#     @staticmethod
#     def add_task(task):
#         Todo.tasks.append(task)
#         print(f"Task added: {task}")

#     @staticmethod
#     def remove_task(task):
#         if task in Todo.tasks:
#             Todo.tasks.remove(task)
#             print(f"Task removed: {task}")
#         else:
#             print("Task not found in list.")

#     @staticmethod
#     def show_tasks():
#         if Todo.tasks:
#             print("Current tasks:")
#             for i, task in enumerate(Todo.tasks, 1):
#                 print(f"{i}. {task}")
#         else:
#             print("No tasks available.")

#     @staticmethod
#     def exit_app():
#         print("Exiting Todo App. Goodbye!")


# def main():
#     while True:
#         print("\n--- Todo App Menu ---")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. Show Tasks")
#         print("4. Exit")

#         try:
#             choice = int(input("What do you want to do (1-4)? "))
#         except ValueError:
#             print("Please enter a valid number.")
#             continue

#         if choice == 1:
#             task = input("Enter the task to add: ")
#             Todo.add_task(task)

#         elif choice == 2:
#             task = input("Enter the task to remove: ")
#             Todo.remove_task(task)

#         elif choice == 3:
#             Todo.show_tasks()

#         elif choice == 4:
#             Todo.exit_app()
#             break

#         else:
#             print("Invalid choice. Please select between 1 and 4.")


# main()




# class Logger:
#     message = "An object is created"
#     message2 = "An object is destructed"

#     def __init__(self):
#         print(self.message)

#     def __del__(self):
#         print(self.message2)



# p = Logger()
# p2 = Logger()


# del p
# del p2





# # This is a public member
# class School:
#     def __init__(self,area):
#         self.area=area
#         print(f"School is in the {self.area}")




# areas=School("FB Area")


# # This is privatemember

# class Brand:
#     def __init__(self,brand):
#         self.__brand=brand


#     def showbrand(self):
#         print(f"The brand name is {self.__brand}")


# brand=Brand("Habib")
# brand.showbrand()        



# # Abstraction is hiding important details and showing what you want to the outside world
# class BankAccount:
#     def __init__(self):
#          self.__id="123545" #This is protected
# class Person(BankAccount):
#     def showid(self):
#         print(f"THe id is {self._BankAccount__id}")


# s=Person()
# s.showid()        
    
# print(BankAccount._id)




class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name                # Public
        print(f"The name is {self.name}")
        self._salary = salary          
        self.__ssn = ssn                

    def showid(self):
        print(f"The salary of {self.name} is {self._salary}")


emp = Employee("Ali", 50000, "123-45-6789")


emp.showid()

class Animal:
    def __init__(self,animal,voice):
        self.Animal=animal
        self.voice=voice
        print(f"{self.Animal} barks with {self.voice}")
# This is inheritance
class Dog(Animal):
    def showname(self):
        print(f"{self.Animal}")


name=Animal("Dog","Roaring sound")
name=Dog("Habib","roar")


class Game:
    def __init__(self, name, id):
        self.name = name
        self.__id = id  # private

class Player(Game):
    def __init__(self, name, id, breed):
        super().__init__(name, id) 
        self.breed = breed

dog2 = Player("Dog", 101, "American")


print(dog2.name)     
print(dog2.breed)    



class Student:
    def __init__(self,grade):
        self.grade=grade
    

student=Student("Ten")
print(student.grade)



class Book:
   def __init__(self,name):
       self.name=name

   def showbook(self,name):
       self.name=name
       print(f"The book name is {self.name}")

        
bookname=Book("The Jokers")
bookname.showbook("The Carnival")    



class BookCount:
    totalbooks=0

    @classmethod
    def increment_book_count(self,book):
        self.book=book
        BookCount.totalbooks+=1




BookCount.increment_book_count("The Carnival")
BookCount.increment_book_count("THe Marathons")
BookCount.increment_book_count("The Science Fiction")



print("Total Books",BookCount.totalbooks)




class TemperatureConvertor:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (1.8*c) +32
    


temperture=TemperatureConvertor()
print(temperture.celsius_to_fahrenheit(37))    





class Engine:
    @classmethod
    def  Showcarname(self,carname):
        self.carname=carname
        print(f"The Car With Brand {self.carname}")
class Car(Engine):
    Engine.Showcarname("BMW")


 

car=Car()
print(car.carname)


class Department:
    employees=[]
    def __init__(self,employee,salary):
        self.employee=employee
        self.__salary=salary
        Department.employees.append(self.employee)
        print(f"A new Employee named {self.employee} is added")

    def showsalary(self):
        print(f"The salary of {self.employee }is {self.__salary}")

emp1=Department("Areeb",2000)
emp2=Department("Zain",3000)
emp3=Department("Hafeez",5000)
emp4=Department("Rohaan",5000)

print(emp1.employees)  
emp1.showsalary()


class A:
    def method(self):
        print("A")
class B(A):
    def method(self):
        print("B")        
class C(A):
    def method(self):
        print("C")  
class D(B,C):
    def method(self):
        print("D")
class E(D,C):
    pass

d=E()
d.method()



    