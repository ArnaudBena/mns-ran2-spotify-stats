from spotify import dataset

riskUser = 0

for user in dataset:
    if (
        float(user["skip_rate"]) > 0.30 and float(user["listening_time"]) < 100
    ) or (
        user["subscription_type"] == "Free"
        and user["offline_listening"] == "0"
        and float(user["ads_listened_per_week"]) > 20
    ):
        # print(user["user_id"])
        riskUser += 1

print(f"Il y a {riskUser} utilisateurs à risque")