## ИСС по искусству

### Для разработки
1) 
```shell
pip3 install pre-commit
```
2) 
```shell 
pre-commit install
```


### Запуск в докере:
1) создать .env файл

```shell
chmod +x scripts/entrypoint.sh
```

```shell
docker-compose -f docker/docker-compose_win.yaml up
```

Если при повторной сборке neo4j жалуется на `neo4j_db/import`:
```shell
sudo chmod -R 755 ./neo4j_db/import
```

Neo4j remote interface available at `http://localhost:7474/`

Логин/пароль по умолчанию : neo4j/password