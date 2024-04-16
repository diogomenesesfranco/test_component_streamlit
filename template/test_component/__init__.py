import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "test_component",

        url="http://localhost:3001",
    )
else:
    pass

def test_component(name, key=None):
        component_value = _component_func(name=name, key=key, default=0)

        return component_value