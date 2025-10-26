import data_fetcher



def user_input():
    animal_input = input("Enter a name of an animal:").lower()
    return animal_input


def load_html(html):
    """Loads an HTML file as a string."""
    with open(html, "r", encoding="utf-8") as file:
        return file.read()


def write_to_html(html, html_string):
    """Writes a string to an HTML file."""
    with open(html, "w", encoding="utf-8") as file:
        file.write(html_string)


animal = user_input()
animals_data = data_fetcher.fetch_data(animal)
html_data = load_html("animals_template.html")
output = ""
if not animals_data:
    new_html_string = html_data.replace("__REPLACE_ANIMALS_INFO__", f"The animal {animal} doesn't exist.")
    write_to_html("animals.html", new_html_string)
    print("Website was generated to the file animals.html.")
else:
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
    print("Website was successfully generated to the file animals.html.")
