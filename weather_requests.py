import requests





zipcode=input("enter zip: ")
key="05dc89dd3fd81bfcc393477e92a0e8d7"

r=requests.get("http://samples.openweathermap.org/data/2.5/weather?zip="+zipcode+",us&appid="+key)

jsonFile=open("jsonWeather.txt","w")
jsonFile.write(str(r.json()))

temperature_kelvin=r.json()['main']['temp']
temperature_fahrenheit=float((9/5*(temperature_kelvin-273)+32))

print("This is your temperature in fahrenheit: ",temperature_fahrenheit)

