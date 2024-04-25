
def computer_sci_ques():

  d = {"Which of the following is not the mode of interacting with python?":["Interactive Mode","Script Mode","Hybrid Mode","None of the above"],
       "Smallest element of of python coding is called":["Identifiers","Token","Keywords","Delimiters"],
       "Which of the following symbol is used to write comment?":["?","//","#","**"],
       "Which keyword is used to define a function in python?":["def","define","new","None of the above"]
       }
  global score
  score = 0
  key_list = list(d.keys())
  corr_ans_list = ['c','b','c','a']
  

  for i in range(1,5):
    k = i-1
    q = key_list[k]
    print(f"Question {i}: {q} \n \n \t A: {d.get(q)[0]} \n \n \t B: {d.get(q)[1]} \n \n \t C: {d.get(q)[2]} \n \n \t D: {d.get(q)[3]}")

    ans = input("Enter Your Answer [A/B/C/D] : ")
    if ans.lower() == corr_ans_list[k]:
      print("\n Yay! Your Answer Is Correct. \n")
      score += 10
    else:
      print("\n Ohh! Your Answer Is Incorrect. Better Luck Next Time. \n")



def gk_ques():

  d = {"The World Largest desert is ?":["Thar","Kalahari","Sahara","Sonoran"],
       "Mount Everest is located in ?":["India","Nepal","Tibet","China"],
       "Which soil is suitable for agriculture ?":["Red","Loamy","Black","Peaty"],
       "The device used for measuring altitudes is ?":["altimeter","ammeter","audiometer","galvanometer"]
       }
  global score
  score = 0
  key_list = list(d.keys())
  corr_ans_list = ['c','b','b','a']
  

  for i in range(1,5):
    k = i-1
    q = key_list[k]
    print(f"Question {i}: {q} \n \n \t A: {d.get(q)[0]} \n \n \t B: {d.get(q)[1]} \n \n \t C: {d.get(q)[2]} \n \n \t D: {d.get(q)[3]}")

    ans = input("Enter Your Answer [A/B/C/D] : ")
    if ans.lower() == corr_ans_list[k]:
      print("\n Yay! Your Answer Is Correct. \n")
      score += 10
    else:
      print("\n Ohh! Your Answer Is Incorrect. Better Luck Next Time. \n")

  

def chem_ques():

  d = {"The nucleus of an atom consists of":["electrons and neutrons","electrons and protons","protons and neutrons","All of the above"],
       "The number of moles of solute present in 1 kg of a solvent is called its":["molality","molarity","normality","formality"],
       "The most electronegative element among the following is":["sodium","bromine","fluorine","oxygen"],
       "The metal used to recover copper from a solution of copper sulphate is":["Na","Ag","Hg","Fe"]
       }
  global score
  score = 0
  key_list = list(d.keys())
  corr_ans_list = ['c','a','c','d']

  for i in range(1,5):
    k = i-1
    q = key_list[k]
    print(f"Question {i}: {q} \n \n \t A: {d.get(q)[0]} \n \n \t B: {d.get(q)[1]} \n \n \t C: {d.get(q)[2]} \n \n \t D: {d.get(q)[3]} \n")

    ans = input("Enter Your Answer [A/B/C/D] : ")
    if ans.lower() == corr_ans_list[k]:
      print("\n Yay! Your Answer Is Correct. \n")
      score += 10
    else:
      print("\n Ohh! Your Answer Is Incorrect. Better Luck Next Time. \n")



def bio_ques():

  d = {"Which of the following is a large blood vessel that carries blood away from the heart?":["Vein","Artery","Capillary","Nerve"],
       "Which blood vessels have the smallest diameter?":["Capillaries","Arterioles","Venules","Lymphatic"],
       "Which of the following is an air-borne disease?":["Measles","Typhoid","Pink eye","None of the above"],
       "Which organ of the body produces the fluid known as bile?":["Liver","Pancreas","Gall bladder","Kidney"]
       }
  global score
  score = 0
  key_list = list(d.keys())
  corr_ans_list = ['b','a','a','a']

  for i in range(1,5):
    k = i-1
    q = key_list[k]
    print(f"Question {i}: {q} \n \n \t A: {d.get(q)[0]} \n \n \t B: {d.get(q)[1]} \n \n \t C: {d.get(q)[2]} \n \n \t D: {d.get(q)[3]} \n")

    ans = input("Enter Your Answer [A/B/C/D] : ")
    if ans.lower() == corr_ans_list[k]:
      print("\n Yay! Your Answer Is Correct. \n")
      score += 10
    else:
      print("\n Ohh! Your Answer Is Incorrect. Better Luck Next Time. \n")


  

def choice():
  print("""Enter:
  '1' For Computer Science
  '2' For Chemistry
  '3' For GK
  '4' For Biology""")
  c = input("\n Enter Your Choice:- ")
  while c not in ['1','2','3','4']:
    print("Please Enter a Valid Input!")
    c = input("Enter Your Choice:- ")
  if c == '1':
    computer_sci_ques()
  elif c == '2':
    chem_ques()

  elif c == '3':
    gk_ques()
  
  elif c == '4':
    bio_ques()
  
  else:
    print("Please Enter a Valid Input!")
    choice()
    
  print(f" \n \n {'='*20} YOUR RESULT IS HERE {'='*20} \n \n")
  print(f"Your Score Is : {score}")
  print("\n")
  c = input("Would You Like To Play Again?")
  if c.lower() == 'yes':
    choice()

  
choice()

