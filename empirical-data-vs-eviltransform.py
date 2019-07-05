import csv
import eviltransform
from geopy.distance import distance

csv_filename = 'empirical-data.csv'
with open(csv_filename, newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:

        # Skip provinces that do not use GCJ-02 on Google Maps
        if row['City'] in ['Hong Kong', 'Macau', 'Taipei']:
            continue

        # Retrieve and compute coordinates
        wgs84_coord = (float(row['WGS84 Lat']), float(row['WGS84 Lon']))
        empirical_coord = (float(row['GCJ-02 Lat']), float(row['GCJ-02 Lon']))
        eviltrans_coord = eviltransform.wgs2gcj(wgs84_coord[0], wgs84_coord[1])

        # Calculate distance between eviltransform and my sampled coordinate
        d = distance(eviltrans_coord, empirical_coord).meters

        print((row['City'] + ':').ljust(15) + str(d) + ' metres')
