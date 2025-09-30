from spotify import dataset

adsPerSub = {"Free": 0.0, "Premium": 0.0, "Family": 0.0, "Student": 0.0}
userFree = 0
userStudent = 0 
userFamily = 0
userPremium = 0

for line in dataset:
    sub = line["subscription_type"]
    ads = int(line["ads_listened_per_week"])
    adsPerSub[sub] += ads
    if line["subscription_type"] == "Free":
        userFree += 1
    elif line["subscription_type"] == "Student":
        userStudent += 1
    elif line["subscription_type"] == "Family":
        userFamily += 1
    elif line["subscription_type"] == "Premium":
        userPremium += 1

print(f"Il y a {userFree} utilisateur avec le plan Free, avec un temps moyen d'écoute de pub de : {round(adsPerSub["Free"] / userFree, 2)} ")
print(f"Il y a {userStudent} utilisateur avec le plan Student, avec un temps moyen d'écoute de pub de : {round(adsPerSub["Student"] / userStudent, 2)}")
print(f"Il y a {userFamily} utilisateur avec le plan Family, avec un temps moyen d'écoute de pub de : {round(adsPerSub["Family"] / userFamily, 2)}")
print(f"Il y a {userPremium} utilisateur avec le plan Premium, avec un temps moyen d'écoute de pub de : {round(adsPerSub["Premium"] / userPremium, 2)}")

