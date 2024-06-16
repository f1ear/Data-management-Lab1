# Unit-тесты

# подключаем модули
import unittest
import sqlite3
import os

# импортируем классы из App.py
from App import Database, Doctors, Patients, Records, Diseases  # Импортируйте ваши классы

# класс TestDatabase - тестирует класс Database
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database('database.db')

    def tearDown(self):
        self.db.close()

    # тест подключения
    def test_connection(self):
        self.assertIsNotNone(self.db.conn)

# класс TestDoctors - тестирует класс Doctors
class TestDoctors(unittest.TestCase):
    def setUp(self):
        self.db = Database('database.db')
        self.doctors = Doctors(self.db)

    def tearDown(self):
        self.db.close()

    # тест получения всех записей о врачах
    def test_get_doctors(self):
        doctors = self.doctors.get_doctors()
        self.assertEqual(len(doctors), 4)  # Пункт 1: Показать врачей

    # тест добавления врача
    def test_add_doctor(self):
        self.doctors.add_doctor('Тестовый Врач', '1234567890', 'Специальность', '2024-06-16', 999)
        doctors = self.doctors.get_doctors()
        self.assertEqual(len(doctors), 4)  # Пункт 5: Добавить врача

# класс TestPatients - тестирует класс Patients
class TestPatients(unittest.TestCase):
    def setUp(self):
        self.db = Database('database.db')
        self.patients = Patients(self.db)

    def tearDown(self):
        self.db.close()

    # тест получения всех записей о пациентах
    def test_get_patients(self):
        patients = self.patients.get_patients()
        self.assertEqual(len(patients), 4)  # Пункт 2: Показать пациентов

    # тест добавления пациента
    def test_add_patient(self):
        self.patients.add_patient('Тестовый Пациент', 999999, 2000, 'М')
        patients = self.patients.get_patients()
        self.assertEqual(len(patients), 4)  # Пункт 6: Добавить пациента

# класс TestRecords - тестирует класс Records
class TestRecords(unittest.TestCase):
    def setUp(self):
        self.db = Database('database.db')
        self.records = Records(self.db)

    def tearDown(self):
        self.db.close()

    # тест получения всех записей
    def test_get_records(self):
        records = self.records.get_records()
        self.assertEqual(len(records), 4)  # Пункт 3: Показать записи

    # тест добавления записи
    def test_add_record(self):
        self.records.add_record(1, 1, 1, '2024-06-16')
        records = self.records.get_records()
        self.assertEqual(len(records), 4)  # Пункт 7: Добавить запись

    # тест получения записей по пациенту и дате
    def test_get_records_by_patient_and_date(self):
        records = self.records.get_records_by_patient_and_date(1, '2024-06-10')
        self.assertEqual(len(records), 1)  # Пункт 8: Показать записи пациента по дате

    # тест получения записей по врачу и дате
    def test_get_records_by_doctor_and_date(self):
        records = self.records.get_records_by_doctor_and_date(1, '2024-06-10')
        self.assertEqual(len(records), 1)  # Пункт 9: Показать записи врача по дате

    # тест получения записей по специальности и дате
    def test_get_records_by_specialty_and_date(self):
        records = self.records.get_records_by_specialty_and_date('Терапевт', '2024-06-10')
        self.assertEqual(len(records), 1)  # Пункт 10: Показать записи врачей определенной специальности по дате

# класс TestDiseases - тестирует класс Diseases
class TestDiseases(unittest.TestCase):
    def setUp(self):
        self.db = Database('database.db')
        self.diseases = Diseases(self.db)

    def tearDown(self):
        self.db.close()

    # тест получения записей о всех болезнях
    def test_get_diseases(self):
        diseases = self.diseases.get_diseases()
        self.assertEqual(len(diseases), 3)  # Пункт 4: Показать болезни

# собственно, main()  • _ •
if __name__ == '__main__':
    # выводим результаты тестов в файл "unit tests.txt"
    with open('unit tests.txt', 'w') as f:
        # инициализируем и запускаем тесты
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
