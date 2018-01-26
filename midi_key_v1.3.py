import keyboard
import os
import mido
import mido.backends.rtmidi


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        

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
		print("\n Please only use numbers given on the list, or type 'default' \n")
		display_and_take_port()

	elif int(port) < (len(mido.get_input_names()) + 1) and int(port) > 0:
		port = mido.get_input_names()[int(port) - 1]
		return mido.open_input(port)

	else:
		print("\n Please only use numbers given on the list, or type 'default' \n")
		display_and_take_port()

inport = display_and_take_port() 

flag = True

def note_check(note, letter, vel, msg):

	if msg.note == note and vel != 0: # C
		keyboard.send(letter, do_release = False) # W
		print(letter)
		print(msg.type)

	elif vel == 0:	
		keyboard.send(letter, do_release = True) # W
		print("that worked kinda")	
		
while flag == True:
 
	for message in inport:
		try:
			message.velocity
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

