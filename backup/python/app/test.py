import swisseph as swe
from datetime import datetime

# ------------------------
# Settings
# ------------------------
latitude = 3.1390   # Kuala Lumpur
longitude = 101.6869

# Date/time: now
now = datetime.now()
jd_ut = swe.julday(now.year, now.month, now.day,
                   now.hour + now.minute/60 + now.second/3600)

# Planets
planets = {
    "Surya": swe.SUN,
    "Chandra": swe.MOON,
    "Budha": swe.MERCURY,
    "Sukra": swe.VENUS,
    "Mangal": swe.MARS,
    "Guru": swe.JUPITER,
    "Shani": swe.SATURN,
    "Rahu": swe.TRUE_NODE,
    "Ketu": swe.TRUE_NODE
}

# ------------------------
# Sidereal positions using True Lahiri
# ------------------------
swe.set_sid_mode(swe.SIDM_LAHIRI)
ayanamsa = swe.get_ayanamsa(jd_ut)

planet_positions = {}
for name, p in planets.items():
    pos, _ = swe.calc_ut(jd_ut, p, swe.FLG_SWIEPH)
    sidereal = (pos[0] - ayanamsa) % 360
    if name == "Ketu":  # opposite Rahu
        sidereal = (sidereal + 180) % 360
    planet_positions[name] = sidereal

# ------------------------
# Fixed-house template (JH style)
# ------------------------
rasi_names = [
    "Makar", "Kumbh", "Meen", "Mesh", "Vrish", "Mith",
    "Kark", "Simh", "Kanya", "Tula", "Dhanu", "Vrisch"
]

house_table = []
for i in range(12):
    start = i * 30.0
    cusp = start + 17 + 32/60 + 36/3600
    end = ((i + 1) * 30.0) % 360
    house_table.append({
        "number": i+1,
        "start": start,
        "cusp": cusp,
        "end": end,
        "planets": []
    })

# ------------------------
# Assign planets to house
# ------------------------
for planet, lon in planet_positions.items():
    for house in house_table:
        if house["start"] <= lon < house["end"] or (house["start"] > house["end"] and (lon >= house["start"] or lon < house["end"])):
            house["planets"].append(planet)
            break

# ------------------------
# Helper: degrees to dms
# ------------------------
def deg_to_dms(deg):
    d = int(deg % 30)
    m = int((deg - int(deg)) * 60)
    s = ((deg - int(deg)) * 3600) % 60
    return f"{d:02d}' {m:02d}' {s:05.2f}\""

# ------------------------
# Print JH-style table
# ------------------------
print(f"{'House':<6} {'Start':<15} {'Cusp':<15} {'End':<15} Planets in it")
for i, h in enumerate(house_table):
    start_rasi = rasi_names[i]
    cusp_rasi = start_rasi
    end_rasi = rasi_names[(i + 1) % 12]
    planets = ", ".join(h["planets"]) if h["planets"] else "-"
    # House label
    if h["number"] == 1:
        label = "1st"
    elif h["number"] == 2:
        label = "2nd"
    elif h["number"] == 3:
        label = "3rd"
    else:
        label = f"{h['number']}th"

    print(f"{label:<6} {deg_to_dms(h['start'])} {start_rasi:<8} "
          f"{deg_to_dms(h['cusp'])} {cusp_rasi:<8} "
          f"{deg_to_dms(h['end'])} {end_rasi:<8} {planets}")
