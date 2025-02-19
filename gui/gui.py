import tkinter as tk
from solar import SolarMonitoringSystem, SolarPanel
from smart_grid import SmartGrid, EnergySource, Consumer
from carbon_footprint import CarbonFootprintCalculator, Activity
from waste_management import WasteSortingSystem, WasteItem
from irrigation import SmartIrrigationSystem, IrrigationZone
from air_quality import AirQualityMonitoringSystem, AirQualitySensor
from ev_charging import EVChargingStation, EV
from smart_home import SmartHomeEnergyManagement, Appliance
from forest_monitoring import ForestMonitoringSystem, ForestSensor

class EnvironmentalManagementSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Environment project")

        self.refresh_interval = 30000  # Refresh interval in milliseconds (30 seconds)
        self.remaining_time = self.refresh_interval // 1000  # Remaining time in seconds

        self.setup_solar_monitoring()
        self.setup_smart_grid()
        self.setup_carbon_footprint()
        self.setup_waste_management()
        self.setup_irrigation()
        self.setup_air_quality()
        self.setup_ev_charging()
        self.setup_smart_home()
        self.setup_forest_monitoring()

        # Timer Label
        self.timer_label = tk.Label(
            root,
            text=f"Next refresh in: {self.remaining_time} seconds",
            font=("Arial", 12),
        )
        self.timer_label.pack()

        # Refresh Now Button
        self.refresh_button = tk.Button(
            root, text="Refresh Now", command=self.refresh_now
        )
        self.refresh_button.pack()

        # Start the timer and refresh data
        self.start_timer()
        self.refresh_data()

    @staticmethod
    def update_label(label, text):
        label.config(text=text)

    def setup_solar_monitoring(self):
        solar_frame = tk.Frame(self.root, padx=10, pady=10)
        solar_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(solar_frame, text="Solar Monitoring System", font=("Arial", 16)).pack()
        self.solar_monitoring_system = SolarMonitoringSystem()
        solar_panel1 = SolarPanel(id=1, location="Rooftop")
        solar_panel2 = SolarPanel(id=2, location="Field")
        self.solar_monitoring_system.add_panel(solar_panel1)
        self.solar_monitoring_system.add_panel(solar_panel2)
        self.solar_result_label = tk.Label(solar_frame)
        self.solar_result_label.pack()

    def monitor_solar(self):
        results = []
        for panel in self.solar_monitoring_system.solar_panels:
            panel.generate_energy()
            results.append(
                f"Panel {panel.id} at {panel.location} generated {panel.energy_generated:.2f} kWh"
            )
        self.update_label(self.solar_result_label, "\n".join(results))

    def setup_smart_grid(self):
        smart_grid_frame = tk.Frame(self.root, padx=10, pady=10)
        smart_grid_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(smart_grid_frame, text="Smart Grid", font=("Arial", 16)).pack()
        self.smart_grid = SmartGrid()
        energy_source1 = EnergySource(id=1, energy_generated=100)
        energy_source2 = EnergySource(id=2, energy_generated=150)
        consumer1 = Consumer(id=1, energy_needed=120)
        consumer2 = Consumer(id=2, energy_needed=80)
        self.smart_grid.add_energy_source(energy_source1)
        self.smart_grid.add_energy_source(energy_source2)
        self.smart_grid.add_consumer(consumer1)
        self.smart_grid.add_consumer(consumer2)
        self.smart_grid_result_label = tk.Label(smart_grid_frame)
        self.smart_grid_result_label.pack()

    def balance_load(self):
        total_energy = sum(
            source.energy_generated for source in self.smart_grid.energy_sources
        )
        total_consumption = sum(
            consumer.energy_needed for consumer in self.smart_grid.consumers
        )
        if total_energy >= total_consumption:
            result = "Energy supply meets demand."
        else:
            result = "Energy shortage. Need to optimize distribution."
        self.update_label(self.smart_grid_result_label, result)

    def setup_carbon_footprint(self):
        carbon_frame = tk.Frame(self.root, padx=10, pady=10)
        carbon_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(
            carbon_frame, text="Carbon Footprint Calculator", font=("Arial", 16)
        ).pack()
        self.carbon_calculator = CarbonFootprintCalculator()
        activity1 = Activity(name="Driving", emissions=150)
        activity2 = Activity(name="Flying", emissions=300)
        self.carbon_calculator.add_activity(activity1)
        self.carbon_calculator.add_activity(activity2)
        self.carbon_result_label = tk.Label(carbon_frame)
        self.carbon_result_label.pack()

    def calculate_footprint(self):
        total_emissions = sum(
            activity.emissions for activity in self.carbon_calculator.activities
        )
        self.update_label(
            self.carbon_result_label,
            f"Total Carbon Footprint: {total_emissions:.2f} kg CO2",
        )

    def setup_waste_management(self):
        waste_frame = tk.Frame(self.root, padx=10, pady=10)
        waste_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(waste_frame, text="Waste Management System", font=("Arial", 16)).pack()
        self.waste_sorting_system = WasteSortingSystem()
        waste_item1 = WasteItem(id=1, type="recyclable")
        waste_item2 = WasteItem(id=2, type="organic")
        waste_item3 = WasteItem(id=3, type="non-recyclable")
        self.waste_sorting_system.sort_waste(waste_item1)
        self.waste_sorting_system.sort_waste(waste_item2)
        self.waste_sorting_system.sort_waste(waste_item3)
        self.waste_result_label = tk.Label(waste_frame)
        self.waste_result_label.pack()

    def display_bins(self):
        results = []
        for bin_type, items in self.waste_sorting_system.waste_bins.items():
            results.append(
                f"{bin_type.capitalize()} Bin: {[item.id for item in items]}"
            )
        self.update_label(self.waste_result_label, "\n".join(results))

    def setup_irrigation(self):
        irrigation_frame = tk.Frame(self.root, padx=10, pady=10)
        irrigation_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(
            irrigation_frame, text="Smart Irrigation System", font=("Arial", 16)
        ).pack()
        self.irrigation_system = SmartIrrigationSystem()
        irrigation_zone1 = IrrigationZone(id=1, moisture_level=20)
        irrigation_zone2 = IrrigationZone(id=2, moisture_level=40)
        self.irrigation_system.add_zone(irrigation_zone1)
        self.irrigation_system.add_zone(irrigation_zone2)
        self.irrigation_result_label = tk.Label(irrigation_frame)
        self.irrigation_result_label.pack()

    def monitor_irrigation(self):
        results = []
        for zone in self.irrigation_system.zones:
            if zone.moisture_level < 30:
                zone.water_plants()
            results.append(f"Zone {zone.id} moisture level: {zone.moisture_level}%")
        self.update_label(self.irrigation_result_label, "\n".join(results))

    def setup_air_quality(self):
        air_quality_frame = tk.Frame(self.root, padx=10, pady=10)
        air_quality_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(
            air_quality_frame, text="Air Quality Monitoring System", font=("Arial", 16)
        ).pack()
        self.air_quality_system = AirQualityMonitoringSystem()
        air_sensor1 = AirQualitySensor(id=1, location="City Center")
        air_sensor2 = AirQualitySensor(id=2, location="Suburbs")
        self.air_quality_system.add_sensor(air_sensor1)
        self.air_quality_system.add_sensor(air_sensor2)
        self.air_quality_result_label = tk.Label(air_quality_frame)
        self.air_quality_result_label.pack()

    def monitor_air_quality(self):
        results = []
        for sensor in self.air_quality_system.sensors:
            sensor.measure_air_quality()
            results.append(
                f"Sensor {sensor.id} at {sensor.location} reports AQI: {sensor.air_quality_index}"
            )
        self.update_label(self.air_quality_result_label, "\n".join(results))

    def setup_ev_charging(self):
        ev_charging_frame = tk.Frame(self.root, padx=10, pady=10)
        ev_charging_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(
            ev_charging_frame,
            text="EV Charging Station Management System",
            font=("Arial", 16),
        ).pack()
        self.ev_charging_station = EVChargingStation()
        ev1 = EV(id=1, battery_level=20)
        ev2 = EV(id=2, battery_level=50)
        self.ev_charging_station.add_ev(ev1)
        self.ev_charging_station.add_ev(ev2)
        self.ev_charging_result_label = tk.Label(ev_charging_frame)
        self.ev_charging_result_label.pack()

    def monitor_ev_charging(self):
        results = []
        for ev in self.ev_charging_station.evs:
            if ev.battery_level < 80:
                ev.charge()
            results.append(f"EV {ev.id} battery level: {ev.battery_level}%")
        self.update_label(self.ev_charging_result_label, "\n".join(results))

    def setup_smart_home(self):
        smart_home_frame = tk.Frame(self.root, padx=10, pady=10)
        smart_home_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(
            smart_home_frame,
            text="Smart Home Energy Management System",
            font=("Arial", 16),
        ).pack()
        self.smart_home = SmartHomeEnergyManagement()
        appliance1 = Appliance(id=1, energy_usage=100)
        appliance2 = Appliance(id=2, energy_usage=200)
        self.smart_home.add_appliance(appliance1)
        self.smart_home.add_appliance(appliance2)
        self.smart_home_result_label = tk.Label(smart_home_frame)
        self.smart_home_result_label.pack()

    def optimize_energy_usage(self):
        total_usage = sum(
            appliance.energy_usage for appliance in self.smart_home.appliances
        )
        results = [f"Total energy usage: {total_usage}W"]
        for appliance in self.smart_home.appliances:
            appliance.turn_on()
            results.append(
                f"Appliance {appliance.id} turned on. Energy usage: {appliance.energy_usage}W"
            )
        self.update_label(self.smart_home_result_label, "\n".join(results))

    def setup_forest_monitoring(self):
        forest_monitoring_frame = tk.Frame(self.root, padx=10, pady=10)
        forest_monitoring_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(
            forest_monitoring_frame, text="Forest Monitoring System", font=("Arial", 16)
        ).pack()
        self.forest_monitoring_system = ForestMonitoringSystem()
        forest_sensor1 = ForestSensor(id=1, location="Amazon")
        forest_sensor2 = ForestSensor(id=2, location="Congo")
        self.forest_monitoring_system.add_sensor(forest_sensor1)
        self.forest_monitoring_system.add_sensor(forest_sensor2)
        self.forest_monitoring_result_label = tk.Label(forest_monitoring_frame)
        self.forest_monitoring_result_label.pack()

    def monitor_forest(self):
        results = []
        for sensor in self.forest_monitoring_system.sensors:
            sensor.measure_deforestation()
            results.append(
                f"Sensor {sensor.id} at {sensor.location} reports deforestation rate: {sensor.deforestation_rate:.2f}"
            )
        self.update_label(self.forest_monitoring_result_label, "\n".join(results))

    def refresh_data(self):
        self.monitor_solar()
        self.balance_load()
        self.calculate_footprint()
        self.display_bins()
        self.monitor_irrigation()
        self.monitor_air_quality()
        self.monitor_ev_charging()
        self.optimize_energy_usage()
        self.monitor_forest()
        self.root.after(self.refresh_interval, self.refresh_data)

    def refresh_now(self):
        self.remaining_time = self.refresh_interval // 1000
        self.refresh_data()

    def start_timer(self):
        if self.remaining_time > 0:
            self.update_label(
                self.timer_label, f"Next refresh in: {self.remaining_time} seconds"
            )
            self.remaining_time -= 1
            self.root.after(1000, self.start_timer)
        else:
            self.remaining_time = self.refresh_interval // 1000
            self.start_timer()


def run_gui():
    root = tk.Tk()
    EnvironmentalManagementSystemApp(root)
    root.mainloop()
