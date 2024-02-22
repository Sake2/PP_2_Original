import json
with open('sample-data.json') as file:
    data = json.load(file)

interface_status = data['imdata']

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for entry in interface_status:
    dn = entry['fvCEp']['attributes']['dn']
    description = entry['fvCEp']['attributes'].get('descr', '')
    speed = entry['fvCEp']['attributes'].get('speed', 'inherit')
    mtu = entry['fvCEp']['attributes'].get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
