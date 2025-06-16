"""Install the built tutorials HTML from astropy-learn/astropy-tutorials into the
built Gatsby site.
"""

from __future__ import annotations

import argparse
import os
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Optional
from zipfile import ZipFile

import requests
from uritemplate import expand


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            'Install the tutorials HTML artifact from '
            'astropy-learn/astropy-tutorials into the build Gatsby site.\n\n'
            'There are two usage modes:\n\n'
            '1. If --tutorials-run is set, get the tutorials from the '
            'corresponding workflow artifact.\n'
            '2. If --tutorials-run is not set, the workflow artifact from '
            'the most recent merge to the main branch is used.\n\n'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--dest',
        required=True,
        help="Directory where the tutorials are installed. This should be "
             "inside the Gatsby 'public' directory."
    )
    parser.add_argument(
        '--tutorials-repo',
        default="astropy-learn/astropy-tutorials",
        help='Tutorials repo slug (should be astropy-learn/astropy-tutorials).'
    )
    parser.add_argument(
        '--tutorials-artifact',
        default="rendered-tutorials",
        help='Name of the artifact from the tutorials repo.'
    )
    parser.add_argument(
        '--tutorials-run',
        help='ID of the workflow run from the tutorials repo.'
    )
    return parser.parse_args()


def main() -> None:
    """The main script entrypoint."""
    args = parse_args()

    github_token = os.getenv("GITHUB_TOKEN")
    if github_token is None:
        raise RuntimeError("Set the GITHUB_TOKEN environment variable")

    if args.tutorials_run is not None:
        artifact = TutorialsArtifact(
            repo=args.tutorials_repo,
            name=args.tutorials_artifact,
            run_id=args.tutorials_run,
            github_token=github_token
        )
    else:
        artifact = TutorialsArtifact.from_latest(
            repo=args.tutorials_repo,
            name=args.tutorials_artifact,
            github_token=github_token
        )

    artifact.install(args.dest)


class TutorialsArtifact:
    """A tutorials build artifact that can be downloaded and installed into
    the site's build directory.

    Parameters
    ----------
    repo : str
        The repository slug (astropy-learn/astropy-tutorials).
    name : str
        The name of the workflow artifact with rendered tutorials.
    run_id : str
        The workflow run ID corresponding to the workflow artifact.
    github_token : str
        A GitHub token.
    """

    def __init__(
        self,
        *,
        repo: str,
        name: str,
        run_id: str,
        github_token: str
    ) -> None:
        self.repo = repo
        self.name = name
        self.run_id = run_id
        self.github_token = github_token
        self._zip_path: Optional[Path] = None

    @classmethod
    def from_latest(
        cls,
        *,
        repo: str,
        name: str,
        github_token: str
    ) -> TutorialsArtifact:
        """Get the artifact from the latest run on the main branch.

        Parameters
        ----------
        repo : str
            The repository slug (astropy-learn/astropy-tutorials).
        name : str
            The name of the workflow artifact with rendered tutorials.
        run_id : str
            The workflow run ID corresponding to the workflow artifact.
        github_token : str
            A GitHub token.
        """
        owner, repo_name = repo.split('/')
        url = expand(
            "https://api.github.com/repos/{owner}/{repo}/actions/runs",
            owner=owner,
            repo=repo_name
        )
        headers = cls._make_github_headers(github_token)
        response = requests.get(
            url,
            headers=headers,
            params={"branch": "main", "event": "push", "status": "success"}
        )
        response.raise_for_status()
        runs_data = response.json()
        first_run = runs_data["workflow_runs"][0]
        run_id = first_run["id"]
        return cls(
            repo=repo,
            name=name,
            run_id=run_id,
            github_token=github_token
        )

    @staticmethod
    def _make_github_headers(github_token) -> Dict[str, str]:
        return {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {github_token}"
        }

    def _download_artifact(self) -> bytes:
        # Note that if there's a large number of artifacts (>30), we need
        # to iterate over all pages of the request. Generally this shouldn't
        # be necessary.
        artifacts_data = self._get_workflow_run_artifacts()
        for artifact in artifacts_data["artifacts"]:
            if artifact["name"] == self.name:
                download_url = artifact["archive_download_url"]
                response = requests.get(
                    download_url,
                    headers={"Authorization": f"Bearer {self.github_token}"}
                )
                return response.content
        raise RuntimeError("Did not find artifact for download")

    def _get_workflow_run_artifacts(self, page=1) -> Dict[str, Any]:
        owner, repo = self.repo.split('/')
        uri = expand(
            "https://api.github.com/repos/{owner}/{repo}/actions/runs/"
            "{run_id}/artifacts",
            owner=owner,
            repo=repo,
            run_id=self.run_id,
        )
        headers = TutorialsArtifact._make_github_headers(self.github_token)
        response = requests.get(
            uri,
            params={"page": str(page)},
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def install(self, destination_directory: str) -> None:
        """Download and install the artifact contents into the desination
        directory, which is created if it does not already exist.
        """
        artifact_archive = self._download_artifact()
        bytes_stream = BytesIO(artifact_archive)
        zip_file = ZipFile(bytes_stream)
        zip_file.extractall(path=Path(destination_directory))


if __name__ == '__main__':
    main()
