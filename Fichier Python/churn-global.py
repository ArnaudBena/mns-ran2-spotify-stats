from spotify import dataset

totalGlobal = 0 # Nombre total d'utilisateurs
churnedGlobal = 0 # Nombre total d'utilisateurs ayant quitté spotify

for record in dataset:
    totalGlobal += 1
    if record["is_churned"] == "1":
        churnedGlobal += 1

print(f"Total Users : {totalGlobal}")
print(f"Churned users : {churnedGlobal}")

percentage = round(churnedGlobal / totalGlobal * 100, 2)

print(f"Churn rate {percentage} %")


