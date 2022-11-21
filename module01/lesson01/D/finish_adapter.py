import requests
from abc import abstractmethod, ABC


class Connection(ABC):
    @abstractmethod
    def get_json(self, url):
        pass


class RequestConnection(Connection):
    def __init__(self, request: requests):
        self.request = request

    def get_json(self, url):
        return self.request.get(url).json()


class ApiClient:
    def __init__(self, fetch: Connection):
        self.fetch = fetch

    def get_json(self, url):
        response = self.fetch.get_json(url)
        return response


def pretty_view(data: list[dict]):
    pattern = '|{:^10}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get('buy')
        sale = el.get(currency).get('sale')
        print(pattern.format(currency, sale, buy))


def data_adapter(data: dict) -> list[dict]:
    return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]


if __name__ == '__main__':
    client = ApiClient(RequestConnection(requests))
    data = client.get_json('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    pretty_view(data_adapter(data))

# ApiClient -> Adapter -> parse_usd
