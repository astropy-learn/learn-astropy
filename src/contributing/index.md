---
title: 'Contributing to Learn Astropy'
slug: '/contributing/'
---

We are always interested in incorporating new tutorials into Learn Astropy and the Astropy Tutorials series. We welcome tutorials covering astro-relevant topics; they do not need to use the Astropy package in order to be hosted or indexed here. If you have astronomy tutorials that you would like to contribute, or if you have a separate tutorial series that you would like indexed by the Learn Astropy website, see below.

## Content Guidelines

### Overview

- Each tutorial should have 3–5 explicit [Learning Goals](http://tll.mit.edu/help/intended-learning-outcomes), demonstrate ~2–3 pieces of functionality relevant to astronomy, and contain 2–3 demonstrations of generic but commonly used functionality (e.g., `numpy`, `matplotlib`).
- Each tutorial should roughly follow this progression:
  - _Input/Output_: read in some data (use [astroquery](https://astroquery.readthedocs.io/en/latest/) where possible to query real astronomical datasets)
  - _Analysis_: do something insightful / useful with the data
  - _Visualization_: make a pretty figure (use [astropy.visualization](http://docs.astropy.org/en/stable/visualization/) where possible)
- The tutorials must be compatible with the versions supported by the latest major release of the Astropy core package

### Introduction cell template

The first cell in every tutorial notebook is a markdown cell used for the title, author list, keywords, and summary. All of this information should be contained in a single cell and should adhere to the following format:

```
# Title name

## Authors
Jane Smith (@GITHUB-ID, ORCID-ID), Jose Jones (@GITHUB-ID, ORCID-ID)

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

Please draw keywords from [this list](https://github.com/astropy-learn/astropy-tutorials/blob/main/resources/keywords.md).

### Code

- Demonstrate good commenting practice
  - Add comments to sections of code that use concepts not included in the Learning Goals
- Demonstrate best practices of variable names
  - Variables should be all lower case with words separated by underscores
  - Variable names should be descriptive, e.g., `galaxy_mass`, `u_mag`
- Use the print function explicitly to display information about variables
- As much as possible, comply with [PEP8](https://www.python.org/dev/peps/pep-0008/).
- As much as possible, comply with Jupyter notebook style guides - [STScI style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md) and [Official Coding Style](https://docs.jupyter.org/en/stable/contributing/ipython-dev-guide/coding_style.html).
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

To contribute tutorial content, open an issue in the [astropy-tutorials repository](https://github.com/astropy-learn/astropy-tutorials/issues). When you click 'New issue', select the 'Tutorial submission' option, completing all fields of that form. You have the option to have your tutorial made citable via an upload (by the Astropy Learn maintainers) to Zenodo. If you have any data files needed by the notebook to run, see the 'Data files' section below.

Maintainers will review your notebook and may ask questions and/or suggest edits (e.g., to conform to the above content guidelines). When the review is complete and the tutorial is ready to be incorporated, maintainers will create a new repository for the tutorial, add the notebook(s), and upload your tutorial(s) to the [learn website](https://learn.astropy.org/tutorials/).

### Data files

If your tutorial includes large data files (where large means >~ 1 MB), including them in the tutorial's repository would drastically slow down cloning of the repository. Instead, for files < 10 MB, we encourage use of the `astropy.utils.download_files` function, and we will host data files on the http://data.astropy.org server (or you can do this directly by opening a PR at the https://github.com/astropy/astropy-data repository). Alternatively, if the file size is > 10 MB, the data should be hosted on Zenodo. To do the former, use the following procedure:

- Assuming you have a data file named `mydatafile.fits`, you can access the file in the notebook with something like this at the top of the notebook:

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

  If you do this, the only change necessary in your submission of the notebook to [astropy-tutorials](https://github.com/astropy-learn/astropy-tutorials/issues) will be to set `tutorialpath` to `'http://data.astropy.org/tutorials/My-tutorial-name/'`.

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
