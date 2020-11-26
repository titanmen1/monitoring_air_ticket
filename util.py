import json


def create_button_for_buy(data):
    date_departure = str(data[0]['depart_date'].split('-')[2]) + str(data[0]['depart_date'].split('-')[1])
    url_for_buy = 'https://www.aviasales.ru/search/{}'.format(data[0]['origin'] + date_departure + data[0]['destination'] + '1')
    button = {
        'inline_keyboard': [
            [
                {'text': 'Купить билет', 'url': url_for_buy, 'callback_data': None,
                 'switch_inline_query': None,
                 'switch_inline_query_current_chat': None, 'callback_game': None, 'pay': None, 'login_url': None}
            ]
        ],
        'row_width': 1
    }
    return json.dumps(button)
