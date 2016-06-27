#ONC/scripts/softlinkTickets.py
#soft links tickets in individual novae directories

import os

for directoryName in os.listdir("../IndividualNovae"):
	for ticketType in ["CompletedTickets", "PendingTickets"]:	
		for fileName in os.list("../IndividualNovae/" + directoryName + "/Tickets/" + ticketType):
			os.symlink("../Tickets/" + ticketType + "/" + fileName, "../IndividualNovae/" + directoryName + "/Tickets/" + ticketType + "/" + fileName)
