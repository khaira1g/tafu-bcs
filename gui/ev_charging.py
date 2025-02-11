class EV:
    def __init__(self, id, battery_level):
        self.id = id
        self.battery_level = battery_level

    def charge(self):
        self.battery_level += 10
        print(f"EV {self.id} charged. Battery level: {self.battery_level}%")

class EVChargingStation:
    def __init__(self):
        self.evs = []

    def add_ev(self, ev):
        self.evs.append(ev)

    def monitor_and_charge(self):
        for ev in self.evs:
            if ev.battery_level < 80:
                ev.charge()
            else:
                print(f"EV {ev.id} does not need charging.")