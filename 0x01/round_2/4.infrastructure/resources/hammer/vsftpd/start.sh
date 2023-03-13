#!/bin/bash

# Start the first process
bash process1.sh &

# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?
