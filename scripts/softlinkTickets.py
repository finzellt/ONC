#ONC/scripts/softlinkTickets.py
#soft links tickets in individual novae directories

import os

for directoryName in os.listdir("../Individual_Novae"):
	if "." not in directoryName:
		for ticketType in ["CompletedTickets", "PendingTickets"]:	
			for fileName in os.listdir("../Individual_Novae/" + directoryName + "/Tickets/" + ticketType):
				os.symlink("../Tickets/" + ticketType + "/" + fileName, "../Individual_Novae/" + directoryName + "/Tickets/" + ticketType + "/" + fileName)
