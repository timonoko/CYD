import network,time,os
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
while not sta_if.isconnected():
    try: sta_if.connect('Jorpakko', 'Juhannusyona')
    except:
         print("virhe")
    time.sleep(1)
print('network config:', sta_if.ifconfig())
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)


