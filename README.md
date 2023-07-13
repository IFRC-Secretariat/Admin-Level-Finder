# Admin levels finder

Get the admin levels of a point give it's coordinates.
Admin levels are from [GADM](https://gadm.org/index.html).


## Setup

To use the project, clone the repository from Github, and install the package as a Python package:

```bash
# Clone the repository
git clone git@github.com:IFRC-Secretariat/Admin-Levels-Finder.git
cd Admin-Levels-Finder

# Install packages from the requirements file
python3 -m pip install -r requirements.txt

# Install the package with pip from the root directory
python -m pip install .
```


## Example

The following is an example of how to use the package to get the details of a point, including admin 1 and admin 2 levels (from GADM).

https://github.com/IFRC-Secretariat/Admin-Level-Finder/blob/3a4b6d6f1bde431c68118dbcc9f3d39d4dabcf3f/examples/find_point.py#L1-L26