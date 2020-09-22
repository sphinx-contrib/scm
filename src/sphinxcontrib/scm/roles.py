from __future__ import annotations

import textwrap

import sphinx.util
from docutils import nodes
from docutils.nodes import Node, system_message
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxRole

from .util import Helper

logger = sphinx.util.logging.getLogger(__name__)


class ContribsRole(SphinxRole, Helper):
    def run(self) -> tuple[list[Node], list[system_message]]:
        """Role to list all SCM contributors"""
        contributors = self.get_contibutors()
        contributors_str = (
            ", ".join(contributors) if contributors else "<no SCM contributors found>"
        )

        new_content = textwrap.dedent(
            """\
            {contributors}\
            """
        ).format(contributors=contributors_str)
        # new_content = StringList(new_content.splitlines(), source="")

        # node = nodes.Element()
        # sphinx.util.nested_parse_with_titles(self.state, new_content, node)
        node = nodes.inline(rawsource=new_content, text=new_content)

        return [node], []
