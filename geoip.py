import tkinter as tk
import tkinter.filedialog
import geoip2.database

window = tk.Tk()

ip_label = tk.Label(window, text="IP address:")
ip_label.pack()

ip_entry = tk.Entry(window)
ip_entry.pack()

db_label = tk.Label(window, text="GeoIP2 database path:")
db_label.pack()

db_entry = tk.Entry(window)
db_entry.pack()

def browse_file():
    file_path = tk.filedialog.askopenfilename(filetypes=[("GeoIP2 Database", "*.mmdb")])
    db_entry.delete(0, tk.END)
    db_entry.insert(0, file_path)

browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

results_label = tk.Label(window, text="")
results_label.pack()

def geolocate_ip():
    ip_address = ip_entry.get()
    db_path = db_entry.get()
    try:
        reader = geoip2.database.Reader(db_path)
        response = reader.city(ip_address)
        results_label.config(text=f"City: {response.city.name}\nCountry: {response.country.name}")
    except geoip2.errors.GeoIP2Error as e:
        results_label.config(text=f"Error: {str(e)}")

geolocate_button = tk.Button(window, text="Geolocate", command=geolocate_ip)
geolocate_button.pack()

window.mainloop()
