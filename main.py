import requests
from database import Database

cities = ["Paris", "Nantes", "Dieppe", "Rennes", "Rouen"]
BASE_URL = "https://wttr.in/{}?format=j1"

def get_weather_data(city):
    """Récupère les données météo d'une ville via l'API"""
    try:
        response = requests.get(BASE_URL.format(city), timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "ville": city,
            "temp_C": int(data["current_condition"][0]["temp_C"])
        }
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données pour {city}: {e}")
        return None

def main():
    db = Database()
    weather_data = []

    for city in cities:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)
            db.insert_data(data)

    for item in weather_data:
        print(f"Il fait {item['temp_C']}°C à {item['ville']}")

    print("--------------------")
    print("Choisissez un type de tri:")
    print("1. Bubble sort")
    print("2. Insertion sort")
    print("3. Quick sort")
    print("4. Selection sort")
    print("5. Quitter")
    
    sort_type = int(input())
    temperatures = [item["temp_C"] for item in weather_data]

    from choose_sort import ChooseSort
    ChooseSort.choose_sort(temperatures, sort_type)

if __name__ == "__main__":
    main()
