from zeep import Client


def task2():
    file_name = 'currencies.txt'
    cost_trip_in_rub = 0
    client = Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')

    with open(file_name, 'r') as f:
        for line in f:
            line = line.split()
            cost_flight_in_rub = client.service.ConvertToNum(
                fromCurrency=line[2],
                toCurrency='RUB',
                amount=line[1],
                rounding=True)
            cost_trip_in_rub += cost_flight_in_rub

    print(round(cost_trip_in_rub))


task2()
