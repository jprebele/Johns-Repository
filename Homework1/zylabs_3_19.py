# John Rebeles
# PSID:22039426

import math

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))

wall_area = wall_width * wall_height

print('Wall area:', wall_area, 'square feet')

paint_area = float(wall_area) / 350

print('Paint needed:', '{:.2f}'.format(paint_area), 'gallons')
cans_needed = int(math.ceil(paint_area))
print('Cans needed:', cans_needed, 'can(s)')
print()

paint_colors = {'red': 35, 'blue': 25, 'green': 23}
user_color = input('Choose a color to paint the wall:\n')
d_value = int(paint_colors.get(user_color))
print('Cost of purchasing', user_color, 'paint: $' + str(d_value * cans_needed))
