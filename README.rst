Rand Toys
=========

``pyrandtoys`` is a python module containing probability-based toys
functions. It works offline and is compatible with both Python 2 and 3.

Installation
~~~~~~~~~~~~

::

   pip install pyrandtoys

Usage
~~~~~

::

   import pyrandtoys

Dice:
^^^^^

+ **Optional:** Number of Dice ``<int>`` 
+ **Default:** Number of Dice = 1
+ **Return Type:** ``<tuple>``

::

   dice(number_of_dice)

Coin:
^^^^^

+ **Optional:** Number of Coins ``<int>`` 
+ **Default:** Number of Coins = 1
+ **Return Type:** ``<tuple>``

::

   coin(number_of_coins)

Card:
^^^^^

+ **Optional:** Number of Cards ``<int>`` 
+ **Default:** Number of Cards = 1
+ **Return Type:** ``<tuple>``

::

   card(number_of_cards)

Similar Toys:
^^^^^^^^^^^^^

+ **Optional:** Number of Items ``<int>`` 
+ **Default:** Number of Items = 1
+ **Return Type:** ``<tuple>``

::

   dreidel(number_of_dreis)
   cat(number_of_cats)
   switch(number_of_switches)

Spinner:
^^^^^^^^

+ **Required:** Lower & Upper Limits ``<int>`` 
+ **Default:** Lower Limit = 0 
+ **Return Type:** ``<tuple>``

::

   spinner(lowerLimit, upperLimit) 

Toy Combinations:
^^^^^^^^^^^^^^^^^

+ **Default:** Number of Toys = 0
+ **Return Type:** ``<tuple>`` 

**If you want to use a combination of toys then,**
   **Required:** List of toys as ``<list>``,\ ``<tuple>``

::

   combi(("switch", "cat", "dice"))
   combi(["dreidel", "coin", "coin", "cat"])

**For combination of x random toys,**

::

   combi(x)

Project Links
~~~~~~~~~~~~~

-  PyPI
   `(https://pypi.org/project/pyrandtoys/) <https://pypi.org/project/pyrandtoys/>`__
-  GitHub
   `(https://github.com/thenithinbalaji/pyrandtoys) <https://github.com/thenithinbalaji/pyrandtoys>`__
