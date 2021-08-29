def sleeping_monsters(mons_desc, monst_life, def_monster, hp_loss):
    print (mons_desc)
    while monst_life > 0:
      command = input("Enter a command: ")
      if command.lower() == "attack":
        monst_life -= hp_loss
    print (def_monster)
    return 0
