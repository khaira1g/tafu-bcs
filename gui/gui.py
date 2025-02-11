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

def run_gui():
    root = tk.Tk()
    root.title("Environment project")

    # solor
    solar_frame = tk.Frame(root, padx=10, pady=10)
    solar_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(solar_frame, text="Solar Monitoring System", font=("Arial", 16)).pack()
    solar_monitoring_system = SolarMonitoringSystem()
    solar_panel1 = SolarPanel(id=1, location="Rooftop")
    solar_panel2 = SolarPanel(id=2, location="Field")
    solar_monitoring_system.add_panel(solar_panel1)
    solar_monitoring_system.add_panel(solar_panel2)
    def monitor_solar():
        solar_monitoring_system.monitor()
    tk.Button(solar_frame, text="Monitor Solar Panels", command=monitor_solar).pack()

    # Smart Grid
    smart_grid_frame = tk.Frame(root, padx=10, pady=10)
    smart_grid_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(smart_grid_frame, text="Smart Grid", font=("Arial", 16)).pack()
    smart_grid = SmartGrid()
    energy_source1 = EnergySource(id=1, energy_generated=100)
    energy_source2 = EnergySource(id=2, energy_generated=150)
    consumer1 = Consumer(id=1, energy_needed=120)
    consumer2 = Consumer(id=2, energy_needed=80)
    smart_grid.add_energy_source(energy_source1)
    smart_grid.add_energy_source(energy_source2)
    smart_grid.add_consumer(consumer1)
    smart_grid.add_consumer(consumer2)
    def balance_load():
        smart_grid.balance_load()
    tk.Button(smart_grid_frame, text="Balance Load", command=balance_load).pack()

    # Carbon Footprint Calculator
    carbon_frame = tk.Frame(root, padx=10, pady=10)
    carbon_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(carbon_frame, text="Carbon Footprint Calculator", font=("Arial", 16)).pack()
    carbon_calculator = CarbonFootprintCalculator()
    activity1 = Activity(name="Driving", emissions=150)
    activity2 = Activity(name="Flying", emissions=300)
    carbon_calculator.add_activity(activity1)
    carbon_calculator.add_activity(activity2)
    def calculate_footprint():
        carbon_calculator.calculate_total_footprint()
    tk.Button(carbon_frame, text="Calculate Carbon Footprint", command=calculate_footprint).pack()

    # Waste Management System
    waste_frame = tk.Frame(root, padx=10, pady=10)
    waste_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(waste_frame, text="Waste Management System", font=("Arial", 16)).pack()
    waste_sorting_system = WasteSortingSystem()
    waste_item1 = WasteItem(id=1, type="recyclable")
    waste_item2 = WasteItem(id=2, type="organic")
    waste_item3 = WasteItem(id=3, type="non-recyclable")
    waste_sorting_system.sort_waste(waste_item1)
    waste_sorting_system.sort_waste(waste_item2)
    waste_sorting_system.sort_waste(waste_item3)
    def display_bins():
        waste_sorting_system.display_bins()
    tk.Button(waste_frame, text="Display Waste Bins", command=display_bins).pack()

    # Smart Irrigation System
    irrigation_frame = tk.Frame(root, padx=10, pady=10)
    irrigation_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(irrigation_frame, text="Smart Irrigation System", font=("Arial", 16)).pack()
    irrigation_system = SmartIrrigationSystem()
    irrigation_zone1 = IrrigationZone(id=1, moisture_level=20)
    irrigation_zone2 = IrrigationZone(id=2, moisture_level=40)
    irrigation_system.add_zone(irrigation_zone1)
    irrigation_system.add_zone(irrigation_zone2)
    def monitor_irrigation():
        irrigation_system.monitor_and_irrigate()
    tk.Button(irrigation_frame, text="Monitor Irrigation", command=monitor_irrigation).pack()

    # Air Quality Monitoring System
    air_quality_frame = tk.Frame(root, padx=10, pady=10)
    air_quality_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(air_quality_frame, text="Air Quality Monitoring System", font=("Arial", 16)).pack()
    air_quality_system = AirQualityMonitoringSystem()
    air_sensor1 = AirQualitySensor(id=1, location="City Center")
    air_sensor2 = AirQualitySensor(id=2, location="Suburbs")
    air_quality_system.add_sensor(air_sensor1)
    air_quality_system.add_sensor(air_sensor2)
    def monitor_air_quality():
        air_quality_system.monitor()
    tk.Button(air_quality_frame, text="Monitor Air Quality", command=monitor_air_quality).pack()

    # EV Charging Station Management System
    ev_charging_frame = tk.Frame(root, padx=10, pady=10)
    ev_charging_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(ev_charging_frame, text="EV Charging Station Management System", font=("Arial", 16)).pack()
    ev_charging_station = EVChargingStation()
    ev1 = EV(id=1, battery_level=20)
    ev2 = EV(id=2, battery_level=50)
    ev_charging_station.add_ev(ev1)
    ev_charging_station.add_ev(ev2)
    def monitor_ev_charging():
        ev_charging_station.monitor_and_charge()
    tk.Button(ev_charging_frame, text="Monitor EV Charging", command=monitor_ev_charging).pack()

    # Smart Home Energy Management System
    smart_home_frame = tk.Frame(root, padx=10, pady=10)
    smart_home_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(smart_home_frame, text="Smart Home Energy Management System", font=("Arial", 16)).pack()
    smart_home = SmartHomeEnergyManagement()
    appliance1 = Appliance(id=1, energy_usage=100)
    appliance2 = Appliance(id=2, energy_usage=200)
    smart_home.add_appliance(appliance1)
    smart_home.add_appliance(appliance2)
    def optimize_energy_usage():
        smart_home.optimize_energy_usage()
    tk.Button(smart_home_frame, text="Optimize Energy Usage", command=optimize_energy_usage).pack()

    # Forest Monitoring System
    forest_monitoring_frame = tk.Frame(root, padx=10, pady=10)
    forest_monitoring_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(forest_monitoring_frame, text="Forest Monitoring System", font=("Arial", 16)).pack()
    forest_monitoring_system = ForestMonitoringSystem()
    forest_sensor1 = ForestSensor(id=1, location="Amazon")
    forest_sensor2 = ForestSensor(id=2, location="Congo")
    forest_monitoring_system.add_sensor(forest_sensor1)
    forest_monitoring_system.add_sensor(forest_sensor2)
    def monitor_forest():
        forest_monitoring_system.monitor()
    tk.Button(forest_monitoring_frame, text="Monitor Forest", command=monitor_forest).pack()

    root.mainloop()