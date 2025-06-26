# Andju's Self-Hosted Obsidian Notes with MkDocs

This repository contains everything you need to set up a self-hosted website for your Obsidian notes using MkDocs.
It provides templates and configuration files to help you publish selected notes from your Obsidian vault to a beautiful, searchable website.

## Quick Start

1. Create a Github repository (if you are using GitHub for free, the repository must be public) with the files. Either
   1. Download the files into a folder (resp. clone the repository) and push them into a new repository or
   2. Fork this repository or use it as a template
2. Set up GitHub Workflows permissions in your repository ⚙️Settings
   1. Actions ➡️ General ➡️ Workflow permissions ➡️ Read and write permissions
3. Configure your `mkdocs.yml`
4. Open the folder in Obsidian
5. Add a [property](https://help.obsidian.md/properties) `publish: true` to any notes you want to publish
6. Push your changes
7. Set up GitHub Pages in your repository ⚙️Settings
   1. Actions ➡️ General ➡️ Workflow permissions ➡️ Read and write permissions
   2. Pages ➡️ Build and deployment:
      1. `Source`: Deploy from a branch
      2. `Branch`: `gh-pages` and  `/ (root)`
8. You may need to push another change to re-trigger the GitHub Pages action.

## File Overview

### 🔄 GitHub Actions Workflow / CD Pipeline

The `deploy.yml` workflow handles:
- Setting up Python and dependencies
- Filtering notes with `publish: true` property
- Excluding private folders (Journal, TODO, etc.)
- Processing Obsidian-specific features
- Deploying to GitHub Pages

### 🛠️ Formatting Scripts

- `preprocess_dataviews.py`: Converts Obsidian Dataview queries into standard markdown
- More scripts can be added for additional Obsidian feature support

## Customization

- Modify the theme in `mkdocs.yml`
- Add custom CSS/JS in the `.overrides` directory
- Adjust preprocessing scripts for your needs
- Customize the GitHub Actions workflow

## Local preview

- Create a virtual python environment in the repository folder: `python -m venv .venv`
- Activate the repository: `venv\scripts\activate`
- Install the dependencies: `pip install -r requirements.txt`
- Run the preprocess scripts (e.g. `python .scripts\collect_published_files.py`)
- Run MkDocs: `mkdocs serve`

## Recommended Obsidian settings

- Wikilinks are not fully supported - so you should disable them
- The "Default location for new attachments" should be the "Same folder as current file"

Recommended plugins:
  - [Obsidian Git Plugin](https://github.com/Vinzent03/obsidian-git): Push updates without leaving Obsidian

## Useful links

[Supported language shortcodes (for code blocks)](https://pygments.org/docs/lexers/)

[Sync with git on iOS for free using iSH](https://forum.obsidian.md/t/mobile-sync-with-git-on-ios-for-free-using-ish/20861)

## Enhancements

Compared to original template, I added the following enhancements:

- Dan uses the \#publish-me tag to mark pages to be published - which mkdocs turns into a header. Therefore I use a property. You can also add the property (together with other default elements) to a [template](https://help.obsidian.md/plugins/templates) (the folder "Templates" is already excluded in `deploy.yml`).
- Add a `.gitignore` file (based on [this example](https://publish.obsidian.md/git-doc/Tips-and-Tricks#Gitignore))
- Move the python package list to `requirements.txt` and the file collection logic to `collect_published_files.py`
- Add a script to correct link identifiers (`preprocess_link_ids.py`)
- Add the following mkdocs plugins:
  - [mkdocs-obsidian-bridge](https://pypi.org/project/mkdocs-obsidian-bridge/): In order to support Obsidian features like [Wikilinks](https://help.obsidian.md/links) or [callouts](https://help.obsidian.md/callouts)
  - [mkdocs-open-in-new-tab](https://pypi.org/project/mkdocs-open-in-new-tab/): Open external links in new tabs

## Credits

This is a fork of the repository [dan1229/tutorial-obsidian-mkdocs-self-hosted](https://github.com/dan1229/tutorial-obsidian-mkdocs-self-hosted) (based on [this blog post](https://www.danielnazarian.com/blog/posts/0d7a916e-cd8f-4931-82a5-f206ab1a938e)).
Copyright © [Daniel Nazarian](https://danielnazarian.com).

