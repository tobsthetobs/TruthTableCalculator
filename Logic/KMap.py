import pandas as pd

def parse_table(table_data):
    try:
        df = pd.DataFrame(table_data)
        return df
    except Exception as e:
        print(f"Error parsing table: {e}")
        return None

table_data = [
    ["Name", "Age", "City"],
    ["John", 25, "New York"],
    ["Jane", 30, "San Francisco"],
    ["Bob", 22, "Los Angeles"]
]

parsed_table = parse_table(table_data)

if parsed_table is not None:
    print("Parsed Table:")
    print(parsed_table)
