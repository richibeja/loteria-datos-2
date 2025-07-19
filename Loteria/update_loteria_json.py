import requests
import json
from datetime import datetime

# URLs de APIs públicas no oficiales
PB_URL = 'https://www.lotteryusa.com/api/draw-results/powerball/us.json'
MM_URL = 'https://www.lotteryusa.com/api/draw-results/megamillions/us.json'

# Obtener resultados Powerball
pb_resp = requests.get(PB_URL)
pb_data = pb_resp.json()[0]  # El más reciente

# Obtener resultados Mega Millions
mm_resp = requests.get(MM_URL)
mm_data = mm_resp.json()[0]  # El más reciente

# Formatear datos para loteria.json
loteria = {
    "powerball": {
        "date": pb_data["draw_date"],
        "numbers": pb_data["winning_numbers"][:-1],
        "powerball": pb_data["winning_numbers"][-1],
        "jackpot": pb_data["jackpot"]
    },
    "megamillions": {
        "date": mm_data["draw_date"],
        "numbers": mm_data["winning_numbers"][:-1],
        "megaball": mm_data["winning_numbers"][-1],
        "jackpot": mm_data["jackpot"]
    }
}

# Convertir números a enteros
loteria["powerball"]["numbers"] = [int(n) for n in loteria["powerball"]["numbers"]]
loteria["powerball"]["powerball"] = int(loteria["powerball"]["powerball"])
loteria["megamillions"]["numbers"] = [int(n) for n in loteria["megamillions"]["numbers"]]
loteria["megamillions"]["megaball"] = int(loteria["megamillions"]["megaball"])

# Guardar archivo
with open('loteria.json', 'w', encoding='utf-8') as f:
    json.dump(loteria, f, ensure_ascii=False, indent=2)

print('Archivo loteria.json actualizado con los últimos resultados.') 