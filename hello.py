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
        print('Exit (3)');
        choice = input('Make your choice: ');

        if choice == '1':
            person = Person();
            person = person.createPerson();

        if choice == '2':
            person = Person();
            person = person.showAllPersons();

        if choice == '3':
            exit = True;

init();