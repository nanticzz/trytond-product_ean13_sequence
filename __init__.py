# This file is part product_ean13_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import configuration
from . import product


def register():
    Pool.register(
        configuration.Configuration,
        product.Product,
        module='product_ean13_sequence', type_='model')
