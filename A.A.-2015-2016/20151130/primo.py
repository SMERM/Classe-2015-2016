nnote= 60 # numero di note complessive 
step= 0.083 # distanza tra una nota e quella succ.
n= 0 # variabile pruduzione note
dur= 1.03**n
at= 0
while (n < nnote): 
	print "i1 %8.4f %8.4f %8.4f" % (at, dur, at) # %8.4f argomenti che vengono sost nella stringa
	n= n+1 
	dur= 1.03**n 
	at= at+dur+step 
