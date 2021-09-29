import csv
import os
from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingOutputNumber,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterRasterDestination,
                        QgsProject,
                        QgsField,
                        QgsPointXY,
                        QgsVectorLayer
                        )
import processing
# 將已開啟的layer轉成變數
layer = QgsProject.instance().mapLayersByName('layer_name')[0] # laye_name放圖層名稱
for i in layer.getFeatures():
    variable = i['column_name'] # 放欄位名稱
    layer.selectByExpression('"column_name"=\'%s\'' %variable)
    output_layer = QgsVectorFileWriter.writeAsVectorFormat(layer, 'c:/path/file.shp' %variable, "utf-8", layer.crs(), "ESRI Shapefile", onlySelected=True) # output選取的features


