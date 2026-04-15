import pandas as pd
from pathlib import Path

# Find all csv files inside the data folder
data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

all_dataframes = []

for file in csv_files:
    # Read one csv file
    df = pd.read_csv(file)

    # Clean column names by removing extra spaces
    df.columns = df.columns.str.strip()

    # Keep only rows where product is Pink Morsel
    df["product"] = df["product"].astype(str).str.strip().str.lower()
    df = df[df["product"] == "pink morsel"]

    # Clean the price column by removing the dollar sign
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.strip()
        .astype(float)
    )

    # Make quantity numeric
    df["quantity"] = pd.to_numeric(df["quantity"])

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep only the columns needed
    df = df[["Sales", "date", "region"]]

    # Rename columns to match the task output
    df.columns = ["Sales", "Date", "Region"]

    # Add cleaned dataframe to list
    all_dataframes.append(df)

# Combine all three files into one dataframe
final_df = pd.concat(all_dataframes, ignore_index=True)

# Save final output
final_df.to_csv("formatted_output.csv", index=False)

print("Done. formatted_output.csv has been created.")