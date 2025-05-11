import os
import subprocess

# clears the terminal and gets the user's desktop directory
os.system("clear")
o = subprocess.check_output("whoami", shell=True).strip()
desktop = "/home/" + o.decode('utf-8') + "/Desktop"
i = ""

# while loop that exits when "quit" is entered as input
while i != "quit":
	# asks user for input
	i = input("What file would you like to create a shortcut for?: ")
	# if "quit" is entered, tells the user that they exited the script, else continues on with the rest of the script
	if i == "quit":
		print("Exited Script")
	else:
		# finds the file while redirecting all errors to /dev/null
		o1 = os.popen("sudo find / -name " + i + " 2>/dev/null").read()
		filePath = o1[:o1.find(i) + len(i)]
		# if the find returns nothing, tells the user that the file doesn't exist, else continue on with the script
		if filePath == "":
			print("File does not exist")
		else:
			# links the file to the user's desktop
			os.system("ln -s " + filePath + " " + desktop)
			# gets current working directory and tells the user it
			o2 = os.popen("pwd").read().strip()
			print("Your current directory is " + o2 + ".")
			# informs the user if they are not in their desktop directory
			if o2 != desktop:
				print("You are currently not in your desktop directory.")
			# gets the number of symbolic links in user's desktop directory by finding it and printing l which is then counted
			o3 = os.popen("find " + desktop + " -type l -printf l").read()
			numLinks = os.popen("echo " + o3 + " | grep -o 'l' | wc -l").read().strip()
			print("There are " + numLinks + " symbolic links in your desktop directory.")
			# lists out the symbolic links as well as their target paths at the end
			os.system("ls -l " + desktop + " | grep ^l")
