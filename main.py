import tkinter as tk
from tkinter import ttk  # ttk module allows use of tk themed widgets
from tkinter import filedialog  # module from tkinter to create file/directory selection window
import csv  # csv file handling
import shutil  # module for file handling

# Creating tkinter window
root = tk.Tk()
root.title("Client Tracking Program")
root.geometry("600x750")
root.configure(background='gray70')
tabControl = ttk.Notebook(root)

# Creating tabs in the GUI
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Client Information')
tabControl.add(tab2, text='Add Client')
tabControl.pack(expand=1, fill="both")

lineCounter = 0


def readCSV():  # reading the csv
    global arr
    input_string = ""
    file1 = open('clientData.csv')  # opening file
    counter = 0  # counter to count through the csv
    for line in file1:  # for each line in the CSV file
        if line != "\n" or line != "":
            input_string += line
            line = line.replace("\n", "")  # used to delete \n when reading into array
            line = line.split(';')  # data is separated by semicolons to allow user to use commas in data
            size = len(line)  # retrieving the length of a line
            for i in range(size - 1):
                arr[counter][i] = line[i]  # define size of array with counter
            counter += 1  # counts up to iterate through column


def csvLength():  # retrieving csv length to build array
    csvFile = open('clientData.csv')
    reader = csv.reader(csvFile)  # reading the csv file
    lineCounter = len(list(reader))  # reading the line count of lines in csv file
    if lineCounter == 0:  # if there are 0 lines in csv, create a line
        lineCounter = 1
        arrayBuilder(lineCounter)  # build array with the length of the csv
    if lineCounter > 0:  # if there are more than 0 lines in the csv, create array with given lines and read csv
        arrayBuilder(lineCounter)
        readCSV()


def arrayBuilder(lineCounter):  # building a 2D array, passing lineCounter as parameter
    global arr, rows, cols
    rows, cols = (lineCounter, 13)  # defining size of the array. Length determined by lineCounter (lines in csv)
    arr = [["" for i in range(cols)] for j in range(rows)]  # building the array out
    return arr, rows, cols


csvLength()

global newName, newPhoneNumber, newEmail, newHomeAddress, newBirthday, newSpouseName, newChildrenName, newPetName, \
    newBusinessType, newDateInteraction, newReferrals, newHouseDate, newNotes


def writeLinesToFile():  # writing new elements in arr to csv lines
    fileToSaveTo = open('clientData.csv', "w")  # opening csv to write to
    rows = (len(arr))  # defining rows by length of array
    loop = 0
    #  iterating through 2D array to write to CSV
    for i in range(rows):
        for j in range(cols):
            if j < cols:
                fileToSaveTo.writelines(arr[i][j] + ";")  # write to CSV, splitting the data with semicolons
        if i != rows - 1:
            fileToSaveTo.write(arr[i][j] + "\n")  # write to CSV with creating new line
        else:
            fileToSaveTo.write(arr[i][j])  # write array to CSV
        loop = loop + 1
    fileToSaveTo.close()


def saveClient():  # saving client data to arr then writing to csv
    arr_length = len(arr)
    arr.append(["", "", "", "", "", "", "", "", "", "", "", "", ""])  # append new element in array
    # retrieving data from entry boxes and saving to arr
    newName = newClientName.get()
    arr[arr_length][0] = newName
    newPhoneNumber = newClientPhone_Num.get()
    arr[arr_length][1] = newPhoneNumber
    newEmail = newClientEmail.get()
    arr[arr_length][2] = newEmail
    newHomeAddress = newClientHome_Address.get()
    arr[arr_length][3] = newHomeAddress
    newBirthday = newClientBirthday.get()
    arr[arr_length][4] = newBirthday
    newSpouseName = newClientSpouse_Name.get()
    arr[arr_length][5] = newSpouseName
    newChildrenName = newClientChildren_Name.get()
    arr[arr_length][6] = newChildrenName
    newPetName = newClientPet_Name.get()
    arr[arr_length][7] = newPetName
    newBusinessType = newClientBusinessType.get()
    arr[arr_length][8] = newBusinessType
    newDateInteraction = newClientDateOfInteraction.get()
    arr[arr_length][9] = newDateInteraction
    newReferrals = newClientReferral.get()
    arr[arr_length][10] = newReferrals
    newHouseDate = newDateHousePurchase.get()
    arr[arr_length][11] = newHouseDate
    newNotes = newClientNotes.get()
    arr[arr_length][12] = newNotes
    writeLinesToFile()
    clearAddClientBoxes()
    dropDownBox()


