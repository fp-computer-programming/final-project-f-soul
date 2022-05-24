# Jason and Larry 2022 / 5 / 2

import turtle
import random
import time


def selection_checker(number):
    li = ["A", "B", "C", "D", "E", "F"]
    while True:
        selection = input('Your Choice: ').upper()
        if selection in li[0:number]:
            return selection
        else:
            print("You entered an invalid choice,please select again")


print("Start")
difficulties = (input("Choose difficulties (easy/middle/hard): ")[0].lower())


class Player:
  def __init__(self):
    self.name = input("Your name: ")
    self.birthday = input("your birthday(mm/dd): ")
    if difficulties == "e":
      self.it = 1.5
    elif difficulties == "m":
      self.it = 1.35
    elif difficulties == "h":
      self.it = 1.2

  def get_it(self):
    return self.it

  def get_name(self):
    return self.name

  def get_birthday(self):
    return self.birthday


player = Player()

time.sleep(1)
print('_________________________________________________________\nWelcome to Fairfieldprep International Student Simulater, in this program \nyou will play as a freshman and become Grad@Grad \nthrough 48 months of efforts, \nGo Prep!\n _________________________________________________________\n')
time.sleep(1)

def entry_test(difficulties):
  print("Entry Test")

  def diff_e():
      point = 0

      #1
      first = input("37 * 89 = ")  # 3293
      if first == "3293":
            point += 1

      #2
      window = turtle.Screen()
      window.setup(500, 500)        
      window.screensize(500, 500)
      window.title('Secon Question')

      Peter = turtle.Turtle()
      Peter.pendown()
      Peter.forward(160)
      Peter.left(143)
      Peter.forward(200)
      Peter.left(127)
      Peter.forward(120)
      Peter.hideturtle()

      Faye = turtle.Turtle()
      Faye.hideturtle()
      Faye.penup()
      Faye.goto(100, -30)
      Faye.write("12 cm", align='right', font=("Verdana", 15, "normal"))
      Faye.goto(-10, 55)
      Faye.write("9 cm", align='right', font=("Verdana", 15, "normal"))
      second = input("The surface area of this triangle is? ")
      if second[0] + second[1] == "54":
          point += 1
      ext = input("The length of the hypotenuse is? ")
      
    #3
      if ext[0] + ext[1] == "15":
        point += 1
      return point
      window.mainloop()
    
  def diff_m():
    point = 0

    #4
    third = input("x^2 + 4x + 4 = 16 Solve for x (enter the positive answer only): ")
    if third == "2":
      point += 1

    #5
    fourth = input("sin(2\u03c0) = ")
    if fourth == "0":
      point += 1
    #6
    fifth = input("e^0 = ")
    if fifth == "1":
      point += 1
    return point
    
  def diff_h():
    point = 0
    #7
    sixth = input("(no space) d/dx (x^3 + 2x^2 + 3x + 4) = ")
    if sixth == "3x^2+4x+3":
      point += 1
    #8
    seventh = input("(no need for integration constant, no space) \u222b 3x^2 - cos x dx= ")       
    if seventh == "x^3-sinx":
      point += 1

    #9
    eighth = input("Evaluate\n\u03c0/2\n\u222b 2xe^(3x) dx\n0\n")
    if eighth == "-1/2" or eighth == "-0.5":
      point += 1
    return point

  if difficulties == "e":
    points = diff_e()
    score = points / 3
  elif difficulties == "m":
    points = diff_e() + diff_m()
    score = points / 6
  elif difficulties == "h":
    points = diff_e() + diff_m() + diff_h()
    score = points / 9

  print("You score for the entry test is {0:.2f}".format(score * 100))
  if score >= 2 / 3:
    return 1
  elif score >= 1 / 3:
    return 2
  else:
    return 3


et = entry_test(difficulties)


class freshman_class:
  def __init__(self):
    if et == 1:
      self.math = "Algebra 2 Hon"
      self.sci = "Biology Hon"
      self.eng = "English 1"
      self.teo = "Theology 1"
      self.oth = "Speech/Theatre"
      self.ela = "English Lang Art 1"
    elif et == 2:
      self.math = "Algebra 2"
      self.sci = "Biology"
      self.eng = "English 1"
      self.teo = "Theology 1"
      self.oth = "Speech/Theatre"
      self.ela = "English Lang Art 1"
    elif et == 3:
      self.math = "Geometry"
      self.sci = "Biology"
      self.eng = "English 1"
      self.teo = "Theology 1"
      self.oth = "Speech/Theatre"
      self.ela = "English Lang Art 1"

  def get_class(self):
    return [self.math, self.sci, self.eng, self.teo, self.oth, self.ela]


