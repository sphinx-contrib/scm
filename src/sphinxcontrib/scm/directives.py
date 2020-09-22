from __future__ import annotations

import textwrap

import sphinx.util
from docutils import nodes
from docutils.nodes import Node
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective

from .util import Helper

logger = sphinx.util.logging.getLogger(__name__)


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

    def run(self) -> Node:
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
        sphinx.util.nested_parse_with_titles(self.state, new_content, node)

        return node.children
