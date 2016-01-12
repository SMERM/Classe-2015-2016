import math 
# t0: punto di partenza del processo
# t1: fine del processo
# w0: durata iniziale della cella
# w1: durata finale della cella
phi= 0.6180339 # s aurea
def accelerando(t0,t1,w0,w1):
	totdur= t1-t0
 	ftime= totdur*phi # durata del processo di accelerando
	p0= 0.96 #rapporto tra le due funzioni dur e step
	p1= 0.01 # fine del rapporto
        aw= (math.log(w1)-math.log(w0))/ftime # coeff angolare pendenza
	bw=  math.log(w0)-(aw*t0) # quota, altezza della retta dall origine w
	ap= (math.log(p1)-math.log(p0))/ftime # coeff angolare del rapporto tra le funz dur e step
	bp= math.log(p0)-(ap*t0) # quota della retta  p
	at= t0 # dove parte la riproduzione e il processo di accellerando
	print ";nota con arg %5.2f %5.2f %5.2f %5.2f" % (t0,t1,w0,w1)
	while (at < t0+ftime):
		w= math.exp(aw*at+bw)  # prima funz lineare (larghezza finestra)
		p= math.exp(ap*at+bp) # seconda funz sul rapporto tra dur e step 
		step= w*p # distanza vuota tra una nota e l altra
		dur= w-step # durata di ogni singola nota
		print "i1 %8.4f %8.4f %8.4f ;w=%7.4f,p=%7.4f,step= %7.4f" % (at, dur, at,w,p, step)
		at= at+w # trigger
	print "i1 %8.4f %8.4f %8.4f" % (at,totdur-ftime, at) # pezzo continua normalmente dopo il processo di accellerando 
 
