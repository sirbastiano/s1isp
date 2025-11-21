"""PDM build hook for Cython extensions."""

import numpy as np
from Cython.Build import cythonize
from setuptools import Extension


def pdm_build_initialize(context):
    """
    Initialize the build with Cython extensions.
    
    This hook is called during PDM build to compile Cython extensions.
    
    Args:
        context: PDM build context object
        
    """
    extensions = [
        Extension(
            's1isp._huffman',
            sources=['s1isp/_huffman.pyx', 'src/huffman.c'],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
            include_dirs=['src', np.get_include()],
        )
    ]
    
    # Cythonize the extensions
    cythonized = cythonize(
        extensions,
        compiler_directives={'language_level': '3'},
    )
    
    # Update the metadata with the extensions
    if hasattr(context, 'config'):
        context.config.data['ext_modules'] = cythonized


def pdm_build_update_setup_kwargs(context, setup_kwargs):
    """
    Update setup kwargs with Cython extensions.
    
    Args:
        context: PDM build context object
        setup_kwargs: Dictionary of setup() keyword arguments
        
    """
    if hasattr(context, 'config'):
        ext_modules = context.config.data.get('ext_modules', [])
        if ext_modules:
            setup_kwargs['ext_modules'] = ext_modules
