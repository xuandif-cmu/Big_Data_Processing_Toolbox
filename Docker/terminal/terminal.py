import os

if __name__ == '__main__':
	print("Welcome to Big Data Processing Application")
	print("Please type the number that corresponds to which application you woule like to run:")
	print("1. Apache Hadoop")
	print("2. Apache Spark")
	print("3. Jupyter Notebook")
	print("4. SonarQube and SonarScanner")
	s = "Type the number here (press any other key to exit)>"

	while True:
		option = input(s)
		if option == "1" : #hadoop
			print("http://35.231.127.135:5000/")
		elif option == "2" : #spark
			print("http://34.138.63.90:8081/")
		elif option == "3" : #jupyter
			print("http://34.75.13.117:8888/")
		elif option == "4": #sonar
			print("http://35.243.226.87:8080/")
		else: 
			break


