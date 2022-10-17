import requests
import xmltodict


# https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
class ApiClient:
    def __init__(self, fetch: requests):
        self.fetch = fetch

    def get_xml(self, url):
        response = self.fetch.get(url)
        return response.text


def parse_usd(xml):
    # Сущности не должны зависеть от интерфейсов, которые они не используют
    data = dict(xmltodict.parse(xml))
    exc = data.get("exchangerates", None)
    if exc:
        return exc.get("row")[0].get("exchangerate").get("@buy")
    return None


if __name__ == "__main__":
    client = ApiClient(requests)
    xml = client.get_xml("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11")
    print(parse_usd(xml))

# ApiClient -> Adapter -> parse_usd
