class EnergySource:
    def __init__(self, id, energy_generated):
        self.id = id
        self.energy_generated = energy_generated

class Consumer:
    def __init__(self, id, energy_needed):
        self.id = id
        self.energy_needed = energy_needed

class SmartGrid:
    def __init__(self):
        self.energy_sources = []
        self.consumers = []

    def add_energy_source(self, source):
        self.energy_sources.append(source)

    def add_consumer(self, consumer):
        self.consumers.append(consumer)

    def balance_load(self):
        total_energy = sum(source.energy_generated for source in self.energy_sources)
        total_consumption = sum(consumer.energy_needed for consumer in self.consumers)
        if total_energy >= total_consumption:
            print("Energy supply meets demand.")
        else:
            print("Energy shortage. Need to optimize distribution.")