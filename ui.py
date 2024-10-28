import tkinter as tk
from main import get_weather

def show_weather():
    city = entry.get()  
    weather_info = get_weather(city) 

    if weather_info:
        temperature, humidity, weather_desc = weather_info
        label.config(text=f"{city.capitalize()}\nSıcaklık: {temperature}°C\nNem: {humidity}%\nDurum: {weather_desc}")
    else:
        label.config(text="Hava durumu bulunamadı veya şehir geçersiz.")


root = tk.Tk()
root.title("Hava Durumu Uygulaması")

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Göster", command=show_weather)
button.pack(pady=5)

label = tk.Label(root, text="Write the name of the city where you want to know the weather in English.", font=("Arial", 12))
label.pack(pady=10)

root.mainloop()
