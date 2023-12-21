import os
from sys import argv, modules
from argparse import ArgumentParser
import importlib
from importlib import import_module
from importlib.util import spec_from_file_location, module_from_spec

"""
Runner Module
-------------

This module can be used to run functions in modules of this project.
This is especially useful in training different models each with their own training method.

    ```bash
    python runner.py models.sentence train
    ```

For this to work, all you need to do is have a function in the module with the right type-annotations
and all optional values should have a default value.

    ```python
    # Here model_name is required and data_path is optional
    def train(
            model_name: str, 
            data_path: str = "./path/to/data"):
        ...
    ```

You can even see the required inputs for a particular model's training
using the `--help` flag.

    ```bash
    python runner.py models.sentence train --help
    >>> usage: runner.py [-h] [--base_path BASE_PATH] [--epochs EPOCHS] [--batch_size BATCH_SIZE] [--device DEVICE]

    options:
    -h, --help            show this help message and exit
    --base_path BASE_PATH
    --epochs EPOCHS
    --batch_size BATCH_SIZE
    --device DEVICE
    ```
"""


def run():
    TARGET = argv[1]

    if '.' in TARGET:
        path, name = TARGET.rsplit('.', 1)
        target_path = os.path.abspath(os.path.curdir)
        
        # os.chdir(target_path)
        print(target_path)
        print(os.listdir())
        
        # specify the module that needs to be imported relative to the path of the module
        spec = spec_from_file_location(path, f"{target_path}/{path.replace('.', '/')}.py")
        module = module_from_spec(spec)
        
        # executes the module in its own namespace when a module is imported or reloaded.
        spec.loader.exec_module(module)
        
        func = getattr(module, name)
    else:
        # We cant yet handle root level modules
        raise NotImplementedError

    annotations = func.__annotations__
    defaults = func.__defaults__

    parser = ArgumentParser(description = func.__doc__)

    # Required args are the first arguments for which a default value
    # is not available. This will add those as required.
    required = list(annotations.items())[:len(annotations) - len(defaults)]
    for aname, atype in required:
        parser.add_argument(f"--{aname}", 
                            type=atype, 
                            help='%(type)s',
                            required=True)

    # Optional args are those for which a default value is available.
    optional = list(annotations.items())[len(annotations) - len(defaults):]
    for (aname, atype), dvalue in zip(optional, defaults):
        parser.add_argument(f"--{aname}", 
                            type=atype, 
                            help='%(type)s (default %(default)s)',
                            default=dvalue)

    if "--help" in argv:
        parser.print_help()
        exit()
    
    args = parser.parse_args(argv[3:])
    func(**dict(args._get_kwargs()))


if __name__ == "__main__":
    run()