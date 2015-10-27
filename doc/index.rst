.. Ramon Test documentation master file, created by
   sphinx-quickstart on Tue Oct 27 14:45:15 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Ramon Test's documentation!
======================================

Contents:

.. toctree::
   :maxdepth: 2

   a_page

Setup
=====

To `start` using ``my code`` *you* **have** to run the here.py file

.. code-block:: python

   cd /path/to/files
   python setup.py install


.. important::
   The ``here.py`` module will call all the classes.

.. automodule:: here
   :members:

* "attention"
* "caution"
* "danger"
* "error"
* "hint"
* "important"
* "note"
* "tip"
* "warning"

A paragraph containing only two colons 
indicates that the following indented 
or quoted text is a literal block. 

:: 

  Whitespace, newlines, blank lines, and 
  all kinds of markup (like *this* or 
  \this) is preserved by literal blocks. 

  The paragraph containing only '::' 
  will be omitted from the result. 

The ``::`` may be tacked onto the very 
end of any paragraph. The ``::`` will be 
omitted if it is preceded by whitespace. 
The ``::`` will be converted to a single 
colon if preceded by text, like this:: 

  It's very convenient to use this form. 

Literal blocks end when text returns to 
the preceding paragraph's indentation. 
This means that something like this 
is possible:: 

      We start here 
    and continue here 
  and end here. 

Per-line quoting can also be used on 
unindented literal blocks:: 

> Useful for quotes from email and 
> for Haskell literate programming.


.. code-block:: python

   import tete
   a = 4 + 'string'
   tete.func(a)

   return beach


.. danger::
   BE CAREFUL!




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