def clearAddClientBoxes():  # clears the boxes in tab2 when the save button is pressed
    newClientName.delete(0, tk.END)
    newClientName.insert(0, "")
    newClientPhone_Num.delete(0, tk.END)
    newClientPhone_Num.insert(0, "")
    newClientEmail.delete(0, tk.END)
    newClientEmail.insert(0, "")
    newClientHome_Address.delete(0, tk.END)
    newClientHome_Address.insert(0, "")
    newClientBirthday.delete(0, tk.END)
    newClientBirthday.insert(0, "")
    newClientSpouse_Name.delete(0, tk.END)
    newClientSpouse_Name.insert(0, "")
    newClientChildren_Name.delete(0, tk.END)
    newClientChildren_Name.insert(0, "")
    newClientPet_Name.delete(0, tk.END)
    newClientPet_Name.insert(0, "")
    newClientBusinessType.delete(0, tk.END)
    newClientBusinessType.insert(0, "")
    newClientDateOfInteraction.delete(0, tk.END)
    newClientDateOfInteraction.insert(0, "")
    newClientReferral.delete(0, tk.END)
    newClientReferral.insert(0, "")
    newDateHousePurchase.delete(0, tk.END)
    newDateHousePurchase.insert(0, "")
    newClientNotes.delete(0, tk.END)
    newClientNotes.insert(0, "")


# Tab2 Add Client: creating the labels and entry boxes for each data type
ttk.Label(tab2, text="Client Name:").grid(column=0, row=0, padx=10, pady=10)
newClientName = ttk.Entry(tab2)
newClientName.grid(column=1, row=0, padx=5, pady=5)
ttk.Label(tab2, text="Client Phone Number:").grid(column=0, row=1, padx=10, pady=10)
newClientPhone_Num = ttk.Entry(tab2)
newClientPhone_Num.grid(column=1, row=1, padx=5, pady=5)
ttk.Label(tab2, text="Client Email:").grid(column=0, row=2, padx=5, pady=5)
newClientEmail = ttk.Entry(tab2)
newClientEmail.grid(column=1, row=2, padx=5, pady=5)
ttk.Label(tab2, text="Client Home Address:").grid(column=0, row=3, padx=5, pady=5)
newClientHome_Address = ttk.Entry(tab2)
newClientHome_Address.grid(column=1, row=3, padx=5, pady=5)
ttk.Label(tab2, text="Client Birthday:").grid(column=0, row=4, padx=5, pady=5)
newClientBirthday = ttk.Entry(tab2)
newClientBirthday.grid(column=1, row=4, padx=5, pady=5)
ttk.Label(tab2, text="Spouse Name:").grid(column=0, row=5, padx=5, pady=5)
newClientSpouse_Name = ttk.Entry(tab2)
newClientSpouse_Name.grid(column=1, row=5, padx=5, pady=5)
ttk.Label(tab2, text="Child(ren) Name(s):").grid(column=0, row=6, padx=5, pady=5)
newClientChildren_Name = ttk.Entry(tab2)  # need to separate somehow
newClientChildren_Name.grid(column=1, row=6, padx=5, pady=5)
ttk.Label(tab2, text="Pet Name(s):").grid(column=0, row=7, padx=5, pady=5)
newClientPet_Name = ttk.Entry(tab2)  # need to separate somehow
newClientPet_Name.grid(column=1, row=7, padx=5, pady=5)
ttk.Label(tab2, text="Business Type:").grid(column=0, row=8, padx=5, pady=5)
newClientBusinessType = ttk.Entry(tab2)
newClientBusinessType.grid(column=1, row=8, padx=5, pady=5)
ttk.Label(tab2, text="Date of Late Interaction:").grid(column=0, row=9, padx=5, pady=5)
newClientDateOfInteraction = ttk.Entry(tab2)
newClientDateOfInteraction.grid(column=1, row=9, padx=5, pady=5)
ttk.Label(tab2, text="Referrals:").grid(column=0, row=10, padx=5, pady=5)
newClientReferral = ttk.Entry(tab2)
newClientReferral.grid(column=1, row=10, padx=5, pady=5)
ttk.Label(tab2, text="Date of House Purchase:").grid(column=0, row=11, padx=5, pady=5)
newDateHousePurchase = ttk.Entry(tab2)
newDateHousePurchase.grid(column=1, row=11, padx=5, pady=5)
ttk.Label(tab2, text="Notes:").grid(column=0, row=12, padx=5, pady=5)
newClientNotes = ttk.Entry(tab2)
newClientNotes.grid(column=1, row=12, padx=5, pady=5, ipady=15)
ttk.Button(tab2, text='Save Client', command=saveClient).grid(column=0, row=13, padx=5, pady=10)


