import pygeoip
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    #region = rec['region_name']
    country = rec['country_name']
    longitude = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt + ' Geo-loacted. '
    print '[+] ' + str(city) + ', ' + str(country) # ', ' + str(region)
    print '[+] Latitude: ' + str(lat) + ', Longitude: ' + str(longitude)
tgt = '125.128.185.20'
printRecord(tgt)
