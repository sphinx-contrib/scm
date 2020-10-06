from __future__ import annotations

from pathlib import Path
from typing import Any

import git
import sphinx.util
from docutils.parsers.rst import directives

logger = sphinx.util.logging.getLogger(__name__)


class Helper:
    def get_contibutors(self) -> list[str]:
        """Return list of Git contributors for given path using `git shortlog`

        :path: Path of which to get contributors
        :flags: Additional flags passed to `git shortlog`
        """
        docpath = self.get_source_info()[0]
        docdir = Path(docpath).resolve().parent
        min_commits = self.optn_over_conf("min_commits", "scm_contribs_min_commits")

        limit_authors = self.optn_over_conf(
            "limit_authors", "scm_contribs_limit_authors"
        )
        if limit_authors is not None and limit_authors < 1:
            logger.warning(
                "List of contributors limited to less than one entry. "
                "Check '(scm_contribs_)limit_authors' option/config value"
            )

        flags = []

        contribs_email = directives.choice(
            self.optn_over_conf("email", "scm_contribs_email"),
            ("true", "false"),
        )
        flags += ["-e"] if contribs_email == "true" else []

        contribs_sort = directives.choice(
            self.optn_over_conf("sort", "scm_contribs_sort"),
            ("name", "num"),
        )
        flags += ["-n"] if contribs_sort == "num" else []

        contribs_type = directives.choice(
            self.optn_over_conf("type", "scm_contribs_type"),
            ("author", "committer"),
        )
        flags += ["-c"] if contribs_type == "committer" else []

        git_options = ["-s", *flags, "--", docpath]

        contributors = []
        for item in git.Git(docdir).shortlog(*git_options).split("\n"):
            if not item:
                continue
            num, contributor = item.split("\t")
            if int(num) < min_commits:
                continue
            contributors += [contributor]

        return contributors[:limit_authors]

    def optn_over_conf(self, option_name: str, config_value: str) -> Any:
        """Return option if option is set, else return config value"""
        # logger.debug("Option '%s': '%s'", option_name, self.options.get(option_name))
        # logger.debug("Config '%s': '%s'", config_value, self.config[config_value])
        if self.options.get(option_name) is not None:
            # logger.debug("-[Option]-> '%s'", self.options.get(option_name))
            return self.options.get(option_name)
        # logger.debug("-[Config]-> '%s'", self.config[config_value])
        return self.config[config_value]
