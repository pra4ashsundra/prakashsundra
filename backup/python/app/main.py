import os
from dotenv import load_dotenv
import openai
import random

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Sample planetary positions for tomorrow (replace with real data later)
planet_positions_tomorrow = {
    "Surya": "Simha 16°00'",
    "Chandra": "Dhanu 2°00'",
    "Budha": "Simha 4°00'",
    "Shukra": "Karka 14°00'",
    "Mangal": "Kanya 22°30'",
    "Guru": "Mithuna 23°50'",
    "Shani": "Meena 5°50'",
    "Rahu": "Kumbha 24°39'",
    "Ketu": "Simha 24°39'"
}

# Vedic terms in Tamil Romanized
rasi_list = [
    "Mesha", "Rishabam", "Midhunam", "Kadagam", "Simham", "Kanni",
    "Thulam", "Viruchigam", "Dhanusu", "Makaram", "Kumbam", "Meenam"
]

# Grahas in Tamil Romanized
planet_map = {
    "Surya": "Surya",
    "Chandra": "Chandra",
    "Budha": "Budha",
    "Shukra": "Sukra",
    "Mangal": "Mangal",
    "Guru": "Guru",
    "Shani": "Shani",
    "Rahu": "Rahu",
    "Ketu": "Ketu"
}

# Function to pick icon based on luck %
def luck_icon(luck):
    if luck < 40:
        return "🔴"
    elif luck <= 70:
        return "🟡"
    else:
        return "🟢"

# Generate Rasi Palan for each Rasi
for rasi in rasi_list:
    luck_percent = random.randint(30, 90)  # Replace with real calculation if available
    icon = luck_icon(luck_percent)

    prompt = f"""
    You are a Vedic astrologer. Using these planetary positions for tomorrow,
    write a short, WhatsApp-friendly Rasi Palan for {rasi}.
    Keep it concise (1-2 lines), motivational, and useful.
    Include a short tip starting with 'Tip: ...'.
    Keep planets in Tamil Romanized terms.
    Format like this example:

    *Kadagam Rasi Palan*
    A surge of creativity and emotional strength is on the horizon. Use this time to express your feelings and share your ideas openly!
    _Tip:_ Good for collaborations and artistic pursuits. Embrace teamwork!
    _Luck:_ 59% 🟡

    Planetary positions:
    {planet_positions_tomorrow}
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful Vedic astrology assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    message = response.choices[0].message.content
    print(message + f"\n_Luck:_ {luck_percent}% {icon}\n")
