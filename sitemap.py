import os
from lxml import etree

def generate_sitemap(root_dir, base_url):
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

if __name__ == "__main__":
    root_directory = "path/to/your/static/website"  # Change this to your website's root directory
    root_directory='../100websites/mini-games'
    base_url = "https://minigames.silkandpepper.com"  # Change this to your website's base URL
    # root_directory='../100websites/Slope-Game-1'
    # base_url='https://slope-unblocked-games.silkandpepper.com'
    # root_directory='../100websites/coolmathsgames'
    # base_url='https://coolmathsgames.silkandpepper.com'

    sitemap = generate_sitemap(root_directory, base_url)
    
    # Save the sitemap to a file
    with open(root_directory+"/sitemap.xml", "wb") as f:
        f.write(sitemap)
    
    print("Sitemap generated successfully!")
