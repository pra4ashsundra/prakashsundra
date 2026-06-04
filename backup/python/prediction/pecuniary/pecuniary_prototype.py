import json
import openai  # Make sure you have the OpenAI Python package installed

# -----------------------------
# CONFIGURATION
# -----------------------------
openai.api_key = "YOUR_OPENAI_API_KEY"  # Add your API key here

PECUNIARY_FILE = "pecuniary_houses.json"  # 2nd, 6th, 8th, 10th, 11th
BIRTH_DATA_FILE = "birth_data.json"      # Birth chart, planetary strengths, transit, Dasha

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def create_prompt(pecuniary_data, birth_data):
    return f"""
You are an expert Vedic astrologer AI. Generate a comprehensive pecuniary report
based on the birth chart, current Dasha, planetary transits, and planetary strengths.
Use the following data:

Pecuniary Houses Dictionary:
{json.dumps(pecuniary_data, indent=2)}

Birth Data:
{json.dumps(birth_data, indent=2)}

Instructions:
1. Analyze all five pecuniary houses: 2nd, 6th, 8th, 10th, 11th.
2. Provide 3-5 key financial insights per house.
3. Check Marana Karaka Sthanas:
   - Saturn → 1st house
   - Moon → 6th house
   - Rahu → 9th house
   - Sun → 12th house
   - Mercury & Mars → 7th house
   - Jupiter → 3rd house
   - Ketu → 4th house
   If present, mark the planet as dysfunctional and explain the impact.
4. Include optional advice/remedies for malefic influences.
5. Use clear English, structured by house.
6. Output format:

House: 2nd – Income and Assets
- Insight 1: ...
- Insight 2: ...
- Marana Karaka Alert: ...
- Advice: ...

House: 6th – Debts and Obligations
...

Continue for 8th, 10th, 11th.
"""

def generate_report(prompt_text):
    response = openai.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "You are an expert Vedic astrologer."},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    pecuniary_data = load_json(PECUNIARY_FILE)
    birth_data = load_json(BIRTH_DATA_FILE)

    prompt = create_prompt(pecuniary_data, birth_data)
    report = generate_report(prompt)

    # Save the report to a text file
    with open("pecuniary_mega_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("Pecuniary mega-report generated: pecuniary_mega_report.txt")
