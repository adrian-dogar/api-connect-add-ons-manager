class Command:
    def __init__(self, name, alias, description):
        self.name = name
        self.alias = alias
        self.description = description

COMMANDS = [
    Command("get", "g", "Retrieve resources"),
    Command("apply", "a", "Apply changes to resources"),
    Command("rollout", "r", "Deploy resource"),
    Command("create", "c", "Create resources"),
    Command("edit", "e", "Edit resources"),
    Command("backup", "b", "Fetch resources from API Connect itself, and store them locally"),
    Command("api-resources", "ar", "List all available resources"),
    # Add more commands as needed
]

COMMAND_MAP = {command.name: command for command in COMMANDS}
COMMAND_MAP.update({command.alias: command for command in COMMANDS})

def get_command_names():
    return [command.name for command in COMMANDS]

def get_command_by_name(name):
    return COMMAND_MAP.get(name)