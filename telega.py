# -*- coding: utf-8 -*-
import requests
import json
from main import search_air_ticket
import const
from util import create_button_for_buy

url = "https://api.telegram.org/bot{}/".format(const.api_bot_telegram)


def get_last_update(offset):
    update_url = url + 'getUpdates'
    if offset:
        # Сообщение считается прочитаным если был запрос ИД последнего сообщения + 1
        update_url = update_url + "?offset={}".format(offset + 1)
    res = requests.get(update_url).json()
    return res["result"]


def update_message():
    xx = requests.get(url + 'getUpdates')
    return xx.text


def send_message(origin, destination, beginning_of_period):
    data = search_air_ticket(origin, destination, beginning_of_period)
    button_buy = create_button_for_buy(data)
    requests.get(url + 'sendMessage?chat_id=296765474&text={}&reply_markup={}'.format('Цена: {} руб. Дата вылета {}. Время полета '
                                                                           '{}.'.format(data[0]['value'],
                                                                                        data[0]['depart_date'],
                                                                                        data[0]['duration']), button_buy))
    return True


def main():
    update_id = None
    while True:
        try:
            message = get_last_update(update_id)
            if message:
                for mes in message:
                    print(mes)
                    update_id = mes['update_id']
                    data_text = mes['message']['text'].split(' ')
                    if len(data_text) == 2:
                        data_text.append(const.beginning_of_period)
                    send_message(data_text[0], data_text[1], data_text[2])

        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)