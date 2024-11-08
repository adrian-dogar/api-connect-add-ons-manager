import argparse
from models.resource import get_resource_names, RESOURCES
from models.command import get_command_names, get_command_by_name

def create_home_parser():
    home_parser = argparse.ArgumentParser(description="API Connect Gateway add-ons handler")
    home_parser.add_argument("-v", "--verbose", action="store_true", help="Activate verbose output")

    home_subparser = home_parser.add_subparsers(dest="command")
    for command_name in get_command_names():
        command = get_command_by_name(command_name)
        create_resource_parser(home_subparser, command.name, command.alias, command.description)

    return home_parser

def create_resource_parser(parent_subparser, name, alias, description):
    command_parser = parent_subparser.add_parser(name, help=description)
    command_subparser = command_parser.add_subparsers(dest="resource")
    create_get_all_resource_parser(command_subparser)

    for resource in RESOURCES:
        resource_parser = command_subparser.add_parser(resource.name, help=f"Manage {resource.name}")
        resource_parser.add_argument("name", nargs="?", default="all", help=f"The {resource.name} name")
        resource_parser.add_argument("alias", nargs="?", default="all", help=f"The {resource.name} name")
        resource_parser.add_argument("-i", "--instance", help="Instance where the resource resides")
        resource_parser.add_argument("-s", "--service", help="Service name or id")

def create_api_resources_command_parser(parent_subparser):
    api_resources_parser = parent_subparser.add_parser("api-resources", help="List all available resources")

def create_get_all_resource_parser(get_subparser):
    get_all_parser = get_subparser.add_parser("all", help="Get all resources")
    get_all_parser.add_argument("-i", "--instance", help="Instance where the resources reside")

def parse_args():
    parser = create_home_parser()
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        exit(1)
    return args