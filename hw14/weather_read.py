import csv

def read_col(filename, col_name):
    dataset = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header row
        if col_name not in header:
            raise ValueError(f"'{col_name}' column not found in the file.")
        col_idx = header.index(col_name)
        for row in reader:
            if len(row) > col_idx:  # Check if the row has enough columns
                value = row[col_idx].strip()
                if value:
                    dataset.append(float(value))
    return dataset

def read_col_int(filename, col_name):
    dataset = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header row
        if col_name not in header:
            raise ValueError(f"'{col_name}' column not found in the file.")
        col_idx = header.index(col_name)
        for row in reader:
            if len(row) > col_idx:  # Check if the row has enough columns
                value = row[col_idx].strip()
                if value:
                    dataset.append(int(value))
    return dataset