import sys
import csv 
import json


def main():
	data = None
	if len(sys.argv) < 2:
		print("Need an argument for the file")
		sys.exit(1)
	
	try:
		with open(sys.argv[1]) as f:
			data = f.read()
	except EnvironmentError:
		print("File not found")
		sys.exit(1)
	data = data.split("\n")
	#Trailing newline and headers are no fun
	data = data[1:len(data) - 1]
	delimiter = ','
	if len(sys.argv) >= 3:
		delimiter = sys.argv[2]
	data = map(lambda x : x.split(delimiter), data)
	num_cols = len(data[0])
	affected_set = []

	for i in range(num_cols):
		if (data[0][i].isdigit()):
			continue	
		d = {}
		counter = 0
		for row in data:
			if row[i][1:-1] not in d:
				d[row[i][1:-1]] = counter
				counter += 1
		for row in data:
			row[i] = d[row[i][1:-1]]
		d['COLUMN_INDEX'] = i
		affected_set.append(d)
	
	with open("output.csv", "wb") as f:
    		writer = csv.writer(f)
		writer.writerows(data)
	print("Output written to: output.csv")
	with open("legend.txt", "wb") as f:
		json.dump(affected_set, f, indent=4)
	print("Legend written to: legend.txt")

if __name__ == '__main__':
	main()
