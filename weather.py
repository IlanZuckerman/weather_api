import requests
import logging
import json
import helpers.pretty_print as pretty_print_helper

class Weather:
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self, unit, log, pretty_print, appid):
        self.unit = unit
        self.log = log
        self.format = format
        self.appid = appid
        self.pretty_print = pretty_print
        pass

    def lookup_by_city(self, city):
        url = "%s?q=%s&units=%s&mode=%s&APPID=%s" \
              % (self.URL, city, self.unit, self.format, self.appid)
        results = self._call(url)
        return results

    def lookup_by_city_id(self, id):
        url = "%s?id=%s&units=%s&mode=%s&APPID=%s" \
              % (self.URL, id, self.unit, self.format, self.appid)
        results = self._call(url)
        return results

    def forecast_by_city(self, city, cnt):
        url = "%s?q=%s&units=%s&mode=%s&cnt=%s&APPID=%s" \
              % (self.FORECAST_URL, city, self.unit, self.format, cnt, self.appid)
        results = self._call(url)
        return results

    def forecast_by_city_id(self, city_id, cnt):
        url = "%s?q=%s&units=%s&mode=%s&cnt=%s&APPID=%s" \
              % (self.FORECAST_URL, city_id, self.unit, self.format, cnt, self.appid)
        results = self._call(url)
        return results


    def _call(self, url):
        try:
            req = requests.get(url)
            if self.log:
                self.logger.info("Request URL: %s" % req.url)
                self.logger.info("Status Code: %s" % req.status_code)
                self.logger.info("JSON Response: %s" % req.content)
            if not req.ok:
                raise WeatherException
                # req.raise_for_status()

            if self.pretty_print:
                pretty_print_helper.pretty_print(json.loads(req.text))
            return req

        except WeatherException:
            self.logger.error("WeatherException was caught")

class WeatherException(Exception): pass