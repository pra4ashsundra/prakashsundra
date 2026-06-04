import re
import os
from datetime import datetime

# ---------------------------
# Delete the output file if it exists BEFORE doing anything else
# ---------------------------
output_file_path = r'C:\Code\local\python\tools\birth data extract\output.txt'
if os.path.exists(output_file_path):
    os.remove(output_file_path)

# Define input file path
input_file_path = r'C:\Code\local\python\tools\birth data extract\input.txt'

# ---------------------------
# Mapping Dictionaries
# ---------------------------
tithi_to_tamil = {
    "Pratipat": "Pirathipatham",
    "Dvitīyā": "Thvithiyai",
    "Tritīyā": "Thrithiyai",
    "Chaturthī": "Sathurthi",
    "Pañchamī": "Panjami",
    "Shashṭhī": "Sashti",
    "Saptamī": "Sapthami",
    "Ashtami": "Ashtami",
    "Navamī": "Navami",
    "Daśamī": "Dhasami",
    "Ekādaśī": "Eghadhasi",
    "Dvādaśī": "Dhvadhasi",
    "Trayodaśī": "Thrayodasi",
    "Chaturdaśī": "Sathurthasi",
    "Purnima": "Pournami",
    "Amavasya": "Amavasai"
}

shukla_tithi_deities = {
    "Pratipat": "Goddess Kamakshi, Lord Shiva, Lord Kuberan, Goddess Durga",
    "Dvitīyā": "Lord Krisha, Lord Shiva",
    "Tritīyā": "Lord Murugan, Goddess Durga, Lord Hanuman, Lord Narasimha",
    "Chaturthī": "Lord Ganesha",
    "Pañchamī": "Goddess Saraswati, Goddess Vaarahi",
    "Shashṭhī": "Lord Murugan",
    "Saptamī": "Lord Shiva",
    "Ashtami": "Lord Kaalabairavar, Goddess Kaali",
    "Navamī": "Lord Rama or Lord Shiva",
    "Daśamī": "Lord Rama or Lord Shiva",
    "Ekādaśī": "Lord Krishna",
    "Dvādaśī": "Lord Murugan, Goddess Durga, Lord Hanuman, Lord Narasimha",
    "Trayodaśī": "Lord Shiva",
    "Chaturdaśī": "Lord Dakshinamurthy, Lord Murugan, Any gurus or saints",
    "Purnima": "Goddess Durga, Lord Shiva or Pitrus",
    "Amavasya": "Goddess Durga, Lord Shiva or Pitrus"
}

krishna_tithi_deities = {
    "Pratipat": "Goddess Kamakshi, Lord Shiva, Lord Kuberan, Goddess Durga",
    "Dvitīyā": "Lord Krisha, Lord Shiva",
    "Tritīyā": "Lord Murugan, Goddess Durga, Lord Hanuman, Lord Narasimha",
    "Chaturthī": "Lord Ganesha",
    "Pañchamī": "Goddess Saraswati, Goddess Vaarahi",
    "Shashṭhī": "Lord Murugan",
    "Saptamī": "Lordh Shiva",
    "Ashtami": "Goddess Kali, Lord Kaala Bairavar",
    "Navamī": "Lord Rama or Lord Shiva",
    "Daśamī": "Lord Krishna, Lord Shiva, Lord Hanuman, Goddess Kaali or Lord Murugan",
    "Ekādaśī": "Lord Krishna",
    "Dvādaśī": "Vamana, Dhanvantari",
    "Trayodaśī": "Lord Shiva",
    "Chaturdaśī": "Lord Dakshinamurthy, Lord Murugan, Any gurus or saints",
    "Purnima": "Chandra, Satyanarayana",
    "Amavasya": "Kali, Pitru Devatas"
}

raasi_mapping = {
    "Mesh": "Mesham",
    "Vrish": "Rishabam",
    "Vrisch": "Vritchigam",
    "Mith": "Mithunam",
    "Kark": "Kadagam",
    "Simh": "Simham",
    "Kanya": "Kanni",
    "Tula": "Tulam",
    "Vrishchik": "Vritchigam",
    "Dhanu": "Dhanasu",
    "Makar": "Makaram",
    "Kumbh": "Kumbam",
    "Meen": "Meenam"
}

nakshatra_mapping = {
    "Aswini": "Ashvini",
    "Bharani": "Bharani",
    "Krittika": "Kritigai",
    "Rohini": "Rohini",
    "Mrigashira": "Mirugasirisham",
    "Aardra": "Thiruvadhirai",
    "Punarvasu": "Punarpoosam",
    "Pushyami": "Poosam",
    "Aasresha": "Aayiliyam",
    "Magha": "Magam",
    "Poorva Phalguni": "Pooram",
    "Uttara Phalguni": "Uttiram",
    "Hasta": "Hastham",
    "Chitra": "Chitirai",
    "Swati": "Swathi",
    "Vishakha": "Visaagam",
    "Anuraadha": "Anusham",
    "Jyeshtha": "Kehtai",
    "Jyestha": "Kehtai",
    "Mula": "Moolam",
    "Poorvashadha": "Pooradam",
    "Uttarashadha": "Uttiradam",
    "Sravanam": "Tiruvovam",
    "Dhanishtha": "Avittam",
    "Satabhishak": "Sadayam",
    "Poorvabhadra": "Pooratathi",
    "Uttarabhadra": "Uttiratathi",
    "Revati": "Revathi"
}

