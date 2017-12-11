import math
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
 


# mass of rocket in in kg
rocket_mass_oz = 100
rocket_mass_kg = rocket_mass_oz / (16 * 2.2)

# Area of rocket
rocket_diameter = 3 # in inches
rocket_area = ((rocket_diameter / 24) * 0.3048)**2 * math.pi

# Air resistance
k = 0.5 * 1.2 * 0.75 * rocket_area

# I327DM, I600R, J340M, J350W, J500G
motor_impulses = [532.8932, 640.1420,652.7670,697.4,722.6640]
motor_thrusts = [309.2822, 542.4930,298.0671,387.4444,498.3890]
motor_mass = [0.628, 0.617, 0.5773, 0.650, 0.654]

# Find burn times for each motor
burn_times = []

for motor in range(len(motor_impulses)):
    burn_times.append(motor_impulses[motor] / motor_thrusts[motor])

# Finding max velocity and altitudes
max_velocities = []
alt = []


for motor in range(len(motor_thrusts)):
    
    M = (rocket_mass_kg + motor_mass[motor])
    Mg = (rocket_mass_kg + motor_mass[motor]) * 9.8 
    T = motor_thrusts[motor]
    t = burn_times[motor]
    
    q = math.sqrt((T - Mg) / k)
    x = (2*k*q) / M
    
    v = (q * (1 - math.e**(-x * t))) / (1 + math.e**(-x * t))
    
    yb = (-M/(2*k)) * math.log((T - Mg - k*v**2) / (T - Mg)) * 3.3
    yc = (M /(2*k)) * math.log( (Mg + k * v**2) / Mg) * 3.3
    alt.append((yb+yc))

motors = ('I327DM', 'I600R', 'J340M', 'J350W', 'J500G')
y = np.arange(len(motors))

plt.bar(y, alt, align='center', alpha=0.5)
plt.xticks(y, motors)
plt.ylabel('Usage')
plt.title('Predicted Altitude with 100 oz mass (Miranda Rocket + Payload)')
plt.xlabel('Motors')
plt.ylabel('Predicted Altitude')
plt.show()

'''print("This simulation assumes a rocket with a ", rocket_diameter, " inch diameter and a total mass of ", rocket_mass_kg, " kg PLUS the mass of the motor.", '\n')

for i, motor in enumerate(motors, 1):
    
    print(motors[i-1], " shall reach ", alt[i-1], " feet in altitude.")'''
