from spotify import dataset

countries = {}

for line in dataset:
    country = line["country"]
    if country not in countries:
        countries[country] = {"Mobile":0, "Desktop":0, "Web":0}
    if line["device_type"] == "Mobile":
        countries[country]["Mobile"] += 1
    elif line["device_type"] == "Desktop":
        countries[country]["Desktop"] += 1
    elif line["device_type"] == "Web":
        countries[country]["Web"] += 1

for country in countries:
    print(f"{country}")
    print(f"Le device le plus utilisé est {max(countries[country], key = countries[country].get)}")

