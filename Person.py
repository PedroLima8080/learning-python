from Address import Address;
from datetime import datetime;
from Connection import Connection;

class Person:
    _name = '';
    _email = '';
    _birth_date = '';
    _zip_code = '';
    _city = '';
    _district = '';
    _address = '';
    
    def createPerson(self):
        self._name = input("Your name: ");
        self._email = input("Your email: ");

        while(not self._birth_date):
            try:
                self._birth_date = datetime.strptime(input("Your birth date: "), "%d/%m/%Y").strftime("%Y-%m-%d");
            except (ValueError):
                print('Incorrect date format!\nEx: 12/03/2005')
                self._birth_date = None;


        self._zip_code = input("Your zip code: ");
        
        address = Address(self._zip_code)
        infoAddress = address.getAddressByApi();
        
        if infoAddress:
            self._city = infoAddress['localidade'];
            self._district = infoAddress['bairro'];
            self._address = infoAddress['logradouro'];
        else:
            self._city = input('Your city: ');
            self._district = input('Your district: ');
            self._address = input('Your address: ');

        sql = "INSERT INTO persons (name, email, birth_date, zip_code, city, district, address) VALUES (%s, %s, %s, %s, %s, %s, %s)";
        val = (self._name, self._email, self._birth_date, self._zip_code, self._city, self._district, self._address);

        connection = Connection().getConnection();
        connection.execute(sql, val);

        print('== PERSONS CREATED SUCCESSFULLY ===');
        
        return self;

    def showAllPersons(self):
        connection = Connection().getConnection();
        data = connection.execute('SELECT * FROM persons').fetchall();
        print('========PERSONS======');
        for row in data:
            print(f'Nome: {row["name"]}');
            print(f'Email: {row["email"]}');
            print(f'Data de Nascimento: {row["birth_date"]}');
            print(f'CEP: {row["zip_code"]}');
            print('----------------------');
        
        
        