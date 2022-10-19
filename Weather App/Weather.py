from tkinter import *
from unicodedata import category
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Weather App')
root.iconbitmap('Weather App/Pictures/Clouds.ico')
root.geometry('400x100')


def zipLookup():
    try:
        apiRequest = requests.get(
            f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip.get()}&distance=5&API_KEY=44E50F75-AC9C-4423-B7EF-813B4DBCF67F')
        api = json.loads(apiRequest.content)

        city = api[0]['ReportingArea']
        aqiNum = api[0]['AQI']
        aqiCategoryName = api[0]['Category']['Name']

        if aqiCategoryName == "Good":
            weather_color = "green"
        elif aqiCategoryName == "Moderate":
            weather_color = "yellow"
        elif aqiCategoryName == "Unhealthy for Sensitive Groups":
            weather_color = "orange"
        elif aqiCategoryName == "Unhealthy":
            weather_color = "red"
        elif aqiCategoryName == 'Very Unhealthy':
            weather_color = 'purple'
        elif aqiCategoryName == 'Hazardous':
            weather_color = 'black'

        root.configure(bg=weather_color)
        myLabel = Label(
            root, text=f"{city}: {aqiNum}-{aqiCategoryName}", font=('Helvetica', 20), fg='White', bg=weather_color)
        myLabel.grid(row=0, column=0, columnspan=2, padx=20)
    except Exception as e:
        api = "Error"


zip = Entry(root)
zip.grid(row=1, column=0, padx=10)

zipButton = Button(root, text='Lookup Zipcode', command=zipLookup, pady=10)
zipButton.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
