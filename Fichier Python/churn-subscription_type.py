from spotify import dataset

def calculChurned(type):
    typeTotal = 0
    typeChurned = 0
    for record in dataset:
        if type == record["subscription_type"]:
            typeTotal += 1
            if record["is_churned"] == "1":
                typeChurned += 1
    typePercentage = round(typeChurned / typeTotal * 100, 2)
    print(f"Churn Rate pour l'abonnement {type} : {typePercentage} %")


calculChurned("Free")
calculChurned("Family")
calculChurned("Student")
calculChurned("Premium")