def dropDownBox():
    ttk.Label(tab1, text="Client Information: Select a Client").grid(column=0, row=0, padx=5, pady=5)
    global OPTIONS
    OPTIONS = [item[0] for item in arr]  # printing first item in element of arr (client name)
    global variable
    variable = tk.StringVar(tab1)
    variable.set(OPTIONS[0])
    global dropDown
    dropDown = tk.OptionMenu(tab1, variable, *OPTIONS)  # creating the dropdown box and inserting the client names
    dropDown.grid(column=0, row=1)  # Placing the dropdown box
    dropDown.config(width=15)


def loadClient():  # finding the index number of clients, will be used to load their data into entry boxes
    name = variable.get()
    index = OPTIONS.index(name)
    return index


# Tab1: Main Page Layout
ttk.Label(tab1, text="Client Name:").grid(column=0, row=3, padx=10, pady=10)
clientName = ttk.Entry(tab1)
clientName.grid(column=1, row=3, padx=5, pady=5)
ttk.Label(tab1, text="Client Phone Number:").grid(column=0, row=4, padx=10, pady=10)
clientPhone_Num = ttk.Entry(tab1)
clientPhone_Num.grid(column=1, row=4, padx=5, pady=5)
ttk.Label(tab1, text="Client Email:").grid(column=0, row=5, padx=5, pady=5)
clientEmail = ttk.Entry(tab1)
clientEmail.grid(column=1, row=5, padx=5, pady=5)
ttk.Label(tab1, text="Client Home Address:").grid(column=0, row=6, padx=5, pady=5)
clientHome_Address = ttk.Entry(tab1)
clientHome_Address.grid(column=1, row=6, padx=5, pady=5)
ttk.Label(tab1, text="Client Birthday:").grid(column=0, row=7, padx=5, pady=5)
clientBirthday = ttk.Entry(tab1)
clientBirthday.grid(column=1, row=7, padx=5, pady=5)
ttk.Label(tab1, text="Spouse Name:").grid(column=0, row=8, padx=5, pady=5)
clientSpouse_Name = ttk.Entry(tab1)
clientSpouse_Name.grid(column=1, row=8, padx=5, pady=5)
ttk.Label(tab1, text="Child(ren) Name(s):").grid(column=0, row=9, padx=5, pady=5)
clientChildren_Name = ttk.Entry(tab1)
clientChildren_Name.grid(column=1, row=9, padx=5, pady=5)
ttk.Label(tab1, text="Pet Name(s):").grid(column=0, row=10, padx=5, pady=5)
clientPet_Name = ttk.Entry(tab1)
clientPet_Name.grid(column=1, row=10, padx=5, pady=5)
ttk.Label(tab1, text="Business Type:").grid(column=0, row=11, padx=5, pady=5)
clientBusiness_Type = ttk.Entry(tab1)
clientBusiness_Type.grid(column=1, row=11, padx=5, pady=5)
ttk.Label(tab1, text="Date of Late Interaction:").grid(column=0, row=12, padx=5, pady=5)
clientDate_Of_Interaction = ttk.Entry(tab1)
clientDate_Of_Interaction.grid(column=1, row=12, padx=5, pady=5)
ttk.Label(tab1, text="Referrals:").grid(column=0, row=13, padx=5, pady=5)
clientReferral = ttk.Entry(tab1)
clientReferral.grid(column=1, row=13, padx=5, pady=5)
ttk.Label(tab1, text="Date of House Purchase:").grid(column=0, row=14, padx=5, pady=5)
clientDate_Of_HousePurchase = ttk.Entry(tab1)
clientDate_Of_HousePurchase.grid(column=1, row=14, padx=5, pady=5)
ttk.Label(tab1, text="Notes:").grid(column=0, row=15, padx=5, pady=5)
clientNotes = ttk.Entry(tab1)
clientNotes.grid(column=1, row=15, padx=5, pady=5, ipady=15)
dropDownBox()


def populateEntryBoxes():  # uses index number from loadClient to gather and insert data data into entry boxes
    indexNumber = loadClient()
    clientName.delete(first=0, last=500)
    clientName.insert(0, arr[indexNumber][0])
    clientPhone_Num.delete(first=0, last=500)
    clientPhone_Num.insert(0, arr[indexNumber][1])
    clientEmail.delete(first=0, last=500)
    clientEmail.insert(0, arr[indexNumber][2])
    clientHome_Address.delete(first=0, last=500)
    clientHome_Address.insert(0, arr[indexNumber][3])
    clientBirthday.delete(first=0, last=500)
    clientBirthday.insert(0, arr[indexNumber][4])
    clientSpouse_Name.delete(first=0, last=500)
    clientSpouse_Name.insert(0, arr[indexNumber][5])
    clientChildren_Name.delete(first=0, last=500)
    clientChildren_Name.insert(0, arr[indexNumber][6])
    clientPet_Name.delete(first=0, last=500)
    clientPet_Name.insert(0, arr[indexNumber][7])
    clientBusiness_Type.delete(first=0, last=500)
    clientBusiness_Type.insert(0, arr[indexNumber][8])
    clientDate_Of_Interaction.delete(first=0, last=500)
    clientDate_Of_Interaction.insert(0, arr[indexNumber][9])
    clientReferral.delete(first=0, last=500)
    clientReferral.insert(0, arr[indexNumber][10])
    clientDate_Of_HousePurchase.delete(first=0, last=500)
    clientDate_Of_HousePurchase.insert(0, arr[indexNumber][11])
    clientNotes.delete(first=0, last=500)
    clientNotes.insert(0, arr[indexNumber][12])


