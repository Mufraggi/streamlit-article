import csv
from datetime import datetime

import psycopg2
from psycopg2.extras import execute_values

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname="mydb",
    user="user",
    password="password",
    host="localhost",
    port=5432
)

cur = conn.cursor()


def parse_csv_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')


insert_query = """
    INSERT INTO real_estate_properties (
         name, url, floor_size_value,
        address_locality, address_region, address_postal_code,
        geo_latitude, geo_longitude, rooms, bead_rooms, bathroom,
        shower_room, price, price_m2, dpe, ges
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
"""

with open('donnees_immobilieres.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        name = row['name']
        url = row['url']
        floor_size_value = float(row['floorSize.value'])
        address_locality = row['address.addressLocality']
        address_region = row['address.addressRegion']
        address_postal_code = row['address.postalCode']
        geo_latitude = float(row['geo.latitude'])
        geo_longitude = float(row['geo.longitude'])
        rooms = int(row['announce_detail.rooms'])
        bead_rooms = int(row['announce_detail.bead_rooms'])
        bathroom = int(row['announce_detail.bathroom'])
        shower_room = int(row['announce_detail.shower_room'])
        price = float(row['announce_detail.price'])
        price_m2 = float(row['announce_detail.price_m2'])
        dpe = row['announce_detail.dpe']
        ges = row['announce_detail.ges']

        # Execute the SQL INSERT query
        cur.execute(
            insert_query,
            (name, url, floor_size_value,
             address_locality, address_region, address_postal_code,
             geo_latitude, geo_longitude, rooms, bead_rooms, bathroom,
             shower_room, price, price_m2, dpe, ges)
        )
conn.commit()
cur.close()
conn.close()
