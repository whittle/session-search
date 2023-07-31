==============
session-search
==============

A sketch of how to search session logs for funnel alignment.

It creates a `rose tree`_ composed of all the funnels of interest, and
then each session gets matched against the rose tree to find complete
and partial funnel matches.

.. _`rose tree`: https://en.wikipedia.org/wiki/Rose_tree

The primary way that a rose tree is a mismatch for the problem is that
sessions are allowed to include pages in between funnel steps without
interrupting the funnel match. This means that instead of a simple
tree search, it is necessary to keep a fringe of reached nodes in the
tree and process search steps against the entire fringe.
