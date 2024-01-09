# Truth Table Calculator

This repo is for a python application for which with a simple UI the user can input the resulting output for a N-1 binary table. 

## Installation

Use the a package manager like [pip](https://pip.pypa.io/en/stable/) to install the required packages these are packed into a requirements file and can be installed using the following command.

```bash
pip install -r requirements.txt
```
Then use git to clone the repo to your preferred folder. 

```bash
git clone https://github.com/tobsthetobs/TruthTableCalculator
```

## Usage
Simply to navigate to installed directory and launch.

```bash
cd project_dir
python gui.py
```

## Tests

Tests can be run in the project directory using the following command. 
``` bash
cd project_dir
python -m unittest discover -p "test_*"
```

## Todo

- [x] Add basic table to expression via GUI functionality
- [X] Add support for entry of Dont Care conditions.
- [X] Add parser for estimating number of gates needed to implement given function from table.
- [ ] Allow for user to rename variables.


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
