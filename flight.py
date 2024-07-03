import os
import json
import random
from datetime import datetime, timedelta

# Parameters
N = 5000  # Number of JSON files
M_min = 50  # Minimum number of flights per file
M_max = 100  # Maximum number of flights per file
K_min = 100  # Minimum number of cities
K_max = 200  # Maximum number of cities
L_min = 0.001  # Minimum probability of NULL value (0.1%)
L_max = 0.005  # Maximum probability of NULL value (0.5%)

# Function to generate random dates
def random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Generate random flight data
def generate_flight():
    date = random_date().strftime('%Y-%m-%d')
    origin_city = f"City{random.randint(1, K)}"
    destination_city = f"City{random.randint(1, K)}"
    flight_duration_secs = random.randint(3600, 14400)  # Random duration between 1 to 4 hours
    passengers_on_board = random.randint(50, 300)  # Random number of passengers

    # Introduce null values based on probability L
    if random.random() < L:
        date = None
    if random.random() < L:
        origin_city = None
    if random.random() < L:
        destination_city = None
    if random.random() < L:
        flight_duration_secs = None
    if random.random() < L:
        passengers_on_board = None

    return {
        'date': date,
        'origin_city': origin_city,
        'destination_city': destination_city,
        'flight_duration_secs': flight_duration_secs,
        'passengers_on_board': passengers_on_board
    }

# Generate JSON files
for i in range(N):
    M = random.randint(M_min, M_max)  # Number of flights in this file
    K = random.randint(K_min, K_max)  # Total number of cities
    L = random.uniform(L_min, L_max)  # Probability of NULL value

    flights = []
    for _ in range(M):
        flights.append(generate_flight())

    # Prepare file path and name
    month_year = datetime.now().strftime('%m-%Y')
    origin_city = f"City{random.randint(1, K)}"
    filename = f"tmp/flights/{month_year}-{origin_city}-flights.json"

    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Write flights to JSON file
    with open(filename, 'w') as file:
        json.dump(flights, file, indent=2)

    print(f"Generated file {filename} with {M} flights.")
