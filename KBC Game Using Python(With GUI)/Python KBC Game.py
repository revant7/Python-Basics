####importing required modules
import sys
import time
import random
import datetime as dt
import pytz
####infinite while loop for continuous running of game
while True:
  name = input('Enter Your Name: ') #name input from user 
  print() #for leaving a line just for good look of game
  print('~'*40,'GAME - Online KBC','~'*40)
  print()
  print(f'{name}, Welcome To Online KBC Python Game!')  
  print()
  print("""Rules Of The Game : 

    1. 10 Points Will Be Awarded For Each Correct Answer.

    2. 5 Points Will Be Deducted For Every Incorrect Answer.

    3. There Are Total Of 10 Questions In This Game.

    5. All Questions Will Be Multiple Choice With Single Correct Answer.

    6. There Will Be A Time Limit Of 10 Minutes For The Full Game.

    7. No Particular Time Limit Is There For A Paricular Question.

    8. After The Game Will Be Finished, Your Result Will Be Displayed On The Screen.
    
    NOTE:- You Will Win If Your Score Is Above 60.
    
    """)
  print()
  a = input(f'{name}, Are You Ready To Play The Game ? [yes/no] ')
  
  while a.lower() not in ['yes','no']:
    a = input(f'{name}, Are You Ready To Play The Game ? [yes/no] ')
  if a.lower() == 'no':
    break

  print()
  print(f'  {name}, All The Best For The Game!!!    ')
  print()
  
  initial = time.time() ####initial time noted 
  start_t = dt.datetime.now(pytz.timezone('Asia/Kolkata')) ####time when game started

  print(f"{name}, You Started The Game At : {start_t}")
  print()

  score = 0 #### initialising user score 
  ques = 20 ##### total ques

  #### dictionary of all questions.
  q_dict = {'Which of these sounds would you associate with the heart?':['Tring Tring','Tap Tap','Click Click','Dhak Dhak'],
            'Who is the \' Bharat Ka Veer Putra \' Aaccording to the title of a 2013 TV Series?':['Tipu Sultan','Chandragupta Maurya','Maharana Pratap','Ashoka'],
            'In 2013, where did the natural calamity known as Himalayan tsunami occur?':['Uttrakhand','Arunachal Pradesh','Jammu and Kashmir','Sikkim'],
            'Who is the only leader to be elected Prime Minister of Pakistan three times?':['Syed Yousaf Raza Gillani','Benazir Bhutto','Liaqat Ali Khan','Nawaz Sharif'],
            'Which of these persons has not walked on the Moon?':['Charles Duke','James A Lovell','Alan Bean','Pete Conrad'],
            'Which team retained the ashes Trophy in 2013?':['Australia','South Africa','West Indies','England'],
            'With Which of these cards would you associate the phrase "Aam Aadmi ka Adhikaar"?':['PAN Card','Voter ID Card','AADHAR Card','Ration Card'],
            'Which of these words or phrases was famously used in many of his dialogues by actor Pran?':['Khamosh','Barkhurdaar','Jaani','Babu Moshai'],
            'With Which of these states do Chhattisgarh, Jharkhand and Andhra Pradesh all share their borders?':['Madhya Pradesh','Odisha','Bihar','Uttar Pradesh'],
            "On a restaurant menu, which of these items is often listed as 'Jeera', 'Curd', 'Boiled' or 'Fried'?":['Manchurian','Burger','Rice','Pasta'],
            "Which of the following corresponds to ‘ek bataa do’?":['Pura','Sawa','Adha','Pauna'],
            "In the game of ludo the discs or tokens are of how many colours?":['One','Two','Three','Four'],
            "Starting with the earliest, the First event in Narendra Modi’s life is?":['CM of Gujarat','Took oath as','Joined BJP','Became RSS Pracharak'],
            "The International Literacy Day is observed on":['Sep 8','Nov 28','May 2','Sep 22'],
            "The language of Lakshadweep. a Union Territory of India, is":['Tamil','Hindi','Malayalam','Telugu'],
            "In which group of places the Kumbha Mela is held every twelve years?":['Ujjain. Purl; Prayag. Haridwar','Prayag. Haridwar, Ujjain,. Nasik','Rameshwaram. Purl, Badrinath. Dwarika','Chittakoot, Ujjain, Prayag,Haridwar'],
            "Bahubali festival is related to":['Islam','Hinduism','Buddhism','Jainism'],
            "Which day is observed as the World Standards  Day?":['June 26','Oct 14','Nov 15','Dec 2'],
            "Which Day Is celebrated as Valentine's Day?":['2 Feb','7 Feb','14 Feb','21 Feb'],
            "September 27 is celebrated every year as":['Teachers Day','National Integration Day','World Tourism Day','International Literacy Day']
            }
  #### list of correct answers
  corr_ans = ['D','C','A','D','B','D','C','B','B','C','C','D','D','A','C','B','D','B','C','C']

  l = [i for i in range(0,20)]
  #### list of all ques.
  q_list = list(q_dict)
  #### empty list for storing 10 random ques from all 20 ques.
  sel_q_list = []
  print()
  #### using for loop, printing all 10 randomly selected ques. one by one and asking user for ans inp.
  for i in range(1,11):
    b = random.choice(l)
    while q_list[b] in sel_q_list:
      b = random.choice(l)
    c = q_list[b]
    index = l.index(b)
    #### apending the index of selec. ques. in sel_q_list for further refer. 
    sel_q_list.append(c)
    temp_1 = q_list[index]
    #### printing questions and thier resp. options.
    print(f'Question {i}. {c} \n  \n A: {q_dict.get(c)[0]} \n B: {q_dict.get(c)[1]} \n C: {q_dict.get(c)[2]} \n D: {q_dict.get(c)[3]}')
    print()
    #### geting answer from user
    ans = input('Enter Your Answer: [A/B/C/D] : ')
    ans = ans.upper()
    #### using while loop to check that user have entered the desired input.
    while ans not in ['A','B','C','D']:
      print()
      print("Please Enter a Valid Input!!!")
      print()
      ans = input('Enter Your Answer: [A/B/C/D] : ')
    print()
    #### checking if user have entered the corr_ans or not.
    if ans == corr_ans[q_list.index(c)]:
      print('Yay! Your Answer Is Correct.')
      print()
      score += 10 #incres. score by 10  for every corr ans.

    else:
      print('Ohh, Your Answer Is Incorrect. Better Luck Next Time.')
      print()
      score -= 5 #decreas. score for every incorr ans.
