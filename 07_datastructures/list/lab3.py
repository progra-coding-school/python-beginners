cricket_team = ["Aarav", "Kabir", "Rohan", "Meera", "Diya"]
print("Cricket team :", cricket_team)

print(cricket_team[0])
print(cricket_team[1])

print(cricket_team[-1])

print(len(cricket_team))

cricket_team.append("Kumar")
print("Cricket team :", cricket_team)
cricket_team.insert(0, "Raja")
print("Cricket team :", cricket_team)
cricket_team.insert(3, "Raja")
print("Cricket team :", cricket_team)

# new_players = ["Dhoni", "Sewag", "Rohit", "Kohli"]
# cricket_team.extend(new_players)
#
# print("Cricket team :", cricket_team)

cricket_team.remove("Aarav")
print("Cricket team :", cricket_team)

cricket_team.pop()
print("Cricket team :", cricket_team)

cricket_team.pop(0)
print("Cricket team :", cricket_team)
