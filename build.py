#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_default
import os
def _is_not_shared(build):
    return build.options['ImageLoaderPlugin:shared'] == False
    
if __name__ == "__main__":

    builder = build_template_default.get_builder() 
    builder.remove_build_if(_is_not_shared)  
    builder.run()
