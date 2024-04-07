## ИСС по искусству

### Запуск в докере:
1) создать .env файл

```shell
chmod +x scripts/entrypoint.sh
```

```shell
docker-compose -f docker/docker-compose.yaml up
```

Если при повторной сборке neo4j жалуется на `neo4j_db/import`:
```shell
sudo chmod -R 755 ./neo4j_db/import
```

Neo4j remote interface available at `http://localhost:7474/`

Логин/пароль по умолчанию : neo4j/password