import os

# for file_name in os.listdir("Data"):
file_name = input("AAVSO Data Filename: ")
data = open(file_name, "r")

string = []
while True:
	
	flag = 0
	line = data.readline()
	if not line:
		break
	cols = line.split(",")
	
	try:
		for char in cols[1]:
			if char == "<":
				cols[1] = cols[1][1:]
				flag += 1
	except IndexError:
		continue

	if flag == 1:
		cols[1] += ",1"
	else:
		cols[1] += ",0"
	
	line = ",".join(cols)
	string.append(line)

data.close()

string = "".join(string)

data = open(file_name, "w")
data.write(string)
data.close()
