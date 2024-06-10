# module2.py
from .module1 import function1
from .. import module3

function1()         # Output: Function 1 from module1
module3.function1()  # Output: Function 1 from module3
