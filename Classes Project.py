#!/usr/bin/env python
# coding: utf-8

# ## Classes Project -- Student Information System

# #### Introduction:
# 
# At Lawrenceville, there are three main computer systems that we utilize, to manage all the business of the school:
# 
# - Canvas... our Learning Management System (LMS), which is written in Ruby on Rails.
# - Blackbaud... our Client Management Sytem (CMS), which handles all the financial information for the school.  Couldn't figure out what it's written in.
# - Veracross - our Student Information System (SMS), which is written in a combination of Javascript, Python, and SQL.
# 
# The purpose of an SIS is to store all the information about the students, parents, and employees that are related to the school.  Large database systems that involve specialized data types (like employees or parents or students) are almost always written using Object-Oriented programming (i.e. classes) because you can tailor each object to the information being stored.  For instance, you don't need to collect and store the same information about a parent as you do a student or an employee.  You can also create additional objects for anything else you might need to store, like grades, transcripts, etc.
# 
# #### The Task:
# 
# Your task for this project is to create an SIS for a school.  Don't worry--you don't need to create a complete one, as that would take months even working together.  But we do want to build the basic pieces that one would need to have students in a school taking classes and recording grades.  
# 
# #### The Details:
# 
# For this task you will create three different classes and an interface that will allow the user to interact with them.  Listed below are the minimum requirements for the different classes.  You are free to build them out, adding other attributes and/or methods as you have time. Here are the classes you will need to create:
# 
# <u>#1 - Grade:</u>  This class should have at least three attributes, one to hold the letter grade, one to hold the course the grade was earned in, and one for the term that it was earned in.  It should also have one method that converts the grade to its GPA equivalent.
# 
# <u>#2 - Student:</u>  This class should have the following attributes plus any others you wish to add:
# 
# - sid = student sid 
# - last = last name
# - first = first name
# - address = their address
# - form = what form they are in
# - house = what House they are in
# - email = should actually be a property that is created dynamically as we did in class
# - course_dict = starts out as an empty dictionary that can be filled later.  We aren't going to create a class object called course (unless you have time and want to!) so entries in this dictionary can be as simple as the period as the key and the course name as a string for the value.  Something like {"C":"MA564: Advanced Python", "A":"VA440: Ceramics", etc.}, for example.
# - grade_list = starts out as an empty list that can be filled later with Grade objects.
# 
# The Student class should also have the following methods plus any more that you want to add:
# 
# - add_course... adds a course to the their course list.  You will obviously need to feed it the period and the course.
# 
# - drop course... should list off all their courses and allow the user to delete one.
# 
# - calculate_GPA... should go through all the Grade objects in the grade_list and calculate an overall GPA.
# 
# - change_info... allows the user to change the address, first name, or last name.
# 
# - a string operator that prints out the student name, form, and House.
# 
# - enter_grades... loops through course_dict and allows the student to enter a grade for each course.
# 
# 
# <u>#3 School:</u> This class holds all the students for your school.  It only needs four attributes - the school name (i.e. "Lawrenceville"), the current term (T1, T2 or T3), the school year (like 2023), and a dictionary of students, which starts out empty.  This class should have at least three methods:
# 
# - add_student = adds the student object the dictionary, with id as the key and the student object as the value
# 
# - remove_student = removes the student from the student dictionary
# 
# - print_students = loops through the student dictioanry and prints their id, name, email, and House
# 
# - set_term = this should be a property (so not exactly a method) and will return something like "Fall 2023" if the term is T1 and the year is 2023.
# 
# Once you have those three classes created and working, your final task is to create an interface that allows the user to interact with these three classes.  Your main interface should either load (if you want to attempt some pickling!) or create a school class and allow the user to add students to the dictionary and run any of the School methods.  It allow you should also let you access a second menu that allows you to access all the methods of the student class, like adding a course, entering grades, etc.  
# 
# #### Miscellaneous Details:
# 
# - You will have 3 days in class (including one long-block class) plus 4 nights of homework to complete this project.  The project is due on Tuesday, April 4th.  After the 4th, there will be 5% late penalty for each day the project is late.  If more time is needed as a class (first time doing this project!) we can make those adjustments in the syllabus.
# 
# - Grading will be based on the rubric provided in class.  
# 
# - I strongly suggest that you build each class (any order) and thoroughly test them before you move on to the next class.  Do them in different cells of a notebook so that you know each portion works.  The interface will likely take the most work, so save that for last.
# 
# - Make sure that your code is well documented and commented, particularly those portions that you add that are not part of the original assignment!

