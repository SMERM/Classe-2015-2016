nnote= 500 # numero di note complessive
dur= 0.083 # durata di ciascuna nota
step= dur/3 # distanza tra una nota e quella succ.
n= 0 # variabile pruduzione note
at= 0
while (n < nnote): 
	print "i1 %8.4f %8.4f %8.4f" % (at, dur, at) # %8.4f argomenti che vengono sost nella stringa
	n= n+1 
	at= at+dur+step
