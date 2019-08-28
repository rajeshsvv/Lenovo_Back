"""
in ths video we get started with logging by repalcing our print satetments with log statements we
are also set different logging levels and also log information to files
In Next Video how we can use loggers through out multiple modules and how can we configure the levels so that diffferent
inforamtion get sent exactly where we wanted to go
python comes with logging module built in 

logging levels are debug=10 info=20 warning=30 error=40 critical=50 


debug:detailed information, typically of interest only  when diagnosing the problems

info:confirmation that things are working as expected

warning:An indication that something unexpectedly happened,or indication of some problem in the future(eg disk space low)
The software still working as expected.

error:Due to more serious problem, the software has not been able to perform some function.

critical:A serious error,indicating that the problem itself may be unable to continue running  

default level for logging ---warning means it will capture everything that is warning and above log levels like warning error critical
 so by default it will log warning error critical and ignore the debug and info log statements 


printing debug statements in the console window is good to see 
but we need that to log to file k got it not jusst printing it to the console
log files are great way to capture the information because it allows us to see our log inforamtion over time in one place 
"""
import logging

logging.basicConfig(filename="50_sample.log", level=logging.DEBUG,format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
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
    return x / y


num_1 = 30
num_2 = 5


add_result = add(num_1, num_2)
# print("addition result is: {}+{}={}".format(num_1, num_2, add_result))
logging.debug("addition result is: {}+{}={}".format(num_1, num_2, add_result))
# logging.info("addition result is: {}+{}={}".format(num_1, num_2, add_result))
# logging.warning("addition result is: {}+{}={}".format(num_1, num_2, add_result))
# logging.error("addition result is: {}+{}={}".format(num_1, num_2, add_result))
# logging.critical("addition result is: {}+{}={}".format(num_1, num_2, add_result))

sub_result = sub(num_1, num_2)
# print("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))
logging.debug("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))
# logging.info("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))
# logging.warning("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))
# logging.error("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))
# logging.critical("Sub result is: {}-{}={}".format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# print("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))
logging.debug("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))
# logging.info("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))
# logging.warning("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))
# logging.error("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))
# logging.critical("Multiply result is: {}*{}={}".format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# print("Division result is {}/{}={}".format(num_1, num_2, div_result))
logging.debug("Division result is {}/{}={}".format(num_1, num_2, div_result))
# logging.info("Division result is {}/{}={}".format(num_1, num_2, div_result))
# logging.warning("Division result is {}/{}={}".format(num_1, num_2, div_result))
# logging.error("Division result is {}/{}={}".format(num_1, num_2, div_result))
# logging.critical("Division result is {}/{}={}".format(num_1, num_2, div_result))
