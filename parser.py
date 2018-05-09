import os

email_data = open("email_data.txt", "w+")

def clean_item(item):
	item = item.split(" on ")[0]
	item = item.split("/")[0]
	item = item.split(" [")[0]
	return item

def parse_line(line):
	if ';' in line:
		return line.split(";")
	if line.count(",") > 1:
		return line.split(",")
	if line.count(",") == 1 and line.count("@") > 1:
		return line.split(",")

	return line


def extract_email_header(email):
	f = open(email)
	try:
		while True:
			line = f.readline()
			if line == '':
				break
			if "From:" in line and "X-" not in line and ">" not in line:
				line = line.strip('\n')
				line = clean_item(line)
				line2 = f.readline()
				if line2 == '':
					break
				if "Sent:" in line2:
					line2 = f.readline()
				if "To:" in line2 and "X-" not in line2 and ">" not in line2:
					line2 = line2.strip('\n')
					while True:
						line3 = f.readline().strip('\n').strip('\t')
						if ':' in line3 or line3 == '':
							break
						line2 = line2 + line3
						line3 = line3.strip('\n')
						line3 = line3.strip('\t')

					line2 = line2.replace("To:", "")
					recipients = parse_line(line2)
					if type(recipients) == list:
						for person in recipients:
							person = clean_item(person)
							email_data.write(line + '\n')
							email_data.write("To:" + person + '\n')
					else:
						recipients = clean_item(recipients)
						email_data.write(line + '\n')
						email_data.write("To:" + recipients + '\n')


	except UnicodeDecodeError:
		f.close()
		return
	f.close()


def find_email_file(file_path):
	print(file_path)
	for email in os.listdir(file_path):
		email = os.path.join(file_path, email)
		if os.path.isfile(email):
			extract_email_header(email)
		else:
			find_email_file(email)


find_email_file("data_set")
