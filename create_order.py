import configuration
import requests
import data


# Запрос на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=order_body,
                         headers=data.headers)


response = post_new_order(data.order_body);
print(response.status_code)
print(response.json())


def get_track_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + str(track))


print(response.json())