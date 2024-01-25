from datetime import datetime
import pytz


class DatetimeProvider:
    @staticmethod
    def now() -> datetime:
        '''Timezone: Brazil/East"'''
        tz = pytz.timezone("Brazil/East")
        return datetime.now(tz)

    @staticmethod
    def utc_now() -> datetime:
        """Timezone: UTC"""
        return datetime.now(pytz.utc)
