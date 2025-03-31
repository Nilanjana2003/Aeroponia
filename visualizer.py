# visualizer.py
import matplotlib.pyplot as plt

# Plot data with anomalies
def plot_data(data, anomalies, plant):
    # Extract values for plotting
    temp_values = [reading["temp"] for reading in data]
    humidity_values = [reading["humidity"] for reading in data]
    pH_values = [reading["pH"] for reading in data]
    
    # Plot temperature, humidity, and pH
    plt.figure(figsize=(12, 6))
    plt.plot(temp_values, label="Temperature (°C)", color="red")
    plt.plot(humidity_values, label="Humidity (%)", color="blue")
    plt.plot(pH_values, label="pH", color="green")
    
    # Plot anomalies
    temp_label_added = humidity_label_added = pH_label_added = False
    for anomaly in anomalies:
        idx = anomaly["index"]
        param = anomaly["parameter"]
        value = anomaly["value"]
        
        if param == "temp":
            if not temp_label_added:
                plt.scatter(idx, value, color="red", marker="x", label="Anomaly: Temp")
                temp_label_added = True
            else:
                plt.scatter(idx, value, color="red", marker="x")
        elif param == "humidity":
            if not humidity_label_added:
                plt.scatter(idx, value, color="blue", marker="x", label="Anomaly: Humidity")
                humidity_label_added = True
            else:
                plt.scatter(idx, value, color="blue", marker="x")
        elif param == "pH":
            if not pH_label_added:
                plt.scatter(idx, value, color="green", marker="x", label="Anomaly: pH")
                pH_label_added = True
            else:
                plt.scatter(idx, value, color="green", marker="x")
    
    plt.title(f"Sensor Data for {plant}")
    plt.xlabel("Reading Number")
    plt.ylabel("Temperature (°C), Humidity (%), pH")
    plt.legend()
    
    # Save and show the plot
    plt.savefig(f"{plant}_sensor_data.png")
    plt.show()