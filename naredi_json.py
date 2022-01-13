import re
import orodja
import os

vzorec = re.compile( r'<title>(?P<ime>.*?)</title>.*?'
    r'Višina:</b>\s(?P<visina>\d+)&nbsp.*?'
    r'Vrsta:</b>\s(?P<vrsta>.*?)</div>.*?'
    r'Ogledov:</b> (?P<ogledi>.*?)</div>.*?'
    r'Priljubljenost:.*?\((?P<priljubljenost>\d+).&.*?'
    r'Število slik:.*?slike">(?P<stevilo_slik>\d+)</a>.*?'
    r'Število poti:.*?poti">(?P<stevilo_poti>\d+)</a></div>.*?'
    r'Število GPS sledi:.*?GPS sledi">(?P<stevilo_gps_sledi>\d+)</a>',re.DOTALL)
vzorec_stevila_vpisov_v_vpisni_knjigi =    r'Vpisna knjiga:.*?Število vpisov v vpisni knjigi">(?P<stevilo_vpisov_v_vpisni_knjigi>\d+)</a>'

seznam = []
for filename in os.listdir("gore"):
    ime = "gore/" + filename
    vsebina = orodja.vsebina_datoteke(ime)
    slovar = re.search(vzorec, vsebina).groupdict()
    stevilo_vpisov_v_vpisni_knjigi = re.search(vzorec_stevila_vpisov_v_vpisni_knjigi, vsebina)
    if stevilo_vpisov_v_vpisni_knjigi:
        slovar['stevilo_vpisov_v_vpisni_knjigi'] = stevilo_vpisov_v_vpisni_knjigi['stevilo_vpisov_v_vpisni_knjigi']
    else:
        slovar['stevilo_vpisov_v_vpisni_knjigi'] = None
    slovar['ogledi'] = slovar['ogledi'].replace(".","")
    seznam.append(slovar)

print(seznam)
print(len(seznam))
orodja.zapisi_json(seznam, "obdelani-podatki/hribi.json")  
orodja.zapisi_csv(seznam, ["ime", "visina", "vrsta", "ogledi", "priljubljenost", "stevilo_slik", "stevilo_poti", "stevilo_gps_sledi", "stevilo_vpisov_v_vpisni_knjigi"], "obdelani-podatki/hribi.csv")