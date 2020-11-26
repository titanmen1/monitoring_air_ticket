import requests
from main import search_air_ticket

url = "https://api.telegram.org/bot1493989548:AAGzaIHRvcTP40tLZ5rGnInP-FvnQKNm4VI/"


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


def send_message(origin, destination):
    data = search_air_ticket(origin, destination)
    requests.get(url + 'sendMessage?chat_id=296765474&text={}'.format('Цена: {} руб. Дата вылета {}. Время полета '
                                                                           '{}.'.format(data[0]['value'],
                                                                                        data[0]['depart_date'],
                                                                                        data[0]['duration'])))
    return True


def main():
    update_id = None
    while True:
        message = get_last_update(update_id)
        if message:
            for mes in message:
                print(mes)
                update_id = mes['update_id']
                data_text = mes['message']['text'].split(' ')
                send_message(data_text[0], data_text[1])


if __name__ == '__main__':
    main()
