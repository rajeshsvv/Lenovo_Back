print("import Find Index module......" )

text="Test String"

def find_index(to_search,target):
	"""Find the index of value in the sequence"""
	for i, value in enumerate(to_search):
		if value==target:
			return i

	return -1
