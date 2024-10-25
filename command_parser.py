from kv_store import set_key_value, get_key

HELP_TEXT = """
Usage:
1. set <key> <value> -> Set a value for a particular key
2. get <key> -> Get value for the given key. Return -None- if nothing found.
"""

def read_command():
    # TODO : Use cleaner logging
    command = input().lower()
    print(f"Command is: << {command} >>")
    if not (command.startswith("set") or command.startswith("get")):
        print("COMMAND WRONG!", command)
        print(HELP_TEXT)
        return
    
    split_command = [token.strip() for token in command.split()]
    print(split_command)
    if split_command[0] == "set" and not len(split_command) == 3:
        print("SET COMMAND WRONG!")
        print(HELP_TEXT)
        return
    
    if split_command[0] == "get" and not len(split_command) == 3:
        print("GET COMMAND WRONG!")
        print(HELP_TEXT)
        return
    
    if (split_command[0] == "set"):
        print("Handling set command...")
        _handle_set_command(split_command[1], split_command[2])
    else:
        print("Handling get command...")
        _handle_get_command(split_command[1])



def _handle_set_command(key, value):
    set_key_value(key, value)


def _handle_get_command(key):
    get_key(key)
