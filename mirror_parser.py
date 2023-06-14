import re

def parse_mirror (file_path):
    mirrors = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Ignore empty lines and comment lines
            if not line or line.startswith('#'):
                continue

            # Extract the mirror URL
            match = re.match(r'^\s*deb\s+\S+\s+(\S+)', line)
            if match:
                mirror = match.group(1)
                mirrors.append(mirror)

    return mirrors
