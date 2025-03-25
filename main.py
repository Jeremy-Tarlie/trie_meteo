import requests
import choose_sort

url_paris = "https://wttr.in/Paris?format=j1"
url_nantes = "https://wttr.in/Nantes?format=j1"
url_dieppe = "https://wttr.in/Dieppe?format=j1"
url_rennes = "https://wttr.in/Rennes?format=j1"
url_rouen = "https://wttr.in/Rouen?format=j1"

response_paris = requests.get(url_paris)
response_nantes = requests.get(url_nantes)
response_dieppe = requests.get(url_dieppe)
response_rennes = requests.get(url_rennes)
response_rouen = requests.get(url_rouen)

def main():
    print(f"Il fait {response_paris.json()["current_condition"][0]["temp_C"]}°C à Paris")
    print(f"Il fait {response_nantes.json()["current_condition"][0]["temp_C"]}°C à Nantes")
    print(f"Il fait {response_dieppe.json()["current_condition"][0]["temp_C"]}°C à Dieppe")
    print(f"Il fait {response_rennes.json()["current_condition"][0]["temp_C"]}°C à Rennes")
    print(f"Il fait {response_rouen.json()["current_condition"][0]["temp_C"]}°C à Rouen")
    print("--------------------")
    print("Choisissez un type de tri:")
    print("1. Bubble sort")
    print("2. Insertion sort")
    print("3. Quick sort")
    print("4. Selection sort")
    print("5. Quitter")
    sort_type = int(input())
    array = [response_paris.json()["current_condition"][0]["temp_C"], response_nantes.json()["current_condition"][0]["temp_C"], response_dieppe.json()["current_condition"][0]["temp_C"], response_rennes.json()["current_condition"][0]["temp_C"], response_rouen.json()["current_condition"][0]["temp_C"]]
    choose_sort.ChooseSort.choose_sort(array, sort_type)
    

if __name__ == "__main__":
    main()