#### declaring result ####
  if score > 60:
    temp_2 = 'Congratulations! You Won The Game.'
    em = ":)"
  else:
    temp_2 = 'Sorry, You Loose The Game Better Luck Next Time.'
    em = ':('

  final = time.time()
  end_t = dt.datetime.now(pytz.timezone('Asia/Kolkata'))
  print()
  print('~'*40,'YOUR RESULT IS HERE','~'*40)
  print(f"""
    Your Total Score Is : {score}

    Your Result Is : {temp_2}

    Your Emoji Is : {em}

    You Started The Game At : {start_t}

    You Completed The Game At : {end_t}

    Total Time Taken For The Game : {round(final - initial,2)} Seconds 

    Thanks For Playing! Visit Us Again Soon.
  """)
  print()
  print()
#### printing the 10 questions and thier correct ans for usr reference.
  print('~'*40,'ALL QUESTIONS AND THIER CORRECT ANSWERS','~'*40)
  print()
  print()

  for i in sel_q_list:
    for j in q_list:
      if j == i:
        index_of_q_resp_q_list = q_list.index(i)
        break
    print(f'Question {sel_q_list.index(i) + 1}. {i} \n  \n A: {q_dict.get(i)[0]} \n B: {q_dict.get(i)[1]} \n C: {q_dict.get(i)[2]} \n D: {q_dict.get(i)[3]}')
    print()
    print(f'The Correct Answer For This Question Is Option : {corr_ans[index_of_q_resp_q_list]}')
    print()
#### asking if user wants to play again, loop continue else it break game, game will end.
  print("""
            Created By:- Revant Khanna
            Class:- XII
            Section:- F
            St. Andrews Scotts Senior Secondary School""")
  print()
  again = input("Do You Want To Play The Game Again? [yes/no]")
  while again.lower() not in ['yes','no']:
    print()
    print('Please Enter A Valid Input!!!')
    again = input("Do You Want To Play The Game Again? [yes/no]")
    print()
  if again.lower() == 'yes':
    continue
  else:
    break
######################################################## CODE COMPLETED #############################################################
############### MADE BY:- Revant Khanna XII-F ##########
######### --------- Thank You ---------- ##################


