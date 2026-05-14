.. ...........................................................................
.. © Copyright IBM Corporation 2025                                          .
.. File needs to be contributed by a collection, likely the ref's won't work
.. since the source will be in another, so need to create an external link.
.. ...........................................................................

==========
Life Cycle
==========

The IBM z/OSMF® (``ibm_zosmf``) collection is developed and released on a flexible release cycle; generally, we'll release on a per feature basis aiming for one major release yearly. Occasionally, the cycle may be extended to properly implement and test larger changes before a new release is made available.

**End of Life** (EOL) for this collection is generally a 2-year cycle unless a dependency reaches EOL prior to the 2 years. For example, if a collection has released and its dependency reaches EOL 1 year later, then the collection will EOL at the same time as the dependency, 1 year later.

Product Life Cycle
==================

Review this matrix for the status of the IBM z/OS core collection version, its critical dates, and which type of support it's currently eligible for.

+------------+----------------+-----------------------+-------------------+-------------------+------------------------+
| Version    | Status         | Changelogs            | GA Date           | EOL Date          | Life Cycle Phase       |
+============+================+=======================+===================+===================+========================+
| 1.6.x      | Released       | `1.6.x changelogs`_   |   January 2026    |   January 2028    | `Full support`_        |
+------------+----------------+-----------------------+-------------------+-------------------+------------------------+
| 1.5.x      | Released       | `1.5.x changelogs`_   |   June 2024       |   June 2026       | `Maintenance support`_ |
+------------+----------------+-----------------------+-------------------+-------------------+------------------------+

.. .............................................................................
.. Global Links
.. .............................................................................
.. _1.6.x changelogs:
    https://github.com/IBM/ibm_zosmf/blob/main/CHANGELOG.rst#v160
.. _1.5.x changelogs:
    https://github.com/IBM/ibm_zosmf/blob/main/CHANGELOG.rst#v150
.. _Full support:
    ../../../collections_content/collection-life-cycles.html#life-cycle-phase
.. _Maintenance support:
    ../../../collections_content/collection-life-cycles.html#life-cycle-phase
