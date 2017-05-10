
import sys
import re
import argparse


parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

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
		if l:  
			#print(l[0]+" "+l[1]) 
			#http://stackoverflow.com/questions/29325809/python-re-findall-prints-output-as-list-instead-of-string
			#split : :
			split_start =l[0].split(":")
			split_end = l[1].split(":") 
			split_start = split_start[2] 
			split_end = split_end[2]
			
			rexp = re.compile(r'(,)')
			
			split_start = rexp.sub(r'.',split_start)
			
			split_end = rexp.sub(r'.',split_end)
			#print (split_start + "->" + split_end)
			first_num_first = split_start[0] 
			first_num_second = split_end[0]
			
			if (first_num_first=='0'):
				new_split_start = float(split_start)+float(offset) #to orisma otan trexei
				new = "0" + format(new_split_start)
			else:
				new_split_start = float(split_start)+float(offset)
				new = (format(new_split_start))
			#print (line)
			line = str(l)
			
			#print (str(new))
			rexp = re.compile(r'(\.)') 
			split_start = rexp.sub(r',',split_start)
			
			line = line.replace(str(split_start),str(new))
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
