# computational_chemistry_tools
Some tools that I made for my computational chemistry research, which I've put here to share with the other members of my lab. If you are a non-chemist/physicist looking at this directory, the most interesting thing for you is probably the jupyter notebook inside butadiene_iterator.

A brief chapter of contents of this repo:

butadiene_iterator: (Includes jupyter notebook!) This tool is something I used to generate batches of hundreds of frames of molecular coordinate data for butadiene when I was using butadiene as a model to test the computational chemistry algorithms I was developing.

hartree_fock_lesson: This was a quick demo of how to code the hartree-fock method that I did on the fly as a demo when I was a grad student, in order to teach some undergrads working in my lab how hartree fock worked. Will mostly be of interest to chemists/physicists

psi4_energy_reader: Includes a python script that reads output logfiles made by psi4 and plots the energy data in them
terachem_energy_reader: Same as above but for terachem logfiles

xyz_zmat_convert: This has its own extended readme. The short version is that it converts between normal cartesian xyz coordinates, and internal coordinates (aka z-matrices).
