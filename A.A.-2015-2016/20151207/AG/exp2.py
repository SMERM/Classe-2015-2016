import math 
phi= 0.6180339
# t0= inizio del processo
# t1= fine del processo
# w0= dur iniziale della cella
# w1= dur finale della cella
def accelerando(t0, t1, w0, w1):
	totdur= t1-t0 	  
	ftime= totdur*phi # durata del processo di accelerando
	p0= 0.96 # rapporto tra le due funzioni dur e step
	p1= 0.01
	aw= (math.log(w1)-math.log(w0))/(ftime) # coeff ang funzione
	bw= math.log(w0)-(aw*t0) 
	ap= (p1)-(p0)/(ftime) 
	bp= (p0)-(ap*t0) 
	at= t0
	print ";nota con arg %5.2f %5.2f %5.2f %5.2f" % (t0, t1, w0, w1) 
	while (at < t0+ftime):
		w= math.exp(aw*at+bw) # prima funzione lineare (larghezza della finestra) 
		p= (ap*at+bp) # seconda f sul rapporto tra dur e step (percentuale tra dur e step) 
		step= w*p
		dur= w-step
		print "i1 %8.4f %8.4f %8.4f ;w= %7.4f, p= %7.4f, step= %7.4f" % (at, dur, at, w, p, step) # %8.4f argomenti che vengono sost nella stringa
		at= at+w
	print "i1 %8.4f %8.4f %8.4f" % (at, totdur-ftime, at) # %8.4f argomenti che vengono sost nella stringa

