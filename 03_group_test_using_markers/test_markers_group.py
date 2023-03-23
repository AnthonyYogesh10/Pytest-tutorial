import pytest

pytstmark = pytest.mark.yogesh
@pytest.mark.yogesh
def test_login():
    print("login works")


def test_home():
    print("Home works")


@pytest.mark.yogesh
def test_search():
    print("Home works")

# for custom markers just add the marker_name after the @pytest.mark.
# example @pytest.mark.yogesh here yogesh is the custom marker
