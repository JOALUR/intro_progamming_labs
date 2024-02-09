Header = "Madlib Game" #header assigned name
print(Header, end="... ") #printed header

print("\n", "\n" "Enter the follower words: ") #they'll enter the following words

#input variables
PNOUN1 = input("Plural Noun: ")
FNAME = input("Person's First Name: ")
NOUN1 = input("Noun: ")
LNAME = input("Person's Last Name: ")
PNOUN2 = input("Plural Noun: ")
PLACE1 = input("Place: ")
PNOUN3 = input("Plural Noun: ")
PLACE2 = input("Place: ")
PNOUN4 = input("Plural Noun: ")
NOUN2 = input("Noun: ")
ADJECTIVE1 = input("Adjective: ")
ADJECTIVE2 = input("Adjective: ")
VERB = input("Verb: ")
ADJECTIVE3 = input("Adjective: ")

#the big game line
print("\n", "The Big Game", end="!!!")

#1st line of paragraph
print("\n","\n","Hello there, sports",PNOUN1, end="!")

#2nd line in paragraph
print("\n","This is",FNAME + ",","talking to you from the press",NOUN1)

#3rd line
print("in",LNAME,"Stadium, where 57,000 fans are cheering",PNOUN2)

#4th line
print("Have gathered to watch (the)",PLACE1,PNOUN3)

#5th line
print("take on (the)",PLACE2,PNOUN4 + ".")

#line 6
print("Even though the", NOUN2, "is shining, it's a/an",ADJECTIVE1)

#line 7
print("cool day with the temperature in the",ADJECTIVE2,"20s", end=".")

#line8
print("\n","We'll be back for the opening", VERB, "-off after a few words")

#line 9
print("from our",ADJECTIVE3,"sponsor.")