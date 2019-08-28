# import employee details into log file got it

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("50_employee.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename="50_employee.log", level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print("Create Employee:{}-{}".format(self.fullname, self.email))
        # logging.info("Create Employee:{}-{}".format(self.fullname, self.email))
        # logging.debug("Create Employee:{}-{}".format(self.fullname, self.email))
        # logger.info("Create Employee:{}-{}".format(self.fullname, self.email))
        logger.warning("Create Employee:{}-{}".format(self.fullname, self.email))

    @property
    def email(self):
        return("{}.{}@gmail.com").format(self.first, self.last)

    @property
    def fullname(self):
        return("{} {}".format(self.first, self.last))


emp_1 = Employee("Devid", "Wille")
emp_2 = Employee("John", "Dheere")
emp_3 = Employee("Corey", "Schafer")
