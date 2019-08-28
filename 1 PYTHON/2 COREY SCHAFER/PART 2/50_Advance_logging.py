"""
log DEBUG logger root
its  best habit of logging to specific loggers that can all be seperated configure.
working with root logger is not best idea
how to get a specific logger we will seee in this file
"""

import logging
import advlogemployee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("50_sample.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# logging.basicConfig(filename="50_sample.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
# logging.basicConfig(level=logging.INFO)


def add(x, y):
    "Add Function"
    return x + y


def sub(x, y):
    "Subtract Function"
    return x - y


def multiply(x, y):
    "Multiply Function"
    return x * y


def divide(x, y):
    "Division Function"
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error("Tried to divided by zero")
        logger.exception("Tried to divided by zero")
    else:
        return result


num_1 = 30
num_2 = 0

add_result = add(num_1, num_2)
# print("addition result is: {}+{}={}".format(num_1, num_2, add_result))
# logging.info("addition result is: {}+{}={}".format(num_1, num_2, add_result))
logger.debug("Addition result is: {}+{}={}".format(num_1, num_2, add_result))

sub_result = sub(num_1, num_2)
# print("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))
# logging.info("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))
logger.debug("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# print("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))
# logging.info("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))
logger.debug("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# print("Division result is {}/{}={}".format(num_1, num_2, div_result))
# logging.info("Division result is {}/{}={}".format(num_1, num_2, div_result))
logger.debug("Division result is {}/{}={}".format(num_1, num_2, div_result))
