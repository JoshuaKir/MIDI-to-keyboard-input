import keyboard
import os
import mido
import mido.backends.rtmidi

#Function for testing if a string is a usable number
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
#Function for displaying and choosing the midi port. The function will call itself again when an unusable answer is given. 
def display_and_take_port(): 
	input_list = 0
	print ("Choose the port that is recieving midi \n")
	while input_list < len(mido.get_input_names()): 
		print(mido.get_input_names()[input_list], '[', input_list + 1, ']', "\n")
		input_list = input_list + 1
	
	port = input("Enter the corresponding port number of the port you would like to use to recieve midi or enter 'default' to use the computer's default port \n")

	if port == 'default':
		return mido.open_input() 

	elif is_number(port) == False:
		print("\n Please only use numbers given on the list, or type 'default' \n")
		display_and_take_port()		

	elif int(port) > (len(mido.get_input_names()) + 1) and int(port) < 0:
		print("\n Please only use numbers given on the list, this number was either above or below the list. \n")
		display_and_take_port()

	elif int(port) < (len(mido.get_input_names()) + 1) and int(port) > 0:
		port = mido.get_input_names()[int(port) - 1]
		return mido.open_input(port)

	else:
		print("\n Please only use numbers given on the list, or type 'default' \n")
		display_and_take_port()

#sets the port
inport = display_and_take_port() 

print("You are using", inport, "to recieve midi \n", "Midi note Key: \n", "60 = W \n", "62 = A \n", "64 = S \n", "65 = D \n", "67 = F \n", "70 = Close this progeam \n")

flag = True

#This function handles reading the midi and outputting button presses
def note_check(note, letter, vel, msg):

	if msg.note == note and vel != 0 and msg.type != "note_off": 
		keyboard.send(letter, do_release = False) 
		print(letter)
		print(msg.type)

	elif msg.note == note and (vel == 0 or msg.type == "note_off"):	
		keyboard.send(letter, do_release = True) 
		print(msg.type)	
		
while flag == True:
 
 	#This is just the main loop really
	for message in inport:
		try:
			message.velocity
		except AttributeError:
			break

		try:
			message.note
		except AttributeError:
			break	

		note_check(60, 'w', message.velocity, message)

		note_check(62, 'a', message.velocity, message)

		note_check(64, 's', message.velocity, message)

		note_check(65, 'd', message.velocity, message)

		note_check(67, 'f', message.velocity, message)	
		
		if message.note == 70: # B Flat
			print("this should end it!")
			inport.close()
			flag = False
			break

