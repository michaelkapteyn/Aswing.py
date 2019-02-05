# Aswing.py
Python wrapper for [ASWING](http://web.mit.edu/drela/Public/web/aswing/)

# Dependencies
### ASWING
A licensed copy of ASWING must be obtained separately. ASWING should be installed and the directory containing the executable added to your system path. Currently, this wrapper does not require any modifications to the ASWING source files. For more information about ASWING, see the documentation on the [ASWING home page.](http://web.mit.edu/drela/Public/web/aswing/)

### Python
This package has been developed and tested using Python 3.7.0.

### Linux/OSX
This package was developed and tested using MacOS Mojave and Linux 18.04.

# Functionality
This wrapper provides a python interface for defining ASWING models, and performing ASWING analysis.

The following functionality has been implemented:
- Geometry Definition
    - Read .asw file
    - Manipulate geometry via python object
    - Write .asw file
- Operating Point Definition
    - Define Operating Point via python object
- Steady Solution
    - Write ASWING commands file
    - Execute ASWING and generate results files

The following functionality is on my to-do list:
- Results Parsing
    - Read results files into python object
    - Analyze and plot results
- Unsteady Solution

# Usage
See the `example.py` script for an example use-case that showcases the wrapper functionality

# Disclaimer
I do not provide any guarantees that this code will work for you. I have developed and used this wrapper in my research successfully, and am sharing it in the hopes that it might help others.

# Contact
If you are using this package, I'd love to hear from you! Please drop me an email at mkapteyn@mit.edu