# In[1]:


# creating the Grade class to store Grade objects. Useful for the enter_grades method of the Student class (below).
class Grade: 
    # the three attributes of the Grade class are:
    # letter_grade = the letter grade the student recieved as a string (ie. 'A-')
    # course = the name of the course as a string (ie. 'MA564: Advanced Python')
    # term = the trimester as a string (ie. 'T3')
    def __init__(self, letter_grade, course, term):
        self.letter_grade = letter_grade
        self.course = course
        self.term = term
    
# method that converts the letter grade to numerical equivalent. Useful for the calculate_GPA method of Student class.
    def grade_converter(self):
        my_dict = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 
               'D+': 1.3, 'D': 1.0, 'D-': 0.7} 
        return my_dict[self.letter_grade]

# testing out the Grade class through example Grade objects!
g1 = Grade('A+', 'MA564: Advanced Python', 'T3')
print(g1.letter_grade)
print(g1.course)
print(g1.term)
print(g1.grade_converter())


# In[2]:


# importing datetime to get the current year. Useful to get graduation year (given a student's form) and consequently
# useful for creating a student's email. 
import datetime 

# The Student class stores basic information about the student. Explanations of Student class attributes below: 
class Student: 
    def __init__(self, sid, last, first, address, form, house):
        self.sid = sid ## sid = the student's student id, which is a five digit integer with no spaces (ie. 99853).
        self.last = last ## last = the student last name aas a string (ie. 'García').
        self.first = first ## first = the student's first name (ie. 'Jamie').
        self.address = address ## address = the student's address as a string (ie. '10 Main Street').
        self.form = form ## form = the student's form as an integer between 2 and 5, inclusive. 
        self.house = house ## house = the house in which the student resides, as a string. 
        self.course_dict = {} ## initializing an empty course_dict to be filled later. 
        # The keys of course_dict will be the course's period as a string and value will be course name, as a string. 
        self.grade_list = [] # initializing an empty grade_list to be filled later with Grade class objects. 
        self.community_service_dict = {} ## initializing an empty community_service_dict 
        #to be filled later. The number of one time event's (OTE's) the student has completed
        #will be the dictionary's key; the number of Lawrenceville Community Action Project's (LCAP's)
        # the student has completed will be the dictionary's value. Both keys/values are integers. 
        
    # email is a property that is created dynamically and returns the student's email based on first/last name & form
    @property 
    def email(self):
        dt = datetime.datetime.now()
        curr_year = dt.year ## curr_year holds the current year
        grad_year = curr_year - self.form + 5 # way to get the graduation year from the form
        return f'{self.first[0].lower()}{self.last.lower()}{int(str(grad_year)[-2:])}@lawrenceville.org' 
    # obtained last two digits of grad_year by acessing its two indices. 

    def add_course(self, period, course):#method that adds a course for a student based on period and course name
        self.course_dict[period] = course# course dict(initially empty) now includes period as key & course as value

    def drop_course(self, course_period): #method that drops a course for a student based on period
        if len(self.course_dict) != 0: ## checks to see if the course dict is empty (ie. no courses inputted)
            del self.course_dict[course_period]
            print('\n')
            print(f'\033[1mCourse successfully dropped for your desired student!\033[0m') # prints bolded!
        else: ## ie if len(self.course_dict) is 0 -- that is, the user never added a course.
            print(f'\033[1mCannot drop course if course was never added.\033[0m')
            
            
    def calculate_GPA(self):# method that calculates the student's GPA based on inputted classes and inputted grades
        num_classes = 0
        grade_total = 0
        if len(self.grade_list)!=0: ## grade_list contains grade objects -- see enter_grades method below
            for i in self.grade_list: 
                grade_total += i.grade_converter() ## accessing grade_converter() method of Grade class!
                num_classes+=1
            return (grade_total/num_classes) 
        else: ## ie if the grade_list is empty becuase no grades were inputted
            print(f'\033[1mNo classes to calculate_GPA for because no grades were inputted by the user.\033[0m') 

    def change_info(self, attribute_to_be_changed, what_to_be_changed_to): 
        #the change_info method changes an attribute based on what the user wants ie.user can change student's name).
        setattr(self, attribute_to_be_changed, what_to_be_changed_to)
        # note that I recieved help from the following link: https://www.programiz.com/python-programming/methods/built-in/setattr
        # essentially, that website introduced me to the setattr() function, where the inputs are self
        ## the desired attribute to be changed (name), and what the user wants to change it to (value). 
        ## this seemed pretty intuitive, especially given our study of getattr(); rather than getting/obtaining
        ## the attribute though, we are (re)setting it!!

    def __str__(self): ## defining a string operator -- that is, how class is printed. Prints name, form, and house:
        if self.form == 2: ## if second former, returns '2nd form'
            return f'{self.first} {self.last} is in the {self.form}nd form and in {self.house} house.'
        elif self.form == 3: ## if third former, returns '3rd form'
            return f'{self.first} {self.last} is in the {self.form}rd form and in {self.house} house.'
        else: ## if fourth or fifth former, returns 'th' form (ie. 4th form, 5th form)
            return f'{self.first} {self.last} is in the {self.form}th form and in {self.house} house.'

    def enter_grades(self):#method that allows the user to input grades for the classes they've added ; 
        # handles error of user trying to add grades for a free period.
        while True:
                free_period = input('Enter the free period of the student(A,B,C,D,E, or F):')
                if free_period not in ['A', 'B', 'C', 'D', 'E', 'F']: ## handles error of invalid free period entry
                    print(f'\033[1mInvalid free period entry. Please try again!\033[0m') 
                else: ## ie if valid free_period entry
                    break
        if len(self.course_dict)!=0: ## that is, if courses exist 
            for key, value in self.course_dict.items(): # key = period; value = course name
                if key!=free_period:
                    while True:#continues until user enters a valid grade they recieved in the courses that they inputted
                        letter_grade_inp = input(f'Enter the LETTER grade the student recieved during their {key} period class, which was {value}:')
                        if letter_grade_inp.upper() not in ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']:
                            print(f'\033[1mInvalid letter grade. Please try again!\033[0m') 
                        else:
                            break # if the user inputs a valid letter grade entry, the while loop breaks
                    while True: # continues until user enters a valid term in which they recieved said grade. 
                        term = input('Enter the term for which the student received said grade (T1, T2, or T3):')
                        if term.upper() not in ['T1', 'T2', 'T3']:
                            print(f'\033[1mInvalid term entry. Please try again!\033[0m') 
                        else:
                            break
                    g1 = Grade(letter_grade_inp, value, term) ## creating grade object with appropriate attributes
                    self.grade_list.append(g1) ## grade_list is a list of grade objects
                    print('\n')
                    print(f'\033[1mGrades successfully added for your desired student!\033[0m')
                elif key == free_period: ## error handling the niche the case where the user 
                    #wants to enter_grade for a period that they already claimed was their free period
                    print(f'\033[1mCannot enter a grade for the free period of the student.\033[0m')
        else: ## ie. if len(self.course_dict)==0 -- that is, the user never inputted any courses
            print(f'\033[1mCannot enter grades because the user failed to input any classes.\033[0m')
            
            
    def community_service(self):#community_service is a method beyond project requirements, providing additional
        #additional information regarding community service; it not relays whether or not the student has fufilled 
        #their graduation requirements, and if not, it explicitly lets the user what is needs to complete to graduate.
        while True:
            try:#using try/except because num_otes/num_lcaps inputs need to be integers (ie.'pizza' would throw error)
                num_otes = int(input('How many OTEs does the student have?'))
                num_lcaps = int(input('How many LCAPS does the student have?'))
                self.community_service_dict[num_otes] = num_lcaps#num_otes=key&num_lcaps=value in comm service dict.
                for key, value in self.community_service_dict.items():
                    if key>=3 and value>=1:#if OTES at least 3 and LCAPS at least 1, the student fufilled their reqs.
                        print('The student has fufilled their graduation requirements!')
                    elif 0<=key<=3 and 0<=value<=1:
                        print(f'The student still needs {3-num_otes} OTEs and {1-num_lcaps} LCAPS to graduate.')  
                    elif 0<=key<3 and value>1:
                        print(f'The student still needs {3-num_otes} OTEs to graduate.')
                    elif key>=3 and value == 0:
                        print(f' The student still needs {1-num_lcaps} LCAPS to graduate.')
                    else:#this takes care of the case of negative inputs (ie. num_lcaps = -5), which isn't sensible
                        print('Invalid input for number of OTEs or number of LCAPS. Please try again!') 
                break 
            except: ## print statement below runs if the user enters a non-integer for their lcap/ote inputs
                print('Invalid input for number of OTEs or number of LCAPS. Please try again!')
            ## the above while loop will run until the user enters a valid input for num of OTEs/LCAPS
        


