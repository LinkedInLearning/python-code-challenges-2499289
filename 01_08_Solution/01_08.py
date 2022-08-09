vmax = 120  # km/h
vmax_s = vmax / 3600 # km/s

regelzeit_m = 7 # Minuten
regelzeit_s = regelzeit_m * 60 # Sekunden
weg = 10  # km


# Geschwindigkeit = Weg / Zeit


v_durchschnitt_m = weg/regelzeit_m # km/min


v_durchschnitt_s = v_durchschnitt_m / 60 # km/s

# Geschwindigkeit in Kilometer / Minute
print("Geschwindigkeit in Kilometer / Minute:", v_durchschnitt_m)
# Geschwindigkeit in Kilometer / Stunde
print("Geschwindigkeit in Kilometer / Stunde:", v_durchschnitt_m * 60)


verkuerzte_zeiten = (regelzeit_s - 10, regelzeit_s - 20, regelzeit_s - 30,
 regelzeit_s - 40, regelzeit_s - 50, regelzeit_s - 50,
 regelzeit_s - 70, regelzeit_s - 80, regelzeit_s - 90,
 regelzeit_s - 100, regelzeit_s - 110, regelzeit_s - 120)

for i in verkuerzte_zeiten:
    print("Km/h bei ", i, "Sekunden für den Weg:", weg / i * 3600)  # Erhöhte km/h

max_verzoegerung = weg/vmax_s  

# Minimale Zeit in Sekunden für die Strecke
print("Minimale Zeit in Sekunden für die Strecke:", max_verzoegerung)




