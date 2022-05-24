"""
Implement a performance measuring environment simulator for the vauum cleaner world depicted in Figure 2.2
and specified on Page 38.

Your implementation should be modular so thgat the sensors, actuators and environment charachteristics (size, shape,
dirt placement, etc.) can be changed easily.

For Python there exists an implementation of this at https://aima.cs.berkely.edu
and https://github.com/aimacode/aima-python
"""

import Environment, Thing


class Dirt(Thing):
    def __init__(self):
        pass