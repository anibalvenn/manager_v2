import os, csv
from app.services.classes.player import Player
from app.services.classes.championship import Championship

current_script_path = os.path.dirname(os.path.abspath(__file__))


# Build the path to the base directory dynamically
base_directory = os.path.join(current_script_path, "../../db/championships")
# base_directory = "db/championships"
playersFileCSV = "db/players.csv"

# Get the directory of the current script/file (start_championship.py)

def start_championship(num_series, num_random_series,  championship_name):
    if not championship_name:
        championship_name = 'hay_Skat'

    create_meisterschafts_directory(championship_name)

    players = []
    with open(playersFileCSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = Player(row['name'], row['sex'], row['birthdate'], row['country'], row['player_id'])
            players.append(player)
    
    championship = Championship(num_series,num_random_series,championship_name,players)

def create_meisterschafts_directory(meisterschafts_name):

    # Ensure the base directory exists
    os.makedirs(base_directory, exist_ok=True)

    # Process the directory name to ensure it's a valid folder name
    safe_directory_name = meisterschafts_name.replace(" ", "_")  # Replace spaces with underscores

    # Full path for the new directory
    full_directory_path = os.path.join(base_directory, safe_directory_name)

    try:
        os.makedirs(full_directory_path, exist_ok=True)  # Create the directory
        print(f"Directory '{full_directory_path}' created.")
        return full_directory_path  # Return the full path of the created directory
    except OSError as error:
        print(f"Error creating directory '{full_directory_path}': {error}")
        return None
