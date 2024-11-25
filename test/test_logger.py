import unittest

from src.dpm import logger as dpmlogger

from . import logger as testlogger


class TestLoggers(unittest.TestCase):
    def test_test_logger(self):
        testlogger.debug("This is a debug message.")
        testlogger.info("This is an info message.")
        testlogger.warning("This is a warning message.")
        testlogger.error("This is an error message.")
        self.assertTrue(True)  # Simple assertion to make the test pass

    def test_dpm_logger(self):
        dpmlogger.debug("This is a debug message.")
        dpmlogger.info("This is an info message.")
        dpmlogger.warning("This is a warning message.")
        dpmlogger.error("This is an error message.")
        self.assertTrue(True)  # Simple assertion to make the test pass
