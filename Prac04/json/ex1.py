import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    print(attr["dn"], attr["speed"], attr["mtu"])