#!/bin/bash

encryptTree()
{
	echo "Current directory: " $1
	for item in $1*
	do
		# Handle sub directories by using recursion
		if [ -d "$item" ]; then
			echo "Moving to $item"
			encryptTree $item/
		fi

		# Handle each file and encrypt it
		if test -f "$item"; then
			echo "Encrypting $item"
			aescrypt -e -p purple $item
		fi
	done
}

decryptTree()
{
	echo "Current directory: " $1
	for item in $1*
	do
		# Handle sub directories by using recursion
		if [ -d "$item" ]; then
			echo "Moving to $item"
			decryptTree $item/
		fi

		# Handle each file and encrypt it
		if test -f "$item"; then
			echo "Encrypting $item"
			aescrypt -d -p purple $item
		fi
	done
}

# $1 is the option to encrypt (-e) or decrypt (-d)
# $2 is the source 
# $3 is the destination

if [$3 = ""]

	if [$1 = "-e"]
		encryptTree $2
	fi
	if [$1 = "-d"]
		decryptTree $2
	fi
fi

if [$3 != ""]

	cp -rf $2 $3

	if [$1 = "-e"]
		encryptTree $2
	fi
	if [$1 = "-d"]
		decryptTree $2
	fi
fi