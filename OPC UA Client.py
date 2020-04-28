from opcua import Client
from time import sleep

url = "opc.tcp://127.0.0.1:2020"

client = Client(url)

client.connect()
print("Client is Connected to Room1")

namespace = client.get_namespace_array()
print(namespace)

objects = client.get_objects_node()
print (objects)

print(objects.get_children())

bulb = objects.get_children()[2]
tempsens = objects.get_children()[1]

temp = tempsens.get_children()[2]

print(bulb.get_children()[0].get_browse_name())
print(temp.get_browse_name())

state = bulb.get_children()[0]

try:
    while state.get_value():
        print ("Temperature in Server: " + str(temp.get_value()))
        if temp.get_value() >= 22:
            state.set_value(False)
            break
        sleep(2)
finally:
    client.disconnect()
    print ("Client Disconnected")
