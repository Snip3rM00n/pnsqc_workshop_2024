import datetime
import time

from datetime import datetime as date_time
from datetime import timedelta


class GeneralHelpers:

    @staticmethod
    def get_now_plus(seconds):
        return date_time.now() + timedelta(seconds=seconds)

    @staticmethod
    def wait_for(condition, expectation=True, time_out_in_seconds=60, interval=0.5, throw_on_timeout=True):
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
