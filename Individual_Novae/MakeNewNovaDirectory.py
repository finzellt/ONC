import sys
import string
import os
from pylab import *
import datetime as dt
import math as m 





NewNovaName = sys.argv[1]
CurrentWorkingDirectory = os.getcwd()

NewDirectoryRoot = CurrentWorkingDirectory+'/'+NewNovaName
NewDirectoryTicketDirectory = NewDirectoryRoot+'/Tickets'
NewDirectoryDataDirectory = NewDirectoryRoot+'/Data'
NewDirectoryPendingTicketSubDirectory = NewDirectoryTicketDirectory+'/PendingTickets'
NewDirectoryCompletedTicketSubDirectory = NewDirectoryTicketDirectory+'/CompletedTickets'

if not os.path.exists(NewDirectoryRoot):
    os.makedirs(NewDirectoryRoot)

if not os.path.exists(NewDirectoryTicketDirectory):
    os.makedirs(NewDirectoryTicketDirectory)

if not os.path.exists(NewDirectoryDataDirectory):
    os.makedirs(NewDirectoryDataDirectory)


if not os.path.exists(NewDirectoryPendingTicketSubDirectory):
    os.makedirs(NewDirectoryPendingTicketSubDirectory)

if not os.path.exists(NewDirectoryCompletedTicketSubDirectory):
    os.makedirs(NewDirectoryCompletedTicketSubDirectory)









