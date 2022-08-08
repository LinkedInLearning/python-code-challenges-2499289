vmax = 120  # km/h
vmax_s = vmax / 3600 # km/s

regelzeit_m = 7 # Minuten
regelzeit_s = regelzeit_m * 60 # Sekunden
weg = 10  # km


# Gschwindigkeit = Weg / Zeit


v_durchschnitt_m = weg/regelzeit_m # km/min


v_durchschnitt_s = v_durchschnitt_m / 60 # km/s

print (v_durchschnitt_m) # Geschwindigkeit in Kilometer / Minute
print (v_durchschnitt_m * 60) # Geschwindigkeit in Kilometer / Stunde


verkuerzte_zeiten = (regelzeit_s - 10, regelzeit_s - 20, regelzeit_s - 30,
 regelzeit_s - 40, regelzeit_s - 50, regelzeit_s - 50,
 regelzeit_s - 70, regelzeit_s - 80, regelzeit_s - 90,
 regelzeit_s - 100, regelzeit_s - 110, regelzeit_s - 120)

for i in verkuerzte_zeiten:
    print(weg / i * 3600)  # Erhöhte km/h

max_verzoegerung = weg/vmax_s  

print(max_verzoegerung)  # Minimale Zeit in Sekunden für die Strecke


