from dataclasses import dataclass
from bakery import assert_equal

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
     
def total_rainfall(forecasts: list[Forecast]) -> int:
    '''
    Then, define a function total_rainfall that consumes a list of Forecast
    and produces an integer representing the total amount of
    rainfall over all the reports in each provided Forecast.
    '''
    total_rainfall_amount = 0
    for forecast in forecasts:
        for report in forecast.reports:
            for rainfall in report.rainfall:
                total_rainfall_amount += rainfall.amount
              
    return total_rainfall_amount


test1 = [
    Forecast("today", "here",
             [Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False))]),
    Forecast("today", "there",
             [Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False))])
    ]
test2 = [
    Forecast("today", "here",
             [Report(20, [Measurement(2, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False))]),
    Forecast("today", "there",
             [Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False))])
    ]
test3 = [
    Forecast("today", "here",
             [Report(20, [Measurement(3, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False))]),
    Forecast("today", "there",
             [Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False)),
              Report(20, [Measurement(1, True), Measurement(2, True), Measurement(1, True)], WeatherOptions(True, False, False))])
    ]

assert_equal(total_rainfall(test1), 24)
assert_equal(total_rainfall(test2), 25)
assert_equal(total_rainfall(test3), 26)