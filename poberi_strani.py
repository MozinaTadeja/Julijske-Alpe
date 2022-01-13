import re
import orodja

url_prve_strani = "https://www.hribi.net/gorovje/julijske_alpe/1"
datoteka = f'prva_stran.html'
orodja.shrani_spletno_stran(url_prve_strani, datoteka)
vsebina = orodja.vsebina_datoteke(datoteka)

vzorec = r'(\/|\d)\d">(?P<ime>.*)</a></td>.*?<a href="(?P<povezava>.*?)">\d\d\d'

for blok in re.findall(vzorec, vsebina):
    krneki, ime_gore, delni_url = blok
    ime_gore_brez_slasha = ime_gore.replace("/", "-")
    print(ime_gore_brez_slasha)
    popoln_url = "https://www.hribi.net" + delni_url
    datoteka = f'gore/{ime_gore_brez_slasha}.html'
    orodja.shrani_spletno_stran(popoln_url, datoteka)
    vsebina2 = orodja.vsebina_datoteke(datoteka)

