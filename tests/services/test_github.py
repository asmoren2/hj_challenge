import requests_mock

from services.github import fork_repo


def test_200_success_from_github(caplog):
    with requests_mock.Mocker() as m:
        expected_response = {'full_name': 'owner/repo'}
        m.post(
            'https://api.github.com/repos/owner/repo/forks',
            json={'full_name': 'owner/repo'},
            status_code=202,
        )

        response = fork_repo('owner', 'repo')

        assert 'Repo was forked' in caplog.text
        assert response == expected_response


def test_error_from_github(caplog):
    with requests_mock.Mocker() as m:
        m.post(
            'https://api.github.com/repos/owner/repo/forks',
            status_code=403,
        )

        response = fork_repo('owner', 'repo')

        assert 'Failed to fork repo' in caplog.text
        assert response is None
