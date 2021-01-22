from tests.all_klass import all_klass

def test_basic():
	assert all(all_klass("sub"))

def test_offset():
	assert all(all_klass("sub", "&o=1"))