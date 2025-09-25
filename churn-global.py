from spotify import dataset

total = 0 # Nombre total d'utilisateurs
churned = 0 # Nombre total d'utilisateurs ayant quitté spotify

for record in dataset:
    total = total + 1
    if record["is_churned"] == "1":
        churned = churned + 1
        
print(f"Total Users : {total}")
print(f"Churned users : {churned}")

percentage = round(churned / total * 100, 2)

print(f"Churn rate {percentage} %")