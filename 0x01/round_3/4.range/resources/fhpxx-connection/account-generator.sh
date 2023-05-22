#!/bin/bash

sudo apt install pwgen -y

# Create an array to hold the generated keys and passwords
declare -A keys
declare -A passwords

# Function to generate a random string of lowercase letters
generate_random_string() {
    cat /dev/urandom | tr -dc 'a-z' | fold -w 5 | head -n 1
}

# Create 5 users
for i in {1..3}
do
    username=$(generate_random_string)
    password=$(pwgen -s -1 20)
    
    # Create the user and set their password
    sudo useradd -m "$username"
    echo "$username:$password" | sudo chpasswd

    # Create .ssh directory for the user
    sudo mkdir "/home/$username/.ssh"
    sudo chown "$username":"$username" "/home/$username/.ssh"
    sudo chmod 700 "/home/$username/.ssh"

    # Generate a key pair
    sudo ssh-keygen -t rsa -b 4096 -f "/home/$username/.ssh/id_rsa" -N "" -q
    sudo chown "$username":"$username" "/home/$username/.ssh/id_rsa"
    sudo chown "$username":"$username" "/home/$username/.ssh/id_rsa.pub"
    
    # Allow SSH access with the key
    sudo mv "/home/$username/.ssh/id_rsa.pub" "/home/$username/.ssh/authorized_keys"
    sudo chown "$username":"$username" "/home/$username/.ssh/authorized_keys"
    sudo chmod 600 "/home/$username/.ssh/authorized_keys"

    # Store the private key and password to the arrays
    private_key=$(sudo cat "/home/$username/.ssh/id_rsa" | tr -d '\n')
    keys["$username"]="$private_key"
    passwords["$username"]="$password"

    # Notify the executing user about the account creation
    echo "Created new user, $username"
done

# Export the usernames, passwords and keys to a CSV file
echo "username,password,private_key" > keys.csv
for username in "${!keys[@]}"
do
    # Escape double quotes in the private key
    private_key=${keys["$username"]//\"/\"\"}
    password=${passwords["$username"]}

    # Output the username, password and key to the CSV file
    echo "\"$username\",\"$password\",\"$private_key\"" >> keys.csv
done
