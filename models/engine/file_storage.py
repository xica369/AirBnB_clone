#!/usr/bin/python3
from os.path import exists
from json import dump, load, dumps


class FileStorage:
    __file_path = "objects.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        iden = obj.id
        cl_id = class_name + "." + iden
        FileStorage.__objects[cl_id] = obj

    def save(self):
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict() #review error, firts case send a object that not contain this method
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fil:
            dump(dict_to_json, fil)

    def reload(self):
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                FileStorage.__objects = load(fil)
