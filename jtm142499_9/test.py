#!/usr/bin/python -tt


print " ------------It is assignment 9--------------- "

############  FOR DETERMINIG BEHAVIOUR OF ANY USER  ############################
		
import sys #This module have command line argument

## List are created for each user and given zero valur
a = [0,0,0,0,0,0,0]
b = [0,0,0,0,0,0,0]
c = [0,0,0,0,0,0,0]
d = [0,0,0,0,0,0,0]
e = [0,0,0,0,0,0,0]
g = [0,0,0,0,0,0,0]




	
contentfile = open( sys.argv[1], 'rU' )#file opened

for line in contentfile:#loop to travell through the text file


##########     COMPUTING FOR A    ###################
	if line[0] == 'A':
		for mood in line.split():# to traverse through each line
			if (mood == ":)") or (mood == ":D"):
				a[0] = a[0] + 1
			if (mood == ":(") or (mood == ":'("):
				a[1] = a[1] + 1
			if (mood == ":P") or (mood == ";)"):
				a[2] = a[2] + 1
			if (mood == ":-o") or (mood == "O_O"):
				a[3] = a[3] + 1
			if (mood == "B-)") or (mood == ";)"):
				a[4] = a[4] + 1
			if (mood == ":-/") or (mood == "=_="):
				a[5] = a[5] + 1
			if (mood == "x-(") or (mood == ">_<"):
				a[6] = a[6] + 1
			
	
##########     COMPUTING FOR B    ###################
	if line[0] == 'B':
		for mood in line.split():# to traverse through each line
			if (mood == ":)") or (mood == ":D"):
				b[0] = b[0] + 1
			if (mood == ":(") or mood == (":'("):
				b[1] = b[1] + 1
			if (mood == ":P") or (mood == ";)"):
				b[2] = b[2] + 1
			if (mood == ":-o") or (mood == "O_O"):
				b[3] = b[3] + 1
			if (mood == "B-)") or (mood == ";)"):
				b[4] = b[4] + 1
			if (mood == ":-/") or (mood == "=_="):
				b[5] = b[5] + 1
			if (mood == "x-(") or (mood == ">_<"):
				b[6] = b[6] + 1
		
##########     COMPUTING FOR C    ###################
	if line[0] == 'C':
		for mood in line.split():# to traverse through each line
			if (mood == ":)") or (mood == ":D"):
				c[0] = c[0] + 1
			if (mood == ":(") or (mood == ":'("):
				c[1] = c[1] + 1
			if (mood == ":P") or (mood == ";)"):
				c[2] = c[2] + 1
			if (mood == ":-o") or (mood == "O_O"):
				c[3] = c[3] + 1
			if (mood == "B-)") or (mood == ";)"):
				c[4] = c[4] + 1
			if (mood == ":-/") or (mood == "=_="):
				c[5] = c[5] + 1
			if (mood == "x-(") or (mood == ">_<"):
				c[6] = c[6] + 1
		
##########     COMPUTING FOR D    ###################
	if line[0] == 'D':
		for mood in line.split():# to traverse through each line
			if (mood == ":)") or (mood == ":D"):
				d[0] = d[0] + 1
			if (mood == ":(") or (mood == ":'("):
				d[1] = d[1] + 1
			if (mood == ":P") or (mood == ";)"):
				d[2] = d[2] + 1
			if (mood == ":-o") or (mood == "O_O"):
				d[3] = d[3] + 1
			if (mood == "B-)") or (mood == ";)"):
				d[4] = d[4] + 1
			if (mood == ":-/") or (mood == "=_="):
				d[5] = d[5] + 1
			if (mood == "x-(") or (mood == ">_<"):
				d[6] = d[6] + 1
		
