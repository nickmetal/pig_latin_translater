## English-to-Pig-Latin translator

REST Web server to translate english phrases to pig latin.

#### Dialects

| dialect | input text | output    |
|---------|------------|-----------|
| yay     | hello      | ello-hyay |
| way     | hello      | ello-hway |
| ay      | hello      | ello-hay  |

### Install dependencies

1. Install `cmake` utility.
2. Python 3.6+ to run project locally.
3. Install `docker` to run server in container.


### Build and Run web server in Docker

```sh
$ make build
$ make run
```

### Run web server locally

```sh
$ make install
$ make run_locally
$ curl http://localhost:8000/translation/eng_to_pig_latin?text=hell&dialect=ay
{"translated_text": "ell-hay"}
```
