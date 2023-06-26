#!/usr/bin/bash

# ensure the gcloud sdk is installed
if !(command -v gcloud &> /dev/null)
then
    echo "'gcloud' is not installed. Please install Google Cloud SDK."
fi

# prompt the user for a variable
echo -n "Please set a version tag, ie:'alpha-v1.0.0' > "
read release_tag

# ensure authentication to the remote registry
account=$(gcloud config get-value account)

# If not authenticated, run the login command
if [ "$account" = "(unset)" ]; then
    gcloud auth login
else
    echo "Already authenticated as $account."
fi

gcloud config set project hackabit-sand-playhouse
gcloud auth configure-docker us-central1-docker.pkg.dev

# build the worker from the Dockerfile
docker build . -t coin-worker

# tag the worker for remote push
docker tag coin-worker:latest us-central1-docker.pkg.dev/hackabit-sand-playhouse/coin/coin-worker:$release_tag

# push the content to artifacts registry
docker push us-central1-docker.pkg.dev/hackabit-sand-playhouse/coin/coin-worker:$release_tag
