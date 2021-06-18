import csv
import sys
import xml.etree.ElementTree as ET


# Validate args
if len(sys.argv) != 3:
    print("Usage: XGchecker.py <inputfile.itxml> <valid_XG_list.csv>")
    sys.exit()
else:
    inputfile = sys.argv[1]
    valid_XGs_file = sys.argv[2]


# Get Schedule to parse
try:
    tree = ET.parse(inputfile)
# error for file not found
except FileNotFoundError:
    print(f"couldn't find {sys.argv[1]}")
    print("Usage: XGchecker.py <inputfile.itxml> <valid_XG_list.csv>")
    sys.exit()
# error for invalid file
except:
    print("Couldn't read .itxml file")
    sys.exit()
schedule = tree.getroot()


# Read authorized XG names
authorized_XG = set()
try:
    with open(valid_XGs_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            authorized_XG.add(row[0])
except FileNotFoundError:
    print(f"couldn't find {sys.argv[2]}")
    print("Usage: XGchecker.py <inputfile.itxml> <valid_XG_list.csv>")
    sys.exit()
except:
    print("Couldn't read .csv file")
    sys.exit()



# Store all XG events present in schedule
XG_events = []
for event in schedule:
    try:
        if event[1].find("SecondaryEvent").text == "true":
            XG_events.append(event)
    except:
        #print("Not a XG")
        pass


# Check if XG Templates names are valid
valid_count = 0
invalid_count = 0

for event in XG_events:
    name = event[2].find("Template").text
    if name in authorized_XG:
        valid_count += 1
    else:
        # Show the invalid Templates to user
        print(f"Invalid Template name: [{name}] at {event.attrib['originalStartTime']}\n")
        invalid_count += 1

# Print report
print(f"Checked if every XG in Schedule is one of these:\n{authorized_XG}\n")
print(f"{len(XG_events)} templates checked.")
print(f"invalid: {invalid_count}")
print(f"valid: {valid_count}")
