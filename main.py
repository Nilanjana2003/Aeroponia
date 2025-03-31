from sensors import generate_sensor_data
from analyzer import analyze_data
from visualizer import plot_data

# List of plants to simulate
plants = ["Tomato", "Potato", "Strawberry"]

# Simulate data for each plant
for plant in plants:
    print(f"Simulating data for {plant}...")
    
    # Generate sensor data
    data = generate_sensor_data(plant, num_readings=50)
    
    # Analyze data for anomalies
    anomalies = analyze_data(data, plant)  # Pass the plant name here
    
    # Plot data with anomalies
    plot_data(data, anomalies, plant)

print("Simulation complete! 🚀")