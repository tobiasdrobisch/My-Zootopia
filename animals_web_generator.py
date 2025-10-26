import data_fetcher


def user_input():
    """
    Prompt the user to enter the name of an animal.

    Returns:
        str: Lowercase name of the entered animal.
    """
    animal_input = input("Enter a name of an animal: ").lower()
    return animal_input


def load_html(file_path):
    """
    Load an HTML file and return its content as a string.

    Args:
        file_path (str): Path to the HTML file.

    Returns:
        str: HTML file content.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_to_html(file_path, html_string):
    """
    Write a string of HTML to a file.

    Args:
        file_path (str): Output HTML file name.
        html_string (str): HTML content to write.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_string)


def main():
    """
    Main program logic:
    - Ask the user for an animal name.
    - Fetch data from the API.
    - Fill the HTML template with the animal information.
    - Write the final HTML to 'animals.html'.
    """
    animal_name = user_input()
    animals_data = data_fetcher.fetch_data(animal_name)
    html_template = load_html("animals_template.html")

    # Output string that will replace the placeholder in the template
    output = ""

    # If no data was found, show a message instead of cards
    if not animals_data:
        new_html = html_template.replace(
            "__REPLACE_ANIMALS_INFO__",
            f"The animal '{animal_name}' does not exist."
        )
        write_to_html("animals.html", new_html)
        print("Website was generated to the file animals.html.")
        return

    # Iterate over all returned animals and build HTML list items
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

        if name:
            output += f"<strong>Name:</strong> {name}<br/>\n"
        if diet:
            output += f"<strong>Diet:</strong> {diet}<br/>\n"
        if locations:
            # Convert the list of locations into a human-readable string
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
        if animal_type:
            output += f"<strong>Type:</strong> {animal_type}<br/>\n"

        output += "</p></li>\n"

    # Replace the placeholder in the HTML template and save it
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_to_html("animals.html", new_html)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
