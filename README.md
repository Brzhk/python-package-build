# My Awesome Package

A bootstrapped python package that supports multiple OS (Solaris, AIX, Windows, Linux) and Architectures (s390x, aarch64, amd64). It requires Python 3.11.

## Installation

You can install this package using pip:

```bash
pip install .
```

If you are publishing it to a PyPI repository, you can install it with:

```bash
pip install my-awesome-package
```

## Running the Package Scripts

Once installed, there are two primary ways to run the scripts provided by this package.

### 1. Using the Console Script

The package exposes a console script command that you can execute directly from your terminal:

```bash
my-awesome-script --name "Universe"
```

### 2. Using Python Module Execution

You can also run the script by specifying the python module:

```bash
python -m my_awesome_package.cli --name "Universe"
```

## Specifying the Python Interpreter

This package requires Python 3.11. If you have multiple versions of Python installed, you may need to explicitly specify the Python 3.11 interpreter.

### Linux/macOS (Unix-like)

You can specify the Python 3.11 executable directly:

```bash
python3.11 -m pip install .
python3.11 -m my_awesome_package.cli
```

### Windows

On Windows, you can use the Python Launcher (`py`) to specify the version:

```cmd
py -3.11 -m pip install .
py -3.11 -m my_awesome_package.cli
```

### Running the console script with a specific interpreter

If you want to ensure the console script `my-awesome-script` runs with a specific Python interpreter, you should install the package using that specific interpreter. The `pip` executable associated with that Python environment will hardcode the correct interpreter path in the script's shebang (the first line of the script file, like `#!/path/to/python3.11`).

```bash
# Install with the specific interpreter
/path/to/python3.11 -m pip install .

# Now, the script will automatically use that interpreter
my-awesome-script
```
