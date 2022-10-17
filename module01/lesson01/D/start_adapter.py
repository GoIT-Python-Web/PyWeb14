import requests
import xmltodict

"""
Dependency inversion. Согласно принципу модули должны зависеть от других модулей не напрямую, а от абстракций. Модули верхних уровней не должны зависеть от модулей нижних уровней. 

Добавляем Connection и RequestConnection в работу класса ApiClient
"""

# https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
class ApiClient:
    def __init__(self, fetch: requests):
        self.fetch = fetch

    def get_xml(self, url):
        response = self.fetch.get(url)
        return response.text


def parse_usd(data):
    exc = data.get("exchangerates", None)
    if exc:
        return exc.get("row")[0].get("exchangerate").get("@buy")
    return None


def xml_adapter(xml):
    return dict(xmltodict.parse(xml))


if __name__ == "__main__":
    client = ApiClient(requests)
    data = client.get_xml(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    print(parse_usd(xml_adapter(data)))

# ApiClient -> Adapter -> parse_usd
