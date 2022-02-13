import requests
import hashlib
import sys

def request_API(query_char):
	url = "https://api.pwnedpasswords.com/range/" + query_char
	results = requests.get(url)
	if results.status_code != 200:
		raise RuntimeError(f"Error Feching: {results.status_code}, check the api and try again")
	return results
def get_pass_leaks_count(hash, hash_to_check):
	hash = (line.split(":") for line in hash.text.splitlines())
	for h ,count in hash:
		if h == hash_to_check:
			return count
	return 0

def pwned_api_checker(password):
		sha1pass = hashlib.sha1(password.encode("UTF-8")).hexdigest().upper()
		first_char, remaining_char = sha1pass[:5], sha1pass[5:]
		stored_information = request_API(first_char)
		return get_pass_leaks_count(stored_information, remaining_char)

def main(argvs):
	for password in argvs:
		the_count = pwned_api_checker(password)
		if the_count:
			print(f".... {password} was found {the_count} times,  please change it")
		else:
			print(f".... {password} was not found, carry on!")
main(sys.argv[1:])
