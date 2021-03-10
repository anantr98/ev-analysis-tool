# Encodings- converting user input to categories
def new_dict_driving(user_string):
  if(user_string == '50-250'):
    return 0
  elif(user_string == '250-450'):
    return 1
  elif(user_string == '450-650'):
    return 2

def new_dict_budget(user_string):
  if(user_string == '0-50000'):
    return 0
  elif(user_string == '50000-100000'):
    return 1
  elif(user_string == '100000-150000'):
    return 2
  elif(user_string == '150000-200000'):
    return 3
  elif(user_string == '200000-250000'):
    return 4
  elif(user_string == '300000-350000'):
    return 5

def new_dict_rapidcharge(string):
  if string == 'Yes' or 'yes' or 'YES':
    return 1
  elif string == 'No' or 'no' or 'NO':
    return 0

class Question:
     def __init__(self, prompt, answer, column_name):
          self.prompt = prompt
          self.answer = answer
          self.column_name = column_name

question_prompts = [
     "How many seats do you prefer? \n2 \n4 \n5 \n6 \n7 ",
     "Do you want rapid charge capabilities? \nYes \nNo ",
     "What is your preferred driving range? \n50-250 \n250-450 \n450-650 ",
     "What is your budget range? \n0-50000 \n50000-100000 \n100000-150000 \n150000-200000 \n200000-250000 \n300000-350000 ",
]

columns_names = ['Seats','RapidCharge','Range_Mi','PriceUS']


questions = [
     Question(question_prompts[0], " ",columns_names[0]),
     Question(question_prompts[1], " ",columns_names[1]),
     Question(question_prompts[2], " ",columns_names[2]),
     Question(question_prompts[3], " ",columns_names[3])
]

# Create a unit test to validate responses

def get_input(text):
    return input(text)

def seats():
    # Ensure seats is a a valid int
    while True:
        answer_0 = get_input(questions[0].prompt)
        try:
            answer_0= int(answer_0)
        except:
            raise TypeError('The number of seats must be an integer.')


        if answer_0 not in [2,4,5,6,7]:
            raise Exception("Please enter one of the following numbers: 2,4,5,6,7")
            continue
        break

    return answer_0

def rapid_charge():
# Ensure RapidChange input is either Yes or No
    while True:
        answer_1 = get_input(questions[1].prompt)
        #if input is not a number
        if(isinstance(answer_1, str)):
                if answer_1 not in ['Yes', 'No', 'NO', 'YES', 'no', 'yes']:
                    raise Exception('Choose Yes if you would like your EV to have Rapid Charge and No if not.')
                else:
                    return answer_1
        else:
            raise TypeError("Input must be not a digit")
        break
    return answer_1



def driving_range():
    # Ensure driving range input is one of the options
    while True:
        answer_2 = get_input(questions[2].prompt)
        if(isinstance(answer_2, str)):
            if answer_2 not in ['50-250', '250-450','450-650']:
                raise Exception('Please choose one of the following ranges: 50-250, 250-450,450-650')
            else:
                return answer_2
        else:
            raise TypeError("Input must be a range.")
        break
    return answer_2


def budget_range():
    # Ensure budget range input is one of the options
    while True:
        answer_3 = get_input(questions[3].prompt)
        if(isinstance(answer_3, str)):
            if answer_3 not in ['0-50000', '50000-100000','100000-150000','150000-200000','200000-250000','300000-350000']:
                raise Exception('Please choose one of the following ranges: 0-50000, 50000-100000,100000-150000,150000-200000,200000-250000,300000-350000')
            else:
                return answer_3
        else:
            raise TypeError("Input must be a range.")

        break
    return answer_3


def run_questions(questions):
    questions_answers = {}
    results_lst = []

    #questions_answers[questions[0].column_name[0]]= seats()
    results_lst.append(seats())

    #questions_answers[questions[1].column_name[1]]= rapid_charge()
    results_lst.append(rapid_charge())

    #questions_answers[questions[2].column_name[2]]= driving_range()
    results_lst.append(driving_range())

    #questions_answers[questions[3].column_name[3]]= budget_range()
    results_lst.append(budget_range())

    results_lst[1] = new_dict_rapidcharge(results_lst[1])
    results_lst[2] = new_dict_driving(results_lst[2])
    results_lst[3] = new_dict_budget(results_lst[3])

    return questions_answers,results_lst


# user_results = run_questions(questions)
# print(user_results[1])
