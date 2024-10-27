import os
from lxml import etree

def generate_sitemap_old(root_dir, base_url):
    # Create a root element for the XML
    urlset = etree.Element("urlset", nsmap={None: "http://www.sitemaps.org/schemas/sitemap-image/0.9"})
    
    # Traverse the directory
    for dirpath, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                # Construct the URL
                file_path = os.path.join(dirpath, file)
                # Convert to a relative URL
                relative_path = os.path.relpath(file_path, root_dir)
                url = os.path.join(base_url, relative_path).replace(os.sep, '/')
                
                # Create a URL element
                url_element = etree.SubElement(urlset, "url")
                loc = etree.SubElement(url_element, "loc")
                loc.text = url
                
                # Optionally add lastmod, changefreq, priority
                lastmod = etree.SubElement(url_element, "lastmod")

                lastmod.text = "2024-10-25"  # Example date
                # changefreq = etree.SubElement(url_element, "changefreq")
                # changefreq.text = "monthly"
                # priority = etree.SubElement(url_element, "priority")
                # priority.text = "0.5"
                
    # Convert the tree to a string
    xml_str = etree.tostring(urlset, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    return xml_str

def generate_sitemap(root_dir, base_url):
    # Create root element with namespaces and schema location
    urlset = etree.Element(
        "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset",
        nsmap={
            None: "http://www.sitemaps.org/schemas/sitemap/0.9",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance"
        }
    )
    urlset.set(
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
        "http://www.sitemaps.org/schemas/sitemap/0.9 "
        "http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    )

    # Traverse the directory
    for dirpath, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                # Construct the URL
                file_path = os.path.join(dirpath, file)
                relative_path = os.path.relpath(file_path, root_dir)
                url = os.path.join(base_url, relative_path).replace(os.sep, '/')

                # Create a URL element
                url_element = etree.SubElement(urlset, "{http://www.sitemaps.org/schemas/sitemap/0.9}url")
                loc = etree.SubElement(url_element, "{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
                loc.text = url

                # Optionally add lastmod, changefreq, priority
                lastmod = etree.SubElement(url_element, "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")
                lastmod.text = "2024-10-25"  # Example date
                
                # Uncomment to add changefreq and priority
                # changefreq = etree.SubElement(url_element, "{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq")
                # changefreq.text = "monthly"
                # priority = etree.SubElement(url_element, "{http://www.sitemaps.org/schemas/sitemap/0.9}priority")
                # priority.text = "0.5"

    # Convert the tree to a string
    xml_str = etree.tostring(urlset, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    return xml_str
def savelinks(root_dir,base_url):

    output_file = 'sitemap-links.txt'


# List to store found links
    found_links = []

# Walk through the folder and find HTML files
    for dirpath, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(dirpath, file)
                relative_path = os.path.relpath(file_path, root_dir)

                # Find all matching links
                url = os.path.join(base_url, relative_path).replace(os.sep, '/')

                url=url.replace('.html','')
                found_links.append(url)

# Write the links to a text file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for link in list(set(found_links)):
            out_file.write(link + '\n')

        print(f'Found {len(found_links)} links and saved to {output_file}.')

if __name__ == "__main__":
    root_directory = "path/to/your/static/website"  # Change this to your website's root directory
    root_directory='../100websites/mini-games'
    base_url = "https://minigames.silkandpepper.com"  # Change this to your website's base URL
    root_directory='../100websites/Slope-Game-1'
    base_url='https://slope-unblocked-games.silkandpepper.com'
    root_directory='../100websites/coolmathsgames'
    base_url='https://coolmathsgames.silkandpepper.com'

    
    root_directory='../100websites/fafgamesunblocked'
    base_url='https://onlineunblockedgames.silkandpepper.com'
# 
    # root_directory='../100websites/papasgamesx.github.io'
# 
    # base_url='https://papasgames.silkandpepper.com'



    # sitemap = generate_sitemap(root_directory, base_url)
    
    # Save the sitemap to a file
    # with open(root_directory+"/sitemap.xml", "wb") as f:
        # f.write(sitemap)
    
    # print("Sitemap generated successfully!")

    savelinks(root_directory,base_url)
