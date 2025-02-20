# Tutorial: Self-Hosted Obsidian Notes with MkDocs
#### By: [Daniel Nazarian](https://www.danielnazarian.com) 🐧👹
##### Contact me at <dnaz@danielnazarian.com>

-------------------------------------------------------

## Description

This repository contains everything you need to set up a self-hosted website for your Obsidian notes using MkDocs. It provides templates and configuration files to help you publish selected notes from your Obsidian vault to a beautiful, searchable website.

## Quick Start

1. Copy these files into your Obsidian vault
2. Add `#publish-me` to any notes you want to publish
3. Configure your `mkdocs.yml` (use either basic or advanced template)
4. Set up GitHub Pages in your repository settings
5. Push your changes - GitHub Actions will handle the rest!

## File Overview

### 📄 mkdocs.yml Templates

Two configuration templates are provided:

- `mkdocs.yml.basic`: A minimal configuration to get started quickly
- `mkdocs.yml.adv`: A feature-rich configuration with:
  - Material theme customization
  - Dark/light mode support
  - Advanced markdown extensions
  - Search functionality
  - Custom navigation
  - And more!

### 🔄 GitHub Actions Workflow / CD Pipeline

The `deploy.yml` workflow handles:
- Setting up Python and dependencies
- Filtering notes with `#publish-me` tag
- Excluding private folders (Journal, TODO, etc.)
- Processing Obsidian-specific features
- Deploying to GitHub Pages

### 🛠️ Formatting Scripts

- `preprocess_dataviews.py`: Converts Obsidian Dataview queries into standard markdown
- More scripts can be added for additional Obsidian feature support


## Setup Instructions

See my blog post [here](https://www.danielnazarian.com/blog/posts/) to get started.


## Customization

- Modify the theme in `mkdocs.yml`
- Add custom CSS/JS in the `.overrides` directory
- Adjust preprocessing scripts for your needs
- Customize the GitHub Actions workflow

-------------------------------------------------------

##### Copyright © [Daniel Nazarian](https://danielnazarian.com)
