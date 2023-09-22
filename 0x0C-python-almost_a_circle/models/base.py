#!/usr/bin/python3
""" class base model """
import json
import turtle
import csv


class Base:
    """ the base of all other classess """
    __nb_objects = 0

    def __init__(self, id=None):
        """ it initializes a Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethods
    def to_join_string(list_dictionaries):
        """ returns a list of dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ wrights a list of objects to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dicts_l = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(dicts_l))

    @staticmethod
    def from_json_string(json_string):
        """ returns the json string """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns a class from a dictionary attrs """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                m = cls(1, 1)
            else:
                m = cls(1)
            m.update(**dictionary)
            return m

    @classmethod
    def load_from_file(cls):
        """ list of classes fro ama json string """
        f_name = str(cls.__name__) + ".json"
        try:
            with open(f_name, "r") as jsonfile:
                l_d = Base.from_json_string(jsonfile.read())
                return [cls.create(**i) for i in l_d]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves a list of objects to a file in csv format """
        f_name = cls.__name__ + ".csv"
        with open(f_name, "w", newline="") as csvfile:
            if list_objs id None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fld_name = ["id", "width", "height", "x", "y"]
                else:
                    fld_name = ["id", "size", "x", "y"]
                w = csv.DictWriter(csvfile, fld_name=fld_name)
                for i in list_objs:
                    writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ a list of classess from a csv file """
        f_name = cls.__name__ + ".csv"
        try:
            with open(f_name, "w", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fld_name = ["id", "width", "height", "x", "y"]
                else:
                    fld_name = ["id", "size", "x", "y"]
                    l_d = csv.DictReader(csvfile, fld_name=fld_name)
                    l_d = [dict([m, int(n)] for m, n in a.items())
                           for a in l_d]
                    return [cls.create(**a) for a in l_d]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ useing turtle to draw rectagles and squares """
        t = turtle.Turtle()
        t.screen.bgcolor('#b7312c')
        t.pensize(3)
        t.shape("turtle")

        t.color('#ffffff')
        for i in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(i.x, i.y)
            t.down()
            for j in range(2):
                t.forward(i.width)
                t.left(90)
                t.forward(i.height)
                t.left(90)
            t.hideturtle()
        t.color("#b5e3d8")
        for k in list_squares:
            t.showturtle()
            t.up()
            t.goto(k.x, k.y)
            t.down()
            for m in range(2):
                t.forward(k.width)
                t.left(90)
                t.forward(k.height)
                t.left(90)
            t.hideturtle()
        t.exitonclick()
