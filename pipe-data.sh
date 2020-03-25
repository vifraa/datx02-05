#!/bin/bash

helpFunction() {
    echo ""
    echo "Usage: $0 -i inputPath -o outputPath"
    echo -e "\t-i The path to the folder of the data that wants to be moved"
    echo -e "\t-o The path to the folder of the data that wants to be moved to"
    exit 1
}

while getopts "i:o:" opt 
do
    case "$opt" in
        i ) inputPath="$OPTARG" ;;
        o ) outputPath="$OPTARG" ;;
        ? ) helpFunction ;;
    esac
done

if [ -z "$inputPath" ] || [ -z "$outputPath" ] 
then
    echo "Some of the parameters are empty!"
    helpFunction
fi

if ! [ -d "$inputPath" ]; then
    # Input path exists
    echo "Input path: " "$inputPath"  " does not exists"
    helpFunction
fi

# Only remove output path if it alreadt exists.
if [ -d "$outputPath" ]; then
    rm -r "$outputPath"
fi
    
cp -r "$inputPath" "$outputPath"


