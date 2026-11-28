import grade 
class student:
    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.__marks = marks
     
    def display(self):
        print("roll no :" ,self.rollno)
        print("name :" ,self.name)
        print("marks: ", self.get_marks())

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if marks < 0 or marks > 100:
            raise ValueError("invalid marks")
        self.__marks = marks
        print("new_marks: ", self.get_marks())

s1 = student(64, "rhiya",60)
s1.display()
s1.set_marks(90)
