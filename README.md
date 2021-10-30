# What Todo

Create todo lists and select the location of items.
The colour of the items reflects the current weather conditions of the locations. 

(Inititial Django project boilerplate adapted from: [edjchapman/djangoboilerplate](https://github.com/edjchapman/DjangoBoilerplate))

---

# Development

### Build the images and spin up the containers

```shell
docker-compose up
```

### Migrating

```shell
docker-compose exec backend python manage.py migrate --noinput
```

### Postgres shell

```shell
docker-compose exec db psql --username=what_todo --dbname=what_todo_dev
```

---

# Production

```shell
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput
```

---

# Troubleshooting

### DANGER: Remove the volumes along with the containers

```shell
docker-compose down -v
```

### Verify logs

```shell
docker-compose -f docker-compose.prod.yml logs -f
```