##########     COMPUTING FOR E  ###################
	if line[0] == 'E':
		for mood in line.split():# to traverse through each line
			if (mood == ":)") or (mood == ":D"):
				e[0] = e[0] + 1
			if (mood == ":(") or (mood == ":'("):
				e[1] = e[1] + 1
			if (mood == ":P") or (mood == ";)"):
				e[2] = e[2] + 1
			if (mood == ":-o") or (mood == "O_O"):
				e[3] = e[3] + 1
			if (mood == "B-)") or (mood == ";)"):
				e[4] = e[4] + 1
			if (mood == ":-/") or (mood == "=_="):
				e[5] = e[5] + 1
			if (mood == "x-(") or (mood == ">_<"):
				e[6] = e[6] + 1
##########     COMPUTING FOR G   ###################
	if line[0] == 'G':
		for mood in line.split():# to traverse through each line
			if (mood == ":)") or (mood == ":D"):
				g[0] = g[0] + 1
			if (mood == ":(") or (mood == ":'("):
				g[1] = g[1] + 1
			if (mood == ":P") or (mood == ";)"):
				g[2] = g[2] + 1
			if (mood == ":-o") or (mood == "O_O"):
				g[3] = g[3] + 1
			if (mood == "B-)") or (mood == ";)"):
				g[4] = g[4] + 1
			if (mood == ":-/") or (mood == "=_="):
				g[5] = g[5] + 1
			if (mood == "x-(") or (mood == ">_<"):
				g[6] = g[6] + 1
		
contentfile.close()#FILE CLOSED

 
#########   METHOD FOR DETERMINING BEHAVIOUR OF USERS  ##########
def findBehaviour(mylist):
	maxm = 0
	for num in mylist:
		if num > maxm:
			maxm = num#FINDING THE MAXIMUM NO IN LIST

	if mylist[0] == maxm:
		return "Happy"	
	if mylist[1] == maxm:
		return "Sad"
	if mylist[2] == maxm:
		return "Sarcastic"
	if mylist[3] == maxm:
		return "Surprised"
	if mylist[4] == maxm:
		return	"Crook"
	if mylist[5] == maxm:
		return	"Neutral" 
	if mylist[6] == maxm:
		return "Angry"



print "..........Behaviour of different users................"
print "A is ",findBehaviour(a)
print "B is ",findBehaviour(b)
print "C is ",findBehaviour(c)
print "D is ",findBehaviour(d)
print "E is ",findBehaviour(e)
print "G is ",findBehaviour(g)





########################################   FOR FINDING PERCENTAGE OF MOODS USED  #####################################
Happy = 0    
Sad = 0       
Sarcastic = 0    
Surprised = 0    
Crook = 0    
Neutral = 0   
Angry = 0


##########    CALCULATING FREQUENCY OF EACH MOOD   ##########
happy = a[0] + b[0] + c[0] + d[0] + e[0] + g[0]
sad = a[1] + b[1] + c[1] + d[1] + e[1] + g[1]
Sarcastic = a[2] + b[2] + c[2] + d[2] + e[2] + g[2]
Surprised = a[3] + b[3] + c[3] + d[3] + e[3] + g[3]
Crook = a[4] + b[4] + c[4] + d[4] + e[4] + g[4]
Neutral = a[5] + b[5] + c[5] + d[5] + e[5] + g[5]
Angry = a[6] + b[6] + c[6] + d[6] + e[6] + g[6]

Total = happy + sad + Sarcastic + Surprised + Crook + Neutral + Angry# TOTAL NO. OF MOODS USED
##############   CALCULATING PERCENTAGE FOR DIFFERENT MODES  ###############
per1=float(happy)*(100/Total)
per2=float(sad)*(100/Total)
per3=float(Sarcastic)*(100/Total)
per4=float(Surprised)*(100/Total)
per5=float(Crook)*(100/Total)
per6=float(Neutral)*(100/Total)
per7=float(Angry)*(100/Total)

print "----------------------------------------------------------------------"
print "......Percentage of different moods used............"
print "Happy :",per1
print "Sad",per2
print "Sarcastic",per3
print "Surprised",per4
print "Crook",per5
print "Neutral",per6
print "Angry",per7
 
		
	

