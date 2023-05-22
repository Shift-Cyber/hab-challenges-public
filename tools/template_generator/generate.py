"""
Simple python script to generate README and challenge directories/templates.

USAGE: /generate.py <config-file> <target-dir>

You must have an equal number of challenges per category and point values are the same per row.
"""

import os
import sys
import yaml
import string
import random

from yes_no import query_yes_no

# ensure proper input
if len(sys.argv) != 3:
    print("./generate.py config.yaml ./0x01/round_3/")
    sys.exit(-1)

def challenge_file_content(challenge_name, challenge_value, year, category_single_digit_id, challenge_code, category_description, challenge_resource_directory):
    return \
f"""# {challenge_name} - {challenge_value}pts
### {year}-{category_single_digit_id}-{challenge_code}
Author: First Last (Handle)<br>
Challenge Resources: [{challenge_resource_directory}]({challenge_resource_directory})

{category_description}

## Teaching Points
1. What is a CTF challenge?

## Challenge Prompt
This is the stuff that goes on CTFd.

## Solution Guide
1. Submit the flag.

## Reference Material
### What is a CTF challenge?
Capture the Flag (CTF) is a special kind of information security competitions. There are three common types of CTFs: Jeopardy, Attack-Defence and mixed. Jeopardy-style CTFs has a couple of questions (tasks) in range of categories. For example, Web, Forensic, Crypto, Binary or something else.

### Why do we do CTFs?
...
"""

def generate_readme(readme_challenges):
    categories = [key for key in readme_challenges.keys()]
    max_len = max([len(category) for category in categories])

    # this really dirty format string extracts the point values
    points_per_row = [[ readme_challenges[category][challenge][0] for challenge in readme_challenges[category] ] for category in categories ][0]
    challenges_per_col = [[readme_challenges[category][challenge] for challenge in readme_challenges[category].keys()] for category in categories]

    # this even dirtier format string gives us our text per row
    def generate_challenge_string(unique_identifier, name, relative_file_path):
        return f'[{unique_identifier},<br>{name}]({relative_file_path})'
    
    challenge_rows = []
    for row_index in range(len(points_per_row)):
        challenge_rows.append([generate_challenge_string(col[row_index][1], col[row_index][2], col[row_index][3]) for col in challenges_per_col])

    for row in challenge_rows:
        for challenge in row:
            if len(challenge) > max_len: max_len = len(challenge)

    def generate_readme_row(max_len, point_value, challenges):
        return f"| {'{:>3}'.format(point_value)} | {''.join([f'{challenge:<{max_len}} | ' for challenge in challenges])}\n"
    
    return\
f"""# Hack a Bit x - Round x (X)

## Challenge Navigation
| Pts | {''.join([f'{category:<{max_len}} | ' for category in categories])}
| --- | {''.join([f'{"":-<{max_len}} | ' for category in categories])}
{''.join([generate_readme_row(max_len, pts, challenge_rows[n]) for n,pts in enumerate(points_per_row)])}

## Categories
### X
x

## Contributors
### Nate Singer (Helix)
https://www.linkedin.com/in/nathanielmsinger/ | https://github.com/natesinger

Nate is a leader in the youth cyber security space. After struggling to find good resources back in highschool he managed to figure out how to break into the industry and now spends signficant energy trying to improve the lives of young people and create more opportunity. Hack a Bit is just one of many ways he has been working to move the ball forward in the industry.

### First Last (Handle)

## Writeups
writing...
- x: link

"""

# create dict to save challenge results to for readme
"""readme_challenges = {
    category_name: {
        challenges: {
            challenge_1: pts
        }
    }
}"""
readme_challenges = {}

# save inputs as named vars
configuration_file_path = sys.argv[1]
target_directory_path = sys.argv[2]

with open(configuration_file_path,'r') as fio_config_file:
    configuration = yaml.safe_load(fio_config_file)

    for category in configuration['categories']:
        category_key = category
        category_description = configuration['categories'][category_key]['description']
        category_challenges_dict = configuration['categories'][category_key]['challenges']

        print(f"{category_key}:\r\n\tDescription: {category_description}\r\n\tChallenges: {category_challenges_dict}\n")

    if not query_yes_no("Continue?"): sys.exit(0)
    else:
        for id,category in enumerate(configuration['categories']):
            # save for radme
            if category != 'Welcome': readme_challenges[category] = {}

            category_description = configuration['categories'][category]['description']
            category_single_digit_id = configuration['categories'][category]['single_digit_id']
            category_challenges_dict = configuration['categories'][category]['challenges']

            category_dir = f"{target_directory_path}/{id}.{category.lower()}/"
            # create the root category directory
            if not os.path.exists(f"{category_dir}/resources"):
                os.makedirs(f"{target_directory_path}/{id}.{category.lower()}/resources")

            

            # create the challenge markdown files
            for challenge in category_challenges_dict:
                year_code = configuration['configuration']['year']
                challenge_code = ''.join(
                    random.choices(string.ascii_uppercase,
                    k=int(configuration['configuration']['unique_code_length'])))

                # create resource directory for speicfic hcallenge
                if not os.path.exists(f"{category_dir}/resources/{challenge_code.lower()}-{challenge.lower()}"):
                    os.makedirs(f"{category_dir}/resources/{challenge_code.lower()}-{challenge.lower()}")

                # ensure there is a file in the resources dir so it acutally pushes
                with open(f"{category_dir}/resources/{challenge_code.lower()}-{challenge.lower()}/.gitignore", 'wt') as fio_gitignore: pass


                ### CREATE CHALLENGE FILE ###
                challenge_file_name = f"{year_code}-{category_single_digit_id}-{challenge_code}-{challenge.lower()}.md"

                with open(f"{category_dir}{challenge_file_name}", 'wt') as fio_challenge_file:
                    fio_challenge_file.write(challenge_file_content(
                        challenge_name = challenge,
                        challenge_value = configuration['categories'][category]['challenges'][challenge],
                        year = year_code,
                        category_single_digit_id = category_single_digit_id,
                        challenge_code = challenge_code,
                        category_description = category_description,
                        challenge_resource_directory = f"./resources/{challenge_code.lower()}-{challenge.lower()}/"
                    ))

                # save for readme
                if category != 'Welcome':
                    unique_code = challenge_code
                    name = challenge
                    points = configuration['categories'][category]['challenges'][challenge]
                    relative_file_path = f"./{id}.{category.lower()}/{year_code}-{category_single_digit_id}-{challenge_code}.md"

                    readme_challenges[category][challenge] = [points, unique_code, name, relative_file_path]


with open(f"{target_directory_path}/README.md", 'wt') as fio_readme:
    fio_readme.write(generate_readme(readme_challenges))
