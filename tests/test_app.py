import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("#app-title")
    assert header.text == "Pink Morsel Sales Dashboard"


def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None