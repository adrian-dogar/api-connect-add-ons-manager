import json

import globals

from args import home as args_handler
from controllers import commands
from logger import setup_logger, set_log_level

# import sys
from configobj.config import Config
from light_token_manager import LightTokenManager

logger = setup_logger(__name__, "INFO")

def main():

    args = args_handler.parse_args()

    if args.verbose:
        globals.set_verbose()
        set_log_level(logger, "DEBUG")

    # Read instances config
    config = Config("config.yaml", env_file=".env").items()
    # print(json.dumps(config, indent=2))

    refresh_tokens(config)

    commands.run(args)


def refresh_tokens(config):
    for instance, instance_details in config['instances'].items():
        for interface, interface_details in instance_details.items():
            if interface_details.get('enabled'):
                logger.debug(f"Fetching token for [{interface}] interface of the [{instance}] instance")
                ltm = LightTokenManager(
                    token_url=f"{interface_details['url']}/api/token",
                    payload_format="json",
                    body={
                        "client_id": interface_details['client_id'],
                        "client_secret": interface_details['client_secret'],
                        "grant_type": interface_details['grant_type'],
                        "username": interface_details['username'],
                        "password": interface_details['password'],
                        "realm": interface_details['realm']
                    }
                )
                globals.append_token(
                    instance=instance,
                    interface=interface,
                    token=ltm.get_token()
                )


if __name__ == "__main__":
    main()