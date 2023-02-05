#!/bin/bash
if [[ $# -ne 1 || $1 -ne "backend" || $1 -ne "frontend" ]]; then
    echo "Script takes one arguement which must be either 'backend' or 'frontend'. Value given: '$1'"
    exit 1
fi

echo "Running docker pipeline for: $1"
echo ""

echo "Building container"
build_command="docker build $1 -f $1/$1.dockerfile -t dangg/k8app-$1-image"
echo -e "\t$build_command"
eval $build_command
echo ""

echo "Pushing container"
push_command="docker push dangg/k8app-$1-image"
echo -e "\t$push_command"
eval $push_command
echo ""
