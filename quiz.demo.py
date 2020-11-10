# Question

class Question:
     def __init__(self,text,choices,answer):
          self.text = text
          self.choices = choices
          self.answer = answer
     
     def checkAnswer(self,answer):
          return self.answer == answer

q1 = Question('en iyi programlama dili hangisidir ?',['C#','Python','javascript','java'],'Python')
q2 = Question('en popüler programlama dili hangisidir ?',['Python','javascript','C#','java'],'Python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?',['C#','javascript','java','python'],'Python')
list = [q1,q2,q3]
print(q1.checkAnswer('Python'))
print(q2.checkAnswer('C#'))
# Sonuç olarak ;
# True
# False   olarak gelecektir.


# Quiz Tanımlamak istersek;

# Question

class Question:
     def __init__(self,text,choices,answer):
          self.text = text
          self.choices = choices
          self.answer = answer
     
     def checkAnswer(self,answer):
          return self.answer == answer

# Quiz
class Quiz:
     def __init__(self,questions):
          self.questions = questions
          self.score = 0
          self.questionsIndex = 0 

q1 = Question('en iyi programlama dili hangisidir ?',['C#','Python','javascript','java'],'Python')
q2 = Question('en popüler programlama dili hangisidir ?',['Python','javascript','C#','java'],'Python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?',['C#','javascript','java','python'],'Python')
questions = [q1,q2,q3]

quiz = Quiz(questions)
question = quiz.questions[quiz.questionsIndex]
print(question)  # Sonuç olarak; <__main__.Question object at 0x000001F9B801F708> gelir.
print(question.text) # Sonuç olarak; en iyi programlama dili hangisidir ?  cevabı gelecektir.

# print(question.text) # Eğer en başta self.questionsIndex = 1 deseydik cevap : en popüler programlama dili hangisidir ? şeklinde gelirdi. 


          
