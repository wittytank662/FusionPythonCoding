account = {}

def createAccount(username, password):
    if username in account:
        return "Error - that username already exists."
    else:
        account[username] = {"password": password}
        return account

places = {}

def createPlace(placeName):
    if placeName in places:
        return "Error - place already exists."
    places[placeName] = {}
    return f"Place '{placeName}' created."

def createRoom(placeName, roomName):
    if placeName not in places:
        return "Error - place does not exist."
    if roomName in places[placeName]:
        return "Error - room already exists in this place."
    places[placeName][roomName] = {}
    return f"Room '{roomName}' created in place '{placeName}'."

def createAsset(placeName, roomName, assetName, price):
    if placeName in places and roomName in places[placeName]:
        places[placeName][roomName][assetName] = price
        return f"Asset '{assetName}' added to room '{roomName}' in place '{placeName}'."
    return "Error - place or room does not exist."

def deleteAsset(placeName, roomName, assetName):
    if placeName in places and roomName in places[placeName] and assetName in places[placeName][roomName]:
        del places[placeName][roomName][assetName]
        return f"Deleted asset '{assetName}' from room '{roomName}' in place '{placeName}'."
    return "Error - place, room, or asset not found."

def editAsset(placeName, roomName, assetName, newPrice):
    if placeName in places and roomName in places[placeName] and assetName in places[placeName][roomName]:
        places[placeName][roomName][assetName] = newPrice
        return f"Asset '{assetName}' in room '{roomName}' of place '{placeName}' updated to ${newPrice}."
    return "Error - place, room, or asset not found."

def deleteRoom(placeName, roomName):
    if placeName in places and roomName in places[placeName]:
        del places[placeName][roomName]
        return f"Deleted room '{roomName}' from place '{placeName}'."
    return "Error - place or room not found."

def deletePlace(placeName):
    if placeName in places:
        del places[placeName]
        return f"Deleted place '{placeName}'."
    return "Error - place not found."


def displayAll():
    if not places:
        print("No places have been created yet.")
        return
    for place, rooms in places.items():
        print(f"\nPlace: {place}")
        if rooms:
            for room, assets in rooms.items():
                print(f"  Room: {room}")
                if assets:
                    for asset, price in assets.items():
                        print(f"    - {asset}: ${price}")
                else:
                    print("    (No assets in this room)")
        else:
            print("  (No rooms in this place)")

def createStuff():
    place = input("Enter the name of the place you'd like to create: ")
    print(createPlace(place))

    room = input(f"What is the name of the room you'd like to create in '{place}'? ")
    print(createRoom(place, room))

    asset = input(f"What asset would you like to enter for room '{room}' in place '{place}'? ")
    price = float(input(f"What is the asset's price? "))
    print(createAsset(place, room, asset, price))

    print("\nHere's everything you've added so far:")
    displayAll()

username = input("What is your username: ")
password = input("What is your password: ")
print(createAccount(username, password))

createStuff()