import math  
sfdur= 220    # durata totale del pezzo
phi= 0.6180339
ftime= sfdur*phi # durata del processo di accelerando
w0= 2
w1= 0.03
p0= 0.96 # rapporto tra le due funzioni dur e step
p1= 0.01
t0= 0
t1= ftime
aw= (w1-w0)/(t1-t0) # coeff ang funzione
bw= w0-(aw*t0) 
ap= (p1-p0)/(t1-t0) 
bp= p0-(ap*t0) 
at= t0
while (at < ftime):
	w= aw*at+bw # prima funzione lineare (larghezza della finestra) 
	p= ap*at+bp # seconda f sul rapporto tra dur e step (percentuale tra dur e step) 
	step= w*p
	dur= w-step
	print "i1 %8.4f %8.4f %8.4f; w= %8.4f p= %8.4f step= %8.4f" % (at, dur, at, w, p, step) # %8.4f argomenti che vengono sost nella stringa
	at= at+w
print "i1 %8.4f %8.4f %8.4f" % (at, sfdur-ftime, at) # %8.4f argomenti che vengono sost nella stringa

