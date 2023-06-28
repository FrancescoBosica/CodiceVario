import xml.etree.ElementTree as ET
data = '<person><name>Francesco</name><phone type="intl">369874512</phone><email hide="yes" /></person>'
tree = ET.fromstring(data)
print("nome:",tree.find('name').text)
print("Attr:",tree.find('email').get('hide'))