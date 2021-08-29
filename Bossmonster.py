from random import choice
monst_moves = ["Nothing", "Attack"]

def boss_fight (user_life, hp_loss, monst_life):
  while monst_life > 0 and user_life > 0:
    command = input ("Enter a command: ")
    monst_move = choice(monst_moves)
    if command.lower() == "attack":
        monst_life -= hp_loss
    elif command.lower() == "block":
        pass
    if monst_move.lower() == "attack":
      if command.lower() == "block":
        pass
      else:
        user_life -= 20
    print(f"Boss hp: {monst_life}, Player hp: {user_life}")
  return user_life, monst_life
