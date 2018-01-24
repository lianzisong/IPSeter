import wmi
import random
import re


wmiService = wmi.WMI()

colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)
index = 0 

arrIPAddresses = ['134.161.154.19']
arrSubnetMasks = ['255.255.255.0']
arrDefaultGateways = ['134.161.154.1']
arrGatewayCostMetrics = [1]
arrDNSServers = ['134.176.22.9']

for item in colNicConfigs:
    pattern = re.compile(r"Intel")
    match = pattern.search(item.Description)
    if match:
        index = item.Index -1

objNicConfig = colNicConfigs[index]


returnValue = objNicConfig.EnableStatic(IPAddress = arrIPAddresses, SubnetMask = arrSubnetMasks) 

if returnValue[0] == 0:
    print('set ip ok')
elif returnValue[0] == 1:
    print('set ip ok')
else:
    print('set ip failed')
    exit()

returnValue = objNicConfig.SetGateways(DefaultIPGateway = arrDefaultGateways, GatewayCostMetric = arrGatewayCostMetrics)
if returnValue[0] == 0:
    print('set gateway ok')
elif returnValue[0] == 1:
    print('set gateway ok')
else:
    print('set gateway fail')
    exit() 

returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder = arrDNSServers)
if returnValue[0] == 0:
    print('set dns ok')
elif returnValue[0] == 1:
    print('set dns ok')
else:
    print('set dns fail')
    exit() 



