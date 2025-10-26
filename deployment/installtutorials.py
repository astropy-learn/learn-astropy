"""Install the built tutorials HTML from astropy-learn/astropy-tutorials into the
built Gatsby site.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import tempfile
from subprocess import CalledProcessError, check_call
import glob
import shutil
import requests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Install the tutorials HTML files from "
            "each tutorial repo into the build Gatsby site."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dest",
        required=True,
        help="Directory where the tutorials are installed. This should be "
        "inside the Gatsby 'public' directory.",
    )

    return parser.parse_args()


def process_repo(repo, destination_directory):
    """Process a tutorial repository to copy its rendered tutorial(s) into `destination_directory`."""
    os.makedirs(destination_directory, exist_ok=True)

    repo_name = repo["full_name"]
    if not repo_name.split("/")[1].startswith("tutorial--"):
        return
    if repo_name.split("/")[1] == "tutorial--template":
        return

    print(f"\nProcessing {repo_name}")

    with tempfile.TemporaryDirectory() as tmp:
        branch_name = "converted"
        try:
            check_call(
                f"git clone --depth 1  --branch {branch_name} https://github.com/{repo_name}.git {tmp}".split()
            )
        except CalledProcessError:
            print(f"Failed to clone {repo_name}")
            return

        repo = Path(tmp)
        # os.system(f'tree {repo}')
        tutorials = glob.glob(f"{repo}/_sources/*.ipynb")
        for t in tutorials:
            tname = os.path.splitext(os.path.basename(t))[0]
            print(f"Copying tutorial {tname}")
            shutil.copy(t, destination_directory)
            shutil.copy(
                f"{repo}/{tname}.html",
                destination_directory,
            )
        # if len(tutorials) > 1:
        #     index_files = glob.glob(f"{repo}/index-*.html")
        #     if index_files:
        #         index = index_files[0]
        #         print(f"More than 1 tutorial found; also copying index file {index}")
        #         shutil.copy(index, destination_directory)
        #     else:
        #         raise FileNotFoundError(f"No index-*.html file found for {repo_name}.")

        # copy files for in-notebook search bar
        # shutil.copy(
        #     f"{repo}/search.html",
        #     destination_directory,
        # )
        # shutil.copy(
        #     f"{repo}/searchindex.js",
        #     destination_directory,
        # )

        # copy _static files (CSS, JS) for page rendering
        shutil.copytree(
            f"{repo}/_static",
            f"{destination_directory}/_static",
            dirs_exist_ok=True,
        )

        # copy images (plots) in notebook for faster page loading
        images = glob.glob(f"{repo}/_images/*.png")
        if len(images) > 0:
            print("Copying notebook cell output images")
            image_dir = f"{destination_directory}/_images"
            os.makedirs(image_dir, exist_ok=True)
            for i in images:
                shutil.copy(i, image_dir)
        else:
            print("No notebook cell output images found to copy")


if __name__ == "__main__":
    args = parse_args()
    dest_dir = args.dest
    url = "https://api.github.com/orgs/astropy-learn/repos"
    with requests.Session() as s:
        while True:
            response = s.get(url)
            response.raise_for_status()
            data = response.json()
            list(map(process_repo, data, [dest_dir] * len(data)))
            url = response.links.get("next", {}).get("url")
            if not url:
                break
