import datetime

import matplotlib.pyplot as plt

# Beispiel-Daten
daten = {
    '2023-10-01': 120,
    '2023-10-02': 125,
    '2023-10-03': 130,
    '2023-10-04': 128,
    '2023-10-05': 122,
    '2023-10-06': 126,
    '2023-10-07': 124
}

# Daten sortieren
daten = dict(sorted(daten.items()))

# Datum und Blutdruckwerte extrahieren
datum = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in daten.keys()]
blutdruck = list(daten.values())

# Plot erstellen
plt.figure(figsize=(10, 5))
plt.plot(datum, blutdruck, marker='o', linestyle='-', color='b')
plt.title('Blutdruckkurve')
plt.xlabel('Datum')
plt.ylabel('Blutdruck')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()