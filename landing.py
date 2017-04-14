#ursa_minor

alt = 100
spd = 10
fuel = 50
thrust = 0

while alt != 0:
  thrust = False
  print("altitude: " + str(alt) + " speed: " + str(spd) + " fuel: " + str(fuel))
  thrust = int(input('Will you thrust this turn? (Type 1 for true or 0 for false) '))
  if thrust == 1:
    if fuel > 0:
      fuel -= 5
      spd -= 1
    else:
      pass
  elif thrust == 0:
    spd += 1
  thrust = 0
  alt -= spd
  if alt < 0:
    alt = 0
  if alt == 0:
    if spd > 5:
      print("You crashed.")
    else:
      print("You landed safely.")
  if alt > 100 and spd < 0:
    print("You got stranded in space, never to see anyone again.")
    break
