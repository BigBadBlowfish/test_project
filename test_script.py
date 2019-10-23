from node import *

###Class and function declarations

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

    def get_question_num(self, value):
        if self.question_num == value:
            return self.question_num

    def get_correct_answer(self):
        for answer in self.answers:
            if answer.is_correct:
                return answer

class Answer:
    def __init__(self, name, answer_num, is_correct=False):
        self.name = name
        self.answer_num = answer_num
        self.is_correct = is_correct

    def set_answer_correct(self):
        self.is_correct = True


def blankspace(loop_num=2):
    for i in range(loop_num):
        print("")

def generate_quiz():
    blankspace()
    print("Welcome to the Quiz Generator. Please enter a name for the quiz you would like to create.")
    quiz_name = input()
    print("Thank you. Please enter the number of questions you would like to create.")
    blankspace()
    quiz_num_questions = int(input())
    active_quiz = Test(quiz_name, quiz_num_questions)
    print("Thank you. Now, we will create the questions and answers for your quiz")
    return active_quiz

def generate_question(current_question=None):
    blankspace()
    print("Please type out question number " + str(current_question) + ".")
    question_name = input()
    question_num = current_question
    question = Question(question_name, question_num)
    return question

def generate_answers(current_question=None):
    question_answers = []
    for i in range(question.num_answers):
        answer_num = i + 1
        print("Please enter possible answer number " + str(answer_num))
        answer_name = input()
        answer = Answer(answer_name, answer_num)
        question_answers.append(answer)
    question.answers = question_answers
    return question_answers

def print_active_quiz(active_quiz=None):
    print("Okay, now we will display the entire quiz")
    blankspace()
    print("Quiz Name: " + active_quiz.name)
    blankspace(1)
    current_node = active_quiz.questions.head_node
    for i in range(active_quiz.questions.list_length()):
        print("Q: " + current_node.data.name)
        for i in current_node.data.answers:
            print ("A: " + i.name)
        current_node = current_node.next_node


def renaming_prompt(active_quiz=None):
    rename = True
    while rename == True:
        print_active_quiz(active_quiz)
        blankspace()
        print("Would you like to edit any of this information? y/n")
        user_input = input()
        if user_input == "n":
            rename = False
        elif user_input == "y":
            print("Quiz name: " + active_quiz.name)
            print("Enter new quiz name, or enter 'n' to continue.")
            user_input = input()
            if user_input != 'n':
                active_quiz.name = user_input
                print("New quiz name: " + active_quiz.name)
            print("If you would like to edit a question, please enter the question number.")
            user_input = input()
            current_node = active_quiz.questions.head_node
            question_to_rename = None
            for i in range(active_quiz.questions.list_length()):
                current_question_num = current_node.data.get_question_num(i+1)
                if str(current_question_num) == user_input:
                    question_to_rename = current_question_num
                    break
                else:
                    if current_node.has_next_node():
                        current_node = current_node.next_node
            new_question = generate_question(question_to_rename)
            new_question.answers = generate_answers(new_question)   
            current_node.data = new_question

def generate_answer_key(quiz):
    current_node = quiz.questions.head_node
    answer_key = {}
    question_num = 0
    for i in range(quiz.questions.list_length()):
        answer_key[current_node.data.question_num] = current_node.data.get_correct_answer()
        current_node = current_node.next_node
    for question_num, answer in answer_key.items():
        print("Q: " + str(question_num) + " = " "A[" + str(answer.answer_num) + "]" )
        print("Answer text: " + answer.name)
    return answer_key
        





### Program starts here


question_list = LinkedList()
has_restarted = False
while True:
    active_quiz = generate_quiz()
    current_question = 1
    while True:
        question = generate_question(current_question)
        while True:
            generate_answers()
            print("Thank you. We will now list the question followed by the answers you input.")
            blankspace(1)
            print("Question " + str(question.question_num) + ": " + question.name)
            for i in question.answers:
                print("A[" + str(i.answer_num) + "]: " + i.name)
            blankspace(1)
            print("Does this look good? Type 'restart' to go back. Type anythign else to proceed.")
            user_input = input()

            #Clears previsouly input answers
            if user_input == "restart":
                has_restarted = True
                question.answers = []
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
        
        if current_question == active_quiz.num_questions:
            active_quiz.questions = question_list
            break
        if not has_restarted:
            current_question += 1
        else:
            has_restarted = False
    print("Finished")
    blankspace()
    print(generate_answer_key(active_quiz))
    #renaming_prompt(active_quiz)