import pytest


@pytest.fixture(scope="session")
def user_credential(request):
    return request.param


@pytest.fixture(scope="session")
def get_details(request):
    return request.param
