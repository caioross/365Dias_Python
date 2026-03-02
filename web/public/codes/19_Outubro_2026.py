import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def generate_sitemap(directory, output_file='sitemap.xml'):
    """
    Gera um sitemap.xml para um site local.

    Args:
        directory (str): O caminho para o diretório raiz do site local.
        output_file (str): O nome do arquivo sitemap.xml a ser gerado.
    """
    urlset = Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.html', '.htm')):
                url = SubElement(urlset, 'url')
                loc = SubElement(url, 'loc')
                # Assuming the directory structure maps to URLs
                loc.text = os.path.relpath(os.path.join(root, file), directory).replace(os.sep, '/')
                # Add more sitemap elements like lastmod, changefreq, priority if needed

    # Convert the ElementTree to a pretty XML string
    rough_string = tostring(urlset, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml_as_string = reparsed.toprettyxml(indent="  ")

    # Write the pretty XML to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(pretty_xml_as_string)

def main():
    """
    Função principal para executar o script de geração de sitemap.
    """
    site_directory = 'path/to/your/site'  # Replace with your site's directory
    generate_sitemap(site_directory)
    print(f'Sitemap generated successfully in {site_directory}/sitemap.xml')

if __name__ == '__main__':
    main()