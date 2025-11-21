"""PDM build hook for Cython extensions."""

import numpy as np
from Cython.Build import cythonize
from setuptools import Extension


def pdm_build_update_setup_kwargs(context, setup_kwargs):
    """
    Update setup kwargs with Cython extensions.
    
    This hook is called during PDM build to add Cython extensions
    to the build process.
    
    Args:
        context: PDM build context object
        setup_kwargs: Dictionary of setup() keyword arguments
        
    """
    extensions = [
        Extension(
            's1isp._huffman',
            sources=['s1isp/_huffman.pyx', 'src/huffman.c'],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
            include_dirs=['src', np.get_include()],
        )
    ]
    
    # Cythonize the extensions and add to setup kwargs
    setup_kwargs['ext_modules'] = cythonize(
        extensions,
        compiler_directives={'language_level': '3'},
    )
