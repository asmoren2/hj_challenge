import json

from flask import Flask, Response, request

from services import github

app = Flask(__name__)


@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    return Response("I'm Alive!!", status=200)


@app.route("/api/v1/fork_repo", methods=['POST'])
def fork_repo():
    res = github.fork_repo('asmoren2', 'hj_challenge')

    if res:
        forked_repo_location = res['full_name']

        return Response(
            json.dumps(
                {'fork_location': forked_repo_location}
            ),
            status=201,
            mimetype='application/json'
        )

    return Response(
        'Unable to fork repository',
        status=424,
        mimetype='application/json'
    )
