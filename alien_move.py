alien_o = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position:{alien_o['x_position']}")

#Move the alien to the right
if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_o['x_position'] = alien_o['x_position'] + x_increment
print(f"New position:{alien_o['x_position']}")

# Alien points
point_value = alien_o.get('points','No point value assigned.')
print(point_value)
