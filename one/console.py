#!/usr/bin/python3
"""Command Line Interpreter for HBNB"""
import cmd
import json
import re
import sys

from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exits the program"""
        print()
        return True

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in storage.classes():
            print("** class doesn't exist **")
            return
        instance = storage.classes()[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Shows the details of a specific instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes a specific instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Displays all instances of a class or all classes"""
        instances = []
        if arg:
            if arg not in storage.classes():
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if key.startswith(arg):
                    instances.append(str(obj))
        else:
            for obj in storage.all().values():
                instances.append(str(obj))
        print(instances)

    def do_update(self, arg):
        """Updates a specific instance"""
        args = re.match(r'^(\w+)\s([\w-]+)\s(.*)$', arg)
        if not args:
            print("** class name missing **")
            return
        class_name, instance_id, rest = args.groups()
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]

        # Handle dictionary update
        if rest.startswith('{') and rest.endswith('}'):
            try:
                updates = json.loads(rest)
            except json.JSONDecodeError:
                print("** invalid syntax **")
                return
            for attr, value in updates.items():
                setattr(instance, attr, value)
            instance.save()
            return

        # Handle attribute update
        rest_args = re.match(r'^"([^"]+)"\s"([^"]+)"$', rest)
        if not rest_args:
            print("** value missing **")
            return
        attr, value = rest_args.groups()
        setattr(instance, attr, value)
        instance.save()

    def emptyline(self):
        pass

    def precmd(self, line):
        """Preprocesses command line input"""
        match = re.match(r'^(\w+)\.(\w+)\(([^)]*)\)$', line)
        if match:
            class_name, method, args = match.groups()
            args = args.split(", ")
            args = " ".join([arg.strip('"') for arg in args])
            return f"{method} {class_name} {args}"
        return line

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in storage.classes():
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all() if key.startswith(arg))
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