f_class = freshman_class()

print(f_class.get_class())
time.sleep(0.5)
f_class = freshman_class()
class_lst = f_class.get_class()
schedule = ("Day A: \n1st Period {0} \n2nd Period {1} \n3rd Period {2} \n4th Period {3} \n5th Period {4} \n6th Period None \n\nDay B: \n1st Period {1} \n2nd Period {2} \n3rd Period {3} \n4th Period None \n5th Period {5} \n6th Period {0}\n\nDay C: \n1st Period {4} \n2nd Period {5} \n3rd Period None \n4th Period {3} \n5th Period {1} \n6th Period {2} \n\n".format(class_lst[0], class_lst[1], class_lst[2], class_lst[3], class_lst[4], class_lst[5]))
print(schedule)
time.sleep(1)

it = player.get_it()


def gpa_is_lower_than_three(health, pressure, time_usage):
    print("You wants to have a higher GPA.\nA. Spent more time on study, less sleep time.\nB. Not change\n" )
    c_s_1 = selection_checker(3)
    if c_s_1 == "A":
        health -= 1
        pressure -= 0.5
        time_usage += 0.2


def happiness_event(happiness, gpa, sport, club, pressure):
    print("The happiness level is to low, you tried to find something to reduce the pressure.")
    x = random.randint(1, 4)
    if sport == None and club == None:
        print("you went to play tons of computer games")
        gpa -= x * 0.1
        happiness += 2
    if sport != None or club != None:
        print("You got a bunch a good friends to express your pressure")
        happiness += 2
        pressure += 0.5

    return [gpa, happiness, pressure]


def birthday(month, player):
  if player.get_birthday()[0:2] == month:

    print("Happy Birthday, {0}! This is your first birthday at Prep!\n".format(player.get_name()))
    print("_________________________________________________________\n")
    time.sleep(1)
  return True


