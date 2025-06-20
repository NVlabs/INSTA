#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# graph_tool -- a general graph manipulation python module
#
# Copyright (C) 2006-2024 Tiago de Paula Peixoto <tiago@skewed.de>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
``graph_tool.util``
-------------------

This module contains miscelaneous utility functions.

Summary
+++++++

.. autosummary::
    :nosignatures:
    :toctree: autosummary

    find_vertex
    find_vertex_range
    find_edge
    find_edge_range

"""

from .. dl_import import dl_import
dl_import("from . import libgraph_tool_util")

from .. import _degree, _prop, _converter

__all__ = ["find_vertex", "find_vertex_range", "find_edge", "find_edge_range"]


def find_vertex(g, prop, match):
    """Find all vertices `v` for which `prop[v] = match`. The parameter prop
    can be either a :class:`~graph_tool.VertexPropertyMap` or string with value "in",
    "out" or "total", representing a degree type."""
    if prop in ["in", "out", "total"]:
        val = int(match)
    else:
        val = _converter(prop.value_type())(match)
    ret = libgraph_tool_util.\
          find_vertex_range(g._Graph__graph, _degree(g, prop),
                            (val, val))
    return ret


def find_vertex_range(g, prop, range):
    """Find all vertices `v` for which `range[0] <= prop[v] <= range[1]`. The
    parameter prop can be either a :class:`~graph_tool.VertexPropertyMap` or string
    with value "in", "out" or "total", representing a degree type."""
    if prop in ["in", "out", "total"]:
        convert = lambda x: int(x)
    else:
        convert = _converter(prop.value_type())
    ret = libgraph_tool_util.\
          find_vertex_range(g._Graph__graph, _degree(g, prop),
                            (convert(range[0]), convert(range[1])))
    return ret


def find_edge(g, prop, match):
    """Find all edges `e` for which `prop[e] = match`. The parameter prop
    must be a :class:`~graph_tool.EdgePropertyMap`."""
    val = _converter(prop.value_type())(match)
    ret = libgraph_tool_util.\
          find_edge_range(g._Graph__graph, _prop("e", g, prop),
                          (val, val))
    return ret


def find_edge_range(g, prop, range):
    """Find all edges `e` for which `range[0] <= prop[e] <= range[1]`. The
    parameter prop can be either a :class:`~graph_tool.EdgePropertyMap`."""
    convert = _converter(prop.value_type())
    ret = libgraph_tool_util.\
          find_edge_range(g._Graph__graph, _prop("e", g, prop),
                          (convert(range[0]), convert(range[1])))
    return ret
