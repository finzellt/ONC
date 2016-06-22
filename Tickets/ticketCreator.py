#ticketCreator.py
#creates tickets for the ONC
#Max Morehead
#6/21/16


dataFields = ["OBJECT NAME: ", "TIME UNITS: ", "FLUX UNITS: ",  "FLUX ERROR UNITS: ", "FILTER SYSTEM: ", "Data Type: ", "MAGNITUDE SYSTEM: ", "WAVELENGTH REGIME: ", "TIME SYSTEM: ", "ASSUMED DATE OF OUTBURST: ", "TELESCOPE: ", "OBSERVER: ", "REFERENCE: ", "DATA FILENAME: ", "TIME COLUMN NUMBER: ", "FLUX COLUMN NUMBER: ", "FLUX ERROR COLUMN NUMBER: ", "FILTER/FREQUENCY/ENERGY RANGE COLUMN NUMBER: ", "UPPER LIMIT FLAG COLUMN NUMBER: ", "TELESCOPE COLUMN: ", "OBSERVER COLUMN: ", "FILTER SYSTEM COLUMN: ", "TICKET STATUS: "]

ticketText = ""
i = 0
length = []
userInput = []
while i < len(dataFields):
	userInput.append(input(dataFields[i]))
	if userInput in ["goback", "Goback", "go_back", "Go_back"]:
		if i == 0:	
			print("You can't go back now. This is the first field.")
		else:
			i -= 1
			#careful...this uses a variable that isn't created until the first iteration
			ticketText = ticketText[0:-length[i-1]]
	else:
		if i == len(dataFields) - 1	
			if userInput[i][0] in ["C", "c"]:
				directory = "CompletedTickets"
				continue
			else if userInput[i][0] in ["P", "p"]:
				directory = "PendingTickets"
		length.append(len(dataFields[i]) + len(userInput[i]))
		ticketText = ticketText + userInput[i] + "\n"			
		i += 1
	
ticketText = ticketText[:-1]

author = userInput[12].lstrip()


myFile = open(directory + "/" + userInput[0] + "_" + author.split()[0] + "_" + userInput[7] + "_" + userInput[5] + ".txt", "w")
myFile.write(ticketText)
myFile.close()

