import random

class AirQualitySensor:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.air_quality_index = 0

    def measure_air_quality(self):
        # Simulate air quality measurement
        self.air_quality_index = random.randint(0, 500)
        print(f"Sensor {self.id} at {self.location} reports AQI: {self.air_quality_index}")

class AirQualityMonitoringSystem:
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def monitor(self):
        for sensor in self.sensors:
            sensor.measure_air_quality()