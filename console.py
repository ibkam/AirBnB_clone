#!/usr/bin/python3
"""Defines the HBNBCommand class"""

import cmd
from shlex import split

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'Amenity': Amenity,
        'Place': Place,
        'City': City,
        'Review': Review
        }


class HBNBCommand(cmd.Cmd):
    """HBNBCommand commands"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the console"""
        return True

    def do_EOF(self, line):
        """Exit the console"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self):
        """Creates command: to create new user"""
        command = split(line)
        if not command:
            print("** class name missing **")
        elif command[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[command[0]]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """Show command: show an instance based on the class name and id"""
        command = line.split()

        if not command:
            print("** class name missing **")
        elif command[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            new_instance = "{}.{}".format(command[0], command[1])
            objs = storage.all()

            if new_instance not in objs:
                print("** no instance found **")
            else:
                print(objs[new_instance])

    def do_destroy(self):
        """Delete command: delete an instance based on class name and id"""
        command = split(line)

        if not command:
            print("** class name missing **")
            return False
        elif command[0] not in classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            new_instance = command[0] + '.' + command[1]
            if new_instance not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[new_instance]
                storage.save()

    def do_all(self):
        """All comman: print all instances based one"""
        instance_list = []

        if not line:
            for new_instance in storage.all().values():
                instance_list.append(str(new_instance))
        else:
            command = split(line)
            if command[0] in classes:
                for key, value in storage.all().items():
                    if value.__class__.__name__ == command[0]:
                        instance_list.append(str(value))
                    else:
                        print("** class doesn't exist **")
                        return False
        print(instance_list)

    def do_update(self):
        """Update command: an instance based on the class name and id"""
        command = split(line)

        if not command:
            print("** class name missing **")
        elif command[0] not in classes:
            print("** class doesn't exist **")
        elif len(command[0]) < 2:
            print("** instance id missing **")
        elif len(command[0]) < 3:
            print("** attribute name missing **")
        elif len(command[0]) < 4:
            print("** value missing **")
        else:
            new_instance = command[0] + '.' + command[1]
            if new_instance not in storage.all()[new_instance]:
                print("** no instance found **")
            else:
                setattr(storage.all()[new_instance], command[2], command[3])
                storage.save()

    def default(self, line):
        i = 0
        command = line.split('.', 1)
        if len(command) >= 2:
            line = command[1].split('c')
            if line[0] == 'all':
                self.do_all(command[0])
            elif line[0] == i:
                for key, in storage.all():
                    if command[0] == key.split(".")[0]:
                        i += 1
                print(i)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
