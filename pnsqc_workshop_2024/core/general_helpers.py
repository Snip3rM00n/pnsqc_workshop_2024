import time

from datetime import datetime as date_time
from datetime import timedelta


class GeneralHelpers:

    @staticmethod
    def get_now_plus(seconds):
        """
        Gets the current time plus a given number of seconds.

        :param seconds: The ammount of seconds to add.
        :return: A DateTime object representing a time in the future plus a given amount of seconds.
        """
        return date_time.now() + timedelta(seconds=seconds)

    @staticmethod
    def wait_for(condition, expectation=True, time_out_in_seconds=60, interval=0.5, throw_on_timeout=True):
        """
        Handles waiting for a given condition.

        :param condition: The condition to wait for as a callable function.
        :param expectation: The expected outcome of the condition.
        :param time_out_in_seconds: The amount of time, in seconds, to wait for the condition to meet its expectation.
        :param interval: The polling time between checks of the condition function.
        :param throw_on_timeout: Whether to throw an error on timeout or not.
        :return: A Boolean determining of the condition has been met or not.
        """
        timeout = GeneralHelpers.get_now_plus(time_out_in_seconds)
        condition_met = False

        while GeneralHelpers.get_now_plus(0) < timeout:
            condition_met = condition() == expectation

            if condition_met:
                break

            time.sleep(interval)
        else:
            if throw_on_timeout:
                error_message = f"{condition.__name__} not met after {time_out_in_seconds} seconds."
                raise TimeoutError(error_message)

        return condition_met
