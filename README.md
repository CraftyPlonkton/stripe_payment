### Запуск проекта на тестовом сервере:

1. Клонировать репозиторий
2. Перейти в папку проекта "stripe_payment"
3. При необходимости изменения переменных окружения создать .env файл со следующими строками:  
 
 
        "Включить или выключить режим отладки Django"  
        DEBUG = False or True, по умолчанию установлено False

        "Изменить ключ шифрования Django"  
        SECRET_KEY = str, по умолчанию установлен простой ключ только для тестового сервера

        "Изменение API key для доступа к stripe"  
        STRIPE_API_KEY = str, по умолчанию установлен тестовый апи ключ


4. Создать Docker образ из докер файла  

    
        sudo docker build -t pay .

5. Запустить контейнер  


        sudo docker run --name pay -p 8000:8000 pay  

Сайт будет доступен на локалхосте http://localhost:8000/  
Будут загружены фикстуры в базу данных с несколькими записями для удобства тестирования

### Структура сайта:
На стартовой странице находится список товаров со ссылками на индивидуальную страницу товара `http://localhost:8000/item/<id>/`.  
По кнопке "Купить" происходит редирект на адрес `http://localhost:8000/buy/<id>/` и инициируется сессия оплаты stripe.  
На странице `http://localhost:8000/order/` возможно создать заказ из нескольких товаров, выбрать налог и скидку, и инициировать оплату.
