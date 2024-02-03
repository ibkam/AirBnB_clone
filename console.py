#!/usr/bin/python3
"""Defines the HBNBCommand class"""

import cmd


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
            objs = models.storage.all()

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
        elif: len(command) < 2:
            print("** instance id missing **")
        else:
            new_instance = command[0] + '.' + command[1]
            if new_instance not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[new_instance]
                storage.save()

    def do_all(self):
        """Prints all string representation of all instances
        based or not on the class name"""
        pass

    def do_update(self):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file)"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
