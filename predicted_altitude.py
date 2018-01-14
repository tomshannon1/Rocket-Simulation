import pylab
import math

# Gravitational constant (m/s^2)
GRAVITY = 9.8

# Meter to foot conversion
METER_CONV = 3.28084

# Mass of rocket (kg)
mass = 3.9

# Diameter of rocket (in)
diameter = 3.0me

# Radius of rocket (m), Area of the rocket (m^2)
radius = (diameter / 2) * 0.0254
area = math.pi * radius**2

# Air resistance: rho (kg/m^3), Cd (dimensionless)
rho = 1.2
cD = 0.75
k = 0.5 * rho * cD * area

# Motor selection and information
motor = {
    "I327DM" :  {"impulse" : 532.8932, "thrust" : 309.2822, "mass" : 0.628},
    "I600R"  :  {"impulse" : 640.1420, "thrust" : 542.4930, "mass" : 0.617},
    "J340M"  :  {"impulse" : 652.7670, "thrust" : 298.0671, "mass" : 0.577},
    "J350W"  :  {"impulse" : 697.4000, "thrust" : 387.4444, "mass" : 0.650},
    "J500G"  :  {"impulse" : 722.6640, "thrust" : 498.3890, "mass" : 0.654},
}

# Find burn times, maximum velocities, and altitudes
for key, value in motor.items():
    
    # Calculate the burn time
    motor[key]["burntime"] = motor[key]["impulse"] / motor[key]["thrust"]

    # Total mass including rocket and motor
    M = mass + motor[key]["mass"]

    # Gravitational force on rocket
    Mg = M * GRAVITY

    # Shorten variables for thrust and burn time
    T = motor[key]["thrust"]
    t = motor[key]["burntime"]

    # Compute maximum velocity that rocket will achieve
    q = math.sqrt((T - Mg) / k)
    x = (2 * k * q) / M
    v = (q * (1 - math.e**(-x * t))) / (1 + math.e**(-x * t))
    
    motor[key]["vel"] = v

    # Calculate boost phase distance and coast phase distance
    yb = (-M / (2 * k)) * math.log((T - Mg - k * v**2) / (T - Mg)) * METER_CONV
    yc = (M / (2 * k)) * math.log((Mg + k * v**2) / Mg) * METER_CONV

    motor[key]["alt"] = yb + yc

# Print out results for predicted altitude with performance measures based on area and mass
print("This simulation assumes a rocket with a ", diameter, " inch diameter and a total mass of ", mass, " kg PLUS the mass of the motor")

for key, value in motor.items():
    
    print(key, ":")

    for otherKey, otherValue in value.items():

        print("    ", otherKey, ":", otherValue)
