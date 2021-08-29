
from description import DROP_WEAPON

def handleChoice(wep_desc, got_wep, wep_get):
  print(wep_desc)
  print(wep_get)
  command = input("Enter a command [get weapon, drop weapon]: ")
  if command.lower() == "get weapon" and not wep_get:
    print(got_wep)
    return True
  elif command.lower() == "get weapon" and wep_get:
    print("You already have a weapon")
    return True
  elif command.lower() == "drop weapon" and not wep_get:
    print("You do not have a weapon")
    return False
  elif command.lower() == "drop weapon" and wep_get:
    print(DROP_WEAPON)
    return False
