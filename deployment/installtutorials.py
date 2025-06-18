"""Install the built tutorials HTML from astropy-learn/astropy-tutorials into the
built Gatsby site.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import tempfile
from subprocess import CalledProcessError, check_call
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
    """Process a tutorial repository to copy its rendered tutorial(s) into the `dest_dir` directory."""
    repo_name = repo["full_name"]
    destination_directory = Path(destination_directory)
    print(f"destination_directory: {destination_directory}")
    if not repo_name.split("/")[1].startswith("tutorial--"):
        return
    if repo_name.split("/")[1] == "tutorial--template":
        return

    print(f"\nProcessing {repo_name}")

    with tempfile.TemporaryDirectory() as tmp:
        print(f"pwd: {os.getcwd()}")
        branch_name = "converted"
        try:
            check_call(
                f"git clone --depth 1  --branch {branch_name} https://github.com/{repo_name}.git {tmp}".split()
            )
        except CalledProcessError:
            print(f"Failed to clone {repo_name}")
            return

        repo = Path(tmp)
        print(f"pwd: {os.getcwd()}")
        print(f"repo: {repo}")
        # tutorial filename should match repo name
        tutorial = repo_name.split("/")[1].replace("tutorial--", "")
        try:
            shutil.copy(f"{repo}/{tutorial}.html", dest_dir)
            print(f"Found tutorial {tutorial}.html")
        except FileNotFoundError:
            # this must be a book.
            # filenames of tutorials (chapters in the book) should be of the format 1_Name.html
            # (see https://github.com/astropy-learn/dev-guide/blob/main/README.md)
            chapters = [
                f
                for f in os.listdir(repo)
                if f[0].isdigit() and "_" in f[:3] and f.endswith(".html")
            ]
            print(f"Found chapters {chapters}")
            for t in chapters:
                shutil.copy(f"{repo}/{t}", dest_dir)
            # also include the book index (first page)
            shutil.copy(f"{repo}/index.html", dest_dir)


if __name__ == "__main__":
    args = parse_args()
    dest_dir = args.dest
    url = "https://api.github.com/orgs/astropy-learn/repos"
    with requests.Session() as s:
        while True:
            response = s.get(url)
            response.raise_for_status()
            data = response.json()
            list(map(process_repo, data, dest_dir))
            url = response.links.get("next", {}).get("url")
            if not url:
                break
