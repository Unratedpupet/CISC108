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

def rainiest_cloudy(forecasts: list[Forecast]) -> bool:
    if not forecasts:
        return False
    if forecasts[0].when == "empty":
        return False
    
    reports_list = []
    for forecast in forecasts:
        for report in forecast.reports:
            reports_list.append(report)
    
    max_rain_report = max_rainfall(reports_list)
    if was_cloudy(max_rain_report):
        return True
    else:
        return False


def was_cloudy(report: Report) -> bool:
    if report.weather.cloudy:
        return True
    else:
        return False

def max_rainfall(reports: list[Report]) -> Report:    
    max_rain = 0
    max_report_index = None
    for report_index, report in enumerate(reports):
        for rainfall in report.rainfall:
            if rainfall.amount > max_rain:
                max_rain = rainfall.amount
                max_report_index = report_index
                
    
    return reports[max_report_index]


today = Forecast("today", "Newark, DE", [
    Report(54, [Measurement(1, True), Measurement(2, True)],
        WeatherOptions(True, True, False)),
    Report(65, [Measurement(2, True)],
        WeatherOptions(True, True, False)),
    Report(45, [],
        WeatherOptions(False, True, False))
])
tomorrow = Forecast("tomorrow", "Newark, DE", [
    Report(54, [Measurement(1, True), Measurement(1, True)],
        WeatherOptions(True, True, False)),
    Report(65, [Measurement(3, True), Measurement(5, True), Measurement(10, False)],
        WeatherOptions(True, True, True)),
    Report(45, [Measurement(20, True)],
        WeatherOptions(True, False, False))
])
soon = Forecast("soon", "Newark, DE", [
    Report(14, [Measurement(5, False)],
        WeatherOptions(False, True, True))
])
empty = Forecast("empty", "Newark, DE", [])

assert_equal(rainiest_cloudy([]), False)
assert_equal(rainiest_cloudy([empty]), False)
assert_equal(rainiest_cloudy([today]), True)
assert_equal(rainiest_cloudy([tomorrow]), False)
assert_equal(rainiest_cloudy([soon]), True)
assert_equal(rainiest_cloudy([today, tomorrow]), False)
assert_equal(rainiest_cloudy([today, tomorrow, soon]), False)
assert_equal(rainiest_cloudy([soon, soon, soon, soon, soon]), True)

