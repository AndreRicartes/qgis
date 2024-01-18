import os
from qgis.core import QgsProject, QgsRasterLayer, QgsVectorLayer, QgsSimpleLineSymbolLayer, QgsFillSymbol, QgsSingleSymbolRenderer
from qgis.utils import iface

# Get the path to the image layer
image_path_bing = os.path.join(os.path.dirname(__file__), "C:/base_catografica/qgis/referencias/frmt_wms_virtualearth.xml")
image_path_google = os.path.join(os.path.dirname(__file__), "C:/base_catografica/qgis/referencias/frmt_wms_googlemaps_tms.xml")

# Get the path to the fusos layer
vector_path_fusos_features = os.path.join(os.path.dirname(__file__), "C:/base_catografica/qgis/referencias/UTMWorldZone_features.shp")
vector_path_fusos_labels = os.path.join(os.path.dirname(__file__), "C:/base_catografica/qgis/referencias/UTMWorldZone_labels.shp")

# Get the path to WFS for ceitificações INCRA

uri = "http://acervofundiario.incra.gov.br/i3geo/ogc.php?tema=certificada_sigef_particular_ms&service=WFS&version=1.0.0&request=GetFeature"

# Create a raster layer from the path
bingImg = QgsRasterLayer(image_path_bing, "Imagem Bing")
googleImg = QgsRasterLayer(image_path_google, "Imagem Google")
utmGrade = QgsVectorLayer(vector_path_fusos_features, "Grade UTM", "ogr")
fusos = QgsVectorLayer(vector_path_fusos_labels, "Fuso", "ogr")
#incra = QgsRasterLayer(uri, "my wfs layer", "WFS")


# Obtendo a camada atual
#layerIncra = iface.activeLayer(utmGrade)

# Criando um novo símbolo de linha
line_symbol = QgsSimpleLineSymbolLayer()
line_symbol.setWidth(0.96)  # Definindo a largura da linha para 0,96
line_symbol.setColor(QColor(255, 0, 0))  # Definindo a cor da linha para vermelho

# Criando um novo símbolo de preenchimento
fill_symbol = QgsFillSymbol()
fill_symbol.changeSymbolLayer(0, line_symbol)
fill_symbol.setColor(QColor(0, 0, 0, 0))  # Definindo a cor de preenchimento para transparente

# Criando um renderizador de símbolo único
renderer = QgsSingleSymbolRenderer(fill_symbol)

# Aplicando o renderizador à camada
#layerIncra.setRenderer(renderer)

# Atualizando a camada
#layerIncra.triggerRepaint()




# Get the group
root = QgsProject.instance().layerTreeRoot()
group_name = "Base Cartográfica"
group = root.findGroup(group_name)

if group is None:
    # Create the group
    group = root.addGroup(group_name)

# Add the layer to the group
group.addLayer(fusos)
#group.addLayer(incra)
group.addLayer(utmGrade)
group.addLayer(bingImg)
group.addLayer(googleImg)