# In[3]:


# ## testing out the Student class through an example Student object (instance)!
s1 = Student(78910, 'Hahami', 'Ely', '57 Robbins Drive', 5, 'Kennedy')
print(s1.sid)
print(s1.last)
print(s1.first)
print(s1.address)
print(s1.form)
print(s1.house)
print(s1.email)
print(s1.course_dict)
print(s1.grade_list)
# print(s1.enter_grades())
# #adding my course schedule as an example: 
# s1.add_course('A', 'IN512: Heuristics')
# s1.add_course('B', 'SC553: Honors Physics / Mechanics and Theory')
# s1.add_course('C', 'MA564: Advanced Python')
# s1.add_course('D', 'MA537: Honors Math Seminar: Differential Equations')
# s1.add_course('E', 'BS101: Course to Be Dropped')
# s1.add_course('F', 'HI553: Honors Economics')
# s1.calculate_GPA()
# s1.community_service()
# print(s1.course_dict)
# s1.drop_course('E')
# print(s1.course_dict) ##prints everything as before, but updating to delete E period class (BS101)
# s1.enter_grades() ## allows user to enter grades
# print(s1.grade_list)
# s1.calculate_GPA()
# print(s1) ## testing to see if __str__ (ie. the string operator) is working
# s1.change_info('address', '8 Percheron Lane')
# print(s1.first) #shows that since we did not change/update the first name attribute, it stays the same of value 'Ely'
# print(s1.last)
# print(s1.address)#new address updates to '8 Percheron Lane' rather than the original '57 Robbins Drive,' as desired!!


