import csv
data = csv.reader(open('mozilla.csv', 'rb'), dialect='excel')
marker_file = open("markers_test.js","a")
testing_teams = ["Akan","Armenian","Kazakh","Kurdish","Luganda","Maithili","Northern Sotho","Oriya","Serbian","Songhai","Tamil","Tamil (Sri Lanka)","Zulu"]
markers=[]
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
            m_name="marker"+id
            markers.insert(0,m_name)
            marker = "var markerll"+id+"=new L.LatLng("+lat+","+lon+");var marker"+id+"=new L.Marker(markerll"+id+",{icon:betaIcon});marker"+id+".bindPopup(\"<b>"+name+"<br></b><a href=\'"+team_page+"\'>L10n Team Page<br><a href=\'"+dashboard+"\'>Dashboard\");"
        else:
            m_name="marker"+id
            markers.insert(0,m_name)
            marker = "var markerll"+id+"=new L.LatLng("+lat+","+lon+");var marker"+id+"=new L.Marker(markerll"+id+",{icon:firefoxIcon});marker"+id+".bindPopup(\"<b>"+name+"<br></b><a href=\'"+team_page+"\'>L10n Team Page<br><a href=\'"+dashboard+"\'>Dashboard\");"
        print marker
        marker_file.write(marker+";")

for marker in markers:
    marker_file.write("l10nLayer.addLayer("+marker+")")
    marker_file.write(";")



