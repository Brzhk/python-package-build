# My Awesome Package

A bootstrapped python package that supports multiple OS (Solaris, AIX, Windows, Linux) and Architectures (s390x, aarch64, amd64). It requires Python 3.11.

## Build Instructions

To build the package, you need the `build` module. You can run the following command from the root of the repository:

```bash
python3 -m build
```

This will create a `.tar.gz` source distribution and a `.whl` binary wheel in the `dist/` directory.

## Installation

You can install this package using pip:

```bash
pip install .
```

If you are publishing it to a PyPI repository, you can install it with:

```bash
pip install my-awesome-package
```

## User Installation (`--user`)

If you install the package using the `--user` flag (e.g., `pip install --user .`), the executable scripts (`my-awesome-script`, `my-other-script`) will be placed in a user-specific directory. To run these scripts from anywhere, you must ensure this directory is in your system's `PATH`.

### Linux/macOS
The scripts are typically installed in `~/.local/bin`. Add it to your `PATH` by adding this line to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```
Then, reload your configuration (e.g., `source ~/.bashrc`).

### Windows
The scripts are typically installed in `%APPDATA%\Python\Python311\Scripts` (adjusting for your specific Python version). Add this directory to your `PATH` via the System Properties -> Environment Variables dialog.

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
