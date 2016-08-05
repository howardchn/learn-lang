from xml.etree import ElementTree
from os import path
from io import open
import os
from utils.ospathex import list_files

def remap_output(csproj_path):
    # ElementTree.register_namespace('xmlns', 'http://schemas.microsoft.com/developer/msbuild/2003')
    tree = ElementTree.parse(csproj_path)
    root = tree.getroot()
    namespace = {'ns':'{http://schemas.microsoft.com/developer/msbuild/2003}'}

    property_groups_els = [elements for elements in root.findall('%(ns)sPropertyGroup'%namespace) if not elements.find('%(ns)sOutputPath' % namespace) == None] 
    for property_group_els in property_groups_els:
        isdebug = 'Debug' in property_group_els.get('Condition')
        output_path_els = property_group_els.find('%(ns)sOutputPath' % namespace)
        source_path = output_path_els.text
        target_path = find_relpath(csproj_path, 'ThinkGeo', isdebug);
        output_path_els.text = target_path

    projectrefs_els = [elements for elements in root.findall('%(ns)sItemGroup/%(ns)sProjectReference'%namespace)]
    for projectref_els in projectrefs_els:
        private_element = projectref_els.find('%(ns)sPrivate'%namespace)
        if private_element == None:
            private_element = ElementTree.Element('%(ns)sPrivate'%namespace)
            projectref_els.append(private_element)
        private_element.text = str(False)

    ElementTree.register_namespace('', 'http://schemas.microsoft.com/developer/msbuild/2003')
    tree.write(csproj_path, xml_declaration=True, encoding='utf-8')
    print('Remap', path.basename(csproj_path), 'completed.')
    

def find_relpath(csproj_path, target_basename, debug = True):
    rel_path = ''
    source_path = path.dirname(csproj_path)
    while not path.basename(source_path) == target_basename:
        source_path = path.dirname(source_path)
        rel_path = rel_path + '..\\'

    target_path = path.join(rel_path, r'MapSuiteGisEditor\MapSuiteGisEditor\MapSuiteGisEditor\bin', debug and 'Debug' or 'Release')
    return target_path

def need_remap(csproj_path):
    return csproj_path.endswith('ForGisEditor-Windows.csproj')

# dirname = r'E:\ThinkGeo\MapSuite\MapSuite'
dirname = r'E:\ThinkGeo\MapSuite\MapSuite'
for csproj_path in list_files(dirname, '.csproj'):
    need_remap = csproj_path.endswith('ForGisEditor-Windows.csproj')
    if need_remap: 
        remap_output(csproj_path)

print('Task complete.')
    