"""
Obsidian uses urlencoded header titles to create links
Mkdocs follows the [standard](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
when creating the ids. Therefore the header links will not match the ids.

The script converts the links of the files ins .site_content, to match the
standard.
"""

import re
from pathlib import Path
from urllib.parse import urlparse

# Define the regex pattern to capture the identifier part
IDENTIFIER_PATTERN = r'(?<!!)\[([^\]]+)\]\(([^\)]+#|#)(?!\^)([^\)]+)\)'

# Function to process and modify the matched link


def process_link(match: re.Match) -> str:
    """Convert the identifier (part after the #) of a markdown link to the
    web-standard.

    Args:
        match (re.Match): Regex match of the markdown link.

    Returns:
        str: Markdown link with converted identifier.
    """

    # Skip external links
    if urlparse(match.group(2)).scheme:
        return match.group(0)

    # Capture the identifier part
    identifier = match.group(3)
    # Modify the identifier
    modified_identifier = re.sub(r'[%20]+', '-', identifier.lower())
    # Rebuild the entire link with the modified identifier
    return f'[{match.group(1)}]({match.group(2)}{modified_identifier})'


for md_file in Path('.site_content').rglob('*.md'):
    content = md_file.read_text(encoding='utf-8')
    modified_content = re.sub(IDENTIFIER_PATTERN, process_link, content)
    if modified_content != content:
        md_file.write_text(modified_content, encoding='utf-8')
