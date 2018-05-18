from zeep import Client


def read_average(file_name):
    temps_sum = 0
    temps_count = 0
    with open(file_name, 'r') as f:
        for line in f:
            temp = line.split()
            temps_sum += int(temp[0])
            temps_count += 1
    return temps_sum / temps_count


def convert_temp(fahrenheit):
    client = Client('https://www.w3schools.com/xml/tempconvert.asmx?WSDL')
    celsius = client.service.FahrenheitToCelsius(fahrenheit)
    return round(float(celsius), 2)


def task1():
    file_name = 'temps.txt'
    average_fahrenheit = read_average(file_name)
    average_celsius = convert_temp(average_fahrenheit)
    print(average_celsius)


task1()
