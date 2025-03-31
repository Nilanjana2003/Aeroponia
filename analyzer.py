from sensors import plant_ranges

# Check for anomalies in data
def analyze_data(data, plant):
    anomalies = []
    
    for i, reading in enumerate(data):
        for key, value in reading.items():
            # Retrieve ideal range for the parameter based on the plant
            ideal_range = plant_ranges.get(plant, {}).get(key)
            
            if ideal_range is None:
                print(f"Warning: No ideal range found for {key} in {plant}. Skipping...")
                continue
            
            # Check if value is outside ideal range
            if not (ideal_range[0] <= value <= ideal_range[1]):
                anomalies.append({"index": i, "parameter": key, "value": value})
    
    return anomalies