# homework-selenium

## Настройка окружения
```bash
python3 -m venv venv
sourсe venv/bin/activate
pip install -r requirements.txt
```

## Запуск
```bash
export ALLURE_OUTPUT_PATH=$(pwd)
./runner_tests.sh
```

## Просморт отчета
```bash
allure serve allure-results --host localhost --port 9999
```
