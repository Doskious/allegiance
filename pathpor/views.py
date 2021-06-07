import io
import pathlib2 as pathlib
from urllib import unquote_plus
from xml.etree import ElementTree as ET
from zipfile import ZipFile
from django.shortcuts import render


def xml_parser(xml_source, top_tag=None):
    parser = ET.XMLParser(encoding='UTF-8')
    document = ET.iterparse(xml_source, ['start', 'end'], parser)
    _, root = next(document)
    start_tag = None
    for event, element in document:
        if event == 'start' and start_tag is None:
            start_tag = element.tag
        if event == 'end' and element.tag == start_tag:
            if top_tag is None or start_tag == top_tag:
                yield element
            start_tag = None
            root.clear()


def xml_snippet(xml_source, top_tag=None):
    # Expected to be unique
    return XMLSnippet(ET.tostring(next(xml_parser(xml_source, top_tag))))


class XMLSnippet(object):

    def __init__(self, raw_xml):
        self.xml = raw_xml


class Character(XMLSnippet):

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self.element = ET.fromstring(self.xml)
        self.party_enemy = self.element.get(
            "relationship", "neutral") == "enemy"


class Portfolio(object):

    def __init__(self, por_path):
        file_path = pathlib.Path(por_path)
        assert file_path.exists()
        assert file_path.is_file()
        assert file_path.suffix == '.por'
        self.path = file_path
        self.name = file_path.stem
        self.characters = []
        por_filepath = "{}".format(file_path)
        with ZipFile(por_filepath, 'r') as por_file:
            index_data = por_file.read('index.xml').decode("utf-8")
            index_element = ET.fromstring(index_data.encode('UTF-8'))
            program_element = index_element.find('program')
            self.program = XMLSnippet(ET.tostring(program_element))
            xml_chars = [
                zinfo for zinfo in por_file.filelist
                if zinfo.filename.startswith('statblocks_xml/')]
            for char_xml in xml_chars:
                char_data = por_file.read(char_xml.filename).decode("utf-8")
                file_element = ET.fromstring(char_data.encode('UTF-8'))
                char_element = file_element.find('public/character')
                self.characters.append(
                    Character(ET.tostring(char_element)))


# Create your views here.
def por_list(request):
    portfolio_path = '/home/doskious/webapps/allegiance/pathpor/portfolios'
    por_path = pathlib.Path(portfolio_path)
    # assert True is False
    return render(
        request,
        'por_list.html',
        {"available_pors": [
            "{}".format(por.name)
            for por in por_path.glob('*.por')
            if " " not in por.name or request.user.is_authenticated()
        ]},
        content_type="text/html")


def por_view(request, por_file):
    portfolio_path = '/home/doskious/webapps/allegiance/pathpor/portfolios'
    file_name = unquote_plus(por_file)
    por_path = pathlib.Path(pathlib.os.path.join(portfolio_path, file_name))
    return render(
        request,
        'por_render.html',
        {"por": Portfolio(por_path)},
        content_type="text/html")
