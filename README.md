Here's a few tools I made that I found myself using constantly, so maybe somebody else will get some use out of them. Please let me know if anything doens't work!

Scripts included:

* **periodic.py**

This is just a dict of {atom_name: atom_number} referenced by a few other scripts. At the moment it's mostly unpopulated.

* **z_matrix_maker.py** (requires: periodic.py) (recommended: a zmatconfig file, see bottom of this section for details)

This tool will transform a molpro-style xyz file into internal coordinates ([Z-matrix](https://en.wikipedia.org/wiki/Z-matrix_(chemistry))). The xyz file should be formatted like the included toluene.xyz example file. Details of formatting below:

Call z_matrix_maker.py like this:

$ python z_matrix_maker *xyzfile.xyz* *zmatconfig_file*

The result z matrix will be put in results/

first line: Number of atoms

second line: Name of molecule (optional)

remaining lines: 

|Atom name |X coordinate|Y Coordinate|Z Coordinate|
---------------------------------------------------

z_matrix_maker reads from the zmatconfig file you provide it to determine which bonds and angles to use. You can ignore this behavior by leaving it out of the command to call z_matrix_maker.py, however the resulting z_matrix, while mathematically valid, will probably not utilize physically meaningful bonds and angles. The zmatconfig file is meant to make a z-matrix like the one in the bottom table on the above wikipedia page (checked on August 11, 2018), where there is a column for bonded atom, angled atom, and atom for dihedral plane respectively. The zmatconfig file's columns are:

|Atom number (in listed order in geometry input) |bonded atom|angled atom|dihedral atom|
---------------------------------------------------

For example if the a column is  1 2 3 4, the bond length will be between atoms 1 and 2, the angle will be between atoms 1, 2, and 3, and the dihedral angle will be between the planes created by atoms 1, 2, 3 and the plane created by atoms 2, 3, 4. Note that the first atom in a z-matrix essentially has no data (due to being arbitrarily placed), the second has only a bond length, and the third has only a bond length and bond angle, so a few numbers in zmatconfig are ignored (last 3 columns in row 1, last 2 columns in row 2, last 1 column in row 3). They need to be there anyway for the file to be parsed; just put any numbers.

Thanks to http://azevedolab.net/resources/dihedral_angle.pdf for a good guide on calculating dihedral angles.

* **xyz_matrix_maker** (requires: periodic.py)

This tool changes a z-matrix into a molpro-style xyz file. Format of source z_matrix should match that in example toluene.z file. 

Call *xyz_matrix_maker* like this:

$ python xyz_matrix_maker *z_matrix_file.z*

The resulting xyz matrix will be put in results/

* **Thanks, citations, linked articles**
http://azevedolab.net/resources/dihedral_angle.pdf - Good guide on calculating dihedral angles
