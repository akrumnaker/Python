# Demo showing off basic functionality of the requests library
# requests Docs: http://docs.python-requests.org/en/master/

# import the third party requests library
import requests

# call the get method from requests in order to obtain a response from the url
response = requests.get('https://en.wikipedia.org/wiki/S100A14')

# prints the status code of the response ie 200 - OK, 404 - Not Found, etc
print(response.status_code)
# prints the header relating to the content type that the page uses
print(response.headers['content-type'])
# prints the encoding that the characters use
print(response.encoding)
# prints the body of the response, the html text that lays out the page
print(response.text)
print(type(response.text))
# print(response.json())