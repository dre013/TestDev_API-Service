# TestDev_API-Service 

Данный сервис был разаработан в качестве тестового задания при рассмотрении вакансии.

Изначально идет расчет на то, что у вас установлен python > 3.8. Это сделано в целях минимизирования веса собранного контейнера.

После того, как проект скачан, необходимо перейти в директорию проекта (Пример : C:\ ... \TestDev_API-Service\).

1) Перед тем, как собрать докер-образ, необходимо установить необходимые библиотеки с помощью команды:

    `pip install -r requirements.txt`
	или
	  `pip3 install -r requirements.txt` в зависимости от ОС

2) Для построения образа контейнера, необходимо запустить скрипт:

	`docker-compose build`

3) Для поднятия контейнера в фоновом режиме, необходимо запустить скрипт:

	`docker-compose up -d`

4) Для запуска локального сервера с портом 80 (если занят, то любой другой свободный), необходимо запустить скрипт:

	`uvicorn app.main:app --reload --port 80`
	
	Сервер запущен, можем переходить на `localhost:80/docs`

5) Перед нами появляется сам веб-сервис с шестью функциями:
	
	-POST - создание записей в базе данных, с помощью сервиса https://jservice.io/api/random?count=1
	-GET - получить все записи из БД
	-GET - получить запись из БД по ID
	-PUT - обновление существующих записей по ID
	-DELETE - удаление записи по ID
	-DELETE - удаление всех записей из БД, соответственно.

	Пример запроса POST представлен ниже:

  ![Снимок экрана 2023-10-20 233852](https://github.com/dre013/TestDev_API-Service/assets/129860279/75850e99-81d6-40e6-8a13-c11268cdabda)

  Ответ сервера представлен далее:
  
  ![Снимок экрана 2023-10-20 233908](https://github.com/dre013/TestDev_API-Service/assets/129860279/16f25d40-48a4-446f-8fe6-40468c3555bc)


  Для создания запроса POST-запроса необходимо нажать `POST->Try it out->Выбрать значение в {question_num}->Execute`
	С остальными функциями по аналогии.

6) Для остановки работы локального сервера, необходимо вернуться в терминал, где его запускали и нажать комбинацию `Ctrl+C`

7) Для остановки работы контейнера, необходимо запустить скрипт:

	`docker-compose down`


Как удалить контейнер и образ можно узнать здесь https://docs.docker.com

