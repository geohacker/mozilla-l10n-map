import csv
data = csv.reader(open('mozilla.csv', 'rb'), dialect='excel')
marker_file = open("markers.js","a")

iter =0
for row in data:
    iter += 1
    if iter >= 2:
        id = row[8]
        lat = row[2]
        lon = row[3]
        name = row[0]
        pop = row[1]
        marker = "var markerll"+id+"=new L.LatLng("+lat+","+lon+");var marker"+id+"=new L.Marker(markerll"+id+");map.addLayer(marker"+id+");marker"+id+".bindPopup('"+name+pop+"');"
        print marker
        marker_file.write(marker)



