"""
Copy files containing published property (excluding excluded folders),
index.md, and .overrides to the temporary directory .site_content.
"""

import re
import shutil
from pathlib import Path

# Create the output directory
output_dir = Path('.site_content')
output_dir.mkdir(parents=True, exist_ok=True)

# Define excluded folders
EXCLUSION = {'Journal', 'TODO', 'Feelings', 'Private', 'Templates'}

# Regular expression to match the published:true in YAML front matter
published_pattern = re.compile(
    r'^---\s*\n(?:.*\n)*?published:\s*true\s*(?:.*\n)*?---',
    re.MULTILINE
)

files_to_copy = []

# Find published markdown files
for path in Path('.').rglob('*.md'):
    # Skip files in excluded folders or folders starting with a "."
    if (any(folder in path.parts for folder in EXCLUSION)
            or any(part.startswith('.') for part in path.parts)):
        print(f'Skipping excluded file: {path}')
        continue

    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f'Error reading file {path}: {e}')

    if published_pattern.search(content):
        files_to_copy.append(path)

# Copy published markdown files
for path in files_to_copy:
    destination = Path(output_dir, path)
    # Recreate folder structure in .site_content
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(path, destination)
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f'Error copying file {path}: {e}')

# Try copying index.md
try:
    shutil.copy2('index.md', Path(output_dir, 'index.md'))
except FileNotFoundError:
    pass

# Copy .overrides directory if it exists
if Path('.overrides').is_dir():
    shutil.copytree('.overrides',
                    Path(output_dir, '.overrides'),
                    dirs_exist_ok=True)

print('Files containing published property (excluding excluded folders), '
      'index.md, and .overrides have been copied to .site_content')
