import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_html(html):
    """Loads an HTML file as a string."""
    with open(html, "r", encoding="utf-8") as file:
        return file.read()


def write_to_html(html, html_string):
    """Writes a string to an HTML file."""
    with open(html, "w", encoding="utf-8") as file:
        file.write(html_string)


animals_data = load_data("animals_data.json")
html_data = load_html("animals_template.html")
output = ""

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations")
    animal_type = animal.get("characteristics", {}).get("type")

    output += (
        '<li class="cards__item">'
        f'<div class="card__title">{name}</div>'
        '<p class="card__text">'
    )

    if name is not None:
        output += f"<strong>Name:</strong> {name}<br/>\n"
    if diet is not None:
        output += f"<strong>Diet:</strong> {diet}<br/>\n"
    if locations:
        if isinstance(locations, list):
            if len(locations) == 1:
                locations_str = locations[0]
            elif len(locations) == 2:
                locations_str = " and ".join(locations)
            else:
                locations_str = ", ".join(locations[:-1]) + " and " + locations[-1]
        else:
            locations_str = str(locations)
        output += f"<strong>Location:</strong> {locations_str}<br/>\n"
    if animal_type is not None:
        output += f"<strong>Type:</strong> {animal_type}<br/>\n\n"

    output += "</p></li>\n"

new_html_string = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
write_to_html("animals.html", new_html_string)
