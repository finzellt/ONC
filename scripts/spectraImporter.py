import os
import os.path
import re
from astropy.io import fits

directory = "Spectra"

author = "Williams"
dataType = "Spectra"


def getNovaName(filePrefix):
	return filePrefix[:-1]

novaDict = {}

metadataFields = ['FILENAME', 'WAVE COL NUM', 'FLUX COL NUM', 'FLUX ERR COL NUM', 'FLUX UNITS', 'DATE', 'OBSERVER', 'TELESCOPE', 'INSTRUMENT', 'DISPERSION', 'RESOLUTION', 'WAVE RANGE 1', 'WAVE RANGE 2']

ticketDataFields = ["OBJECT NAME: ", "FLUX UNITS: ", "FLUX ERROR UNITS: ", "WAVELENGTH REGIME: ", "TIME SYSTEM: ", "ASSUMED DATE OF OUTBURST: ", "REFERENCE: ", "BIBCODE: ", "DEREDDENED FLAG: ", "METADATA FILENAME: ", "FILENAME COLUMN: ", "WAVELENGTH COLUMN: ", "FLUX COLUMN: ", "FLUX ERROR COLUMN: ", "FLUX UNITS COLUMN: ", "DATE COLUMN: ", "TELESCOPE COLUMN: ", "INSTRUMENT COLUMN: ", "OBSERVER COLUMN: ", "SNR COLUMN: ", "DISPERSION COLUMN: ", "RESOLUTION COLUMN: ", "WAVELENGTH RANGE COLUMN: ", "TICKET STATUS: "]


for filename in os.listdir(directory):
	if re.search(".fits?$", filename, re.IGNORECASE):
		filePrefix = filename[:re.search(".fits?$", filename, re.IGNORECASE).start()]	
		novaName = getNovaName(filePrefix)
		fitsFile = fits.open(directory + "/" + filename)
		
		spectra = fitsFile[0]
		header = spectra.header
		dateTime = header["DATE"]
		match = re.match(r"[\d\-/]+[Tt]", dateTime)
		date = dateTime[:match.end()] if match else ""	
		
		string = ""
		data = spectra.data
			
		for i in range(header["NAXIS1"]):			
			wavelength = header["CRVAL1"] + (header["CRPIX1"] - 1 + i) * header["CDELT1"]
			string += "%s,%s\n" %("{:.6f}".format(wavelength),data[i]) 
		
		outputFile = "%s_%s_%s_%s.csv" %(filePrefix, author, dataType, date)

		wl0, wln = wavelength = str(header["CRVAL1"] + (header["CRPIX1"] - 1) * header["CDELT1"]), str(header["CRVAL1"] + (header["CRPIX1"] - 2 + header["NAXIS1"]) * header["CDELT1"])
		disp = '0'	
		res = '0'		

		if novaName not in novaDict:
			novaDict[novaName] = [(outputFile, date, disp, res, wl0, wln)]
		else:
			novaDict[novaName].append((outputFile, date, disp, res, wl0, wln))	

		string = string[:-1]
		csvFile = open("SpectraHolder/" + outputFile, "w")
		csvFile.write(string)
		csvFile.close()
				
			
for novaName in novaDict:
	string = ",".join(metadataFields) + "\n"
	
	sure = False
	while !sure:	
		realNovaName = input(novaName + "'s real name: ", )
		sure = True if input("Are you sure? [Y/N]: ") in ["Y", "y"] else False

	if not os.path.exists("../Individual_Novae/" + realNovaName):
		os.system("python3 MakeNewNovaDirectory.py " + realNovaName)

	for fileName in novaDict[novaName]:
		string += ",".join([fileName[0],'0','1','NA','ergs/cm^2/sec',fileName[1],'Williams','','',fileName[2], fileName[3], fileName[4], fileName[5]]) + "\n"
	string = string[:-1]
	
	metadataFilename = "%s_%s_%s_%s_MetaData.csv" %(realNovaName, "Optical", author, "Spectra")
	metadataFile = open("../Individual_Novae/" + realNovaName + "/Data/" + metadataFilename, "w")
	metadataFile.write(string)
	metadataFile.close()

	ticketFields = [realNovaName, "NA", "NA", "Optical", "YYYY-MM-DD", "NA", "Williams, R. 1982", "NA", "False", metadataFilename, "0", "1", "2", "3", "4", "5", "7", "8", "6", "NA", "9", "10", "11,12", "Completed"]
	
	ticketText = ""
	for i in range(len(ticketDataFields)):
		ticketText += ticketDataFields[i] + ticketFields[i] + "\n"
	ticketText = ticketText[:-1]

	author = ticketFields[6].lstrip().split()[0].replace(",", "")
	regime = ticketFields[3].replace(" ", "")
	ticketFilename = "%s_%s_%s_%s.txt" %(realNovaName, regime, author, "Spectra")
		
	ticketFile = open("../Individual_Novae/" + realNovaName + "/Tickets/" + ticketFilename, "w")
	ticketFile.write(ticketText)
	ticketFile.close()
	