button = ttk.Button(tab1, text="Load Client", command=populateEntryBoxes)
button.grid(column=0, row=2)


def saveEdits():  # used to save data edits made in tab1
    indexNumber = loadClient()  # getting index number from loadClient
    csvLength()
    # using index number to know what element in the array the edits should save to, replacing the data of that element
    newName = clientName.get()
    arr[indexNumber][0] = newName
    newPhoneNumber = clientPhone_Num.get()
    arr[indexNumber][1] = newPhoneNumber
    newEmail = clientEmail.get()
    arr[indexNumber][2] = newEmail
    newHomeAddress = clientHome_Address.get()
    arr[indexNumber][3] = newHomeAddress
    newBirthday = clientBirthday.get()
    arr[indexNumber][4] = newBirthday
    newSpouseName = clientSpouse_Name.get()
    arr[indexNumber][5] = newSpouseName
    newChildrenName = clientChildren_Name.get()
    arr[indexNumber][6] = newChildrenName
    newPetName = clientPet_Name.get()
    arr[indexNumber][7] = newPetName
    newBusinessType = clientBusiness_Type.get()
    arr[indexNumber][8] = newBusinessType
    newDateInteraction = clientDate_Of_Interaction.get()
    arr[indexNumber][9] = newDateInteraction
    newReferrals = clientReferral.get()
    arr[indexNumber][10] = newReferrals
    newDateHousePurchase = clientDate_Of_HousePurchase.get()
    arr[indexNumber][11] = newDateHousePurchase
    newNotes = clientNotes.get()
    arr[indexNumber][12] = newNotes
    writeLinesToFile()
    clearEditBoxes()
    dropDownBox()


def clearEditBoxes():  # clearing the entry boxes in tab1 when edits are saved and a client is deleted
    clientName.delete(0, tk.END)
    clientName.insert(0, "")
    clientPhone_Num.delete(0, tk.END)
    clientPhone_Num.insert(0, "")
    clientEmail.delete(0, tk.END)
    clientEmail.insert(0, "")
    clientHome_Address.delete(0, tk.END)
    clientHome_Address.insert(0, "")
    clientBirthday.delete(0, tk.END)
    clientBirthday.insert(0, "")
    clientSpouse_Name.delete(0, tk.END)
    clientSpouse_Name.insert(0, "")
    clientChildren_Name.delete(0, tk.END)
    clientChildren_Name.insert(0, "")
    clientPet_Name.delete(0, tk.END)
    clientPet_Name.insert(0, "")
    clientBusiness_Type.delete(0, tk.END)
    clientBusiness_Type.insert(0, "")
    clientDate_Of_Interaction.delete(0, tk.END)
    clientDate_Of_Interaction.insert(0, "")
    clientReferral.delete(0, tk.END)
    clientReferral.insert(0, "")
    clientDate_Of_HousePurchase.delete(0, tk.END)
    clientDate_Of_HousePurchase.insert(0, "")
    clientNotes.delete(0, tk.END)
    clientNotes.insert(0, "")


def deleteClient():
    indexNumber = loadClient()
    del arr[indexNumber]  # delete the selected client index from arr and write the changes to the csv
    dropDownBox()
    clearEditBoxes()
    writeLinesToFile()


ttk.Button(tab1, text='Delete Client', command=deleteClient).grid(column=1, row=1, padx=10, pady=10)
ttk.Button(tab1, text='Save Edits', command=saveEdits).grid(column=1, row=16, padx=10, pady=10)


def exportCSV():  # exporting csv as a copy of the existing csv
    root.clientCSV = filedialog.asksaveasfilename(initialdir="read_text/", title="Select file", filetypes=(
        ("csv files", "*.csv"), ("txt files", "*.txt"), ("all files", "*.*")))
    source = "clientData.csv"
    fileToSaveTo = root.clientCSV
    shutil.copyfile(source, fileToSaveTo)


ttk.Button(tab1, text='Export Data', command=exportCSV).grid(column=0, row=16, padx=10, pady=10)
root.mainloop()