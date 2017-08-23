print "Quiz Start! Please select easy, medium or hard mode by typing EASY, MEDIUM, or HARD"
level = raw_input("")

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

def easylvl3():
    print "EASY LEVEL 3"
    print '''Python Specifics:
    1. Python syntax for prompting for input: <variable> = [input1]
    2. Python syntax for looping through each item in a list is: [input2] <expression> [input3] <list>
    3. Adding things to list syntax is: <list>.[input4]'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    list_one = ["raw_input("")", "raw_input()", "raw_input"]
    list_two = ["for"]
    list_three = ["in"]
    list_four = ["append", ".append", ".append()", "append()"]
    if (input1 in list_one) and (input2 in list_two) and (input3 in list_three) and (input4 in list_four):
        print "CONGRATS!"
    else:
        print "One of the inputs is wrong. Try again"
        easylvl3()

def mediumlvl3():
    print "MEDIUM LEVEL 3"
    print '''Python Specifics:
    1. Python syntax for prompting for input: <variable> = [input1]
    2. Python syntax for looping through each item in a list is: [input2] <expression> [input3] <list>
    3. Adding things to list syntax is: <list>.[input4]'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    list_one = ["raw_input("")", "raw_input()", "raw_input"]
    list_two = ["for"]
    list_three = ["in"]
    list_four = ["append", ".append", ".append()", "append()"]
    if (input1 in list_one) and (input2 in list_two) and (input3 in list_three) and (input4 in list_four):
        print "CONGRATS!"
    else:
        print "One of the inputs is wrong. Try again"
        mediumlvl3()

def hardlvl3():
    print "HARD LEVEL 3"
    print '''Python Specifics:
    1. Python syntax for prompting for input: <variable> = [input1]
    2. Python syntax for looping through each item in a list is: [input2] <expression> [input3] <list>
    3. Adding things to list syntax is: <list>.[input4]'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    list_one = ["raw_input("")", "raw_input()", "raw_input"]
    list_two = ["for"]
    list_three = ["in"]
    list_four = ["append", ".append", ".append()", "append()"]
    if (input1 in list_one) and (input2 in list_two) and (input3 in list_three) and (input4 in list_four):
        print "CONGRATS!"
    else:
        print "One of the inputs is wrong. Try again"
        hardlvl3()

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

def easylvl2():
    print "EASY LEVEL 2"
    print '''Solving exercises:
    1. Identify the [input1] and [input2].
    2. Think how a person would do the exercise [input3]
    3. [input4]code (it also helps to solve the simpler exercise then add in sublties)
    4. Code'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    list_one = ["inputs", "outputs", "input", "output"]
    list_two = ["manually", "mechanically"]
    list_three = ["Pseudo", "pseudo"]
    if (input1 in list_one) and (input2 in list_one) and (input3 in list_two) and (input4 in list_three):
        easylvl3()
    else:
        print "One of the inputs is wrong. Try again"
        easylvl2()

def mediumlvl2():
    print "MEDIUM LEVEL 2"
    print '''Solving exercises:
    1. Identify the [input1] and [input2].
    2. Think how a person would do the exercise [input3]
    3. [input4]code (it also helps to solve the simpler exercise then add in sublties)
    4. Code'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    list_one = ["inputs", "outputs", "input", "output"]
    list_two = ["manually", "mechanically"]
    list_three = ["Pseudo", "pseudo"]
    if (input1 in list_one) and (input2 in list_one) and (input3 in list_two) and (input4 in list_three):
        mediumlvl3()
    else:
        print "One of the inputs is wrong. Try again"
        mediumlvl2()

def hardlvl2():
    print "HARD LEVEL 2"
    print '''Solving exercises:
    1. Identify the [input1] and [input2].
    2. Think how a person would do the exercise [input3]
    3. [input4]code (it also helps to solve the simpler exercise then add in sublties)
    4. Code'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    list_one = ["inputs", "outputs", "input", "output"]
    list_two = ["manually", "mechanically"]
    list_three = ["Pseudo", "pseudo"]
    if (input1 in list_one) and (input2 in list_one) and (input3 in list_two) and (input4 in list_three):
        hardlvl3()
    else:
        print "One of the inputs is wrong. Try again"
        hardlvl2()

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

def easylvl1():
    print "EASY LEVEL 1"
    print '''Command Line Refresh:
    The syntax for displaying the current drive location is [input1].
    The syntax for changing the drive location is [input2].
    The syntax for running a python file is [input3]
    The syntax for making a new file is [input4]'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    if input1 == "pwd" and input2 == "cd" and input3 == "python" and input4 == "touch":
        easylvl2()
    else:
        print "One of the inputs is wrong. Try again"
        easylvl1()

def mediumlvl1():
    print "MEDIUM LEVEL 1"
    print '''Command Line Refresh:
    The syntax for displaying the current drive location is [input1].
    The syntax for changing the drive location is [input2].
    The syntax for running a python file is [input3]
    The syntax for making a new file is [input4]'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    if input1 == "pwd" and input2 == "cd" and input3 == "python" and input4 == "touch":
        mediumlvl2()
    else:
        print "One of the inputs is wrong. Try again"
        mediumlvl1()

def hardlvl1():
    print "HARD LEVEL 1"
    print '''Command Line Refresh:
    The syntax for displaying the current drive location is [input1].
    The syntax for changing the drive location is [input2].
    The syntax for running a python file is [input3]
    The syntax for making a new file is [input4]'''
    input1 = raw_input("enter input1")
    input2 = raw_input("enter input2")
    input3 = raw_input("enter input3")
    input4 = raw_input("enter input4")
    if input1 == "pwd" and input2 == "cd" and input3 == "python" and input4 == "touch":
        hardlvl2()
    else:
        print "One of the inputs is wrong. Try again"
        hardlvl1()

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

def level_selector(level):
    if level == "EASY":
        easylvl1()
    elif level == "MEDIUM":
        mediumlvl1()
    elif level == "HARD":
        hardlvl1()
    else:
        print "Error! Please enter EASY MEDIUM or HARD"
        level = raw_input("")
        level_selector(level)

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

level_selector(level)
