---
title: 'Contributing to Learn Astropy'
slug: '/contributing/'
---

We are always interested in incorporating new tutorials into Learn Astropy and the Astropy Tutorials series. We welcome tutorials covering astro-relevant topics; they do not need to use the Astropy package in order to be hosted or indexed here. If you have astronomy tutorials that you would like to contribute, or if you have a separate tutorial series that you would like indexed by the Learn Astropy website, see below.

## Overview

Each tutorial is a [Jupyter notebook](https://jupyter.org/) file in a unique repository `tutorial--*` in the [astropy-learn organization](https://github.com/astropy-learn). For an example, let's look at the [FITS-header](https://github.com/astropy-learn/tutorial--FITS-header/tree/main/) tutorial. The repository has a few files that authors write/amend:

- A single Jupyter notebook file that contains the text and code for the tutorial,
- Any small data files used in the tutorial (in this case, a single FITS file),
- A `requirements.txt` file that specifies the required packages to run the notebook, and
- An `AUTHORS.md` file that lists the notebook authors.

The notebook file is automatically run and converted into a static HTML page ([for example](https://learn.astropy.org/tutorials/FITS-header.html)), which is then displayed in the listing on the main tutorials webpage, http://tutorials.astropy.org. Each tutorial `.ipynb` file also has an intro cell as detailed below.

## Content Guidelines

### Overview

- Each tutorial should have 3–5 explicit [Learning Goals](http://tll.mit.edu/help/intended-learning-outcomes), demonstrate ~2–3 pieces of functionality relevant to astronomy, and contain 2–3 demonstrations of generic but commonly used functionality (e.g., `numpy`, `matplotlib`).
- Each tutorial should roughly follow this progression:
  - _Input/Output_: read in some data (use [astroquery](https://astroquery.readthedocs.io/en/latest/) where possible to query real astronomical datasets)
  - _Analysis_: do something insightful / useful with the data
  - _Visualization_: make a pretty figure (use [astropy.visualization](http://docs.astropy.org/en/stable/visualization/) where possible)
- The tutorials must be compatible with the versions supported by the last major release of the Astropy core package (i.e. Python >= 3.5)

### Template intro

The first cell in every tutorial notebook is a markdown cell used for the title, author list, keywords, and summary. All of this information should be contained in a single cell and should adhere to the following format:

```
# Title name

## Authors
Jane Smith, Jose Jones

## Learning Goals
* Query the ... dataset
* Calculate ...
* Display ...

## Keywords
Example, example, example

## Companion Content
Carroll & Ostlie 10.3, Binney & Tremaine 1.5

## Summary
In this tutorial, we will download a data file, do something to it, and then
visualize it.
```

### Code

- Demonstrate good commenting practice
  - Add comments to sections of code that use concepts not included in the Learning Goals
- Demonstrate best practices of variable names
  - Variables should be all lower case with words separated by underscores
  - Variable names should be descriptive, e.g., `galaxy_mass`, `u_mag`
- Use the print function explicitly to display information about variables
- As much as possible, comply with [PEP8](https://www.python.org/dev/peps/pep-0008/).
- As much as possible, comply with Jupyter notebook style guides - [STScI style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md) and [Official Coding Style](https://jupyter.readthedocs.io/en/latest/development_guide/coding_style.html).
- Imports
  - Do not use `from package import *`; import packages, classes, and functions explicitly
  - Follow recommended package name abbreviations:
    - `import numpy as np`
    - `import matplotlib as mpl`
    - `import matplotlib.pyplot as plt`
    - `import astropy.units as u`
    - `import astropy.coordinates as coord`
    - `from astropy.io import fits`
- Display figures inline using matplotlib's inline backend:
  - `%matplotlib inline # make plots display in notebooks`

### Narrative

- Please read through the other tutorials to get a sense of the desired tone and length.
- Use [Markdown formatting](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html) in text cells for formatting, links, latex, and code snippets.
- Titles should be short yet descriptive and emphasize the learning goals of the tutorial. Try to make the title appeal to a broad audience and avoid referencing a specific instrument, catalog, or anything wavelength dependent.
- List all authors' full names (comma separated) and link to GitHub profiles and/or [ORCID iD](https://orcid.org/) when relevant.
- Include [Learning Goals](http://tll.mit.edu/help/intended-learning-outcomes) at the top as a bulleted list.
- Include Keywords as a comma separated list of topics, packages, and functions demonstrated.
- The first paragraph should give a brief overview of the entire tutorial including relevant astronomy concepts.
- Use the first-person inclusive plural ("we"). For example, "We are going to make a plot which...", or "Above, we did it the hard way, but here is the easier way..."
- Section headings should be in the imperative mood. For example, "Download the data."
- Avoid extraneous words such as "obviously", "just", "simply", or "easily." For example, avoid phrases like "we just have to do this one thing."
- Use `<div class="alert alert-info">Note</div>` for Notes and `<div class="alert alert-warning">Warning</div>` for Warnings (Markdown supports raw HTML)

## Procedure for contributing a notebook or set of notebooks

There are two methods for submitting a tutorial or set of thematically linked tutorials.

### Method 1: Provide a link

- [Open an issue on the astropy-tutorials Github repo](https://github.com/astropy/astropy-tutorials/issues) with a link to your Jupyter notebook(s).

Learn Astropy maintainers will download your notebook, test it, and edit the file if necessary to conform to the above style guide. When the tutorial is ready to be incorporated, maintainers will open a pull request on behalf of the tutorial authors.

### Method 2: Submit a pull request

This process for contributing a tutorial involves the [GitHub fork](https://help.github.com/articles/working-with-forks/) and `git` workflow concepts [branch, push, pull request](https://help.github.com/articles/proposing-changes-to-your-work-with-pull-requests/).

To contribute a new tutorial, first fork the [Astropy Learn tutorial template repository](https://github.com/astropy-learn/tutorial--template). Then clone your fork locally to your machine (replace `<GITHUB USERNAME>` with your GitHub username):

```
git clone git@github.com:<GITHUB USERNAME>/astropy-tutorials.git
```

Next, create a branch in your local repository with the name of the tutorial you'd like to contribute. Say we're adding a tutorial to demonstrate spectral line fitting -- we might call it "Spectral-Line-Fitting":

```
git checkout -b Spectral-Line-Fitting
```

Include the notebook `.ipynb` file(s) and any data files used by the notebook (see the 'Data files' section below). Update the `AUTHORS.md` file. Update the `requirements.txt` file with the Python packages the tutorial depends on and files. For example, if your tutorial requires `scipy` version 1.0 and `numpy` version 1.13 or greater, your `requirements.txt` file would look like:

```
scipy==1.0
numpy>=1.13
```

Push the notebook and other files from your local branch up to your fork of the repository on GitHub (by default, named 'origin'):

```
git push origin Spectral-Line-Fitting
```

When the tutorial is ready for submission, [open a pull request](https://help.github.com/articles/creating-a-pull-request/) against the main `tutorial-template` repository, and your submission will be reviewed.

## Data files

### For tutorial authors

If your tutorial includes large data files (where large means >~ 1 MB), including them in the tutorial's repository would drastically slow down cloning of the repository. Instead, we encourage use of the `astropy.utils.download_files` function, and will host data files on the http://data.astropy.org server by opening a PR at the https://github.com/astropy/astropy-data repository. Alternatively, if the file size is larger than 10 MB, the data should be hosted on Zenodo. To do the former, use the following procedure:

- If contributing your notebook(s) via a pull request, include the data files (e.g., `tutorials/notebooks/My-tutorial-name/mydatafile.fits`). **IMPORTANT**: when you add or modify data files, make sure the only thing in that commit involves the data files. That is, do _not_ edit your notebook and add/change data files in the same commit. This will make it easier to remove the data files when your tutorial is merged.

- To access your data files in the notebook, do something like this at the top of the notebook:

  ```
  from astropy.utils.data import download_file

  tutorialpath = ''
  mydatafilename1 = download_file(tutorialpath + 'mydatafile1.fits', cache=True)
  mydatafilename2 = download_file(tutorialpath + 'mydatafile2.dat', cache=True)
  ```

  And then use them like this:

  ```
  fits.open(mydatafilename1)
  ...
  with open(mydatafilename2) as f:
      ...
  ```

  If you do this, the only change necessary when merging your notebook will be to set `tutorialpath` to `'http://data.astropy.org/tutorials/My-tutorial-name/'`.

For data files that are larger than 10 MB in size, we recommend hosting with Zenodo. To use this approach, follow these steps:

- Sign up for an account at https://zenodo.org/ if you do not have one already.

- Log in to Zenodo and perform a new upload. Follow the Zenodo instructions and complete all the required fields in order to have the data file(s) uploaded to their records. Once this is done you will have a link to share the data.

- With the link to the data file record, which has the format `https://zenodo.org/api/records/:id`, an example HTTP GET request needed to retrieve the data using the Python package `requests` is shown below:

  ```
  import requests
  r = requests.get("https://zenodo.org/api/records/1234)
  ```

To use the output as a locally stored file, you would first need to write the file contents to a file, for example:

```
with open('./some-data-file.fits', 'wb') as f:
    f.write(r.content)
```

If you need information or help with:

- previewing how the rendered Jupyter notebooks will look on the tutorial webpage
- marking a cell with an intentional / expected error

Please see [About the Tutorials Infrastructure](infrastructure).

### For repository maintainers

If this above procedure is followed, you only need to do these three steps when merging your pull request:

1. Do `git rebase -i` and delete the commits that include the data files
2. Upload the data files to `http://data.astropy.org/tutorials/My-tutorial-name/`
3. Update the `tutorialpath` variable