# In[4]:


#School class, which contains four attributes, holds all the students for school:
class School:
    def __init__(self, school, term, year):
        self.school = school ## name of the school as a string (ie. 'The Lawrenceville School')
        self.term = term#the current term (ie.'T1', 'T2', 'T3' for fall, winter, and spring, respectively)as a string.
        self.year = year # the curent year as a string
        self.student_dict = {}#initializing empty student dictionary; keys=sids; values=Student class objects
    #add_student method adds to student_dict defined above, with id as the key and the student object as the value.
    ## requires user to enter the student_obj (ie. how s1 is defined in two kernels above this kernel)
    def add_student(self, student_obj):
        self.student_dict[getattr(student_obj, 'sid', 'Attribute not found')] = student_obj 
    
    #remove_student method removes the student object from the student dict; requires user to enter the sid 
    # of the student that they desire to remove
    def remove_student(self, sid):
        del self.student_dict[sid]
        
    ##print_students method does not require any arguments; rather, it loops through the student dictionary and prints
    # useful information about the student, including their sid, name, email, and House!
    def print_students(self):
         for key, value in self.student_dict.items():
                 print(f'{value.first} {value.last} is in the {value.house} House, has a student id of {value.sid}, and can be reached via email at {value.email}.')        
    #set_term is a property that is responsive to user changes and will return the term and year. 
    @property
    def set_term(self):
        if self.term.upper() == "T1": 
            return f'Fall {self.year}.' 
        if self.term.upper() == "T2":
            return f'Winter {self.year}.'
        if self.term.upper() == "T3":
            return f'Spring {self.year}.'
         


