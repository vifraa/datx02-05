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

rm -r "$outputPath"
cp -r "$inputPath" "$outputPath"

