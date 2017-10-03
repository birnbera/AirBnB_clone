#!/usr/bin/python3
"""class Place that inherits from Basemodel"""


BaseModel = __import__('base_model').BaseModel


class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        self.city_id = kwargs.pop(City.id, "")
        self.user_id = kwargs.pop(User.id, "")
        self.name = kwargs.pop(name, "")
        self.description = kwargs.pop(description, "")
        self.number_rooms = kwargs.pop(number_rooms, 0)
        self.number_bathrooms = kwargs.pop(number_bathrooms, 0)
        self.max_guest = kwargs.pop(max_guest, 0)
        self.price_by_night = kwargs.pop(price_by_night, 0)
        self.latitude = kwargs.pop(float(latitude), float(0.0))
        self.longitude = kwargs.pop(float(longitude), float(0.0))
        self.amenity_ids = kwargs.pop(Amenity_id, "")
