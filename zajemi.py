import re
import orodja

url_prve_strani = "https://www.hribi.net/gorovje/julijske_alpe/1"
datoteka = f'prva_stran.html'
orodja.shrani_spletno_stran(url_prve_strani, datoteka)
vsebina = orodja.vsebina_datoteke(datoteka)

vzorec_bloka = r'<tr class="vr.">.*?</td></tr>'

vzorec = r'href="(?P<povezava>.*)">(?P<ime>.*).*?'

for blok in vzorec_bloka.finditer(vsebina):
    gora = vzorec_bloka.search(blok).groupdict()
    popoln_url = "https://www.hribi.net/" + gora['povezava']
    ime = gora['ime']
    datoteka = f'{ime}.html'
    orodja.shrani_spletno_stran(popoln_url, datoteka)
    vsebina2 = orodja.vsebina_datoteke(datoteka)

