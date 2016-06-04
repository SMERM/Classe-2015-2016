# Lezione di lunedì 30 maggio 2016

## Argomenti

* Realizzazione parziale dell'accesso a `freesound.org` attraverso la sua
  *API*
```python
import freesound, sys,os
API_KEY="myFaYH1c1cSL3G6PFzIDsV1soqz9PpEoiZYa1RhT"
mm=23.0 #bpm
semiminima=60.0/mm
G3= 261.6*(2**(7.0/12.0))
Bb= 261.6*(2**(10.0/12.0))
Eb= 261.6*(2**(3.0/12.0))


c = freesound.FreesoundClient()
c.set_token(API_KEY,"token")
#filter="duration:[0.01 TO %8.4f]&descriptors_filter=lowlevel.pitch.mean:[%8.4f TO %8.4f]"  % (semiminima,G3*0.95, G3*1.05) 
filter="duration:[0.01 TO %8.4f]" % (semiminima)
fields="id,name,duration,analysis&descriptors=lowlevel.spectral_centroid,lowlevel.pitch.mean"
query= "sci-fi"
results = c.text_search(query=query,filter=filter,fields=fields)
print results.count
page = 15
npages = results.count/page
p = 1
while (p<=npages):
        results = c.text_search(query=query,filter=filter,fields=fields,page=p)
        for sound in results:
                print(sound.as_dict())
                
        p = p+1

```
