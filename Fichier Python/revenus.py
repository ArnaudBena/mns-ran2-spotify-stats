from spotify import dataset


mrrCountry = {}
prices = {"Free": 0.0, "Premium": 9.99, "Family": 14.99, "Student": 4.99}
for record in dataset:
    if record["is_churned"] == "0" and record["subscription_type"] != "Free":
        country = record["country"]
        subscriptionType = record["subscription_type"]

        if country not in mrrCountry:
            mrrCountry[country] = {"Premium":0, "Family":0, "Student":0,}
        mrrCountry[country][subscriptionType] += 1


for country in mrrCountry:
    print(f"{country}")
    for plan in mrrCountry[country]:
        earn = float(mrrCountry[country][plan] * float(prices[plan]))
        print(f"{plan} : {round(earn, 2)} €")
    print()



