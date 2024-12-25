import osmnx as ox
import networkx as nx
import folium

# Funzione per calcolare fasce stradali
def aggiungi_fasce_stradali(mappa, coordinate, colore, nomi_feste):
    # Scarica il grafo stradale intorno al punto
    G = ox.graph_from_point(center_point=coordinate, dist=25000, network_type='drive')

    # Crea fasce di distanza (in metri)
    distanze = [10000, 17000, 25000]
    opacita = [0.3, 0.2, 0.1]

    for distanza, opac in zip(distanze, opacita):
        # Calcola il sottografo entro il raggio
        nodo_centrale = ox.nearest_nodes(G, coordinate[1], coordinate[0])  # Correzione qui
        subgraph = nx.ego_graph(G, nodo_centrale, radius=distanza)

        # Ottieni i confini dell'area
        area = ox.graph_to_gdfs(subgraph, nodes=False, edges=True)
        geo_json = area.unary_union

        # Aggiungi il poligono alla mappa
        folium.GeoJson(
            data=geo_json.__geo_interface__,
            style_function=lambda x: {
                'fillColor': colore,
                'color': colore,
                'fillOpacity': opac,
                'weight': 0,
            },
            popup=f"{nomi_feste}"
        ).add_to(mappa)
