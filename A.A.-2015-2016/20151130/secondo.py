fdur= 120 # durata totale 
dur= 0.083 
step= dur/20 # distanza tra una nota e quella succ.
n= 0 # variabile pruduzione note
at= 0
while (at < fdur): 
	print "i1 %8.4f %8.4f %8.4f" % (at, dur, at) # %8.4f argomenti che vengono sost nella stringa
	n= n+1  
	at= at+dur+step 
