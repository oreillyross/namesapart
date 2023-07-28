from namesapart.utils import name_helper

def test_two_names():
  assert name_helper.split_name("John Doodle") == ["John", "Doodle"]

def test_middle_name():
  assert name_helper.split_name("John Patrick Smith") == ["John Patrick", "Smith"]
  assert name_helper.split_name("Bill Bob Jimmy Smith") == ["Bill Bob Jimmy", "Smith"]

def test_lastname():
  assert name_helper.split_name("Smith") == ["", "Smith"]
  
def test_no_name():
  assert name_helper.split_name(" ") == ["", ""]