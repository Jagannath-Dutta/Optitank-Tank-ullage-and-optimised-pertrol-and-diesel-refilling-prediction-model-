import pandas as pd
import numpy as np
import csv

file_path = r"D:\Projects\Tank ullage and optimised pertrol and diesel refilling prediction model\optimal_refillation.csv"

header_row = ["petrol_level", "diesel_level", "petrol_drain_rate", "diesel_drain_rate", "optimal_refill_amount", "last_refill_timestamp"]

data_rows = [
    [60, 80, 1, 2, 20], [50, 70, 1.5, 2.5, 25], [40, 60, 2, 3, 30], [35, 55, 2.5, 3.5, 35], [30, 50, 3, 4, 40],
    [25, 45, 3.5, 4.5, 45], [20, 40, 4, 5, 50], [15, 35, 4.5, 5.5, 55], [10, 30, 5, 6, 60], [5, 25, 5.5, 6.5, 65],
    [60, 80, 1.2, 2.2, 22], [50, 70, 1.7, 2.7, 27], [40, 60, 2.2, 3.2, 32], [35, 55, 2.7, 3.7, 37], [30, 50, 3.2, 4.2, 42],
    [25, 45, 3.7, 4.7, 47], [20, 40, 4.2, 5.2, 52], [15, 35, 4.7, 5.7, 57], [10, 30, 5.2, 6.2, 62], [5, 25, 5.7, 6.7, 67],
    [60, 80, 1.4, 2.4, 24], [50, 70, 1.9, 2.9, 29], [40, 60, 2.4, 3.4, 34], [35, 55, 2.9, 3.9, 39], [30, 50, 3.4, 4.4, 44],
    [25, 45, 3.9, 4.9, 49], [20, 40, 4.4, 5.4, 54], [15, 35, 4.9, 5.9, 59], [10, 30, 5.4, 6.4, 64], [5, 25, 5.9, 6.9, 69],
    [60, 80, 1.1, 2.1, 21], [50, 70, 1.6, 2.6, 26], [40, 60, 2.1, 3.1, 31], [35, 55, 2.6, 3.6, 36], [30, 50, 3.1, 4.1, 41],
    [25, 45, 3.6, 4.6, 46], [20, 40, 4.1, 5.1, 51], [15, 35, 4.6, 5.6, 56], [10, 30, 5.1, 6.1, 61], [5, 25, 5.6, 6.6, 66],
    [60, 80, 1.3, 2.3, 23], [50, 70, 1.8, 2.8, 28], [40, 60, 2.3, 3.3, 33], [35, 55, 2.8, 3.8, 38], [30, 50, 3.3, 4.3, 43],
    [25, 45, 3.8, 4.8, 48], [20, 40, 4.3, 5.3, 53], [15, 35, 4.8, 5.8, 58], [10, 30, 5.3, 6.3, 63], [5, 25, 5.8, 6.8, 68]
]

current_time = pd.Timestamp.now()
last_refill_timestamp = current_time - pd.Timedelta(days=10)

for row in data_rows:
    row.append(last_refill_timestamp)

with open(file_path, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header_row)
    csv_writer.writerows(data_rows)

print("CSV file created successfully.")
