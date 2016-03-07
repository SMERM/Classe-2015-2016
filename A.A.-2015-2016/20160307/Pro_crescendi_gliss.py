import math
# t0(inizio del processo), t1(fine del processo), w0(durata iniziale della cella), w1(durata finale della cella) freq0(frequenza iniziale), freq1(frequenza finale)  
phi= 0.6180339
def accelerando_gliss(t0,t1,w0,w1,freq0,freq1,amp):
	totdur= t1-t0
	ftime= totdur*phi # durata del processo di accelerando 
	p0= 0.96 # rapporto tra dur e step
	p1= 0.01
	freqa= (freq1-freq0)/(ftime) # Coefficente angolare funzione frequenza
	freqb= freq0
	aw= (math.log(w1)-math.log(w0))/(ftime) # decrescita esponenziale cella
	bw= (math.log(w0))
	ap= (p1-p0)/(ftime) # decrescita lineare del rapporto tra dur e step
	bp= p0
	at= t0
	dur = 0
	while (at < (t0+ftime)):
		atstart= at-t0
		w= math.exp((aw*atstart)+bw)
		p= ap*atstart+bp
		step= w*p
		dur= w-step
		at= at+w
	finaldur= at+dur
	c= totdur/finaldur # coeff sommatoria
	print ";nota con arg %5.2f %5.2f %5.2f %5.2f %5.2f %5.2f" % (t0, t1, w0, w1, freq0, freq1)
	print ";valori attesi; w0= %5.2f , w1= %5.2f" % (math.exp(bw) , math.exp(ftime*aw+bw))
	print ";valori attesi frequenza; freqa= %8.5f , freqb= %8.5f" % (freqb, freqa*ftime+freqb) 
	print ";valore c; c= %8.5f" % (c) 
	at= t0
	while (at < (t0+ftime)):
		atstart= at-t0
		w= math.exp((aw*atstart)+bw)*c # prima funzione lineare (larghezza cella)
		p= ap*atstart+bp # seconda funzoine lineare (dur/step)
		step= w*p
		dur= w-step
		freqstart= freqa*(atstart)+freqb
		freqend= freqa*(atstart+dur)+freqb
		print "i1 %8.4f %8.4f %8.4f %8.4f %+8.4f; w= %7.4f, p= %7.4f, step= %7.4f" % (at, dur, freqstart, freqend, amp, w, p, step) 
		at= at+w
	print "i1 %8.4f %8.4f %8.4f %8.4f %+8.4f" % (at, totdur-ftime, freq1, freq1, amp) 
