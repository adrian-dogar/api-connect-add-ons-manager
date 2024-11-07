import argparse

def create_home_parser():
    home_parser = argparse.ArgumentParser(description="API Connect Gateway add-ons handler")
    home_parser.add_argument("-v", "--verbose", action="store_true", help="Activate verbose output")

    home_subparser = home_parser.add_subparsers(dest="command")
    create_get_command_parser(home_subparser)
    create_apply_command_parser(home_subparser)
    create_rollout_command_parser(home_subparser)
    create_create_command_parser(home_subparser)
    create_edit_command_parser(home_subparser)
    create_backup_command_parser(home_subparser)

    return home_parser

def create_backup_command_parser(parent_subparser):
    backup_parser = parent_subparser.add_parser("backup", help="Fetch resources from API Connect itself, and store them locally")
    backup_subparser = backup_parser.add_subparsers(dest="resource")

def create_rollout_command_parser(parent_subparser):
    rollout_parser = parent_subparser.add_parser("rollout", help="Deploy resource")
    rollout_subparser = rollout_parser.add_subparsers(dest="resource")

def create_create_command_parser(parent_subparser):
    create_parser = parent_subparser.add_parser("create", help="Create resources")
    create_subparser = create_parser.add_subparsers(dest="resource")

def create_edit_command_parser(parent_subparser):
    edit_parser = parent_subparser.add_parser("edit", help="Edit resources")
    edit_subparser = edit_parser.add_subparsers(dest="resource")

def create_get_command_parser(parent_subparser):
    get_parser = parent_subparser.add_parser("get", help="Retrieve resources")
    get_subparser = get_parser.add_subparsers(dest="resource")
    create_get_all_resource_parser(get_subparser)
    create_gwext_resource_parser(get_subparser)

def create_gwext_resource_parser(parent_subparser):
    resource_parser = parent_subparser.add_parser("gw-extensions", help="Manage the gateway-extensions")
    resource_parser.add_argument("name", nargs="?", default="all", help="The gateway-extension name")
    resource_parser.add_argument("-i", "--instance", help="Instance where the resource resides")
    resource_parser.add_argument("-s", "--service", help="Service name or id")

def create_get_all_resource_parser(get_subparser):
    get_all_parser = get_subparser.add_parser("all", help="Get all resources")
    get_all_parser.add_argument("-i", "--instance", help="Instance where the resources reside")

def create_apply_command_parser(parent_subparser):
    # Apply command
    apply_parser = parent_subparser.add_parser("apply", help="Apply changes to resources")
    apply_parser.add_argument("resource", help="Resource to apply changes to")

def parse_args():
    parser = create_home_parser()
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        exit(1)
    return args