# In[5]:


#creating an instance of the School class to test out basic functionality!
s1 = Student(78910, 'Hahami', 'Ely', '57 Robbins Drive', 5, 'Kennedy')
o1 = School('The Lawrenceville School', 'T2', '2023')
print(o1.school)
print(o1.term)
print(o1.year)
o1.add_student(s1)
print(o1.student_dict[78910])
# print(o1.print_students())
print(o1.set_term)
s2 = Student(99870, 'Garica', 'Lucas', '10 Main Street', 5, 'Upper')
o1.add_student(s2)
o1.print_students()


# In[6]:


#below is a function, entitled func, that is extremely useful for code efficiency, as I previously had the same
#block of code copied/pasted across 5 different methods which could be cleaned up with one all-econompassing function. 

#essentially, func will take an input (sid) and a desired method; it will search through Student object (which
# are contained in my_list) matches the inputted sid and then it will run the user's desired method using said
# Student object. If the desired method requires arguments, the function takes up to two arguments (as that is 
# the max number of arguments that the methods within the above classes take) and will appropriately 
# run the method with the right number of arguments. For example, the add_course method requires two arguments -- 
# that is, the letter period and name of the course -- so method_atr1 and method_atr2 (defined below) will both 
#not be set to None. On the other hand, the method community serivce does not require any arguments, so I will call 
# on func(input, 'community_service') and the function will find the Student object based corresponding to an inputted 
# sid and then run the community_service method within the Student class for said unique student. 
def func(inp, method, method_atr1=None, method_atr2=None): ## methods needs to be inputted as a string
        for i in my_list: #iterates over each Student object
            if i.sid == inp: ##if the student id's match
                method_to_call = getattr(i, method)
                if method_atr1 !=None and method_atr1!=None: #ie if method requires two arguments
                    return method_to_call(method_atr1, method_atr2)
                elif method_atr1 != None: # ie if method requires one argument
                    return method_to_call(method_atr1)
                else: ## ie if method requires no arguments (other than self, of course!)
                    return method_to_call()
                    


# In[7]:


#second function for efficiency rather than copying/pasting code. As the name implies, the function 
#checks/error handles a user input for a student id!
def check_valid_sid():
    while True:
        try:
            global user_pref_sid
            user_pref_sid = int(input('Enter the student id for the existing student would you like to perform an action on: (1/1)')) ## student id is in integer
            list_of_valid_sids = [i.sid for i in my_list] # list comp!
            if user_pref_sid not in list_of_valid_sids:
                print(f'\033[1mSID is not in SIS.\033[0m')
            else: # ie if j is in list_of_valid_sids (ie thats its a valid sid)
                break
        except:
            print(f'\033[1mYou did not enter the id of an existing/valid student. Please try again!\033[0m')
    


# In[8]:


## Below is the user interface (UI) for the SIS I've created; the main premise to let the user access a menu
## that has all the methods from the School and Student classes and the UI does whatever the user wants while
## appropriately handling errors and guiding the user towards the appropriate options!

#I've started with one Student object, Ely Hahami, who has an sid of 78910. 
s1 = Student(78910, 'Hahami', 'Ely', '57 Robbins Drive', 5, 'Kennedy')
my_list = [s1]
#I've also started with one School object, The Lawrenceville School currently in Spring 2023
o1 = School('The Lawrenceville School', 'T3', '2023') 
o1.add_student(s1)
enter_sis_pref = input(f"Would you like to enter the SIS? Please respond Yes or No:")#initial question to enter SIS
if enter_sis_pref.upper()=='NO':
    print('No worries. Thank you for your time!')

