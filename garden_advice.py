def get_season_advice(season):
    """Return gardening advice for the user-provided season.

    Parameters:
        season (str): The season entered by the user.

    Returns:
        str: Advice for the season, or a message if there is none.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


def get_plant_advice(plant_type):
    """Return gardening advice for the user-provided plant type.

    Parameters:
        plant_type (str): The plant type entered by the user.

    Returns:
        str: Advice for the plant type, or a message if there is none.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Ask the user for a season and plant type, then print the advice."""
    # Get the season and plant type from the user
    season = input("Enter the season (summer or winter): ").strip().lower()
    plant_type = input("Enter your plant type (flower or vegetable): ").strip().lower()

    # Combine the season and plant advice into one message
    advice = get_season_advice(season) + "\n" + get_plant_advice(plant_type)

    # Print the generated advice
    print(advice)


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.