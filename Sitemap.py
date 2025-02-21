"""
_Import Essential libs
"""
import json
"""
_Declare & initialize Variables
_JSON_FILE_PATH & SITEMAP_FILE_PATH must include path/filename.ext
_Change YOUR_DOMAIN, YOUR_JSON_FILE_PATH & YOUR_JSON_FILE_PATH based on domain & file paths.
_Change HTML_CONTENTS & HTML_FILE_NAME according to JSON data structure.
"""
DOMAIN =  f'YOUR_DOMAIN'
JSON_FILE_PATH = f'YOUR_JSON_FILE_PATH'
SITEMAP_FILE_PATH = f'YOUR_JSON_FILE_PATH'
URLSET_OPENING = f'<urlset \n'
URLSET_CLOSING = f'</urlset>'
XML = f'<?xml version="1.0" encoding="UTF-8"?>\n'
XMLNS = f'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
XMLNS_XSI = f'mlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
XSI_SCHEMALOCATION = f'xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\nhttp://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n'

"""
_Define XML_URLs that generates URLs from a JSON file.
__The <loc> tag is the most crucial because it directly identifies the content 
__you want indexed by search engines. Ensuring that your sitemap is up-to-date 
__and accurately reflects the structure of your website can significantly 
__enhance your site's visibility and indexation in search engine results. 

_JSON Data value has been set HTML_CONTENTS. Check out sitemap.json.
_JSON Data value array has been set HTML_FILE_NAME. Check out sitemap.json.
"""
def XML_URLS(path):
    urls = ''
    with open(path, 'r') as json_file:
        data = json.load(json_file)

        for value in data["HTML_CONTENTS"]:
            url = f'<url>\n<loc>{DOMAIN}/{value["HTML_FILE_NAME"]}</loc>\n</url>\n' 
            urls = urls + url
        
        json_file.close()
        return urls
        
URLS = XML_URLS(JSON_FILE_PATH)

XML_DOCUMENT = XML + URLSET_OPENING + XMLNS + XMLNS_XSI + XSI_SCHEMALOCATION + URLS + URLSET_CLOSING

SITMAP_FILE = open(SITEMAP_FILE_PATH,'w', encoding = 'utf-8')
SITMAP_FILE.write(XML_DOCUMENT)
