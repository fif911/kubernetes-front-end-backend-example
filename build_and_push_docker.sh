#!/bin/bash
if [[ $# -ne 1 || $1 -ne "backend" || $1 -ne "frontend" ]]; then
    echo "Script takes one arguement which must be either 'backend' or 'frontend'. Value given: '$1'"
    exit 1
fi

echo "Running docker pipeline for: $1"
echo ""

echo "Building container"
build_command="docker build $1 -f $1/$1.dockerfile -t k8app-$1-image:1.1"
echo -e "\t$build_command"
eval $build_command
echo ""

echo "Tagging container"
tag_command="docker tag k8app-$1-image:1.1 nader2929/sc_course:k8app-$1-image"
echo -e "\t$tag_command"
eval $tag_command
echo ""

echo "Pushing container"
push_command="docker push nader2929/sc_course:k8app-$1-image"
echo -e "\t$push_command"
eval $push_command
echo ""
