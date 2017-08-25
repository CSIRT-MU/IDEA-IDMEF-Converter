
Converter of formats for sharing security alerts


What it is?
-----------

Python library for converting between messages about security incident 
in format IDEA and in format IDMEF.


What does it contain?
-----------------------------

All program is in directory named Converter. It contains three modules:

ExternalData

IdeaAndIdmefConverter

Tests

ExternalData and Tests contain test data and automatic tests. 

In IdeaAndIdmefConverter are two important things:

File ConverterFunctions.py - here are all functions, what you will
need, when you want to convert IDEA to IDMEF or IDMEF to IDEA.

Module InnerConverterStructure - this module contains source code
important for converter functionality. You do not need to know anything
about its content, if you do not want to debug or change something of 
converter code (if you want, see documentation).


Functions of converter
----------------------

See file ConverterFunctions.py in module IdeaAndIdmefConverter. There is
full documentation of function, which you may want to use and their
names and arguments are:

convert_file_idea_into_idmef(input_filename, output_filename, 
			     time_output_filename=None, 
			     unconverted_filename=None,
                             single_message=False, prettify=False, 
			     idmef_namespace=False)

convert_file_idmef_into_idea(input_filename, output_filename, 
                             time_output_filename=None, prettify=False)

convert_string_idea_into_idmef(input_string, idmef_namespace=False)

convert_string_idmef_into_idea(input_string)


How to run it?
--------------

Program is a library. It means you need to import this program and use
functions from ConverterFunctions.py. Before using converter in your code,
do this:

1. Install python packages (for example with command pip):
	lxml
	jsonschema
	python-dateutil
   
   Converter need these packages for conversion and it will throw an error,
   if packages are not installed.

2. Include Converter to your program by adding python commands (must be done
   before any usage of converter):
   > import sys
   > sys.path.insert(0, "/PATH/TO/Converter")
   > import IdeaAndIdmefConverter.ConverterFunctions

   /PATH/TO/Converter - Path to converter directory, which contains module 
			IdeaAndIdmefConverter (parent directory of this
			README file)

3. Now you can use converter functions, you can access it like this
   (replace ..arguments.. with specific arguments of functions according to
   documentation):
 IdeaAndIdmefConverter.ConverterFunctions.convert_file_idea_into_idmef(..arguments..)
 IdeaAndIdmefConverter.ConverterFunctions.convert_file_idmef_into_idea(..arguments..)
 IdeaAndIdmefConverter.ConverterFunctions.convert_string_idea_into_idmef(..arguments..)
 IdeaAndIdmefConverter.ConverterFunctions.convert_string_idmef_into_idea(..arguments..)

Documentation
-------------

All documentation is available at each class, method and function
 in source code.
