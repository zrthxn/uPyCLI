# uPyCLI

A microscopic library to turn any function into a CLI.

Takes some inspiration from [pycli](https://github.com/garenchan/pycli) although I didn't know 
this existed before starting. This lib is even smaller than `pycli` and does not require any setup 
and has no dependencies.

## Usage

```bash
cli path.to.your.function --help
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
