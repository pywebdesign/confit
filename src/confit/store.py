

from config_reader import ConfigReader
from confit.dependencies import resolve_dependencies_order
from confit.utils.import_utils import import_anything
from collections import defaultdict

class PlaceHolderDependency:
    def __init__(self, type_value, key, value, full_key):
        self.key = key
        self.value = value
        self.full_key = full_key
        self.type_value = type_value
        self.resolved = None
        self.params = {}

    def __str__(self):
        return f"PlaceHolderDependency({self.full_key}, {self.type_value})"

    def __repr__(self):
        return str(self)
    

class Store:
    def __init__(self):
        self.store = {}
        self.dependencies = defaultdict(list)

    def get(self, s):
        return self.store[s]

def resolve_module_and_params(store, placeholder: PlaceHolderDependency):
    try:
        for key, maybe_placeholder in placeholder.params.items():
            match maybe_placeholder:
                case PlaceHolderDependency() as param_placeholder:
                    placeholder.params[key] = store.store[param_placeholder.full_key]
        object = import_anything(placeholder.type_value)(**placeholder.params)
        store.store[placeholder.full_key] = object
        return placeholder.full_key
    except TypeError as e:
        raise TypeError(f"Error in {placeholder.full_key} {e}")
    except NameError as e:
        raise NameError(f"Error in {placeholder.full_key} {e}")


def build_params(store, params, parent=None):
    built_params = {}
    for key, value in params.items():
        match value:
            

            case {"type": type_value, **other_params}:
                full_key = f"{parent.full_key}.{key}" if parent is not None else key
                placeholder = PlaceHolderDependency(type_value, key, value, full_key)
                params = build_params(store, other_params, placeholder)
                placeholder.params = params
                built_params[key] = placeholder
                store.store[full_key] = placeholder
                if parent is not None:
                    store.dependencies[parent.full_key].append(full_key)
            case {"_id": full_key}:
                placeholder = PlaceHolderDependency(None, key, value, full_key)
                built_params[key] = placeholder
                if parent is not None:
                    store.dependencies[parent.full_key].append(full_key)
            case _:
                built_params[key] = value
    return built_params

def build_store(confit_config):
    store = Store()
    tree = build_params(store, confit_config)
    for dependency in resolve_dependencies_order(store.dependencies):
        try:
            resolve_module_and_params(store, store.store[dependency])
        except KeyError as e:
            print(f"Error in {dependency} {e}")
    for key, maybe_placeholder in store.store.items():
        match maybe_placeholder:
            case PlaceHolderDependency() as placeholder:
                placeholder.resolved = resolve_module_and_params(store, placeholder)
                store.store[key] = placeholder.resolved
    return store



def init():
    confit_config = ConfigReader("./confit.yaml").read()
    store = build_store(confit_config)
    return store
    


