# Rocket-Simulation

This is a rocket simulation made for the 2018 Wisconsin Space Grant Consortiums (WSGC) Collegiate Rocket Launch (CRL) competition.
This was created to help aid the design process of the rocket. Using simple mechanics, the simulation predicts the apogee of the
rocket based on the overall mass of the rocket, the diameter, and what type of motor is being used. This simulation is very easy to
modify and would helpful to teams launching their first rockets.

To add different motors, users can modify the "motors" dictionary inside the script. The user just has to specify the typical impulse, thrust, and mass of the motor, which can be found on http://www.thrustcurve.org/.

```python
motor = {
    "I327DM" :  {"impulse" : 532.8932, "thrust" : 309.2822, "mass" : 0.628},
    "I600R"  :  {"impulse" : 640.1420, "thrust" : 542.4930, "mass" : 0.617},
    "J340M"  :  {"impulse" : 652.7670, "thrust" : 298.0671, "mass" : 0.577},
    "J350W"  :  {"impulse" : 697.4000, "thrust" : 387.4444, "mass" : 0.650},
    "J500G"  :  {"impulse" : 722.6640, "thrust" : 498.3890, "mass" : 0.654},
}```
