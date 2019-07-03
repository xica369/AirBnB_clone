#!/usr/bin/python3
""" Class FileStorage """
from os.path import exists
from json import dump, load, dumps
from models import base_model, user, place, state, city, amenity, review

BaseModel = base_model.BaseModel
User = user.User
Place = place.Place
State = state.State
City = city.City
Amenity = amenity.Amenity
Review = review.Review
name_class = ["BaseModel", "City", "State", "Place",
              "Amenity", "Review", "User"]


class FileStorage:
    """ Create private class variables """
    __file_path = "objects.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
        <obj class name>.id """
        class_name = obj.__class__.__name__
        iden = obj.id
        cl_id = class_name + "." + iden
        FileStorage.__objects[cl_id] = obj

    def save(self):
        """ serializes __objects to the JSON file
        (path: __file_path) """
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fil:
            dump(dict_to_json, fil)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists )
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised) """
        dict_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                dict_obj = load(fil)
                for key, value in dict_obj.items():
                    class_nm = key.split(".")[0]
                    if class_nm in name_class:
                        FileStorage.__objects[key] = eval(class_nm)(**value)
                    else:
                        pass
