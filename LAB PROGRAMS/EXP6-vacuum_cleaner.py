
# Vacuum Cleaner Problem

rooms = {
    'A': input("Enter status of Room A (Clean/Dirty): ").lower(),
    'B': input("Enter status of Room B (Clean/Dirty): ").lower()
}

location = input("Enter vacuum cleaner location (A/B): ").upper()

while 'dirty' in rooms.values():
    if rooms[location] == 'dirty':
        print("Room", location, "is Dirty. Cleaning...")
        rooms[location] = 'clean'
        print("Room", location, "is now Clean.")
    else:
        print("Room", location, "is already Clean.")

    if 'dirty' in rooms.values():
        location = 'B' if location == 'A' else 'A'

print("\nBoth rooms are Clean!")