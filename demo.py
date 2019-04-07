import weather
import argparse

def get_args():
    """
    Standard args function
    :return: dict which includes all the arguments
    List af arguments:
    -u: Units are metric or imperial. Default is metric
    -l: Logging. De-Activated by default
    -p: Pretty print for the forecast / current conditions. disabled by default. If you dont enable this option, then
        it is recommended to enable -l. otherwise, you wont see any results printed on the cmd.
    -k: Key for API. Default value is used (Authors Account). But you can specify your own.
    -cnt: Represents amount of hours to show if the forecast argument is passed. cnt=1 equals to 3 hours ahead.
    -f: Forecast. If you wish to get forecast for some city, you should use this. This is optional. But if you specify
        it, then you also need to specify the -cnt argument.
    -c: City name. you can specify city name in order to get forecast / current conditions fur it.
    -i: Same is -c, only with ID specified.

    Example for getting 6 hours forecast in London:
    #> python demo.py -p -c "London" -f -cnt "2"

    """
    parser = argparse.ArgumentParser(description='This functionality shows weather conditions in cities'
                                                 ' across the world')
    parser.add_argument('-u', action='store', dest='unit', required=False, default='metric',
                        help='Units are metric or imperial. When you do not use units parameter,'
                             ' then format is Standard by default (Metric). For example, if you wish imperial unit, then'
                             'specify -u "imperial". otherwise, dont mention -u at all')
    parser.add_argument('-l', action='store_true', dest='log', required=False, default=False,
                        help='Activate logging. If you do not specify this, then  default value will be used, which is:'
                             ' deactivated. For example: if you wish to activate logging, then specify -l , otherwise,'
                             ' dont mention this argument at all')
    parser.add_argument('-p', action='store_true', dest='pretty_print', required=False, default=False,
                        help='Pretty print of the Forecast conditions. Disabled by default. If you wish to enable it,'
                             ' then specify this argument -p , otherwise, dont specify it at all')
    parser.add_argument('-k', action='store_true', dest='api_key', required=False,
                        default='b2562e6f43a290665a2e9440d1d72400',
                        help='API key. If you do not specify this, then By default value will be used, which is Ilans key.'
                             ' If you have your own API key for weather service, then specify it as following:'
                             '-k "xyz".')
    parser.add_argument('-cnt', action='store', dest='cnt', nargs='?', required=False,
                        help='This is optional value, and should be specified if you wish to list forecast for some city.'
                             ' it represents the amount of hours for which the forecast is shown. Each unit represents 3 hours.' \
                             ' For example when you specify cnt "2" as an argument, the forecast will be shown for 6 hours')
    parser.add_argument('-f', action='store_true', dest='forecast', required=False, default=False,
                        help='Show forecast of particular city for amount of hours specified by "-c" arg. This argument is '
                             'Optional, but once specified, it Must come in conjunction with "-c" arg.')
    parser.add_argument('-c', action='store', dest='city_name', required=False,
                        help='City name for currect weather conditions or forecast')
    parser.add_argument('-i', action='store', dest='city_id', required=False,
                        help='City id for currect weather conditions or forecast')

    args = parser.parse_args()

    if (args.forecast is True) and (args.cnt is None):
        parser.error("The following arg: '-cnt' (cnt) need to be in conjunction with '-f' (forecast).\n"
                     "Meaning that if you wish to view forecast, you need to specify the period of time (-cnt)")

    if args.city_name is None and args.city_id is None:
        parser.error("You must specify at least one of the following args: -c (city name), -i (city id)")

    if args.city_name and args.city_id:
        parser.error("You can not specify both of the following args together: -c (city name), -i (city id)")

    print(args)
    return args


def main():
    """

    :return:
    """
    args = get_args()

    weather_obj = weather.Weather(unit=args.unit, log=args.log, pretty_print=args.pretty_print, appid=args.api_key,)

    if args.city_name: weather_obj.lookup_by_city(args.city_name)

    if args.city_id: weather_obj.lookup_by_city_id(args.city_id)

    if args.city_name and args.forecast: weather_obj.forecast_by_city(args.city_name, args.cnt)

    if args.city_id and args.forecast: weather_obj.forecast_by_city_id(args.city_id, args.cnt)


if __name__ == '__main__':
    main()
