#!/bin/bash

# Get the IP address of the default interface
ip_address=$(ifconfig | grep 'inet 172' | awk '{print $2}')

# Check if the IP address is equal to a specific value
expected_ip="172.22.1.11"
if [ "$ip_address" == "$expected_ip" ]; then
  echo "The IP address of this machine is correct: $ip_address"
  ./flag
else
  echo "The IP address of this machine is incorrect: $ip_address (expected $expected_ip)"
fi