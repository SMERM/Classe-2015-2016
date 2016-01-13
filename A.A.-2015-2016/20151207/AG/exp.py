import math  
sfdur= 240    # durata totale del pezzo
phi= 0.6180339
ftime= sfdur*phi # durata del processo di accelerando
w0= 2
w1= 0.03
p0= 0.96 # rapporto tra le due funzioni dur e step
p1= 0.01
t0= 0
t1= ftime
aw= (math.log(w1)-math.log(w0))/(t1-t0) # coeff ang funzione
bw= math.log(w0)-(aw*t0) 
ap= (math.log(p1)-math.log(p0))/(t1-t0) 
bp= math.log(p0)-(ap*t0) 
at= sfdur-ftime
while (at < sfdur):
	w= math.exp(aw*at+bw) # prima funzione lineare (larghezza della finestra) 
	p= math.exp(ap*at+bp) # seconda f sul rapporto tra dur e step (percentuale tra dur e step) 
	step= w*p
	dur= w-step
	print "i1 %8.4f %8.4f %8.4f" % (at, dur, at) # %8.4f argomenti che vengono sost nella stringa
	at= at+w


