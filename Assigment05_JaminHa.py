#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   Jamin Ha
# Date:  February 12, 2018
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   jha, 02/1202918, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#


objFile = open("ToDoList.txt","r+")
lstData = []
dictRow = {}

for row in objFile:     #for loop; goes through each row in .txt file and performs code block
    Task, Priority = row.strip().split(",") #declaring 2 variables that serve as our keys; splitting data from text file at the comma and deleting any white space.
    dictRow = {Task:Priority} #populating dictRow dictionary with 2 keys
    lstData.append(dictRow) #populating lstData list with 2 dictionary rows; this creates a 2x2 List Table

print(lstData) #displays contnets of list table to user

# strMenu = A menu of user options
strMenu = "Menu of Options \n \t 1) Show current data \n \t 2) Add a new item. \n \t 3) Remove an existing item. \n \t 4) Save Data to File \n \t 5) Exit Program \n"
print(strMenu)

while(True):
    strChoice = input("Please input your response 1-5: ")

    if strChoice == "1":
        print("Current data stored in table:\n \n ",lstData,"\n")
        if (input("Type 'exit' to end. Any other input to continue. ").lower() == "exit"): break

    elif strChoice == "2":
        strTask = input("Enter new task: ")
        strPri = input("Enter priority level: ")
        dictNewRow = {"Task":strTask,"Priority":strPri}
        lstData.append(dictNewRow)
        objFile.write(strTask)
        objFile.write(strPri)
        objFile.close()
        strViewUpdated = input("Want to see your updated table?").lower()
        if strViewUpdated == "yes": print(lstData)
        elif(input("Type 'exit' to end. Any other input to continue. ").lower() == "exit)"):break

    elif strChoice == "3":
        strRemove = input("Which item would you like to remove? Please indicate by Key Value: ")
        if (strRemove in lstData):
            del lstData[strRemove]  #this is not working
        elif (input("Type 'exit' to end.").lower() == "exit)"): break

    elif strChoice == "4":
        input("You've chosen to save  your data.")
        strConvert = str(lstData)   #how come lstData does not include any new data inlcuded from a user if they had previously chosen option 2????
        objFile = open("ToDoList.txt", "r+")
        objFile.write(strConvert)
        objFile.close()
        break
        
    elif strChoice == "5":
        input("You've chosen to exit out of the program. Your changes will be lost.")
        break

    else:
        continue 
