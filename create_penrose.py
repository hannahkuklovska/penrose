import math
from penrose import PenroseP3, BtileL, psi

# Scale for the tiles
scale = 200

# Create the first Penrose tile
tiling1 = PenroseP3(scale, ngen=5)

# Define the vertices for the first tile
theta1 = 2*math.pi / 5
rot1 = math.cos(theta1) + 1j*math.sin(theta1)
A1 = -scale/2 + 0j
B1 = scale/2 * rot1
C1 = scale/2 / psi + 0j

# Set initial tiles and make tiling
tiling1.set_initial_tiles([BtileL(A1, B1, C1)])
tiling1.make_tiling()

# Write the first SVG file
tiling1.write_svg('example1.svg')

# Create the second Penrose tile
tiling2 = PenroseP3(scale, ngen=5)

# Define the vertices for the second tile (adjusting the rotation angle)
theta2 = 2*math.pi / 5
rot2 = math.cos(theta2) + 1j*math.sin(theta2)
A2 = -scale/2 + 0j
B2 = scale/2 * rot2
C2 = scale/2 / psi + 0j

# Set initial tiles and make tiling
tiling2.set_initial_tiles([BtileL(A2, B2, C2)])
tiling2.make_tiling()

# Write the second SVG file
tiling2.write_svg('example2.svg')

