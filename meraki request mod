import meraki
import json



# Setting the API key and organization ID

api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id = "566327653141842188"



# Initialize the Meraki with the API key

dashboard = meraki.DashboardAPI(api_key)



# Send the requests and get the responses

admins_data = dashboard.organizations.getOrganizationAdmins(org_id)
devices_data = dashboard.organizations.getOrganizationInventoryDevices(org_id)





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


with open("MerakiRequestModule.txt", "w") as f:
    f.write("Admins:\n")
    f.write(json.dumps(admins, indent=4))
    f.write("\n\nDevices:\n")
    f.write(json.dumps(devices, indent=4))
