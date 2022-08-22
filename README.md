# HR Bot Factory Test

This project is a simple FastAPI REST service for managing messages.

## Test

The following subsections state the original test problem (in spanish).

### Descripción

La prueba consta del diseño de BD y un API básica para resolver una necesidad concreta de un
sistema de chatbots. Con esta prueba queremos evaluar cómo se resolvería uno de los tipicos
“problemas” a la hora de crear un sistema de este tipo, donde evaluaremos el conocimiento y
las habilidades como analista y desarrollador.
Suponiendo que queremos implementar una aplicación de chatbots, donde además de texto
plano, nuestro sistema puede enviar otro tipo de mensajes, como carruseles, imágenes, y
botones. Nuestra herramienta es un configurador de conversaciones donde pintamos los
caminos que tiene la conversación conectados entre ellos con una condición (if/else) que nos
hará decidir por qué camino sigue la conversación.

### Objetivos

Se solicita el diseño de BD para cubrir esta necesidad únicamente (no todo el sistema) y el API
CRUD necesaria para crear “mensajes” y “caminos” en la conversación

1. Diseño de BD: Tenemos que crear las entidades necesarias para almacenar mensjaes, y
   la entidad camino que relaciona el mensaje de origen y de destino. Estos caminos
   además tendrán un campo “condición” que nos indica si puede cruzar ese camino o no.
   Los mensajes pueden ser de varios tipos, y contendran información diferente
   dependiendo del tipo que sean. A continuación detallamos los campos por tipo:

    1. Mensaje de texto: respuesta, imagen (optional)

    2. Mensaje de botones: respuesta, imagen (optional), lista de botones (cada botón
       tiene: texto y valor)

    3. Mensaje carrusel: respuesta, lista de tarjetas (cada tarjeta tiene: imagen, texto,
       lista de botones con texto y valor cada botón)

2. API CRUD: Crear el CRUD básico para crear mensajes y caminos entre dos mensajes.

## Repo

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit" style="max-width:100%;"></a>
</p>

This project was written with Python 3.10, using FastAPI, SQLAlchemy and psycopg2.

### File Structure

This project's file structure is a simplified, back-end-only spin on
[Tiangolo's Full Stack Fastapi Postgres base project](https://github.com/tiangolo/full-stack-fastapi-postgresql)
that uses [Pipenv](https://pypi.org/project/pipenv/) instead of
[Poetry](https://pypi.org/project/poetry/) for dependency management.

### Running the project

For running either the tests or the development server, the project expects a `.env`
file in its root containing the following variables:

```env
DOMAIN=localhost
SERVER_NAME=$DOMAIN
SERVER_HOST=https://${DOMAIN}

PROJECT_NAME=hr-bot-factory

# Postgres
POSTGRES_SERVER=127.0.0.1
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=hr-bot-factory
```

You are able (and encouraged) to change their values.

#### Dependency installation

Install Pipenv if you haven't already. You should probably follow their instructions,
but it can be as easy as:

```shell
$ pip install pipenv
```

Then install the project's dependencies:

```shell
$ pipenv install
```

#### Running the tests

Activate the virtual environment by running `pipenv shell` and then run the following
command from the root of the project:

```shell
$ pytest .
```

#### Running the development server

As for testing, start by activating the virtual environment and then run the following
command from the root of the project:

```shell
$ uvicorn app.main:app --reload
```
