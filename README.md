### Github Forking Tool

## Installing
1. Ensure pipenv is installed
2. Run pipenv install with the following command.
```bash
$ pipenv install
``` 

## Running Tests
Within the pipenv environment run the command below to run tests.

```bash
$ pytest tests/
```

## Running application locally
1. Export your Github Personal Access Token.
```bash
export GITHUB_TOKEN=<TOKEN>
```
2. Within the pipenv environment you can run the command below to start server.
```bash
$ flask run
```
3. Request the API fork endpoint.

   `[POST] /api/v1/fork_repo`
   