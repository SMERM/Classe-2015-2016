sr= 44100
kr= 441
ksmps= 100 
nchnls= 1
instr 1
ifreqstart= p4
ifreqend= p5
kfreq line ifreqstart,p3,ifreqend
aout oscil 10000, kfreq, 1
out aout
endin
