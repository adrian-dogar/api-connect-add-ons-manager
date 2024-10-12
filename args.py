import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Script for managing global policies, UDP, and gateway scripts.",
                                     add_help=False)
    parser.add_argument('--help', '-h', action='store_true', help='Show this help message and exit')

    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']):
        print_main_help()
        sys.exit(0)

    scope, operation = sys.argv[1].split(':') if ':' in sys.argv[1] else (sys.argv[1], None)

    if scope not in ['global-policies', 'udps', 'gw-scripts']:
        print(f"Error: Invalid scope '{scope}'. Use --help for more information.")
        sys.exit(1)

    if operation is None:
        print_scope_help(scope)
        sys.exit(0)

    valid_operations = {
        'global-policies': ['list', 'test', 'describe'],
        'udps': ['list', 'build', 'describe'],
        'gw-scripts': ['list', 'build', 'describe']
    }

    if operation not in valid_operations[scope]:
        print(f"Error: Invalid operation '{operation}' for scope '{scope}'. Use '{scope} --help' for more information.")
        sys.exit(1)

    parser.add_argument(f'{scope}:{operation}', help=f'Perform {operation} operation on {scope}')

    # Add specific arguments based on scope and operation
    if scope == 'global-policies':
        if operation == 'test':
            parser.add_argument('--policy-name', required=True, help='Name of the policy to test')
        elif operation == 'describe':
            parser.add_argument('--policy-id', required=True, help='ID of the policy to describe')
    elif scope == 'udps':
        if operation == 'build':
            parser.add_argument('--udp-name', required=True, help='Name of the UDP to build')
            parser.add_argument('--output-dir', default='.', help='Output directory for built UDP')
        elif operation == 'describe':
            parser.add_argument('--udp-id', required=True, help='ID of the UDP to describe')
    elif scope == 'gw-scripts':
        if operation == 'build':
            parser.add_argument('--script-name', required=True, help='Name of the gateway script to build')
            parser.add_argument('--output-dir', default='.', help='Output directory for built script')
        elif operation == 'describe':
            parser.add_argument('--script-id', required=True, help='ID of the gateway script to describe')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        sys.exit(0)

    # Your main logic here, using the parsed arguments


def print_main_help():
    print("Usage: python main.py <scope>:<operation> [options]")
    print("\nAvailable scopes:")
    print("  global-policies")
    print("  udps")
    print("  gw-scripts")
    print("\nUse '<scope> --help' for more information on a specific scope.")


def print_scope_help(scope):
    print(f"Usage: python main.py {scope}:<operation> [options]")
    print(f"\nAvailable operations for {scope}:")
    if scope == 'global-policies':
        print("  list")
        print("  test")
        print("  describe")
    elif scope == 'udps':
        print("  list")
        print("  build")
        print("  describe")
    elif scope == 'gw-scripts':
        print("  list")
        print("  build")
        print("  describe")
    print(f"\nUse '{scope}:<operation> --help' for more information on a specific operation.")
