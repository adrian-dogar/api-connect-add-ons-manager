import globals

from args import home as args_handler
from controllers import commands
from logger import setup_logger, set_log_level

# import sys
# from configobj.config import Config

def main():
    logger = setup_logger(__name__, "INFO")

    args = args_handler.parse_args()

    if args.verbose:
        globals.set_verbose()
        set_log_level(logger, "DEBUG")

    commands.run(args)


    # Read instances config
    # config_parser = Config("instances.json", env_file=".env")
    # instances_config = config_parser.items()

if __name__ == "__main__":
    main()