from models.resource import RESOURCES

def api_resources_command(args):
    print("Available API resources:")
    print("{:<30} {:<15} {}".format("NAME", "SHORTNAME", "DESCRIPTION"))
    print("{:<30} {:<15} {}".format("----", "---------", "-----------"))
    for resource in RESOURCES:
        print("{:<30} {:<15} {}".format(resource.name, resource.alias, resource.description))

def get_command(args):
    from controllers import get
    if args.resource == "all":
        get.all(args)
    else:
        get.resource(args)

def edit_command(args):
    print(f"Getting specific {args.resource}")

def apply_command(args):
    print(f"Applying to {args.resource}")

def run_func(func_string, args=None):
    try:
        global_namespace = globals()
        if func_string in global_namespace and callable(global_namespace[func_string]):
            return global_namespace[func_string](args)
        else:
            raise NameError(f"Function '{func_string}' not found")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def run(args):
    run_func(f"{args.command.replace('-', '_')}_command", args=args)
