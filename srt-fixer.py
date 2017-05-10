
import sys
import re
import argparse


parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")
args = parser.parse_args()
filename = args.fname #gia na mporoume na paroume to onoma arxeiou pou exei dwsei o xrhsths
offset = args.offset
#more info https://docs.python.org/3/howto/argparse.html
#print (args.fname)

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
		#print (line) #emfanizei to keimeno san to sts.stdout.write(line)
		rexp = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3})') #vres 00:00:00,000
		# digit = D
		# to pattern einai DD:DD:DD,DDD
		l = rexp.findall(line)
		#print (l)
		if l: #an vrei apotelesmata kane print auta 
			#print(l[0]+" "+l[1]) #emfanizei ta shmeia pou iparxei o xronos
			#se kathe grammh tou keimenou tha vrei duop apotelesmata 
			#epeidi me tin findall ta emfanizei san lista
			#me to l[0] tha paroume to prwto match se kathe grammh kai antistoixa me to l[1]
			#http://stackoverflow.com/questions/29325809/python-re-findall-prints-output-as-list-instead-of-string
			#split : :
			split_start =l[0].split(":") #gia to 1h timi
			split_end = l[1].split(":") #gia thn 2h timi
			split_start = split_start[2] #ta teleutaia mono psifia (auta pou theloume)
			split_end = split_end[2]
			
			rexp = re.compile(r'(,)') #vre to , kai kanto . gia na tairiazei me to format (float)
			
			split_start = rexp.sub(r'.',split_start)
			
			split_end = rexp.sub(r'.',split_end)
			#print (split_start + "->" + split_end)
			first_num_first = split_start[0] #to prwto apo tis kainourgies times
			first_num_second = split_end[0]
			#de mporesa na valw na arxizei to float me 0.
			if (first_num_first=='0'):
				new_split_start = float(split_start)+float(offset) #to orisma otan trexei
				new = "0" + format(new_split_start)
			else:
				new_split_start = float(split_start)+float(offset)
				new = (format(new_split_start))
			#print (line)
			line = str(l)
			
			#print (str(new))
			rexp = re.compile(r'(\.)') #vre to . kai kanto , gia na tairiazei me to format. To \ gia na ginei escpape alliws shmainei ola
			split_start = rexp.sub(r',',split_start)
			
			line = line.replace(str(split_start),str(new))
			#auth thn stimgh h metatrpi exei ginei omws logw twn regex emfanizeta ws lista
			rexp = re.compile(r"(\.)")
			line = rexp.sub(r',',line)
			rexp = re.compile(r"(\[')")
			line = rexp.sub(r'',line)
			rexp = re.compile(r"(', ')")
			line = rexp.sub(r' --> ',line)
			rexp = re.compile(r"('])")
			line = rexp.sub(r'',line)
			line = line + "\n"
		sys.stdout.write(line)
