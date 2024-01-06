import csv

import pandas as pd


def csv_exporter(load_announces):
    df = pd.json_normalize(load_announces)
    columns_order = ['_id', 'created_at', 'updated_at', '@context', '@type', 'name', 'url',
                     'floorSize.@type', 'floorSize.value', 'floorSize.unitCode',
                     'address.@type', 'address.addressLocality', 'address.addressRegion', 'address.postalCode',
                     'geo.@type', 'geo.addressCountry', 'geo.latitude', 'geo.longitude', 'geo.postalCode',
                     'image', 'announce_detail.rooms', 'announce_detail.bead_rooms', 'announce_detail.bathroom',
                     'announce_detail.shower_room', 'announce_detail.price', 'announce_detail.price_m2',
                     'announce_detail.dpe', 'announce_detail.ges']

    df = df[columns_order]
    df.to_csv('donnees_immobilieres.csv', index=False)

