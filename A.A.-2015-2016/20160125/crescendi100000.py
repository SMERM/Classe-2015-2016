import math
import Pro_crescendi_gliss_amp
import random
print "f1 0 4096 10 1"
amp= -30 #Conversione all'incirca di 1000 in db (1000/32768)
num_note= 100
n=0
totdur= 60.0
ampmin= 20*math.log10(100.0/32768)
ampmax= 20*math.log10(1500.0/32768)
amprange= (ampmax-ampmin)/2
ampfreq= 5/totdur
ampoffset= ampmin+amprange
print "; ampmin= %+8.4f, ampmax= %+8.4f, amprange= %+8.4f, ampoffset= %+8.4f" % (ampmin, ampmax, amprange, ampoffset)
while (n < num_note):
	t0= random.random()*totdur
	t1= (totdur-t0-0.5)*random.random()+0.5+t0
	amp= math.sin(2*math.pi*ampfreq*t0)*amprange+ampoffset
	dur= t1-t0
	w0= random.random()*dur/5.0+dur/10.0
	w1= random.random()*dur/5.0+dur/10.0
	f0= random.random()*4800+200
	f1= random.random()*4800+200
	Pro_crescendi_gliss_amp.accelerando_gliss(t0,t1,w0,w1,f0,f1,amp)
	n=n+1
