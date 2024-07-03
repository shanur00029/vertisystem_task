import os
import json
import glob
import statistics
from collections import defaultdict
import time

# Function to process JSON files
def process_json_files(directory):
    total_records = 0
    dirty_records = 0
    flights_data = []
    start_time = time.time()

    # Dictionary to track passengers arrived and left
    passengers_arrived = defaultdict(int)
    passengers_left = defaultdict(int)

    # Dictionary to store flight durations by destination city
    flight_durations = defaultdict(list)

    # Process each JSON file in the directory
    for file_path in glob.glob(os.path.join(directory, '*.json')):
        with open(file_path, 'r') as file:
            try:
                flights = json.load(file)
                total_records += len(flights)

                for flight in flights:
                    # Check for dirty records
                    if any(value is None for value in flight.values()):
                        dirty_records += 1
                    
                    # Count passengers arriving and leaving
                    if flight['origin_city'] is not None:
                        passengers_left[flight['origin_city']] += flight['passengers_on_board'] or 0
                    if flight['destination_city'] is not None:
                        passengers_arrived[flight['destination_city']] += flight['passengers_on_board'] or 0

                    # Collect flight durations by destination city
                    if flight['destination_city'] is not None and flight['flight_duration_secs'] is not None:
                        flight_durations[flight['destination_city']].append(flight['flight_duration_secs'])

            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {file_path}")

    end_time = time.time()
    total_duration = end_time - start_time

    # Calculate AVG and P95 flight duration for top 25 destination cities
    top_25_cities = sorted(flight_durations.keys(), key=lambda city: len(flight_durations[city]), reverse=True)[:25]

    avg_flight_durations = {}
    p95_flight_durations = {}

    for city in top_25_cities:
        durations = flight_durations[city]
        avg_flight_durations[city] = statistics.mean(durations) if durations else None
        p95_flight_durations[city] = statistics.quantiles(durations, n=20)[18] if durations else None

    # Find cities with max passengers arrived and left
    max_arrived_city = max(passengers_arrived, key=passengers_arrived.get) if passengers_arrived else None
    max_left_city = max(passengers_left, key=passengers_left.get) if passengers_left else None

    # Print results
    print(f"Total records processed: {total_records}")
    print(f"Dirty records (with NULL values): {dirty_records}")
    print(f"Total run duration: {total_duration:.2f} seconds\n")

    print("Average and P95 flight duration for Top 25 destination cities:")
    for city in top_25_cities:
        print(f"{city}:")
        print(f"  AVG duration: {avg_flight_durations[city]:.2f} seconds" if avg_flight_durations[city] is not None else "  AVG duration: N/A")
        print(f"  P95 duration: {p95_flight_durations[city]:.2f} seconds" if p95_flight_durations[city] is not None else "  P95 duration: N/A")
    print()

    print("Cities with maximum passengers arrived and left:")
    print(f"Max passengers arrived: {max_arrived_city} ({passengers_arrived[max_arrived_city]} passengers)" if max_arrived_city else "No data available")
    print(f"Max passengers left: {max_left_city} ({passengers_left[max_left_city]} passengers)" if max_left_city else "No data available")

# Main function
def main():
    directory = '/tmp/flights'
    process_json_files(directory)

if __name__ == "__main__":
    main()