elif enter_sis_pref.upper()=='YES':
    #printing nicely formatted menu 
    print('\n')
    print(f'\033[1mMethod\033[0m:{"":13} Purpose:') #menu contains available methods with corresponding descriptions
    print('\n')
    command_dict = {'add_student': 'Adds the student to the student dictionary, with id as the key and the student obj as value.',
                    'remove_student': 'Removes the student from the student dictionary.',
                    'print_students': 'Loops through the students within the SIS and prints their id, name, email, and House.',
                    'set_term': 'Returns the term and year (ie returns Fall 2023 if term is T1 and year is 2023.'}
    for key, value in command_dict.items(): ##iterates over method and description of purpose and prints in nice way:
        print(f'\033[1m{key:20}\033[0m{value}')
    print('\n')

    while True: #loop until the user inputs a valid method (ie. one that is contained in the menu above)
        user_pref_method = input('Of the options on the menu, which School class method would you like to use (type exit to stop choosing methods)?')
        print('\n')
        if user_pref_method.upper() == 'EXIT':
            break ## ie breaks out of the otherwise infinite loop if the user desires to exit
        if user_pref_method == 'add_student': #if the user desires to add a student:
            while True: ## loop until user enters a valid student sid
                try: 
                    user_pref_sid = int(input('What is the id of the student you want to add? (1/6)')) ## student id is in integer
                    if s1.sid == user_pref_sid: ## ie that student id already exists
                        print('That student id already exists in the SIS. Please try again, entering a new student id!')
                    else:#the above handles the case in which the user enters an SID that already exists in the SIS.
                        break
                except: ## below will run if the user enters a non-integer student id (ie. 'pizza')
                    # use try/except to not terminate program; rather, loop will continue until valid sid entry!
                    print(f'\033[1mYou did not enter a valid student id. Please enter a 5 digit number!\033[0m')

            user_pref_first = input('What is the last name of the student you want to add ? (2/6)')
            user_pref_last = input('What is the first name of the student you want to add? (3/6)')
            user_pref_addy = input('What is the address of the student you want to add? (4/6)')


            while True: ## loop until user enters valid form
                try: #try/except for case that user_pref_form is not an integer; so run except rather than terminate program
                    user_pref_form = int(input('What is the form of the student you want to add? (5/6)')) ## form is also an integer
                    if user_pref_form>5 or user_pref_form<2: ## ie tries an invalid entry like a first former of 11th former
                        print(f'\033[1mWhile you inputted an integer, recall that a form can only be 2,3,4 or 5. Try again!\033[0m')
                    else:
                        break
                except:
                    print(f'\033[1mYou did not enter a valid form. Please enter an integer between 2 and 5, inclusive.\033[0m')

            
            while True: #loop runs until a valid house is inputted by the user
                user_pref_house = input('What is the house of the student you want to add? (6/6)')
                if user_pref_form==2: ## ie. second former
                    if user_pref_house.lower() not in ['boys lower', 'girls lower']:
                        print('The only valid house a second former can be in is girls lower or boys lower. Try again!')
                    else:
                        break
                elif 2<user_pref_form<=5: ## ie non-second former
                    if user_pref_house.lower() not in ['carter', 'cleve','dickinson', 'griswold', 'hamill', 'kennedy', 'kirby', 
                    'mcclellan', 'stanley','stephens', 'woodhull', 'upper', 'mcpherson', 'reynolds', 'kinnan']:
                        print(f'\033[1mYou did not input a valid house. Please try again!\033[0m')
                    else: ## ie if the user enters a valid house
                        break
            s2 = Student(user_pref_sid, user_pref_first, user_pref_last, user_pref_addy, user_pref_form, user_pref_house)
            ## creating the Student class based on the user's inputs above!
            my_list.append(s2) ## add newly created Student object to my_list, which holds Student objects!
            o1.add_student(s2) ## add to o1, the original school object
            print(f'\033[1mStudent successfully added!\033[0m')

        elif user_pref_method.lower() == 'remove_student':
         ## below will error handle using try/except the case where the user inputs an invalid id
         ## for instance, if the user inputted 'pizza' rather than '08997'
            check_valid_sid() #running function defined in kernel above! 
            o1.remove_student(user_pref_sid) # removes student from School object based on inputted id 
            print(f'\033[1mStudent successfully deleted!\033[0m')
    
        elif user_pref_method.lower() == 'print_students': # no need for error handling for this method
            print(o1.print_students()) 

        elif user_pref_method.lower() == 'set_term': # also no need for error handling for this method
            print(f'The term and year is \033[1m{o1.set_term}\033[0m')
        else:#handling the case where the user did not put a method that was on the menu (ie.invalid desired method)!
            print(f'\033[1mYou did not input a valid desired method. Try again, using the options from the menu above!\033[0m')        
