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