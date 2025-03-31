import random

# Define ideal ranges for each plant
plant_ranges = {
    "Tomato": {"temp": (20, 30), "humidity": (60, 80), "pH": (5.5, 6.8)},
    "Potato": {"temp": (15, 25), "humidity": (70, 90), "pH": (4.8, 6.5)},
    "Strawberry": {"temp": (18, 28), "humidity": (50, 70), "pH": (5.0, 6.5)}
}

# Generate sensor data for a plant
def generate_sensor_data(plant, num_readings=50):
    # Validate plant name
    if plant not in plant_ranges:
        valid_plants = ", ".join(plant_ranges.keys())
        raise ValueError(f"Unknown plant: {plant}. Valid plants are: {valid_plants}")
    
    # Validate num_readings
    if not isinstance(num_readings, int) or num_readings <= 0:
        raise ValueError("num_readings must be a positive integer")
    
    data = []
    for _ in range(num_readings):
        # Retrieve ranges for the plant
        temp_range, humidity_range, pH_range = plant_ranges[plant].values()
        
        # Generate random values within range
        temp = round(random.uniform(*temp_range), 2)
        humidity = round(random.uniform(*humidity_range), 2)
        pH = round(random.uniform(*pH_range), 2)
        
        # Append the generated reading to the data list
        data.append({"temp": temp, "humidity": humidity, "pH": pH})
    
    return data