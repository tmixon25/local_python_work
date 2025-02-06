alien_o = {'color':'green','points':5}

print(alien_o)
print(alien_o['color'])
print(alien_o['points'])
new_points = alien_o['points']
print(f"You just earned {new_points} points!")
alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)

print(f"The alien is {alien_o['color']}")
alien_o['color'] = 'yellow'
print(f"The alien is {alien_o['color']}")

del alien_o['points']
print(alien_o)