#!/usr/bin/python3
import argparse
import requests
import random
import string

# python script_name.py input_csv.csv output_file.txt --password_length 12

def parse_input():
    parser = argparse.ArgumentParser(description='Process a list of users from a CSV file and generate passwords.')

    # Host
    parser.add_argument('host', type=str, help='Length of the generated passwords (default: 8).')

    # CSV file input
    parser.add_argument('input_csv', type=str, help='Path to the input CSV file containing users.')

    # Output file specification
    parser.add_argument('output_file', type=str, help='Path to the output file where generated passwords will be saved.')

    # Session token
    parser.add_argument('session_token', type=str, help='Token to authenticate to CTFd with.')

    # CSRF token
    parser.add_argument('csrf_token', type=str, help='Token to pass CSRF with.')

    # Password length flag
    parser.add_argument('-l', '--password_length', type=int, default=8, help='Length of the generated passwords (default: 8).')

    return parser.parse_args()


def process_csv(input_csv, password_length_str):
    # gather all users
    users = []
    with open(input_csv, 'r') as fio:
        return [ {'user': l.strip().split(',')[0],
                 'email': l.strip().split(',')[1],
                 'password': ''.join(random.choices(string.ascii_lowercase, k=int(password_length_str)))
                 }  for l in fio ]


def make_user_request(user, host, session_token, csrf_token, proxy=False):
    if proxy:
        proxies = {
            'https': 'http://127.0.0.1:8080'
            }
        verify = False
    else:
        proxies = None
        verify = True

    response = requests.post(f'https://{host}/api/v1/users',
                                json={
                                    'name': user['user'],
                                    'email': user['email'],
                                    'password': user['password'],
                                    'type': 'user',
                                    'verified': 'true'
                                },
                                headers={
                                    'Csrf-Token': csrf_token,
                                },
                                cookies={
                                    'session': session_token,
                                },
                                proxies=proxies,
                                verify=verify
                            )
    
    print(user, host, session_token, csrf_token)
    
    return response.status_code


def write_outfile(filename, users):
    with open(filename, 'w') as fio:
        for user in users:
            fio.write(f'{user["email"]},{user["password"]}\n')


def main():
    args = parse_input()

    # Process the input CSV file
    users = process_csv(args.input_csv, args.password_length)

    # Itterate over the received users and show what will be comitted to the server
    print(users)

    # Write outfile
    write_outfile(args.output_file, users)
    
    # ensure confirmation before continuing
    try:
        print('\nAre you sure you\'d like to continue? [enter]')
        input()
    except KeyboardInterrupt: exit()

    # Make requests
    for user in users:
        status = make_user_request(user, args.host, args.session_token, args.csrf_token)
        print(f'{status} {user["user"]} {user["password"]}')

if __name__ == '__main__':  main()
