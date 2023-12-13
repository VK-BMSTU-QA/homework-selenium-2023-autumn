# homework-selenium

## Настройка окружения

```bash
python3 -m venv venv
sourсe venv/bin/activate
pip install -r requirements.txt
```

## Настройка окружения 
Создать .env файл формата:

```
EMAIL_ACCOUNT=test@test.com
PASSWORD_ACCOUNT=test_pw
```
За валидными данными можно написать в личку тг: @dyndtikj

## Запуск
```bash
export ALLURE_OUTPUT_PATH=$(pwd)
./runner_tests.sh
```

## Просморт отчета
```bash
allure serve allure-results --host localhost --port 9999
```