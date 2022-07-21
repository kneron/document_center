# Toolchain Document Center

[![Build Status](https://github.com/kneron/document_center/actions/workflows/python-app.yml/badge.svg)](https://github.com/kneron/document_center/actions/workflows/python-app.yml)

This repository is the document center for the documents releasing to customers.

**This repository is moved to Github: <https://github.com/kneron/document_center>.**

## How to add a new page.

1. Create a `.md` markdown file under `docs/` or its subfolder. Edit the content.
2. Add it under `nav` in `mkdocs.yml` so that users can access it from the left-side menu.
3. Run a testing server to check if it looks good.
4. Commit your change.

## How to migrate from gitlab

First, you need to set up your Github account.
Then, you just need to run the following command to reset the remote:

```bash
git remote set-url origin git@github.com:kneron/document_center.git
```

After that, we recommend you switch to master branch and use `git pull` to update the local master branch before your start your work.

## Test environment setup

1. **Please setup anaconda or miniconda and the conda environment with python 3.** Otherwise, it will affect step 2 and step 3.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run `mkdocs serve` to host a debug website locally. If you are not under the anaconda environment, the command `mkdocs` may not be found.
4. Use the browser to visit your local website. And you can check how your modification looks like on the website yourself.
