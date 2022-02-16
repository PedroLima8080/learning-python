from Address import Address;
from datetime import datetime;
from Connection import Connection;
from sqlalchemy.exc import SQLAlchemyError;
from tkinter import Tk, filedialog

class Person:
    _name = '';
    _email = '';
    _birth_date = '';
    _zip_code = '';
    _city = '';
    _district = '';
    _address = '';
    
    _userFileIndex = {
        'name': 0,
        'email': 1,
        'birth_date': 2,
        'zip_code': 3,
        'city': 4,
        'district': 5,
        'address': 6,
    }
    
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
    
    def importPersonsFromFile(self):
        root = Tk() 
        root.withdraw()
        root.attributes('-topmost', True)
        filePath = filedialog.askopenfilename()
        #filePath = input('Name file in this path: ');
        users = [];
        
        with open(filePath, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            
            for line in lines:
                userLine = line.split(';');
                
                user = {};
                user['name'] = userLine[self._userFileIndex['name']];
                user['email'] = userLine[self._userFileIndex['email']];
                user['birth_date'] = userLine[self._userFileIndex['birth_date']];
                user['zip_code'] = userLine[self._userFileIndex['zip_code']];
                user['city'] = userLine[self._userFileIndex['city']];
                user['district'] = userLine[self._userFileIndex['district']];
                user['address'] = userLine[self._userFileIndex['address']];
                
                users.append(user);
                
            valuesString = '';    
            for i, user in enumerate(users):
                valuesString += f"('{user['name']}', '{user['email']}', '{user['birth_date']}', '{user['zip_code']}', '{user['city']}', '{user['district']}','{user['address']}')"; 
                if (len(users) - 1) > i:
                    valuesString += ',';
                    
            try:
                connection = Connection().getConnection();
                connection.execute(f'INSERT INTO persons (name, email, birth_date, zip_code, city, district, address) values {valuesString}')
                
                print('== USERS HAS BEEN IMPORTED ==');
            except SQLAlchemyError as e:
                print('Failed to import persons.\nLog:');
                print(e.__dict__);
                
    def exportToFile(self):
        outputFileName = input('Name output file: ');
        
        file = open('./exports/'+outputFileName+'.txt', 'x', encoding='utf-8');
        
        connection = Connection().getConnection();
        users = connection.execute('SELECT * FROM persons').fetchall();
        
        for user in users:
            file.write(f"{user['name']};{user['email']};{user['birth_date']};{user['zip_code']};{user['city']};{user['district']};{user['address']}\n");
            
        print(f"== FILE EXPORTED AT 'exports/{outputFileName}.txt' ==");
        
                