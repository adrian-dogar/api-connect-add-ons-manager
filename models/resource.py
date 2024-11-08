class Resource:
    def __init__(self, name, alias, description):
        self.name = name
        self.alias = alias
        self.description = description

RESOURCES = [
    Resource("gateway-extension", "gwext", "Manage gateway extensions"),
    Resource("user-defined-policy", "udp", "Manage User Defined Policies"),
    Resource("global-policies", "gp", "Manage global policies"),
    Resource("preflow", "gp-pre", "Manage global policies inside preflows (prehook)"),
    Resource("postflow", "gp-post", "Manage global policies inside postflows (posthook)"),
]

RESOURCE_MAP = {resource.name: resource for resource in RESOURCES}
RESOURCE_MAP.update({resource.alias: resource for resource in RESOURCES})

def get_resource_names():
    return [resource.name for resource in RESOURCES]

def get_resource_by_name(name):
    return RESOURCE_MAP.get(name)