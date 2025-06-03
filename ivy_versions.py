import xml.etree.ElementTree as ET

SHARED_LIBRARIES = [
    "Util",
    "common",
    "occupancy",
    "fire-rating",
    "csm",
    "rating",
    "compose-print"
]

def get_lib_versions(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    versions = {}
    for dep in root.findall(".//dependency"):
        name = dep.attrib.get('name')
        rev = dep.attrib.get('rev')
        if name in SHARED_LIBRARIES:
            versions[name] = rev
    return versions

if __name__ == "__main__":
    versions = get_lib_versions('ivy.xml')
    for lib, v in versions.items():
        print(f"{lib}: {v}")
