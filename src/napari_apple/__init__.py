__version__ = "0.0.5"

from ._reader import napari_get_reader
from ._sample_data import make_sample_data
from ._widget import  do_image_detection, save_as_zip
from ._writer import write_multiple, write_single_image

__all__ = (
    "napari_get_reader",
    "write_single_image",
    "write_multiple",
    "make_sample_data",
    "do_image_detection",
    "save_as_zip",
)
