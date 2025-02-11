import random

class ForestSensor:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.deforestation_rate = 0

    def measure_deforestation(self):
        # Simulate deforestation measurement
        self.deforestation_rate = random.uniform(0, 1)
        print(f"Sensor {self.id} at {self.location} reports deforestation rate: {self.deforestation_rate:.2f}")

class ForestMonitoringSystem:
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def monitor(self):
        for sensor in self.sensors:
            sensor.measure_deforestation()