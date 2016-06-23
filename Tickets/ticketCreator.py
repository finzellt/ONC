#ticketCreator.py
#creates tickets for the ONC
#Max Morehead
#6/21/16


dataFields = ["OBJECT NAME: ", "TIME UNITS: ", "FLUX UNITS: ",  "FLUX ERROR UNITS: ", "FILTER SYSTEM: ", "DATATYPE: ", "MAGNITUDE SYSTEM: ", "WAVELENGTH REGIME: ", "TIME SYSTEM: ", "ASSUMED DATE OF OUTBURST: ", "TELESCOPE: ", "OBSERVER: ", "REFERENCE: ", "DATA FILENAME: ", "TIME COLUMN NUMBER: ", "FLUX COLUMN NUMBER: ", "FLUX ERROR COLUMN NUMBER: ", "FILTER/FREQUENCY/ENERGY RANGE COLUMN NUMBER: ", "UPPER LIMIT FLAG COLUMN NUMBER: ", "TELESCOPE COLUMN: ", "OBSERVER COLUMN: ", "FILTER SYSTEM COLUMN: ", "TICKET STATUS: "]

ticketText = ""
userInput = []
length = []
for i in range(len(dataFields)):
	userInput.append(0)
	length.append(0)

i = 0
directory =""
while i < len(dataFields):
	userInput[i] = input(dataFields[i])
	if userInput in ["goback", "Goback", "go_back", "Go_back"]:
		if i == 0:	
			print("You can't go back now. This is the first field.")
		else:
			ticketText = ticketText[0:-length[i-1]]
			i -= 1
	else:
		if i == len(dataFields) - 1:
			if userInput[i][0] in ["C", "c"]:
				directory = "CompletedTickets"
			elif userInput[i][0] in ["P", "p"]:
				directory = "PendingTickets"
			else:
				continue
		length[i] = len(dataFields[i]) + len(userInput[i])
		ticketText = ticketText + dataFields[i] + userInput[i] + "\n"			
		i += 1
	
ticketText = ticketText[:-1]

author = userInput[12].lstrip()


myFile = open(directory + "/" + userInput[0].replace(" ", "") + "_" + author.split()[0] + "_" + userInput[7].replace(" ", "") + "_" + userInput[5].strip() + ".txt", "w")
myFile.write(ticketText)
myFile.close()

