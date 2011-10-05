import logging
logger = logging.getLogger('collective.flowplayer.metadata_extraction')

from hachoir_parser.guess import createParser, guessParser
from hachoir_metadata.metadata import extractMetadata
from hachoir_core.error import HachoirError
from hachoir_core.stream import InputStreamError, InputIOStream

def make_unicode(string):
    if not isinstance(string, unicode):
        string = string.decode('utf-8')
    return string

def parse_raw(raw):
    stream = InputIOStream(raw)
    parser = guessParser(stream)
    return extract_metadata(parser)

def parse_file(filename):
    filename = make_unicode(filename)
    try:
        parser = createParser(filename)
    except InputStreamError, err:
        logger.error("stream error! %s\n" % unicode(err))
        return None
    return extract_metadata(parser)

def extract_metadata(parser):
    if not parser:
        logger.error("Unable to create parser.\n")
        return None
    try:
        metadata = extractMetadata(parser)
    except HachoirError, err:
        logger.error("stream error! %s\n" % unicode(err))
        return None

    if metadata is None:
        logger.error("unable to extract metadata.\n")
        return None

    return metadata

def scale_from_metadata(metadata):
    try:
        height = metadata.get('height', None)
        width = metadata.get('width', None)
    except (ValueError, AttributeError):
        return None, None
    return height, width
