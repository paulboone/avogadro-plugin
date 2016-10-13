import importlib
import json
import os
import sys

import click

@click.command()
@click.argument('command_module')
@click.option('--print-dialog/--run-transformation', default=False)
@click.option('--language', default='en.us', help="preferred language to use")
def run(command_module, print_dialog, language):
    """
    This command expects to recieve a JSON file via stdin that contains the structure selected in
    avogadro, along with any parameters from the dialog. You can call this method without flags, in
    which case it will attempt to run the transformation, or with the flag --print-dialog, which
    instead returns the JSON necessary via stdout to create a dialog to set the parameters of the
    transformation.

    A note to people using this as a template:

    This method handles the comand line interface, unmarshals the data from JSON, and passes the
    data to either get_dialog_options() or run_transformation(), depending on the flags. Upon
    completion, it marshals the results back to JSON and returns it to avogadro via stdout.

    In general, you shouldn't need to modify this method. Instead, make changes to
    get_dialog_options() and run_transformation().
    """
    input_stream = click.get_text_stream('stdin').read()
    input_json = json.loads(input_stream)
    structure = input_json['cjson']
    options = input_json['options']

    # since this will be run from the plugin's directory, add the current directory to the path
    sys.path.append(os.getcwd())
    plugin = __import__(command_module)
    status = 0
    if print_dialog:
        results = plugin.get_dialog_options(structure, options)
    else:
        status, results = plugin.run_transformation(structure, options)

    # marshal to json and return across stdout
    sys.stdout.write(json.dumps(results))

    if status:
        sys.exit(status)
