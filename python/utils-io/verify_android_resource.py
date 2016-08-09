from utils.ospathex import list_files
from xml.etree import ElementTree
from os import path

ns = '{http://schemas.microsoft.com/developer/msbuild/2003}'

def find_resource(filename):
    tree = ElementTree.parse(filename)
    root = tree.getroot()
    androidResources = root.findall('{ns}ItemGroup/{ns}AndroidResource'.format(ns=ns))
    for r in androidResources:
        include_attr = r.get('Include')
        if include_attr and not include_attr == 'None':
            yield include_attr

dirname = r'E:\ThinkGeo\MapSuite\MapSuite'
files = list_files(dirname, '.csproj')
for file in [f for f in files if str(f).endswith('-Android.csproj')]:
    result = list(find_resource(file))
    if not len(result) == 0:
        print(path.basename(file))
        print(result) 
    
