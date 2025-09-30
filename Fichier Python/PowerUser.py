from spotify import dataset

powerUser = 0

for user in dataset:
    if float(user["listening_time"]) > 200 and float(user["songs_played_per_day"]) > 50:
        powerUser +=1
print(f" Il y a {powerUser} beta testeur potentiel")