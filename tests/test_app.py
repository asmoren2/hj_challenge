from app import app
from pytest_mock import MockFixture


def test_healthcheck():
    with app.test_client() as test_client:
        response = test_client.get('/healthcheck')
        assert response.get_data(as_text=True) == "I'm Alive!!"
        assert response.status_code == 200


def test_fork_success(mocker: MockFixture):
    mocker.patch('services.github.fork_repo', return_value={'full_name': 'asmoren2/hj_challenge'})

    with app.test_client() as test_client:
        response = test_client.post('/api/v1/fork_repo')

        assert response.status_code == 201
        assert 'asmoren2/hj_challenge' in response.get_data(as_text=True)


def test_fork_failure(mocker: MockFixture):
    mocker.patch('services.github.fork_repo', return_value=None)

    with app.test_client() as test_client:
        response = test_client.post('/api/v1/fork_repo')
        assert response.status_code == 424
        assert response.get_data(as_text=True) == 'Unable to fork repository'
