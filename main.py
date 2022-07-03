import requests
from datetime import datetime

MY_LAT = 51.412319
MY_LONG = -0.300440

#function that determines whether there is an ISS overhead within +-5 degrees from long or lat
def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG +5:
        return True

#function that returns if it is currently night time (past sunset and before sunrise)
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    #hour of sunrise and sunset
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <=sunrise:
        return True


if is_overhead() and is_night():
    print("QUICKLY LOOK OUTSIDE!!")

else:
    print("There is nothing to see right now")





