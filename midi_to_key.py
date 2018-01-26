import keyboard
import os
import mido
import mido.backends.rtmidi

print ("Choose the port that is recieving midi")
print(mido.get_input_names())
port = input("write the port name or enter 'default' to use the default port")

if port == 'default':
	inport = mido.open_input() 

else:
	inport = mido.open_input(port)

flag = True

while flag == True:
 
	for message in inport:
		if message.note == 60: # C
			keyboard.write('w', restore_state_after=False) # W
			print("w")
		if message.note == 62: # D
			keyboard.write('a') # A	
			print("a")
		if message.note == 64: # E
			keyboard.write('s') # S	
			print("s")
		if message.note == 65: # F
			keyboard.write('d') # D	
			print("d")
		if message.note == 67: # G
			keyboard.write('f') # F	
			print("f")
		if message.note == 70: # B Flat
			print("this should end it!")
			inport.close()
			flag = False
			break


