<<<<<<< HEAD
import geocoder
import folium
import socket

def get_loc(url, path, file):
    ip = socket.gethostbyname(url)
    
    g = geocoder.ip(ip)
    myaddress = g.latlng

    myMap = folium.Map(location=myaddress, zoom_start=12)
    folium.Marker(myaddress, popup="My Location").add_to(myMap)
    folium.CircleMarker(myaddress, radius=50, color='red', fill_color='red').add_to(myMap)

    myMap.save(path+file+".html")
    return f'Latitude: {myaddress[0]} Longitude: {myaddress[1]}\nLocation saved to {path+file}.html'


if __name__ == "__main__":
    url = input("Enter a url: ")
=======
import geocoder
import folium
import socket

def get_loc(url, path, file):
    ip = socket.gethostbyname(url)
    
    g = geocoder.ip(ip)
    myaddress = g.latlng

    myMap = folium.Map(location=myaddress, zoom_start=12)
    folium.Marker(myaddress, popup="My Location").add_to(myMap)
    folium.CircleMarker(myaddress, radius=50, color='red', fill_color='red').add_to(myMap)

    myMap.save(path+file+".html")
    return f'Latitude: {myaddress[0]} Longitude: {myaddress[1]}\nLocation saved to {path+file}.html'


if __name__ == "__main__":
    url = input("Enter a url: ")
>>>>>>> 97e50f3017aeaf17bbac80f8a53421e8c5629711
    print(get_loc(url, "", 'test'))