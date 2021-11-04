# Weather Tasks

Add tasks and select the location.
The colour of the items reflects the current weather conditions of the locations. 

(Inititial Django project boilerplate adapted from: [edjchapman/djangoboilerplate](https://github.com/edjchapman/DjangoBoilerplate))

---

# Development

Add Open Weather Map API key to the `.env.dev` file
```shell
OPEN_WEATHER_API_KEY=
```

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
docker-compose exec db psql --username=weather_tasks --dbname=weather_tasks_dev
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
