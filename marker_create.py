import csv
data = csv.reader(open('mozilla.csv', 'rb'), dialect='excel')
marker_file = open("markers_test.js","a")
testing_teams = ["Akan","Armenian","Kazakh","Kurdish","Luganda","Maithili","Northern Sotho","Oriya","Serbian","Songhai","Tamil","Tamil (Sri Lanka)","Zulu"]

iter =0
for row in data:
    iter += 1
    if iter >= 2:
        id = row[8]
        lat = row[2]
        lon = row[3]
        name = row[0]
        pop = row[1]
        if any(name for team in testing_teams if name.startswith(team)):
            print name
            marker = "var markerll"+id+"=new L.LatLng("+lat+","+lon+");var marker"+id+"=new L.CircleMarker(markerll"+id+");map.addLayer(marker"+id+");marker"+id+".bindPopup('"+name+pop+"');"
        else:
            marker = "var markerll"+id+"=new L.LatLng("+lat+","+lon+");var marker"+id+"=new L.Marker(markerll"+id+");map.addLayer(marker"+id+");marker"+id+".bindPopup('"+name+pop+"');"
        #print marker
        marker_file.write(marker)



