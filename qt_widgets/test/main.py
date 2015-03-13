# coding=utf-8
"""Main file for showing off widget parameter."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'main'
__date__ = '8/19/14'
__copyright__ = 'ismail@kartoza.com'
__doc__ = ''

import sys
from functools import partial

from PyQt4.QtGui import (QApplication, QWidget, QGridLayout, QPushButton)
from metadata import unit_feet_depth, unit_metres_depth
from boolean_parameter import BooleanParameter
from float_parameter import FloatParameter
from integer_parameter import IntegerParameter
from string_parameter import StringParameter
from unit import Unit

from qt_widgets.parameter_container import ParameterContainer
from qt_widgets.test.custom_parameter.point_parameter import PointParameter
from qt_widgets.test.custom_parameter.point_parameter_widget import (
    PointParameterWidget)


def main():
    """Main function"""
    app = QApplication([])

    def validate_min_max(parent_container):
        """
        :param parent_container: The container that use this validator.
        :type parent_container: ParameterContainer
        :return:
        """
        min_value_parameter = parent_container.get_parameter_by_guid(
            min_integer_parameter.guid)
        max_value_parameter = parent_container.get_parameter_by_guid(
            max_integer_parameter.guid)

        min_value = min_value_parameter.value
        max_value = max_value_parameter.value

        print 'min', min_value
        print 'max', max_value

        if min_value > max_value:
            print 'Not valid'
            return {
                'valid': False,
                'message': (
                    'Your minimum value (%d) should be less than your maximum '
                    'value (%d)' % (min_value, max_value))
            }
        print 'Valid'
        return {'valid': True, 'message': ''}

    unit_feet = Unit('130790')
    unit_feet.load_dictionary(unit_feet_depth)

    unit_metres = Unit('900713')
    unit_metres.load_dictionary(unit_metres_depth)

    string_parameter = StringParameter('28082014')
    string_parameter.name = 'Province Name'
    string_parameter.help_text = 'Name of province.'
    string_parameter.description = (
        'A <b>test _description</b> that is very long so that you need to '
        'read it for one minute and you will be tired after read this '
        'description. You are the best user so far. Even better if you read '
        'this description loudly so that all of your friends will be able '
        'to hear you')
    string_parameter.is_required = True
    string_parameter.value = 'Daerah Istimewa Yogyakarta'

    boolean_parameter = BooleanParameter('1231231')
    boolean_parameter.name = 'Post processor'
    boolean_parameter.help_text = 'This is post processor parameter.'
    boolean_parameter.description = (
        'A <b>test _description</b> that is very long so that you need to '
        'read it for one minute and you will be tired after read this '
        'description. You are the best user so far. Even better if you read '
        'this description loudly so that all of your friends will be able '
        'to hear you')
    boolean_parameter.is_required = True
    boolean_parameter.value = True

    float_parameter = FloatParameter()
    float_parameter.name = 'Flood Depth'
    float_parameter.is_required = True
    float_parameter.precision = 3
    float_parameter.minimum_allowed_value = 1.0
    float_parameter.maximum_allowed_value = 2.0
    float_parameter.help_text = 'The depth of flood.'
    float_parameter.description = (
        'A <b>test _description</b> that is very long so that you need to '
        'read it for one minute and you will be tired after read this '
        'description. You are the best user so far. Even better if you read '
        'this description loudly so that all of your friends will be able '
        'to hear you')
    float_parameter.unit = unit_feet
    float_parameter.allowed_units = [unit_metres, unit_feet]
    float_parameter.value = 1.12

    integer_parameter = IntegerParameter()
    integer_parameter.name = 'Paper'
    integer_parameter.is_required = True
    integer_parameter.minimum_allowed_value = 1
    integer_parameter.maximum_allowed_value = 5
    integer_parameter.help_text = 'Number of paper'
    integer_parameter.description = (
        'A <b>test _description</b> that is very long so that you need to '
        'read it for one minute and you will be tired after read this '
        'description. You are the best user so far. Even better if you read '
        'this description loudly so that all of your friends will be able '
        'to hear you')
    integer_parameter.unit = unit_feet
    integer_parameter.allowed_units = [unit_feet]
    integer_parameter.value = 3

    point_parameter = PointParameter()
    point_parameter.name = 'Point Parameter'
    point_parameter.is_required = True
    point_parameter.help_text = 'Short help.'
    point_parameter.description = 'Long description for parameter.'
    point_parameter.value = (0, 1)

    min_integer_parameter = IntegerParameter()
    min_integer_parameter.name = 'Minimal Stick Length'
    min_integer_parameter.is_required = True
    min_integer_parameter.minimum_allowed_value = 1
    min_integer_parameter.maximum_allowed_value = 50
    min_integer_parameter.help_text = 'Minimum length of a stick'
    min_integer_parameter.description = (
        'Minimum length of a stick that are allowed')
    min_integer_parameter.unit = unit_metres
    min_integer_parameter.allowed_units = [unit_metres]
    min_integer_parameter.value = 3

    max_integer_parameter = IntegerParameter()
    max_integer_parameter.name = 'Maximum Stick Length'
    max_integer_parameter.is_required = True
    max_integer_parameter.minimum_allowed_value = 1
    max_integer_parameter.maximum_allowed_value = 50
    max_integer_parameter.help_text = 'Maximum length of a stick'
    max_integer_parameter.description = (
        'Maximum length of a stick that are allowed')
    max_integer_parameter.unit = unit_metres
    max_integer_parameter.allowed_units = [unit_metres]
    max_integer_parameter.value = 4

    parameters = [
        string_parameter,
        integer_parameter,
        boolean_parameter,
        float_parameter,
        float_parameter,
        boolean_parameter,
        integer_parameter,
        point_parameter]

    extra_parameters = [
        (PointParameter, PointParameterWidget)
    ]
    min_max_parameters = [min_integer_parameter, max_integer_parameter]

    description_text = (
        'These parameters are merely created for showing example only')
    # description_text = ''
    parameter_container = ParameterContainer(
        parameters,
        extra_parameters=extra_parameters,
        description_text=description_text)
    parameter_container.setup_ui()

    parameter_container2 = ParameterContainer(
        extra_parameters=extra_parameters,
        description_text='Empty Parameter Container Description')
    parameter_container2.setup_ui()

    parameter_container3 = ParameterContainer(
        parameters=min_max_parameters,
        extra_parameters=extra_parameters,
        description_text='Minimum Maximum Parameter')
    parameter_container3.add_validator(validate_min_max)
    parameter_container3.setup_ui()

    def show_parameter(the_parameter_container):
        """Print the value of parameter.

        :param the_parameter_container: A parameter container
        :type the_parameter_container: ParameterContainer
        """
        temps = the_parameter_container.get_parameters()
        if temps:
            for temp in temps:
                print temp.guid, temp.name, temp.value

    button = QPushButton('Show parameters')
    # noinspection PyUnresolvedReferences
    button.clicked.connect(
        partial(show_parameter, the_parameter_container=parameter_container))

    validate_button = QPushButton('Validate parameters')
    # noinspection PyUnresolvedReferences
    validate_button.clicked.connect(
        partial(show_parameter, the_parameter_container=parameter_container3))

    widget = QWidget()
    layout = QGridLayout()
    layout.addWidget(parameter_container)
    layout.addWidget(button)
    layout.addWidget(parameter_container2)
    layout.addWidget(parameter_container3)
    layout.addWidget(validate_button)

    widget.setLayout(layout)
    widget.setGeometry(0, 0, 500, 500)

    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
