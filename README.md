# fastapi_shop_example

Команды для выполнения миграций:
alembic init migrations - инициализация alembic \n
alembic revision --autogenerate -m "Initial migration" - создаем первую init миграцию \n
alembic upgrade +2 две версии включая текущую для апгрейда \n
alembic downgrade -1 на предыдущую для даунгрейда \n
alembic current получить информацию о текущей версии \n
alembic history --verbose история миграций, более подробнее можно почитать в документации. \n
alembic downgrade base даунгрейд в самое начало миграций \n
alembic upgrade head применение самой последней созданной миграции \n