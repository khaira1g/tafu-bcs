class Appliance:
    def __init__(self, id, energy_usage):
        self.id = id
        self.energy_usage = energy_usage

    def turn_on(self):
        print(f"Appliance {self.id} turned on. Energy usage: {self.energy_usage}W")

class SmartHomeEnergyManagement:
    def __init__(self):
        self.appliances = []

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    def optimize_energy_usage(self):
        total_usage = sum(appliance.energy_usage for appliance in self.appliances)
        print(f"Total energy usage: {total_usage}W")
        for appliance in self.appliances:
            appliance.turn_on()