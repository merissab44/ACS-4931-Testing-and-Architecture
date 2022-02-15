# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, d_value, d_unit):
        self.d_unit = d_unit
        self.d_value = d_value

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def calculate_kinetic_energy(mass, distance, time):
    if distance.d_unit != 'km' and distance.d_unit == "ly":
        # if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
        in_km = distance.d_value * 9.461e12
        converted_distance = Distance(in_km, "km")
    else:
        print ("unit is Unknown")
        return
    speed = converted_distance.d_value/time # [km per sec]
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = mass.value * 1.98892e30 # [kg]
            converted_mass = Mass(value, 'kg')
        else:
            print ("unit is Unknown")
            return

    kinetic_energy = 0.5 * converted_mass.value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
