from main.solar import SolarMonitoringSystem, SolarPanel
from main.smart_grid import SmartGrid, EnergySource, Consumer
from main.carbon_footprint import CarbonFootprintCalculator, Activity
from main.waste_management import WasteSortingSystem, WasteItem
from main.irrigation import SmartIrrigationSystem, IrrigationZone
from main.air_quality import AirQualityMonitoringSystem, AirQualitySensor

def main():
    # Initialize Solar Monitoring System
    solar_monitoring_system = SolarMonitoringSystem()
    solar_panel1 = SolarPanel(id=1, location="Rooftop")
    solar_panel2 = SolarPanel(id=2, location="Field")
    solar_monitoring_system.add_panel(solar_panel1)
    solar_monitoring_system.add_panel(solar_panel2)
    solar_monitoring_system.monitor()

    # Initialize Smart Grid
    smart_grid = SmartGrid()
    energy_source1 = EnergySource(id=1, energy_generated=100)
    energy_source2 = EnergySource(id=2, energy_generated=150)
    consumer1 = Consumer(id=1, energy_needed=120)
    consumer2 = Consumer(id=2, energy_needed=80)
    smart_grid.add_energy_source(energy_source1)
    smart_grid.add_energy_source(energy_source2)
    smart_grid.add_consumer(consumer1)
    smart_grid.add_consumer(consumer2)
    smart_grid.balance_load()

    # Initialize Carbon Footprint Calculator
    carbon_calculator = CarbonFootprintCalculator()
    activity1 = Activity(name="Driving", emissions=150)
    activity2 = Activity(name="Flying", emissions=300)
    carbon_calculator.add_activity(activity1)
    carbon_calculator.add_activity(activity2)
    carbon_calculator.calculate_total_footprint()

    # Initialize Waste Management System
    waste_sorting_system = WasteSortingSystem()
    waste_item1 = WasteItem(id=1, type="recyclable")
    waste_item2 = WasteItem(id=2, type="organic")
    waste_item3 = WasteItem(id=3, type="non-recyclable")
    waste_sorting_system.sort_waste(waste_item1)
    waste_sorting_system.sort_waste(waste_item2)
    waste_sorting_system.sort_waste(waste_item3)
    waste_sorting_system.display_bins()

    # Initialize Smart Irrigation System
    irrigation_system = SmartIrrigationSystem()
    irrigation_zone1 = IrrigationZone(id=1, moisture_level=20)
    irrigation_zone2 = IrrigationZone(id=2, moisture_level=40)
    irrigation_system.add_zone(irrigation_zone1)
    irrigation_system.add_zone(irrigation_zone2)
    irrigation_system.monitor_and_irrigate()

    # Initialize Air Quality Monitoring System
    air_quality_system = AirQualityMonitoringSystem()
    air_sensor1 = AirQualitySensor(id=1, location="City Center")
    air_sensor2 = AirQualitySensor(id=2, location="Suburbs")
    air_quality_system.add_sensor(air_sensor1)
    air_quality_system.add_sensor(air_sensor2)
    air_quality_system.monitor()

if __name__ == "__main__":
    main()