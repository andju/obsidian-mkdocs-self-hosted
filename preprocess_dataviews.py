import re
import glob


# Process Dataview queries into Markdown tables
def process_dataview(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Example: Replace `dataview` blocks with a placeholder (customize as needed)
    content = re.sub(r"```dataview([\s\S]*?)```", "Dataview Query: \\1", content)

    with open(file_path, "w") as file:
        file.write(content)


# Find and process all Markdown files
for md_file in glob.glob("docs/**/*.md", recursive=True):
    process_dataview(md_file)
