
def check_password(password):
	if len(password) >= 8:
		print('Your pass is strong')
	else:
		print('your pass needs more')

check_password('12345678')