#-------------------------------------------------------------------------------------------------------------------
# now, onto menu for the Student Class:
    second_command_dict={'add_course':'Adds a course to the student course list after you, the user, feed it the period and course.',
                        'drop_course':'Will list off all the student courses and allows you, the user, to delete one',
                         'enter_grades': 'Allows you, the user, to enter a grade for each course the student takes.',
                         'calculate_GPA':'Calculates the student numerical GPA after you, the user, inputs courses and grades.',
                         'change_info':'Allows you, the user, to change the address, first name, or last name of the student.',
                         'community_service':'Relays the graduation requirement status of the desired student after obtaining LCAP/OTE info.'}
    print('\n')
    print(f'\033[1mMethod\033[0m:{"":13} Purpose:')
    print('\n')
    for key, value in second_command_dict.items():
        print(f'\033[1m{key:20}\033[0m {value}') # prints menu of Student class methods in a nicely formatted way!
    
    while True:
        user_pref_method = input('Of the options on the menu, which Student class method would you like to use (type exit to end program)?')
        print('\n')

        if user_pref_method.upper() == 'EXIT':
            break ## ie breaks out of the otherwise infinite loop if the user desires to exit

        if user_pref_method.lower() == 'add_course':
            check_valid_sid()

            while True: ## will continue until the user inputs a valid period 
                user_pref_period = input('What period letter is the course you would like to add?')
                ## checking edge case of invalid period entry (ie. 'K' period)
                if user_pref_period.upper() not in ['A', 'B', 'C', 'D', 'E', 'F']: 
                    print(f'\033[1mInvalid period letter. Recalling that a valid period is either A,B,C,D,E, or F period, try again!\033[0m')
                else: ## that is, if the user's desired period is a valid input 
                    break
            user_pref_course = input('What is the name of the course?')
            func(user_pref_sid, 'add_course', user_pref_period, user_pref_course)
            print('\n')
            print(f'\033[1mCourse successfully added for your desired student!\033[0m')


        elif user_pref_method.lower() == 'drop_course':
            check_valid_sid()
            
            while True:
                k = input('What period letter is the course you would like to drop?')
                try: ## error handling for the case of dropping a course that does not exist!
                    search_id = user_pref_sid
                    for i in my_list:
                        if i.sid == search_id:
                            i.drop_course(k)
                    break
                except:
                    print(f'\033[1mYou are trying to drop a course that does not exist because it was never inputted into the SIS. Please try again and input a valid course to drop!\033[0m')


        elif user_pref_method.lower() == 'enter_grades': 
            check_valid_sid()
            func(user_pref_sid, 'enter_grades')
            ## can see efficiency of functions above


        elif user_pref_method.lower() == 'calculate_gpa': 
            check_valid_sid()
            print('\n') # list comprehension below for code efficiency!
            names_list = [i for obj in my_list if obj.sid == user_pref_sid for i in (obj.first, obj.last)]         
            i_calc_grades = func(user_pref_sid, 'calculate_GPA')
            print(f'The GPA of \033[1m{names_list[0]}\033[1m \033[1m{names_list[1]}\033[1m is \033[1m{i_calc_grades}\033[0m.')
            ## printing the first and last name is important because if the user decides to change one
            ## of their attributes (such as first or last name), the calculate_GPA proves that the name 
            ### actually changes and gives a more personal touch the SID in an increasingly impersonal world. 

        elif user_pref_method.lower() == 'change_info':
            check_valid_sid()
            while True: ## verifying that the user is electing to change a valid attribute!
                    user_pref_change = input('What attribute would you like to change -- pick between address, first name (type first), or last name (type last)?')
                    if user_pref_change.upper() not in ['ADDRESS','FIRST','LAST']:
                        print(f'\033[1mInvalid attribute to change. Recalling that you can elect to change either address, first name (type first) or last name (type last), please try again!\033[0m')
                    else:
                        break
            user_pref_change_to = input(f'What would you like {user_pref_change} to be changed to?')
            func(user_pref_sid, 'change_info', user_pref_change, user_pref_change_to)
            print('\n')
            print(f'\033[1mAttribute, {user_pref_change}, successfully changed to {user_pref_change_to} for your desired student!\033[0m') # prints bolded!

        elif user_pref_method.lower() == 'community_service': ## in order to exceed assignment goals!
            check_valid_sid()
            func(user_pref_sid, 'community_service')#again, we see the efficiency of the check_valid_sid() and func() functions!!

        else: ## handling the case where the user did not put a method that was on the menu!
            print(f'\033[1mYou did not input a valid desired method. Try again, using the options from the menu above!\033[0m')
