from Question import Question

question_prompts=[
     "what color are apples?\n(a)Red\n(b)Yellow\n(c)Green\n\n",
     "what color are Bananas?\n(a)Tale\n(b)Yellow\n(c)Black\n\n",
     "what color are Strawberries?\n(a)Yellow\n(b)White\n(c)Red\n\n"
 ]

questions=[
     Question(question_prompts[0],"a"),
     Question(question_prompts[1],"b"),
     Question(question_prompts[2],"c"),
 ]

def run_test(questions):
     score=0
     for question in questions:
         answer=input(question.prompt)
         if answer==question.answer:
             score+=1
     print("You got "+str(score)+"/"+str(len(questions))+" Correct")

run_test(questions)