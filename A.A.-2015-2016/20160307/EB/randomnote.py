import Pro_crescendi_gliss
import random
import math
print "f1 0 4096 10 1"
amp= -30 # conversione di 1000 amps in db (1000/32769) 
num_note= 100
n= 0
totdur= 60.0 
ampmin= 20*math.log10(100.0/32768)
ampmax= 20*math.log10(1000.0/32768)
amprange= (ampmax-ampmin)/2 #ampiezza dell'oscillazione in db (-6 sarebbe diviso 2 in db)
ampfreq= 5/totdur
ampoffset= ampmin+amprange
print "; ampmin= %+8.4f , ampmax= %+8.4f , amprange= %+8.4f , ampoffset= %+8.4f" % (ampmin, ampmax, amprange, ampoffset)   
while (n < num_note):
	t0= random.random()*totdur
	t1= totdur-t0-0.5*random.random()+0.5+t0 # 0.5 fattore minimo di durata della nota
	dur= t1-t0
	w0= random.random()*(dur/5)+(dur/10)   
	w1= random.random()*(dur/5)+(dur/10)  # larghezza cella, se minore acc se mag decel
	f0min= random.random()*1+200
	f0max= random.random()*1+1000	
	f1min= random.random()*1+4200
	f1max= random.random()*1+5000
	
	Pro_crescendi_gliss.accelerando_gliss(t0 ,t1 ,w0 ,w1 ,f0min, f0max, f1min, f1max ,ampfreq ,amprange ,ampoffset) 
	n= n+1