else:
    print('You did not respond with a Yes or No. Restart the SIS and respond with Yes or No please!')


# In[9]:


# General Notes about project and 20 error handling/edge case considerations:

#Project (went above and beyond project requirements):
# 1. ## added community_service method to Student class and allowed said method to be accessed in menu via UI
# #said method provides useful info on whether of not the student has fufilled their CS reqs based on num LCAPS/OTEs
# 2 ## asked user for free period (where free period was never an attribute/project requirement)
#and handled error of the niche case in which user wants to enter grade for their free period, which isn't sensible!

#List of all the 20 Error Handling/Edge Case Considerations I've done:
# 1. #the user tries to drop a course that has never been inputted.
# 2. # the user tries to calculate_GPA if no courses were added/all courses were removed (ie. grade_list is empty).
# 3. #handled error of user trying to add grades for a free period.
# 4. ## handles niche error of invalid free period entry (ie. not 'A','B','C','D','E', or 'F')
# 5. ## handles error of invalid letter grade entry (ie. not "A+", "A", "A-", and so on and so forth)
# 6. ## handles error of invalid term entry (ie. not T1, T2, or T2)
# 8.## handles error where the user tries to enter grades if no courses were added/all courses were removed.
# 9. ##handles error of non-integer inputs for number of LCAPS/OTEs the student has completed.
# 10. ## handles edge case of when user inputs negative number for numbers of LCAPS/OTEs the student has completed.
# 11. ## handles all combinations of valid integer inputs for number of LCAPS/OTEs (ie. 6 OTEs and 0 LCAPS handled)
# 12.#considers edge case where the user tries to add a student with an sis that already exists within the SIS.
## which cannot happen in real life, as all sids are unique!
# 13.  handles case where the user enters a desired method that doesn't exist (ie. chooses method not on the menu).
#14. handles case where inputted sid is not an integer (ie. 'pizza')
# 15. handles case where inputted form DNE (ie. form = 6) or form = 'pizza' (only valid forms are 2-5, inclusive)!
#16. handles case where user inputs invalid house (ie. inputs 'pizza' or inputs '7'); only valid houses are
#the ones in the circle/cresent (ie. Kennedy, Kirby, etc. )
#17. handles case where a second former tries to put a non-lower house; isn't possible because a freshmen, for instance, 
## cannot be in Kennedy or Kirby (only 3-5th formers, inclusive, can be in circle/crescent houses)
#18. handles case where the user enters an invalid period for a course (ie. 'K' period or 'pizza period')
## rather than A,B,C,D,E, or F period, which are the only valid entries!
#19. handles case where the user tries to drop a course that does not exist. 
#20. ensures that the user inputs a valid attribute to change in change_info method 


# In[ ]:




