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
        pop_list = pop.split("<br>")
        print "processing "+name
        print pop_list
        team_page = pop_list[1]
        try:
            dashboard = pop_list[4]
        except:
            pass
        if any(name for team in testing_teams if name.startswith(team)):
            print name
            marker = "var markerll"+id+"=new L.LatLng("+lat+","+lon+");var marker"+id+"=new L.Marker(markerll"+id+",{icon:betaIcon});map.addLayer(marker"+id+");marker"+id+".bindPopup(\"<b>"+name+"<br></b><a href=\'"+team_page+"\'>L10n Team Page<br><a href=\'"+dashboard+"\'>Dashboard\");"
        else:
            marker = "var markerll"+id+"=new L.LatLng("+lat+","+lon+");var marker"+id+"=new L.Marker(markerll"+id+",{icon:firefoxIcon});map.addLayer(marker"+id+");marker"+id+".bindPopup(\"<b>"+name+"<br></b><a href=\'"+team_page+"\'>L10n Team Page<br><a href=\'"+dashboard+"\'>Dashboard\");"
        print marker
        marker_file.write(marker)



