import time
from linear_search import LinearSearch
from binary_search import BinarySearch

class ChooseSearch:
    @staticmethod
    def choose_search(array, target, search_type):
        algorithms = {
            1: ("Linear Search", LinearSearch().search),
            2: ("Binary Search", BinarySearch.search),
            3: ("Quit", exit)
        }

        if search_type in algorithms:
            name, search_function = algorithms[search_type]
            print(f"Recherche sélectionnée : {name}")

            # Mesure du temps d'exécution
            start_time = time.time()
            result = search_function(array.copy(), target)
            end_time = time.time()

            execution_time = (end_time - start_time) * 1000

            if result != -1:
                print(f"Élément {target} trouvé à l'index {result}")
            else:
                print(f"Élément {target} non trouvé")

            print(f"Recherche effectuée en {execution_time:.2f} ms")

            return result
        else:
            print("Type de recherche invalide.")
            return -1