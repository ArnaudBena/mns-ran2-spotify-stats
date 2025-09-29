from spotify import dataset

riskUser = 0

for record in dataset:
    if (float(record ["skip_rate"]) > 30 and float(record ["listening_time"]) < 100) or (record ["subscription_type"] == "Free" and record ["offline_listening"] == "0" and float(record["ads_listened_per_week"]) > 20):
        print(record["user_id"])
        riskUser += 1

print(f"Il y a {riskUser} utilisateurs à risque")


from spotify import dataset

atRiskUsers = []
total = 0

for record in dataset:
    if record["is_churned"] == "0":
        total += 1
        skipRate = float(record.get("skip_rate"))
        listeningTime = float(record.get("listening_time"))
        adsListenedPerWeek = int(record.get("ads_listened_per_week"))
        if record["subscription_type"] == "Free":
            if record["offline_listening"] == "0" and adsListenedPerWeek > 20:
                atRiskUsers.append(record.get("user_id"))
        if skipRate > 0.3 and listeningTime < 100:
            atRiskUsers.append(record.get("user_id"))

print(atRiskUsers)
print(f"Il y a {len(atRiskUsers)} utilisateurs à risques sur {total} actifs.")