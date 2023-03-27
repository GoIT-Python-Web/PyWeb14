
class ValidPhoneException(Exception):
    pass


class PersonInfo:

    def value_of(self) -> str:
        raise NotImplementedError


class PersonPhoneNumber(PersonInfo):
    def __init__(self, phone: str, operator_code: str):
        if operator_code != '050':
            raise ValidPhoneException('Це не валідний оператор')
        self.phone = phone
        self.operator_code = operator_code

    def value_of(self) -> str:
        return f'+38({self.operator_code}){self.phone}'


class PersonAddress(PersonInfo):
    def __init__(self, zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def value_of(self) -> str:
        return f'{self.zip}, {self.city}, {self.street}'


class Person:
    def __init__(self, name: str, phone_: PersonPhoneNumber, address_: PersonAddress):
        self.name = name
        self.phone = phone_
        self.address = address_

    def get_phone_number(self):
        return f'{self.name} -  phone: {self.phone.value_of()}'

    def get_address(self):
        return f'{self.name} - address: {self.address.value_of()}'


if __name__ == '__main__':

    address = PersonAddress('36007', 'Poltava', 'European, 28')
    phone = PersonPhoneNumber('9995544', '050')
    person = Person('Alexander', phone, address)
    print(person.get_phone_number())
    print(person.get_address())

    phone = PersonPhoneNumber('9995544', '060')