lagna_mapping = raasi_mapping

# ---------------------------
# Helper Functions
# ---------------------------
def extract_field(text, field_name):
    match = re.search(fr"{field_name}:\s*(.+)", text)
    return match.group(1).strip() if match else "Unknown"

def reformat_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%B %d, %Y")
        return dt.strftime("%d-%m-%Y")
    except:
        return date_str

def reformat_time(time_str):
    for fmt in ("%I:%M:%S %p", "%I:%M %p", "%H:%M:%S", "%H:%M"):
        try:
            dt = datetime.strptime(time_str, fmt)
            return dt.strftime("%H:%M") + " hours"
        except:
            continue
    return time_str

def normalize_tithi(tithi_raw):
    match = re.search(r"(Pratipat|Dvitīyā|Tritīyā|Chaturthī|Pañchamī|Shashṭhī|Saptamī|Ashtami|Navamī|Daśamī|Ekādaśī|Dvādaśī|Trayodaśī|Chaturdaśī|Purnima|Amavasya)", tithi_raw)
    return match.group(1) if match else tithi_raw

def extract_place(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("Place:"):
            if i + 1 < len(lines):
                return lines[i + 1].strip()
            else:
                return "Unknown"
    return "Unknown"

# ---------------------------
# Main Script
# ---------------------------
with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Step 1: Replace file-path line with Name field
content = re.sub(r'^G:\\My Drive\\client data\\(.+)$', r'Name: \1', content, flags=re.MULTILINE)

# Step 2: Extract Fields
name = extract_field(content, 'Name')
dob_raw = extract_field(content, 'Date')
time_raw = extract_field(content, 'Time')
tithi_raw = extract_field(content, 'Tithi')
nakshatra_top = extract_field(content, 'Nakshatra')
varam = extract_field(content, 'Vedic Weekday')
varam = re.match(r"([A-Za-z]+)", varam).group(1) if re.match(r"([A-Za-z]+)", varam) else varam

dob = reformat_date(dob_raw)
time_of_birth = reformat_time(time_raw)
place_of_birth = extract_place(content)

tithi_normalized = normalize_tithi(tithi_raw)

paksha = "shukla"
tithi_lower = tithi_raw.lower()
if "krishna" in tithi_lower:
    paksha = "krishna"
elif "shukla" in tithi_lower:
    paksha = "shukla"

presiding_deity = (
    krishna_tithi_deities.get(tithi_normalized)
    if paksha == "krishna"
    else shukla_tithi_deities.get(tithi_normalized)
)

nakshatra_name = nakshatra_top.split('(')[0].strip()
nakshatra_final = nakshatra_mapping.get(nakshatra_name, nakshatra_name)

lagna_line = next((line for line in content.splitlines() if line.startswith("Lagna")), None)
lagna_sign = "Unknown"
if lagna_line:
    tokens = re.sub(r'\s+', ' ', lagna_line).strip().split(' ')
    if len(tokens) >= 7:
        lagna_sign = tokens[2]
lagna_sign_tamil = lagna_mapping.get(lagna_sign, lagna_sign)

chandra_line = next((line for line in content.splitlines() if line.startswith("Chandra")), None)
nakshatra_pada = "Unknown"
raasi = "Unknown"
if chandra_line:
    tokens = re.sub(r'\s+', ' ', chandra_line).strip().split(' ')
    if len(tokens) >= 9:
        nakshatra_pada = tokens[8]
    if len(tokens) >= 5:
        raasi = tokens[4]
raasi_tamil = raasi_mapping.get(raasi, raasi)

# ---------------------------
# Construct Final Output
# ---------------------------
final_statement = f"""Name: {name}
Vaaram (Hindu calendar): {varam}
Raasi: {raasi_tamil}
Nakshatra: {nakshatra_final}
Nakshatra Pada: {nakshatra_pada}
Date of Birth: {dob}
Place of Birth: {place_of_birth}
Time of Birth: {time_of_birth}
Lagna's Sign: {lagna_sign_tamil}

The following Rasi, Nakshatra and Udhaya Lagnam are based on my approach, developed over 20+ years. If the rasi, nakshatra or the Udhaya Lagnam differs from your expectation, it reflects a different astrological method, *not an error.*

Based on the *Chitrapaksha-Lahiri* calculation, you fall under the graces of 
*{nakshatra_final} nakshatiram, {raasi_tamil} raasi in the {nakshatra_pada} paadam with Udaya Lagnam in {lagna_sign_tamil}*.

*Disclaimer & Service Terms*
Making payment to the following account, is also an agreement to our disclaimer, here
https://vt.tiktok.com/ZSmETLRpb/

Please watch the video for your selected service before making payment. The video explains exactly what the service provides. If you do not understand the video, contact me first. Payment confirms that you have *Watched, Understood, and Accepted* the service as explained.

*If you agree*, please proceed with the payment.
** Please *_DO NOT_* use _phone number_ on Duit Now. Instead, use the following account number:
*Bank Details:*
Bank: Maybank  
Account Number: 112157016763  
Account Holder: Prakash A/L Sundaram

Kindly provide proof of payment.

Thank you.
"""

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(final_statement)

os.startfile(output_file_path)
print(f"\n✅ Data extracted and saved to {output_file_path}")
