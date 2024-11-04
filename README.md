# fastapi_shop_example

Команды для выполнения миграций:
### alembic init migrations - инициализация alembic
### alembic revision --autogenerate -m "Initial migration" - создаем первую init миграцию
### alembic upgrade +2 две версии включая текущую для апгрейда
### alembic downgrade -1 на предыдущую для даунгрейда
### alembic current получить информацию о текущей версии
### alembic history --verbose история миграций, более подробнее можно почитать в документации.
### alembic downgrade base даунгрейд в самое начало миграций
### alembic upgrade head применение самой последней созданной миграции