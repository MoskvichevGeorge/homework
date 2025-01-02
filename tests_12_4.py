import logging
import unittest
from hw import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest:
    def test_walk(self):
        try:
            # Передаем отрицательное значение в speed
            runner = Runner(name="Test Runner", speed=-10)
            # Логируем успешное выполнение
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            # Логируем исключение на уровне WARNING
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            # Передаем что-то кроме строки в name
            runner = Runner(name=123, speed=10)
            # Логируем успешное выполнение
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            # Логируем исключение на уровне WARNING
            logging.warning("Неверный тип данных для объекта Runner")

# Пример использования
if __name__ == "__main__":
    #test = RunnerTest()
    #test.test_walk()
    #test.test_run()
    unittest.main()