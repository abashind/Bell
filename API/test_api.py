import pytest
import requests


class TestApi:

    @pytest.mark.parametrize('code', [100, 200, 300, 400, 500, 900])
    def test_api_positive(self, code):

        url = f'https://httpbin.org/status/{code}'
        headers = {'accept': 'text/plain'}
        timeout = 10

        try:
            resp = requests.post(url, headers=headers, timeout=timeout)
        except requests.exceptions.ReadTimeout:
            assert False, f"The server didn't respond for too long to the request {url}, more than {timeout}s."
        except requests.exceptions.RequestException:
            assert False, f"Something went wrong with the request {url}."

        expected_code = code
        received_code = resp.status_code
        assert expected_code == received_code, f'Something went wrong with the request {url}, ' \
                                               f'expected {expected_code}, got {received_code}'
