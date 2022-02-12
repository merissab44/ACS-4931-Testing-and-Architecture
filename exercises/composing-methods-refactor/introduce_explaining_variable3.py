# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def get_time(time):
    return time
def get_temperature(temperature):
    return temperature
def get_pressure(pressure):
    return pressure

def is_cookeding_criteria_satisfied(desired_state):
    if desired_state == 'well-done' and get_time() * get_temperature() * get_pressure() * COOKED_CONSTANT >= WELL_DONE: 
        return True
    if desired_state == 'medium' and get_time() * get_temperature() * get_pressure() * COOKED_CONSTANT >= MEDIUM:
        return True
    return False