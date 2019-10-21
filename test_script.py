from node import *

class Test:
    def __init__(self, name, num_questions, questions=None):
        self.name = name
        self.num_questions = num_questions
        self.questions = None


class Question:
    def __init__(self, name, question_num, num_answers=4, answers=[]):
        self.name = name
        self.num_answers = num_answers
        self.question_num = question_num
        self.answers = answers


class Answer:
    def __init__(self, name, answer_num, is_correct=False):
        self.name = name
        self.answer_num = answer_num
        self.is_correct = is_correct

    def set_answer_correct(self):
        self.is_correct = True




question_list = LinkedList()
has_restarted = False
while True:
    print("Welcome to the Quiz Generator. Please enter a name for the quiz you would like to create.")
    quiz_name = input()
    print("Thank you. Please enter the number of questions you would like to create.")
    quiz_num_questions = int(input())
    active_quiz = Test(quiz_name, quiz_num_questions)
    print("Thank you. Now, we will create the questions and answers for your quiz")
    print("")
    print("")
    current_question = 1
    while True:
        print("Please type out question number " + str(current_question) + ".")
        question_name = input()
        question_num = current_question
        question_answers = []
        question = Question(question_name, question_num)
        while True:
            for i in range(question.num_answers):
                answer_num = i + 1
                print("Please enter possible answer number " + str(answer_num))
                answer_name = input()
                answer = Answer(answer_name, answer_num)
                question_answers.append(answer)
            question.answers = question_answers
            print("Thank you. We will now list the question followed by the answers you input.")
            print("")
            print("Q: " + question.name)
            for i in question.answers:
                print("A: " + i.name)
            print("")
            print("Does this look good? Type 'restart' to go back. Type anythign else to proceed.")
            user_input = input()

            #Clears previsouly input answers
            if user_input == "restart":
                has_restarted = True
                question.answers = []
                question_answers = []
                break
            if user_input != "restart":
                while True:
                    print("Please indicate the correct answer by typing the corresponding number.")
                    correct_answer_input = input()
                    correct_answer_index = 0
                    correct_answer = None

                    #Matches user input with the index of the answer in the question object.
                    for i in range(len(question.answers)):
                        if i + 1 == int(correct_answer_input):
                            correct_answer = question.answers[i]
                            break
                        correct_answer_index += 1
                    print("You picked the following as the correct answer:")
                    print(correct_answer.name)
                    print("If this is correct? y/n")
                    user_input = input()

                    #Breaks while loop if user verifies they selected the correct answer.
                    #Marks the is_correct attribute in the answer object as True
                    #Creates question_node variable and instantiates it as a ListNode object
                    #Adds the new question_node to the question_list LinkedList
                    if user_input == "y":
                        question.answers[correct_answer_index].is_correct = True
                        question_node = ListNode(question)
                        question_list.add_list_item(question_node)
                        print("Answer successfully set")
                        break

            #Prevents breaking the while loop for gathering answers if the user typed 'restart'
            if question.answers != []:
                break
        
        if question_num == active_quiz.num_questions:
            active_quiz.questions = question_list
            break
        if not has_restarted:
            current_question += 1
        else:
            has_restarted = False
    print("Finished")
    print("")
    print("")
    print("Okay, now we will display the entire quiz")
    print("")
    print("")
    print("Quiz Name: " + active_quiz.name)
    print("")
    current_node = active_quiz.questions.head_node
    for i in range(active_quiz.questions.list_length()):
        print("Q: " + current_node.data.name)
        for i in current_node.data.answers:
            print ("A: " + i.name)
        current_node = current_node.next_node
    



    

        
