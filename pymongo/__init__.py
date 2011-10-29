# Copyright 2009-2010 10gen, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Python driver for MongoDB."""


ASCENDING = 1
"""Ascending sort order."""
DESCENDING = -1
"""Descending sort order."""

GEO2D = "2d"
"""Index specifier for a 2-dimensional `geospatial index`_.

.. versionadded:: 1.5.1

.. note:: Geo-spatial indexing requires server version **>= 1.3.3+**.

.. _geospatial index: http://www.mongodb.org/display/DOCS/Geospatial+Indexing
"""

OFF = 0
"""No database profiling."""
SLOW_ONLY = 1
"""Only profile slow operations."""
ALL = 2
"""Profile all operations."""

PRIMARY = 0
"""Send all reads to the primary in a ReplicaSetConnection."""
SECONDARY = 1
"""Send reads to all active members of a ReplicaSetConnection."""
SECONDARY_ONLY = 2
"""Send all reads to secondaries in a ReplicaSetConnection."""

version_tuple = (2, 0, 1, '+')

def get_version_string():
    if version_tuple[-1] == '+':
        return '.'.join(map(str, version_tuple[:-1])) + '+'
    return '.'.join(map(str, version_tuple))

version = get_version_string()
"""Current version of PyMongo."""

from pymongo.connection import Connection
from pymongo.replica_set_connection import ReplicaSetConnection

def has_c():
    """Is the C extension installed?

    .. versionadded:: 1.5
    """
    try:
        from pymongo import _cmessage
        return True
    except ImportError:
        return False
