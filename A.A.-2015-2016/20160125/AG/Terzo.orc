sr= 44100
kr= 441
ksmps= 100 
nchnls= 1
instr 1
ifreqstart= p4
ifreqend= p5
iampstart= p6
iampend= p7
kamp line iampstart,p3, iampend
kfreq line ifreqstart,p3,ifreqend
aout oscil ampdbfs(kamp), kfreq, 1
out aout
endin
