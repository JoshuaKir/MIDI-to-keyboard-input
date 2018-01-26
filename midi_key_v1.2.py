import keyboard
import os
import mido
import mido.backends.rtmidi

print ("Choose the port that is recieving midi")
print(mido.get_input_names())
port = input("write the port name or enter 'default' to use the default port \n")

if port == 'default':
	inport = mido.open_input() 

else:
	inport = mido.open_input(port)

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

