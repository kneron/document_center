# Toolchain Document Center

Build Status: [![Python application](https://github.com/kneron/document_center/actions/workflows/python-app.yml/badge.svg)](https://github.com/kneron/document_center/actions/workflows/python-app.yml)

This repository is the document center for the documents releasing to customers.

**This repository is moved to Github: <https://github.com/kneron/document_center>.**

## How to migrate

First, you need to set up your Github account.
The, you just need to run the following command to reset the remote:

```bash
git remote set-url origin git@github.com:kneron/document_center.git
```

## Test environment setup

1. **Please setup anaconda or miniconda and the conda environment with python 3.** Otherwise, it will affect step 2 and step 3.
2. Install `mkdocs` (version 1.1.2), `pymdown-extensions` and `mkdocs-windmill` using `pip` under the environment. You may also need to check the requirement for <https://github.com/zhaoterryy/mkdocs-pdf-export-plugin>.
3. Run `mkdocs serve` to host a debug website locally. If you are not under the anaconda environment, the command `mkdocs` may not be found.
4. Use the browser to visit your local website. And you can check how your modification looks like on the website yourself.
