# Python Unit Testing Example

This is a simple example of how to use Python's built-in `unittest` module to write and run unit tests.

Interleave string solution is from my own Leetcode [submission](https://leetcode.com/problems/interleaving-string/submissions/856314608).

## Quick Start

- To run the tests and downloaded required packages:

```bash
sh build.sh
```

- Example of Canary and regular tests are in `./tests/interleave_tests.py`
- Expected result is

```bash
Ran 5 tests in 0.000s

OK
```

## Structure

- `build.sh`: This script installs required pip packages and runs the tests using "python3."
- `requirements.txt`: This file is used by pip to install packages. If you require any packages, you can add them here.
- `src`: This directory contains your source files, i.e., your code.
- `tests`: All your tests are located here.

## Testing

`unittest` is the preinstalled Python testing library. There are alternatives you may consider, such as Pytest. Running the test is as simple as:

```bash
python -m unittest [directory]
```

If you prefer a more verbose output, add `-v`:

```bash
python -m unittest -v [directory]
```

## Packages

For most, pip is your go-to for packages. For those coming from JavaScript, there isn't a `package.json`; the alternative is `requirements.txt`. You can include any required packages in this file, and anyone using pip can install them simply.

Example `requirements.txt`:

```makefile
pip==22.3.1
wheel==0.38.4
Pillow==9.5.0
setuptools==65.5.1
packaging==23.1
numpy==1.26.0
```

To install the packages, it is as simple as:

```bash
pip install -r requirements.txt
```

---

Have fun! If you find a mistake or an improvement, please drop a pull request and let me know!
