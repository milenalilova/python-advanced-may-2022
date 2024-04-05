def forecast(*args):
    forecast_dict = {}
    for location, weather in args:
        forecast_dict[location] = weather
    sorted_dict = dict(sorted(forecast_dict.items(), key=lambda x: ((x[1]), x[0])))

    sunny = ''
    cloudy = ''
    rainy = ''

    for k, v in sorted_dict.items():
        if v == 'Sunny':
            sunny += f"{k} - {v}\n"
        elif v == 'Rainy':
            rainy += f"{k} - {v}\n"
        elif v == 'Cloudy':
            cloudy += f"{k} - {v}\n"
    output = sunny + cloudy + rainy
    return output


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
