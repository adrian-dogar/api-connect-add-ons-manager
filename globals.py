_verbose = False

def set_verbose() -> None:
    global _verbose
    _verbose = True

def unset_verbose() -> None:
    global _verbose
    _verbose = False

def get_verbose() -> bool:
    return _verbose

_tokens = {}

def append_token(instance: str, interface: str, token: dict) -> None:
    global _tokens
    _tokens.update({instance: {interface: token}})

def get_token(instance: str, interface: str) -> str:
    global _tokens
    return _tokens[instance][interface]

