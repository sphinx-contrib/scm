from __future__ import annotations

import textwrap

from docutils import nodes
from docutils.nodes import Node
from docutils.statemachine import StringList
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import nested_parse_with_titles

from .util import Helper

logger = logging.getLogger(f"sphinxcontrib-scm.{__name__}")


class ContribsDirective(SphinxDirective, Helper):
    has_content = False
    optional_arguments = 0
    option_spec = {
        "email": str,
        "limit_authors": int,
        "min_commits": int,
        "sort": str,
        "type": str,
    }

    def run(self) -> list[Node]:
        """Directive to list all SCM contributors"""
        contributors = self.get_contibutors()
        contributors_str = (
            ",\n   ".join(contributors)
            if contributors
            else "<no SCM contributors found>"
        )

        new_content = textwrap.dedent(
            """\
            .. sectionauthor::
               {contributors}\
            """
        ).format(contributors=contributors_str)
        new_content = StringList(new_content.splitlines(), source="")

        node = nodes.Element()
        nested_parse_with_titles(self.state, new_content, node)

        return node.children
