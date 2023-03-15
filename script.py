import requests
import json

# Setting the API key and organization ID
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id = "566327653141842188"

#endpoint URLs
admins_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/admins"
devices_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/inventoryDevices"


headers = {
    "Content-Type": "application/json",
    "X-Cisco-Meraki-API-Key": api_key,
}

# Send the requests and get the responses
admins_resp = requests.get(admins_url, headers=headers)
devices_resp = requests.get(devices_url, headers=headers)

admins_data = json.loads(admins_resp.content)
devices_data = json.loads(devices_resp.content)

# Create dictionaries for admins and devices
admins = []
for admin in admins_data:
    admins.append(admin['name'])

devices = []
for device in devices_data:
    device_dict = {
        "serial": device['serial'],
        "mac": device['mac'],
        "networkId": device['networkId'],
        "productType": device['productType'],
    }
    devices.append(device_dict)

with open("PythonRequestModule.txt", "w") as f:
    f.write("Admins:\n")
    f.write(json.dumps(admins, indent=4))
    f.write("\n\nDevices:\n")
    f.write(json.dumps(devices, indent=4))

