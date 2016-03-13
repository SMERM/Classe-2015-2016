import math
# t0(inizio del processo), t1(fine del processo), w0(durata iniziale della cella), w1(durata finale della cella) freq0(frequenza iniziale), freq1(frequenza finale)  
phi= 0.6180339
def accelerando_gliss(t0,t1,w0,w1,freq0min,freq0max,freq1min,freq1max,ampfreq,amprange,ampoffset):
	totdur= t1-t0
	ftime= totdur*phi # durata del processo di accelerando 
	p0= 0.96 # rapporto tra dur e step
	p1= 0.01
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
		freq0a= (freq0max-freq0min)/(ftime)
		freq0b= freq0max
		freq1a= (freq1max-freq1min)/(ftime)
		freq1b= freq1max
		freq0= freq0a*(atstart)+freq0b
		freq1= freq1a*(atstart)+freq1b
		freqa= (freq1-freq0)/(ftime) # Coefficente angolare funzione frequenza
		freqb= freq0
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
		ampstart= math.sin(2*math.pi*ampfreq*at)*amprange+ampoffset
		ampend= math.sin(2*math.pi*ampfreq*(at+dur))*amprange+ampoffset
		freqstart= freqa*(atstart)+freqb
		freqend= freqa*(atstart+dur)+freqb
		print "i1 %8.4f %8.4f %8.4f %8.4f %+8.4f %+8.4f; w= %7.4f, p= %7.4f, step= %7.4f" % (at, dur, freqstart, freqend, ampstart, ampend, w, p, step) 
		at= at+w
	ampstart= math.sin(2*math.pi*ampfreq*at)*amprange+ampoffset
	ampend= math.sin(2*math.pi*ampfreq*(at+dur))*amprange+ampoffset
	print "i1 %8.4f %8.4f %8.4f %8.4f %+8.4f %+8.4f" % (at, totdur-ftime, freq1, freq1, ampstart, ampend) 
