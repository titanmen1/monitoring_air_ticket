# -*- coding: utf-8 -*-
import requests
import json
import const

# xxx = requests.get('http://api.travelpayouts.com/v2/prices/latest?currency={}&origin={}&destination={}&beginning_of_period={}&one_way={}&page=1&limit=10&show_'
#                    'to_affiliates=true&sorting=price&token={}'.format(token))

# print(xxx.content)

# Самые дешевые билеты найденные за последние 48 часов
def search_air_ticket(origin, destination):
    # Последние за 48 часов цены
    data = requests.get(
        'http://api.travelpayouts.com/v2/prices/latest?currency={}&origin={}&destination={}&beginning_of_period={}'
        '&one_way={}&page=1&limit=1000&show_to_affiliates=true&sorting=price&token={}'.format(const.currency, origin,
                                                                                            destination,
                                                                                            const.beginning_of_period,
                                                                                            const.one_way, const.token))

    datat = []
    print(data.text)
    # фильры
    for d in json.loads(data.text)['data']:
        # Без пересадок
        if (d['number_of_changes'] == 0):
            datat.append(d)
        # number_of_changes
    return datat

    # data = requests.get('http://api.travelpayouts.com/v1/prices/direct?origin={}&one_way=true&destination={}&depart_date={}&token={}'
    #                     .format(origin, destination, depart_date, token))
# search_air_ticket()


def search_air_ticket_by_date():

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/RU/RUB/ru-RU/MOW/BCN/2021-01-24"

    headers = {
        'x-rapidapi-key': "c6c8f63fe7msh7f44a13484f8476p192e20jsnc9aa8f5353f0",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    # Ближайшие билеты на неделю как я понимаю
    url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v2/prices/week-matrix"

    querystring = {"origin": "MOW", "destination": "BCN", "depart_date": "2020-12-12", "currency": "RUB"}

    headers = {
        'x-access-token': "faffb19c5eddc4e30957762929007cc1",
        'x-rapidapi-key': "c6c8f63fe7msh7f44a13484f8476p192e20jsnc9aa8f5353f0",
        'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# search_air_ticket_by_date()