


import numpy as np
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_user_agent")
CityCenterListData=['Electronic City,Bangalore',
                    'BTM Layout,Bangalore',
                    'Rajajinagar, Bengaluru, Karnataka',
                    'Brookefield, Bengaluru, Karnataka',
                    'Kengeri, Bengaluru, Karnataka 560060',
                    'Kumaraswamy Layout, Bengaluru, Karnataka 560078',
                    'Bellandur, Bengaluru, Karnataka'
                    ]
LatitudeList=[]
LongitudeList=[]
i=0
for address in CityCenterListData:
        loc = geolocator.geocode(address)
        LatitudeList.append(loc.latitude)
        LongitudeList.append(loc.longitude)
        print(address+" "+"latitude is :-" ,LatitudeList[i],"\nlongtitude is:-" ,LongitudeList[i])
        i=i+1


# from [https://ipython-books.github.io/147-creating-a-route-planner-for-a-road-network/]

# from [https://stackoverflow.com/a/8859667/1595060](https://stackoverflow.com/a/8859667/1595060)
EARTH_R = 6372.8

def geocalc(lat0, lon0, lat1, lon1):
    """Return the distance (in km) between two points
    in geographical coordinates."""
    lat0 = np.radians(lat0)
    lon0 = np.radians(lon0)
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    dlon = lon0 - lon1
    y = np.sqrt((np.cos(lat1) * np.sin(dlon)) ** 2 +
        (np.cos(lat0) * np.sin(lat1) - np.sin(lat0) *
         np.cos(lat1) * np.cos(dlon)) ** 2)
    x = np.sin(lat0) * np.sin(lat1) + \
        np.cos(lat0) * np.cos(lat1) * np.cos(dlon)
    c = np.arctan2(y, x)
    return EARTH_R * c



geocalc(LatitudeList[0],LongitudeList[0],LatitudeList[1],LongitudeList[1])