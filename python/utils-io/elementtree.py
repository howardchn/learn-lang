from xml.etree import ElementTree
from os import path
import os

def load_csproj(source_path):
    root = ElementTree.parse(source_path)
    root = root.getroot()
    namespace = {'ns':'{http://schemas.microsoft.com/developer/msbuild/2003}'}

    property_group_outputs = root.findall('%(ns)sPropertyGroup/%(ns)sOutputPath' % namespace) 
    for output in property_group_outputs:
        print(output)

def find_relpath(source_path, target_basename, debug = True):
    rel_path = ''
    source_path = path.dirname(source_path)
    while not path.basename(source_path) == target_basename:
        source_path = path.dirname(source_path)
        rel_path = rel_path + '..\\'

    target_path = path.join(rel_path, 'MapSuiteGisEditor\MapSuiteGisEditor\MapSuiteGisEditor\bin', debug and 'debug' or 'release')
    print(target_path)

source_path = r"E:\ThinkGeo\MapSuite\MapSuite\Layers\AdornmentLayers\AdornmentLayers-Windows\AdornmentLayersForGisEditor-Windows.csproj"
# load_csproj(path)
find_relpath(source_path, 'ThinkGeo')
    