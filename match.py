import httplib, urllib

host = 'www.host.com'
url = '/api/v1/'

values = {
  'hash' : '00EA4A'
}

headers = {
    'Cookie': 'device_view=full',
    'Content-Type': 'application/json',
    'User-Agent': 'HappyCaps/20 CFNetwork/808.0.2 Darwin/16.0.0',
    'Connection': 'close',
    'Accept': 'application/json',
}

values = urllib.urlencode(values)

conn = httplib.HTTPSConnection(host)
conn.request("POST", url, values, headers)
response = conn.getresponse()

data = response.read()

print 'Response: ', response.status, response.reason
print 'Data:'
print data
