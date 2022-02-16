from Person import Person;
from Connection import Connection;
from datetime import datetime

persons = [];

def init():
    exit = None;

    while(not exit):
        print('Menu: ');
        print('Create new person (1)');
        print('Show all persons (2)');
        print('Import persons from file (3)');
        print('Export to file (4)');
        print('Exit (5)');
        choice = input('Make your choice: ');

        if choice == '1':
            person = Person();
            person = person.createPerson();

        if choice == '2':
            person = Person();
            person = person.showAllPersons();
            
        if choice == '3':
            person = Person();
            person = person.importPersonsFromFile();
            
        if choice == '4':
            person = Person();
            person = person.exportToFile();

        if choice == '5':
            exit = True;

init();