def first_month(it, et):
    m = "09"
    birthday(m, player)
    print("September, Your first month in FairfieldPrep!")

    print("Do you want to play sport?\nA. No\nB. Soccer\nC. Football\nD. Cross Country\n")
    c_1_0 = selection_checker(4)
    if c_1_0.upper() == "A":
        pressure = 3
        happiness = 5
        sport = None
    else:
        pressure = 5
        happiness = 7
        if c_1_0.upper() == "B":
            sport = "soccer"
        elif c_1_0.upper() == "C":
            sport = "football"
        elif c_1_0.upper() == "D":
            sport = "crosscountry"

    health = 10
    gpa = 4
    time.sleep(1)
    print("How long you plan to study each day this month?\nA. 1-2 Hours B. 2-4 Hours C. More than 4 Hours\n ")
    c_1_1 = selection_checker(3)
    if c_1_1 == "A":
        print("Remeber time you spend will affect your grade")
        pressure += 0.5
        happiness += 0.5
        time_usage = 0.8
    elif c_1_1 == "B":
        print("Good choice")
        happiness -= 0.5
        time_usage = 1.1
    else:
        print("You study hard, but get more sleep man!")
        pressure -= 0.5
        happiness -= 1
        time_usage = 1.4
    if c_1_0 != "A" and c_1_1 == "C":
        health -= 1
        happiness -= 0.5
        print("You are very tired")
    time.sleep(1)
    print(
        "Do you want to join a club?\nA. No\nB. Culture Club\nC. Academic club\n"
    )
    c_1_2 = selection_checker(3)

    if c_1_2 != "A":
      if c_1_2 == "B":
          if c_1_0 != "A":
              club = "culture club"
              print("You don't really have time to do sport and clubs at the same time.")
          else:
              club = "culture club"
              happiness += 0.5
              pressure += 0.2
      elif c_1_2 == "C":
          if c_1_0 != "A":
              club = "academic club"
              print("You don't really have time to do sport and clubs at the same time.")
          else:
              club = "academic club"
              happiness += 0.2
              pressure -= 0.2
      print("You joined the {0}, you meet friends and feel happy, but remember to mange your time well".format(club))
    else:
      club = None
      "You didn't join a club, you have more time, use them well"
      happiness -= 0.5
      pressure -= 0.5

    print("_________________________________________________________\n")
    print("\nLaborday, one day off, you feel happy!\n")
    happiness += 0.5
    print("_________________________________________________________\n")

    time.sleep(1)
    print("Test week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))
    time.sleep(1.5)

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_1 = first_month(it, et)


def second_month(it, gpa, happiness, pressure, health, sport, club, et):
    print( "_________________________________________________________\nOctober, Your second month at Prep!\n")

    time_usage = 0

    if gpa <= 3:
        gpa_is_lower_than_three(health, pressure, time_usage)

    print("How long you plan to study each day this month?\nA. 1-2 Hours B. 2-4 Hours C. More than 4 Hours\n")
    c_2_0 = selection_checker(3)
    if c_2_0 == "A":
        print("Remeber time you spend will affect your grade")
        pressure += 0.5
        happiness += 0.5
        time_usage += 0.8
    elif c_2_0 == "B":
        print("Good choice")
        happiness -= 0.5
        time_usage += 1.1
    else:
        print("You study hard, but get more sleep man!")
        pressure -= 0.5
        happiness -= 1
        time_usage += 1.4

    print("_________________________________________________________\n")
    print("Freshman Rally Day! Take part in the activities in the school. \nBrotherhood starts from this moment!")
    print("_________________________________________________________\n")
    happiness += 2
    pressure -= 0.05

    if happiness <= 3:
        happiness_event(happiness, gpa, sport, club, pressure)

    time.sleep(1)
    print("Test week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))
    time.sleep(1.5)

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_2 = second_month(m_1[0], m_1[1], m_1[2], m_1[3], m_1[4], m_1[5], m_1[6],m_1[7])


def third_month(it, gpa, happiness, pressure, health, sport, club, et):
    time.sleep(1)
    print(" _________________________________________________________\nNovember, Your third month at Prep!\n")
    m = "11"
    birthday(m, player)
    time_usage = 0

    if gpa <= 3:
        gpa_is_lower_than_three(health, pressure, time_usage)

    print("How long you plan to study each day this month?\nA. 1-2 Hours B. 2-4 Hours C. More than 4 Hours\n")
    c_3_0 = selection_checker(3)
    if c_3_0 == "A":
        pressure += 0.5
        happiness += 0.5
        time_usage += 0.8
    elif c_3_0 == "B":
        happiness -= 0.5
        time_usage += 1.1
    else:
        pressure -= 0.5
        happiness -= 1
        time_usage += 1.4

    print("_________________________________________________________\nWould you like to join Kairos Retreat\nA. Yes\nB. No\n")
    c_3_1 = selection_checker(2)
    if c_3_1 == "A":
        print("You and your friends participated in kairos retreat, which increased social practice and friendship.")
        pressure += 0.05
        happiness += 2
        health += 2

    if happiness <= 3:
        happiness_event(happiness, gpa, sport, club, pressure)

    time.sleep(1)
    print(
        "_________________________________________________________\nTest week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))
    time.sleep(1.5)

    #School Mass - All Saints Day

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_3 = third_month(m_2[0], m_2[1], m_2[2], m_2[3], m_2[4], m_2[5], m_2[6],m_2[7])


def fourth_month(it, gpa, happiness, pressure, health, sport, club, et):
    print(" _________________________________________________________\n\nDecember, Your fourth month at Prep!\n")
    m = "12"
    birthday(m, player)
    pressure += 1
    time_usage = 0

    if gpa <= 3:
        gpa_is_lower_than_three(health, pressure, time_usage)

    # Midterm
    print("This is your first midterm exam in FP, how do you want to prepare？\nA. Just pass B. Get ready  C. Do your best\n")
    c_4_0 = selection_checker(3)
    if c_4_0 == "A":
        pressure += 0.5
        happiness += 0.5
        time_usage += 0.8
    elif c_4_0 == "B":
        happiness -= 0.5
        time_usage += 1.1
    else:
        pressure -= 0.5
        happiness -= 1
        time_usage += 1.4

    if happiness <= 3:
        happiness_event(happiness, gpa, sport, club, pressure)

    c_4_1 = input("_________________________________________________________\nChristmas holiday is coming. What do you want to do?\n: ")
    print("Enjoy your holiday")
    happiness += 1

    time.sleep(0.5)
    print("_________________________________________________________\nTest week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))
    time.sleep(1.5)

    #School Mass - Immaculate Conception

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_4 = fourth_month(m_3[0], m_3[1], m_3[2], m_3[3], m_3[4], m_3[5], m_3[6], m_3[7])


def fifth_month(it, gpa, happiness, pressure, health, sport, club, et):
    print(" _________________________________________________________\nJanuary, your fifth month at Prep!\n")
    m = "01"
    birthday(m, player)
    time_usage = 0

    if gpa <= 3:
        gpa_is_lower_than_three(health, pressure, time_usage)

    print("How long you plan to study each day this month?\nA. 1-2 Hours B. 2-4 Hours C. More than 4 Hours\n")
    c_5_0 = selection_checker(3)
    if c_5_0 == "A":
        pressure += 0.5
        happiness += 0.5
        time_usage += 0.8
    elif c_5_0 == "B":
        happiness -= 0.5
        time_usage += 1.1
    else:
        pressure -= 0.5
        happiness -= 1
        time_usage += 1.4

    c_5_1 = input("_________________________________________________________\nLearn about Martin Luther King's ideas and the equal rights movement\nA. OK \nPlease selection: ").upper()
    if c_5_1 == "A":
        pressure -= 0.05
        time_usage += 0.1
    else:
        print("You give up a good opportunity to study human rights")

    if happiness <= 3:
        happiness_event(happiness, gpa, sport, club, pressure)

    time.sleep(0.5)
    print("_________________________________________________________\nTest week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))
    time.sleep(1.5)

    #School Mass - All Saints Day

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_5 = fifth_month(m_4[0], m_4[1], m_4[2], m_4[3], m_4[4], m_4[5], m_4[6],m_4[7])


def sixth_month(it, gpa, happiness, pressure, health, sport, club, et):
    print(" _________________________________________________________\nFebruary, your sixth month at Prep!\n")
    m = "02"
    birthday(m, player)
    time_usage = 0

    if gpa <= 3:
        gpa_is_lower_than_three(health, pressure, time_usage)

    print( "How long you plan to study each day this month?\nA. 1-2 Hours B. 2-4 Hours C. More than 4 Hours\n")
    c_6_0 = selection_checker(3)
    if c_6_0 == "A":
        pressure += 0.5
        happiness += 0.5
        time_usage += 0.8
    elif c_6_0 == "B":
        happiness -= 0.5
        time_usage += 1.1
    else:
        pressure -= 0.5
        happiness -= 1
        time_usage += 1.4

    print("Would you like to join Chinese New Year Celebration?\nA. Yes\nB. No\n")
    c_6_1 = selection_checker(2)
    if c_6_1 == "A":
        pressure += 0.05
        happiness += 2
        health += 2

    if happiness <= 3:
        happiness_event(happiness, gpa, sport, club, pressure)

    time.sleep(0.5)
    print("_________________________________________________________\nTest week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))
    time.sleep(1.5)

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_6 = sixth_month(m_5[0], m_5[1], m_5[2], m_5[3], m_5[4], m_5[5], m_5[6],m_5[7])


def seventh_month(it, gpa, happiness, pressure, health, sport, club, et):
    print(" _________________________________________________________\nMarch, your seventh month at Prep!\n")
    m = "03"
    birthday(m, player)
    time_usage = 0

    if gpa <= 3:
        gpa_is_lower_than_three(health, pressure, time_usage)

    print( "How long you plan to study each day this month?\nA. 1-2 Hours B. 2-4 Hours C. More than 4 Hours\n")
    c_7_0 = selection_checker(3)
    if c_7_0 == "A":
        pressure += 0.5
        happiness += 0.5
        time_usage += 0.8
    elif c_7_0 == "B":
        happiness -= 0.5
        time_usage += 1.1
    else:
        pressure -= 0.5
        happiness -= 1
        time_usage += 1.4

    print("\nFreshman Retreat Overnight! \nA. Keep cheerful and humorous\nB. Keep subdued and reflective\n")
    c_7_1 = selection_checker(2)
    if c_7_1 == "A":
        pressure += 0.02
        happiness += 2
        health += 1
    elif c_7_1 == "B":
        pressure -= 0.02
        health += 1
        happiness += 1
        time_usage += 0.05

    if happiness <= 3:
        happiness_event(happiness, gpa, sport, club, pressure)

    time.sleep(0.5)
    print("_________________________________________________________\nTest week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))
    time.sleep(1.5)

    #School Mass - All Saints Day

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_7 = seventh_month(m_6[0], m_6[1], m_6[2], m_6[3], m_6[4], m_6[5], m_6[6],m_6[7])


def eight_month(it, gpa, happiness, pressure, health, sport, club, et):
    print(" _________________________________________________________\nApril, your eighth month at Prep!\n")
    m = "04"
    birthday(m, player)
    time_usage = 0

    if gpa <= 3:
        gpa_is_lower_than_three(health, pressure, time_usage)

    print("How long you plan to study each day this month?\nA. 1-2 Hours B. 2-4 Hours C. More than 4 Hours ")
    c_8_0 = selection_checker(3)
    if c_8_0 == "A":
        pressure += 0.5
        happiness += 0.5
        time_usage += 0.8
    elif c_8_0 == "B":
        happiness -= 0.5
        time_usage += 1.1
    else:
        pressure -= 0.5
        happiness -= 1
        time_usage += 1.4

    print("\nWhat do you want to do during the spring break after Easter? \nA. Go out for sports and go to parties with friends\nB. Go out for a picnic with family or friends\n")
    c_8_1 = selection_checker(2)
    if c_8_1 == "A":
        pressure += 0.05
        happiness += 1
        health += 2
    elif c_8_1 == "B":
        pressure -= 0.05
        health += 1
        happiness += 1
        time_usage += 0.05

    if happiness <= 3:
        happiness_event(happiness, gpa, sport, club, pressure)

    time.sleep(0.5)
    print("_________________________________________________________\nTest week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))
    time.sleep(1.5)

    #School Mass - All Saints Day

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_8 = eight_month(m_7[0], m_7[1], m_7[2], m_7[3], m_7[4], m_7[5], m_7[6],
                  m_7[7])


def ninth_month(it, gpa, happiness, pressure, health, sport, club, et):
    print( " _________________________________________________________\nMay, your last full month at Prep!\n")
    m = "05"
    birthday(m, player)
    pressure += 1
    time_usage = 0

    if gpa <= 3:
        gpa_is_lower_than_three(health, pressure, time_usage)

    print("How long you plan to study each day this month?\nA. 1-2 Hours B. 2-4 Hours C. More than 4 Hours\n")
    c_9_0 = selection_checker(3)
    if c_9_0 == "A":
        pressure += 0.5
        happiness += 0.5
        time_usage += 0.8
    elif c_9_0 == "B":
        happiness -= 0.5
        time_usage += 1.1
    else:
        pressure -= 0.5
        happiness -= 1
        time_usage += 1.4
        it += 0.01

    c_9_1 = input( "\nDo you want to review in the last month before the exam? It will be very tired, but believe it's worth it \nA. Just Pass\nB. Review hard\nC. Do my best！\n")
    if c_9_1 == "A":
        pressure += 0.05

    elif c_9_1 == "B":
        pressure -= 0.05
        time_usage += 0.05
    elif c_9_1 == "C":
        pressure -= 0.5
        health -= 1
        time_usage += 0.05

    if happiness <= 3:
        happiness_event(happiness, gpa, sport, club, pressure)

    time.sleep(0.5)
    print("_________________________________________________________\nTest week")
    loss = random.randint(0, 10) / time_usage
    test_score = (100 - loss)
    print("Your test score is {:.2f}".format(test_score))
    gpa = 4.0 - pressure / 10 * (loss / 10) / (it * time_usage)
    if et >= 2 / 3:
        gpa += 0.1
    print("Your GPA is {:.2f}".format(gpa))

    if gpa >= 3.8:
        print("WOW, you ended the year fantastically. Keep up the good work.")
    elif gpa >= 3.6:
        print("You did very well, and you can certainlly do better!")
    elif gpa >= 3.4:
        print("Good work, put in more efforts and you can be better!")
    else:
        print("You haven't tried your best, be better next year!")

    #School Mass - All Saints Day

    return [it, gpa, happiness, pressure, health, sport, club, et]


m_9 = ninth_month(m_8[0], m_8[1], m_8[2], m_8[3], m_8[4], m_8[5], m_8[6], m_8[7])
