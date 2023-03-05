# MCQ Question and answer:
question_1 = '''(1) English first crector it?
a) Y
b) A
c) J
d) G'''

question_2 = '''(2) What is coding .py what is?
a) JavaSkrip
b) Python
c) Java
d) JS'''

question_3 = '''(3) Bangladesh fevurate flower?
a) Tiki
b) Hasnahena
c) Sofey
d) Lili'''

question_4 = '''(4) Bangladesh national bu=irds?
a) Gugu
b) Doyel
c) kak
d) salik'''

question_5 = '''(5) When you raise?
a) 7:00
b) 8:00
c) 9:00
d) 10:00'''

question_6 = '''(6) What your feveruit frute?
a) Mango
b) Lichi
c) Banna
d) Pinaple'''

question_ = '''() When you raise?
a)
b)
c)
d) '''


question_results = {question_1: "b", question_2: "b", question_3: "d",question_4: "b", question_5: "a", question_6: "a"}

name = input("Enter your name : ")
print("Hello",name,"welcome to the quiz.\n")
score = 0

for p in question_results:
    print(p)
    skip_question = input("\nDo you want to skip the question? please type (Yes/No) : ")
    if skip_question == "Yes" or skip_question == "yes":
        continue
    answer = input("\nEnter your correct answer (a/b/c/d) : ")

    if answer == question_results[p]:
        print("Congratulation! get 1 point")
        score = score+1
        print("Your score is :", score)
    else:
        print("Sorrt, Wrong answer. you have lost 1 points")
        score = score-1
        print("Your score is :", score)

    skip_question = input ("\nDo you want to exit this question? please type (Yes/No) : ")
    if skip_question == "Yes" or skip_question == "yes" or skip_question == "Y" or skip_question == "y":
        break

print("\nFinal Score is",score)