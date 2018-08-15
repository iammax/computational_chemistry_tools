Here's a few tools I made that I found myself using constantly, so maybe somebody else will get some use out of them.

Scripts included:

* **periodic.py**

This is just a dict of {atom_name: atom_number} referenced by a few other scripts. At the moment it's mostly unpopulated.

* **z_matrix_maker.py** (requires: periodic.py, zmatconfig.txt)

This tool will transform a molpro-style xyz file into internal coordinates ([Z-matrix](https://en.wikipedia.org/wiki/Z-matrix_(chemistry))). The xyz file should be formatted like the included butadiene.xyz example file. Details of formatting below:

first line: Number of atoms

second line: Name of molecule (optional)

remaining lines: 

|Atom name |X coordinate|Y Coordinate|Z Coordinate|
---------------------------------------------------

z_matrix_maker reads from zmatconfig.txt to determine which bonds and angles to use. You can ignore this behavior by putting a 0 at the end of its invocation command, but you'll probably get results that are not physically meaningful doing this.

Call z_matrix_maker.py like this:

$ python z_matrix_maker *xyzfile.xyz*

The result z matrix will be put in results/

