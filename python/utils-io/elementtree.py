from xml.etree import ElementTree
from os import path
from io import open

def load_csproj(csproj_path):
    # ElementTree.register_namespace('xmlns', 'http://schemas.microsoft.com/developer/msbuild/2003')
    tree = ElementTree.parse(csproj_path)
    root = tree.getroot()
    namespace = {'ns':'{http://schemas.microsoft.com/developer/msbuild/2003}'}

    property_groups_els = [elements for elements in root.findall('%(ns)sPropertyGroup' % namespace) if not elements.find('%(ns)sOutputPath' % namespace) == None] 
    for property_group_els in property_groups_els:
        isdebug = 'Debug' in property_group_els.get('Condition')
        output_path_els = property_group_els.find('%(ns)sOutputPath' % namespace)
        source_path = output_path_els.text
        target_path = find_relpath(csproj_path, 'ThinkGeo', isdebug);

        output_path_els.text = target_path
        tree.write(csproj_path)

def find_relpath(csproj_path, target_basename, debug = True):
    rel_path = ''
    source_path = path.dirname(csproj_path)
    while not path.basename(source_path) == target_basename:
        source_path = path.dirname(source_path)
        rel_path = rel_path + '..\\'

    target_path = path.join(rel_path, r'MapSuiteGisEditor\MapSuiteGisEditor\MapSuiteGisEditor\bin', debug and 'debug' or 'release')
    return target_path

source_path = r'E:\ThinkGeo\MapSuite\MapSuite\Layers\Background\Background-Windows\BackgroundForGisEditor-Windows.csproj'
load_csproj(source_path)
print('task complete.')
    