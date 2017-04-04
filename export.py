
# Export functions


def export_inventory(inventory, filename="export_inventory.csv"):
    file = open(filename, 'w')
    for i in inventory:
        file.write((i + ',') * inventory[i])
    file.close()
    import os
    with open(filename, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
