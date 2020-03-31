# Write your code here :-)
import py_qmc5883l
sensor = py_qmc5883l.QMC5883L()
m = sensor.get_magnet()
print(m)

# The same matrix, as a Python array:
#
sensor.calibration = [[1.0124554030038653, -0.02946998375102533, -561.7134736702388],
                      [-0.02946998375102533, 1.0697271651520381, 1255.7392354217145],
                      [0.0, 0.0, 1.0]]
#
n = sensor.get_bearing()
n = n+90
if n > 360:
    n=n-360
print(n)