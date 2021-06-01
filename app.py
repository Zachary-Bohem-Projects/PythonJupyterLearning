command = ""
previous_command = ""

while True:
	command = input('> ').lower()
	if command == 'start':
		if previous_command != "start":
			print("Car started...")
			previous_command = "start"
		else:
			print("Car is already started...")
	elif command == 'stop':
		if previous_command != 'stop':
			print("Car stopped...")
			previous_command = command
		else:
			print("Car already stopped...")
	elif command == 'help':
		print("""
start - to start the cars
stop - to stop the cars
quit - to quit
		""")
	elif command == "quit":
		break
	else:
		print("Sorry, I don't understand that!")
