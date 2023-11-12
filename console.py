#!/usr/bin/python3
"""
the console program: this program creates simple command line interpreters
used in handling/operating the AirBnB site.


major commands to be used are the: create, update and destroy. which will
handle the data creation, update and destroyig of data not needed.
"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter
    intro = "A command interpreter to manipulate AirBnB data"
    """
    prompt = '(hbnb) '

    objects = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place,
               'Review': Review
               }

    def do_quit(self, args):
        """quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """called when an empty line is entered in response to the prompt
        """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel

        Return:
            The id of the instance
        """
        if args == '':
            print("** class name missing **")
        elif args in HBNBCommand.objects.keys():
            my_model = HBNBCommand.objects[args]()
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234

        Return:
            The string representation of the object id
        """
        token = args.split()
        if args == "":
            print("** class name missing **")
        elif token[0] in HBNBCommand.objects.keys():
            if len(token) < 2:
                print("** instance id missing **")
                return False
            all_objs = storage.all()
            obj_id = '{}.{}'.format(token[0], token[1])
            if obj_id not in all_objs.keys():
                print("** no instance found **")
            else:
                print(all_objs[obj_id])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234

        Return:
            Nothing
        """
        token = args.split()
        if args == "":
            print("** class name missing **")
        elif token[0] in HBNBCommand.objects.keys():
            if len(token) < 2:
                print("** instance id missing **")
                return False
            all_objs = storage.all()
            obj_id = '{}.{}'.format(token[0], token[1])
            if obj_id not in all_objs.keys():
                print("** no instance found **")
            else:
                del all_objs[obj_id]
                storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
