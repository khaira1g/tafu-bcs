class WasteItem:
    def __init__(self, id, type):
        self.id = id
        self.type = type

class WasteSortingSystem:
    def __init__(self):
        self.waste_bins = {"recyclable": [], "organic": [], "non-recyclable": []}

    def sort_waste(self, waste_item):
        if waste_item.type == "recyclable":
            self.waste_bins["recyclable"].append(waste_item)
        elif waste_item.type == "organic":
            self.waste_bins["organic"].append(waste_item)
        else:
            self.waste_bins["non-recyclable"].append(waste_item)

    def display_bins(self):
        for bin_type, items in self.waste_bins.items():
            print(f"{bin_type.capitalize()} Bin: {[item.id for item in items]}")