import requests

def test_get_station_number3():

    api_key = "018d0068-399c-42b2-b5df-02d9afe0930e"
    lat = "53.195045"
    lng = "45.018312"
    distance = 50
    transport_types = "train"
    station_types = "train_station"

    url = f"https://api.rasp.yandex.net/v3.0/nearest_stations/?apikey={api_key}&lat={lat}&lng={lng}&distance={distance}&transport_types={transport_types}&station_types={station_types}"
    response = requests.get(url)
    data = response.json()

    assert data["stations"][2], "Нет станции номер 3"
    return data["stations"][2]["code"]


def test_get_info_station_number3():

    api_key = "018d0068-399c-42b2-b5df-02d9afe0930e"
    station = test_get_station_number3()
    date = "2024-03-19"
    transport_types = "suburban"
    direction = "на%20Пензу"

    url = f"https://api.rasp.yandex.net/v3.0/schedule/?&date={date}&apikey={api_key}&station={station}&transport_types={transport_types}&direction={direction}"

    response = requests.get(url)
    data = response.json()

    assert data['date'], "Нет даты"
    assert data['pagination'], "Нет информации о постраничном выводе найденных рейсов"
    assert data['station'], "Нет информация об указанной в запросе станции"
    assert data['schedule'], "Нет массива списка рейсов"
    assert data['schedule_direction'], "Нет кода и названия запрошенного направления рейсов"
    assert data['directions'], "Нет кода и названия возможных направлений движения электричек по станции"

    assert data['schedule'][0]['thread']['number'], "Нет номера рейса"
    assert data['schedule'][0]['thread']['title'], "Нет названия нитки"
    assert data['schedule'][0]['thread']['uid'], "Нет идентификатора нитки"
