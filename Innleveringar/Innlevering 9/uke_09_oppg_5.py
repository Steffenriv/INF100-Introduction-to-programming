weather_stations = {
    "Bergen" : {
        "Wind speed": 3.6,
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim" : {
        "Wind speed": 8.2,
        "Wind direction": "northwest",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard" : {
        "Wind speed": 7.5,
        "Wind direction": "southwest",
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    },
}
weatherinfo = ""
for i in weather_stations:
    speed = weather_stations[i]["Wind speed"]
    direction = weather_stations[i]["Wind direction"]
    precipitation = weather_stations[i]["Precipitation"]
    device = weather_stations[i]["Device"]
    weatherinfo += f"The weather in {i}:\n"
    weatherinfo += f"The wind speed is {speed} m/s in the {direction} direction and the precipitation is {precipitation} mm.\n"
    weatherinfo += f"The measurement was done using the {device} weather station.\n\n"

print(weatherinfo.rstrip()) #using rstrip to delete trailing lines