import requests
import tkinter as tk
def Gen_report(city):
    url='https://wttr.in/{}'.format(city)
    try:
        data=requests.get(url)
        T=data.text
    except:
        T="Error Occurred"
    print(T)
root=tk.Tk()
root.title("Simple Weather Forecasting App")
root.geometry("400x200")
input_label=tk.Label(root,text="Enter city:")
input_label.pack()
input_field=tk.Entry(root)
input_field.pack()
submit_button=tk.Button(root, text="Submit", command=lambda: Gen_report(input_field.get()))
submit_button.pack()
weather_label = tk.Label(root, text="")
weather_label.pack()
root.mainloop()