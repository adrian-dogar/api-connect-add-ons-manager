_verbose = False

def set_verbose() -> None:
    global _verbose
    _verbose = True

def unset_verbose() -> None:
    global _verbose
    _verbose = False

def get_verbose() -> bool:
    return _verbose
