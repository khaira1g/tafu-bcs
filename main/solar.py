import random

class SolarPanel:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.energy_generated = 0

    def generate_energy(self):
        # Simulate energy generation in kWh
        self.energy_generated += random.uniform(1.0, 5.0)

class SolarMonitoringSystem:
    def __init__(self):
        self.solar_panels = []

    def add_panel(self, panel):
        self.solar_panels.append(panel)

    def monitor(self):
        for panel in self.solar_panels:
            panel.generate_energy()
            print(f"Panel {panel.id} at {panel.location} generated {panel.energy_generated:.2f} kWh")