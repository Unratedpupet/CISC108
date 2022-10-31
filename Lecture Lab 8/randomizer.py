import random
from dataclasses import dataclass


@dataclass
class WeatherOptions:
    raining: bool
    cloudy: bool
    snowing: bool


@dataclass
class Measurement:
    amount: int
    automatic: bool


@dataclass
class Report:
    temperature: int
    rainfall: list[Measurement]
    weather: WeatherOptions


@dataclass
class Forecast:
    when: str
    where: str
    reports: list[Report]


def randomize_weather() -> WeatherOptions:
    '''
    This function takes no arguments but returns a randomized WeatherOptions class.
    
    Args:
        None
    
    Return:
        WeatherOptions: A randomized WeatherOptions class
    '''
    # Initializes all WeatherOptions subclasses
    rain = None
    cloud = None
    snow = None
    # Randomizes the variables
    if random.randint(0, 1) == 1:
        rain = True
    else:
        rain = False
    if random.randint(0, 1) == 1:
        cloud = True
    else:
        cloud = False
    if random.randint(0, 1) == 1:
        snow = True
    else:
        snow = False

    return WeatherOptions(rain, cloud, snow)


def randomize_measurement() -> Measurement:
    amount = random.randint(0, 20)

    if random.randint(0, 1) == 1:
        automatic = True
    else:
        automatic = False

    return Measurement(amount, automatic)


def randomize_report() -> Report:
    # randomizes temp
    temp = random.randint(0, 40)

    # randomizes the amount of measurements and adds to list
    measures_list = []
    for _ in range(5):
        measures_list.append(randomize_measurement())

    weather = randomize_weather()

    return Report(temp, measures_list, weather)


def randomize_forecast() -> Forecast:

    when = random.choice(["now", "later", "soon", "morning", "noon", "afternoon", "midnight"])
    where = random.choice(["here", "there", "elsewhere", "over there", "far", "near"])

    reports_list = []
    for _ in range(5):
        reports_list.append(randomize_report())

    return Forecast(when, where, reports_list)


def forecast_list_generator() -> list[Forecast]:
    forecast_list = []
    for _ in range(4):
        forecast_list.append(randomize_forecast())
    return forecast_list


print(forecast_list_generator())
