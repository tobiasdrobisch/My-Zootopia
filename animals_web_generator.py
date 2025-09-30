import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html(html):
    with open(html, "r", encoding="utf-8") as file:
        html_string = file.read()
    return html_string

def write_to_html(html, html_string):
    with open(html, "w", encoding="utf-8") as file:
        file.write(html_string)


animals_data = load_data('animals_data.json')
html_data = load_html("animals_template.html")
output = ""

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations")
    animal_type = animal.get("characteristics", {}).get("type")

    if name is not None:
        output += f"Name: {name}\n"
    if diet is not None:
        output += f"Diet: {diet}\n"
    if locations is not None:
        output += f"Location: {locations}\n"
    if animal_type is not None:
        output += f"Type: {animal_type}\n\n"

new_html_string = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
write_to_html("animals.html", new_html_string)