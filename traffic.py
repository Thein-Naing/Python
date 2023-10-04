# Network Traffic Analysis from medium.com

import geoip2.database
reader  = geoip2.database.Reader('GeoLite2-City.mmdb')
response = reader.city('128.101.101.101')
print(response.city.name)


import geoip2.database
reader  = geoip2.database.Reader('GeoLite2-City.mmdb')
response = reader.country('128.101.101.101')
print(response.country.name)


