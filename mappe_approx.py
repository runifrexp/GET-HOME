import folium
from folium import LayerControl

# Crea una mappa centrata a Treviso
mappa = folium.Map(location=[45.6669, 12.242], zoom_start=12)

# Aggiungi i luoghi delle feste
feste = [
    {"nome": "Festa a Cavriè", "coordinate": [45.70111, 12.36806], "descrizione": "Una serata con DJ e drink", "colore": "red"},
    {"nome": "Festa a Istrana", "coordinate": [45.6708, 12.1089], "descrizione": "Musica dal vivo e buffet", "colore": "blue"},
    {"nome": "Festa a Santa Maria del Rovere", "coordinate": [45.6913, 12.2447], "descrizione": "Festa in piazza con luci e balli", "colore": "green"}
]

# Funzione per aggiungere cerchi rappresentanti le fasce di distanza
def aggiungi_fasce(mappa, nome_festa, coordinate, colore):
    # Prima fascia: 0-10 km
    layer_0_10 = folium.FeatureGroup(name=f"{nome_festa} - Fascia 0-10 km")
    folium.Circle(
        location=coordinate,
        radius=10000,  # Raggio in metri
        color=colore,
        fill=True,
        fill_color=colore,
        fill_opacity=0.3
    ).add_to(layer_0_10)
    layer_0_10.add_to(mappa)

    # Seconda fascia: 10-17 km
    layer_10_17 = folium.FeatureGroup(name=f"{nome_festa} - Fascia 10-17 km")
    folium.Circle(
        location=coordinate,
        radius=17000,
        color=colore,
        fill=True,
        fill_color=colore,
        fill_opacity=0.2
    ).add_to(layer_10_17)
    layer_10_17.add_to(mappa)

    # Terza fascia: 17-25 km
    layer_17_25 = folium.FeatureGroup(name=f"{nome_festa} - Fascia 17-25 km")
    folium.Circle(
        location=coordinate,
        radius=25000,
        color=colore,
        fill=True,
        fill_color=colore,
        fill_opacity=0.1
    ).add_to(layer_17_25)
    layer_17_25.add_to(mappa)

# Aggiungi i marker e le fasce sulla mappa
for festa in feste:
    layer_marker = folium.FeatureGroup(name=f"{festa['nome']} - Marker")
    folium.Marker(
        location=festa["coordinate"],
        popup=f"<b>{festa['nome']}</b><br>{festa['descrizione']}",
        tooltip=festa["nome"],
        icon=folium.Icon(color=festa["colore"], icon="info-sign")
    ).add_to(layer_marker)
    layer_marker.add_to(mappa)
    aggiungi_fasce(mappa, festa["nome"], festa["coordinate"], festa["colore"])

# Aggiungi il controllo dei layer
LayerControl().add_to(mappa)

# Salva la mappa come file HTML
mappa.save("mappa_feste_interattiva.html")

print("Mappa salvata come 'mappa_feste_interattiva.html'. Aprila con un browser per visualizzarla!")
