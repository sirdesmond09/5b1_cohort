# class Student():
#     instructor = "Desmond"
    
    
#     def __init__(self, name, grade, stu_num):
#         self.name = name
#         self.grade = grade
#         self.stu_num = stu_num
        
#     def get_grade(self):
#         return self.grade
        
    
    


# student = Student(name="Tunde", grade="C", stu_num="3911XYZ")
# student1 = Student(name="Zara", grade="A", stu_num="3915XYZ")

# print(student.get_grade())
# print(student1.name)


# class Employee():
    
#     def __init__(self, name, salary, years):
#         self.name =name
#         self.salary = salary
#         self.years = years
        
#     @property  
#     def bonus(self):
#         if self.years >= 5:
#             return self.salary*0.1
#         return 0


# class Supervisor(Employee):

#     def __init__(self, name, salary, years, branch):
#         self.branch=branch
#         super().__init__(name, salary, years)
   

 
# emp1 = Employee("Chidu", 250, 2)
# emp2 = Employee("Adeola", 500, 5)  
# sup1 = Supervisor("Charles", 2500, 15, "Yaba")  


# print(sup1.years, sup1.branch)      
        
        
        
        
class QuizQuestion():
    num_questions = 0
    num_correct = 0
    question = ""
    correct_answer = ""
    
    def __init__(self, quest, options:list, answer):
        QuizQuestion.question = quest
        for ans in options:
            QuizQuestion.question+=f"\n{ans}"
            
            
        QuizQuestion.correct_answer = answer.upper()
        
    def __ask(self):
        
        while True:
            print(self.question)
            answer = input(">").upper()
            if answer in ["A","B", "C","D", "E"]:
                return answer
            print("\nInvalid answer. Please enter A, B, C, D, or E.\n")
    
    def check(self):
        QuizQuestion.num_questions+=1
        ans = self.__ask()
        if QuizQuestion.correct_answer == ans:
            QuizQuestion.num_correct+=1
            print("Correct")
        else:
            print("Incorrect")
            
            
    def result(self):
        print(f"{QuizQuestion.num_correct} correct our of {QuizQuestion.num_questions} question(s)")
        
        
q1 = QuizQuestion("What year was java created?", 
                  [
                    "A. 1982", 
                    "B. 1996",
                    "C. 1991",
                    "D. 1891",
                    "E. 1981",
],
                  "B")
q1.check()

q2 = QuizQuestion("Who invented Java?", 
                  [
                    "A. James Gosling", 
                    "B. Dennis Ritchie",
                    "C. Raj Reddy",
                    "D. Guido van Ross",
                    "E. Bill Joy"
],
                  "A")
q2.check()
     

q2.result()
 