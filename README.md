# Toolchain Document Center

This repository is the document center for the documents releasing to customers.

**Please do not upload internal documents into this repository.**

## How to contribute

To contribute to this project, you don't need to be a developer of this project. Here are the steps:

 1. Fork this project. ![fork](docs/imgs/readme/fork.png)
 2. After fork, you will have a repository copy of your own. Do your modification on your own project.
 3. Submit a merge request in the main project when you finish modifying. Remember to set the assignee to Kidd or Jiyuan. ![merge](docs/imgs/readme/merge_request.png)


## Test environment setup

1. **Please setup anaconda or miniconda and the conda environment with python 3.** Otherwise, it will affect step 2 and step 3.
2. Install `mkdocs` (version 1.1.2), `pymdown-extensions` and `mkdocs-windmill` using `pip` under the environment. You may also need to check the requirement for <https://github.com/zhaoterryy/mkdocs-pdf-export-plugin>.
3. Run `mkdocs serve` to host a debug website locally. If you are not under the anaconda environment, the command `mkdocs` may not be found.
4. Use the browser to visit your local website. And you can check how your modification looks like on the website yourself.
