class IrrigationZone:
    def __init__(self, id, moisture_level):
        self.id = id
        self.moisture_level = moisture_level

    def water_plants(self):
        self.moisture_level += 10
        print(f"Zone {self.id} watered. Moisture level: {self.moisture_level}%")

class SmartIrrigationSystem:
    def __init__(self):
        self.zones = []

    def add_zone(self, zone):
        self.zones.append(zone)

    def monitor_and_irrigate(self):
        for zone in self.zones:
            if zone.moisture_level < 30:
                zone.water_plants()
            else:
                print(f"Zone {zone.id} does not need watering.")