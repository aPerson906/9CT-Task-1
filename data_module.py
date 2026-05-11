import pandas as pd
# =========================
# SEARCH DATA
# =========================
def search_data():
    if data.empty:
        print("No data available.")
        return

    keyword = input("Enter keyword to search: ")

    results = data[data.astype(str).apply(
        lambda row: row.str.contains(keyword, case=False).any(),
        axis=1
    )]

    print("\n=== Search Results ===")

    if results.empty:
        print("No matching records found.")
    else:
        print(results)


# =========================
# UPDATE DATA ENTRY
# =========================
def update_data_entry():
    global data

    if data.empty:
        print("No data available.")
        return

    try:
        row = int(input("Enter row number to update: "))

        print("\nAvailable Columns:")
        for column in data.columns:
            print("-", column)

        column = input("Enter column name exactly as shown: ")

        if column not in data.columns:
            print("Invalid column name.")
            return

        new_value = input("Enter new value: ")

        data.at[row, column] = new_value

        print("Entry updated successfully.")

    except ValueError:
        print("Please enter a valid row number.")

    except Exception as error:
        print("Error:", error)


# =========================
# SAVE CHANGES
# =========================
def save_changes():
    if data.empty:
        print("No data to save.")
        return

    data.to_csv("survey_data.csv", index=False)