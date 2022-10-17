from abc import abstractmethod, ABC


class IPerson(ABC):
    @abstractmethod
    def get_phone_number(self):
        pass


class IPhoneNumber(ABC):
    @abstractmethod
    def value_of(self):
        pass


class PhoneNumber(IPhoneNumber):
    def __init__(self, phone: str, operator_code: str):
        self.phone = phone
        self.operator_code = operator_code

    def value_of(self):
        return f'+38({self.operator_code}){self.phone}'


class PersonAddress:
    def __init__(self, zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def value_of(self):
        return f'{self.zip}, {self.city}, {self.street}'


class Person(IPerson):
    def __init__(self, name: str, phone_: IPhoneNumber, address_: PersonAddress):
        self.name = name
        self.phone = phone_
        self.address = address_

    def get_phone_number(self):
        return f'{self.name} -  phone: {self.phone.value_of()}, address: {self.address.value_of()} '


address = PersonAddress('36007', 'Poltava', 'European, 28')
phone = PhoneNumber('9995544', '050')
person = Person('Alexander', phone, address)
print(person.get_phone_number())
