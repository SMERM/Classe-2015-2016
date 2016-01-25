import math
# t0(inizio del processo), t1(fine del processo), w0(durata iniziale della cella), w1(durata finale della cella)  
phi= 0.6180339
def accelerando(t0,t1,w0,w1,freq):
	totdur= t1-t0
	ftime= totdur*phi # durata del processo di accelerando 
	p0= 0.96 # rapporto tra dur e step
	p1= 0.01
	aw= (math.log(w1)-math.log(w0))/(ftime) # decrescita esponenziale cella
	bw= (math.log(w0))-((aw)*(t0))
	ap= (p1-p0)/(t1-t0) # decrescita esponenziale del rapporto tra dur e step
	bp= p0-(ap*t0)
	at= t0
	print ";nota con arg %5.2f %5.2f %5.2f %5.2f %5.2f" % (t0, t1, w0, w1, freq)
	while (at < (t0+ftime)):
		w= math.exp((aw*at)+bw) # prima funzione lineare (larghezza cella)
		p= ap*at+bp # seconda funzoine lineare (dur/step)
		step= w*p
		dur= w-step
		print "i1 %8.4f %8.4f %8.4f ; w= %7.4f, p= %7.4f, step= %7.4f" % (at, dur, freq, w, p, step) 
		at= at+w
	print "i1 %8.4f %8.4f %8.4f" % (at, totdur-ftime, freq)
