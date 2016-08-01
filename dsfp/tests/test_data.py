from dsfp.data import get_photometry

def test_get_photometry():
    data = get_photometry(10)
    assert len(data) == 10
