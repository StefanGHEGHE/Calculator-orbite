# Calculator rapid pentru orbite

Am scris scriptul ăsta pentru că aveam nevoie de o modalitate simplă și rapidă să verific parametrii orbitali de bază direct de pe laptop, fără să trec de fiecare dată prin calculatoarele principale de navigație. 

E un tool mic, scris în Python, care îți dă numerele esențiale pe loc.

## Ce face mai exact
* Calculează viteza de menținere pe orbită (în km/s) pentru orice altitudine.
* Îți spune cât durează o rotație completă în jurul Pământului (în minute).
* Dă un avertisment clar dacă altitudinea introdusă scade sub 160 km. De acolo în jos, frecarea atmosferică începe să ne degradeze serios traiectoria și orbita nu mai e stabilă.

## Cum se folosește
Nu ai nevoie de librării externe sau dependențe complicate. Folosește doar modulul `math` standard din Python 3.

1. Rulezi scriptul din terminal:
   ```bash
   python main.py
