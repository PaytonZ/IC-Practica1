#!/bin/bash

if [ "$#" == "2" ]; then

	echo "COMPILING GUI $1 to $2"

	ui=`echo $1 | grep .ui`

	if [ "$ui" != "" ]; then

		py=`echo $2 | grep .py`

		if [ "py" != "" ]; then

			pyside-uic "$1" -o "$2"
		fi
	else
		echo "Parameter order incorrect..."
		echo "first parameter must be a .ui file and second must be a .py file"
	fi
else
	echo "Parameter number error..."
	echo "Usage: compileGUI.sh inputfile.ui outputfile.py"
fi