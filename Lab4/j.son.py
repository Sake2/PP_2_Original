import json
with open('Lab4/sample-data.json') as file:
    data = json.load(file)

interface_status = data['imdata']

print("Interface Status")
print("=" * 85)
print("DN"," "*48 ,"Description" ," "*7, "Speed" ," "*3, "MTU")
print("-" * 51 ,"-"*19,"-"*9,"-"*6 )

for entry in interface_status:
    dn = entry["l1PhysIf"]['attributes']['dn']
    description = entry["l1PhysIf"]['attributes'].get('descr', '')
    speed = entry["l1PhysIf"]['attributes'].get('speed', 'inherit')
    mtu = entry["l1PhysIf"]['attributes'].get('mtu', '')
    print(dn , description," "*27 , speed," ", mtu)
