from spotify import dataset

riskUser = 0

for record in dataset:
    if (float(record ["skip_rate"]) > 30 and float(record ["listening_time"]) < 100) or (record ["subscription_type"] == "Free" and record ["offline_listening"] == "0" and float(record["ads_listened_per_week"]) > 20):
        print(record["user_id"])
        riskUser += 1

print(f"Il y a {riskUser} utilisateurs à risque")
