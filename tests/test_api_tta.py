from tests.all_klass import all_klass

def test_basic():
	assert all(all_klass("tta"))

def test_offset():
	assert all(all_klass("tta", "&o=1"))