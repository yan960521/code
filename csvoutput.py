from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingOutputNumber,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterRasterDestination,
                       QgsProcessingFeatureSourceDefinition,
                        QgsProject,
                        QgsField,
                        QgsPointXY,
                        QgsVectorLayer,
                        QgsMapLayer,
                        QgsVectorFileWriter
                        )
import processing
import csv
import os


for layer in  QgsProject.instance().mapLayers().values():
    lst=[]
    lst.append(['column_name_1', 'column_name_2'])
    layer_name = layer.name()
    if 'string' in layer_name:
        path  = 'C:/path/%s.csv'%layer_name
        features = []
        for feature in layer.getFeatures():
            filed_1 = feature['column_name_1']
            filed_2 = feature['column_name_2']
            values = [filed_1, filed_2]
            lst.append(values)
        with open(path, 'w', newline='', encoding='utf-8') as outputfile:
            writer = csv.writer(outputfile)
            for i in lst:
                writer.writerows(i)

            
