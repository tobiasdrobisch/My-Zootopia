import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations")
    animal_type = animal.get("characteristics", {}).get("type")

    if name is not None:
        print(f"Name: {name}")
    if diet is not None:
        print(f"Diet: {diet}")
    if locations is not None:
        print(f"Location: {locations}")
    if animal_type is not None:
        print(f"Type: {animal_type}")

    print()