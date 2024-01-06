from typing import Optional, List

from bson import ObjectId
from pydantic import BaseModel, Field


class FloorSize(BaseModel):
    floor_type: str
    value: float
    unitCode: str


class Address(BaseModel):
    address_type: str
    addressLocality: str
    addressRegion: str
    postalCode: str


class GeoCoordinates(BaseModel):
    geo_type: str
    addressCountry: str
    latitude: float
    longitude: float
    postalCode: str


class AnnounceDetail(BaseModel):
    rooms: int
    bead_rooms: int
    bathroom: int
    shower_room: int
    price: int
    price_m2: int
    dpe: str
    ges: str


class Announce(BaseModel):
    document_id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    created_at: Optional[str]
    updated_at: Optional[str]
    context: str
    announce_type: str
    name: str
    url: str
    floorSize: FloorSize
    address: Address
    geo: GeoCoordinates
    image: str
    announce_detail: AnnounceDetail
