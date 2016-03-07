sr= 44100
kr= 441
ksmps= 100 
nchnls= 1
instr 1
ifreqstart= p4
ifreqend= p5
iamp= ampdb(p6)
kfreq line ifreqstart,p3,ifreqend
aout oscil iamp, kfreq, 1
out aout
endin
