class Vehicle:
    def __init__(self, model='Baleno', chasis=45645, color='Blue'):
        self.model = model
        self.chasis = chasis
        self.color = color

    def vehicleDetails(self, description):
        return description + '\n' \
               + 'MODEL: ' + self.model + '\n' \
               + 'CHASIS NUMBER: ' + str(self.chasis) + '\n' \
               + 'COLOR: ' + self.color


object = Vehicle()
print(object.vehicleDetails('Here is the quotation'))




