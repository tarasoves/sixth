from flask import Blueprint, render_template
from . import order


@order.route('/privet')
def privet():
    return render_template('privet.html')