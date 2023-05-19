import data
import create_order

# Тест проверяет, что по треку заказа можно получить данные о заказе.
def test_order_track():
    # Создание нового заказа и получение его трека
    track_number = create_order.post_new_order(data.order_body).json()["track"]
    # Получение заказа по треку
    resp_get_track_order = create_order.get_track_order(track_number)
    # Проверка, что код ответа равен 200.
    assert resp_get_track_order.status_code == 200