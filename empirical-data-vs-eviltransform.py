import csv
import eviltransform
from geopy.distance import distance

csv_filename = 'empirical-data.csv'
with open(csv_filename, newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    print('{:<13s}{:<18s}{:<21s}{:<9s}'.format(
        'City', 'My Sample', 'EvilTransform', 'Difference'))
    for row in csv_reader:

        # Skip provinces that do not use GCJ-02 on Google Maps
        if row['City'] in ['Hong Kong', 'Macau', 'Taipei']:
            continue

        # Retrieve and compute coordinates
        wgs84_coord = (float(row['WGS84 Lat']), float(row['WGS84 Lon']))
        empirical_coord = (float(row['GCJ-02 Lat']), float(row['GCJ-02 Lon']))
        eviltrans_coord = eviltransform.wgs2gcj(wgs84_coord[0], wgs84_coord[1])

        # Calculate distance between eviltransform and my sampled coordinate
        wgs84_empirical_diff = distance(wgs84_coord, empirical_coord).meters
        wgs84_eviltrans_diff = distance(wgs84_coord, eviltrans_coord).meters
        empirical_eviltrans_diff = distance(eviltrans_coord, empirical_coord).meters

        print(
            '{:<13s}{:<6.2f} metres     {:<6.2f} metres       {:>6.2f} metres'
            .format(
                row['City'],
                wgs84_empirical_diff,
                wgs84_eviltrans_diff,
                empirical_eviltrans_diff
            )
        )
