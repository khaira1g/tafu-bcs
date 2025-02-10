class Activity:
    def __init__(self, name, emissions):
        self.name = name
        self.emissions = emissions

class CarbonFootprintCalculator:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def calculate_total_footprint(self):
        total_emissions = sum(activity.emissions for activity in self.activities)
        print(f"Total Carbon Footprint: {total_emissions:.2f} kg CO2")