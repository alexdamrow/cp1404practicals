"""
Estimated: 35 minutes
Actual: 50  minutes

"""
"""
Wimbledon winners program
"""


FILE_NAME = "wimbledon.csv"
NAME_INDEX = 2
COUNTRY_INDEX = 1
def main():
    """Wimbledon winners based off number of wins and countries."""
    records = read_file()
    player_to_win, countries = process_records(records)
    print_results(player_to_win, countries)


def print_results(player_to_win, countries):
    """Print the results."""
    print("Wimbledon champions: ")
    for player, win in player_to_win.items():
        print(f"{player} {win}")
    print(f"These {len(countries)} have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))

def process_records(records):
    """Process  records into dictionary and set."""
    player_to_win = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            player_to_win[record[NAME_INDEX]] += 1
        except KeyError:
            player_to_win[record[NAME_INDEX]] = 1
    return player_to_win, countries

def read_file():
    """Read file."""
    records = []
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records











main()