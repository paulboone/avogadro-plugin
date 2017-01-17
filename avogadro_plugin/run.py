
import argparse
import json
import sys

def avogadro_plugin_call(method_name, run_workflow_method, print_options_method, menu_path):
    parser = argparse.ArgumentParser('Scale molecular coordinates.')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--print-options', action='store_true')
    parser.add_argument('--run-workflow', action='store_true')
    parser.add_argument('--display-name', action='store_true')
    parser.add_argument('--menu-path', action='store_true')
    args = vars(parser.parse_args())

    debug = args['debug']
    status = None

    if args['display_name']:
        results = {"display_name": method_name}
    elif args['menu_path']:
        results = {"menu_path": menu_path}
    elif args['print_options']:
        input_json = json.loads(sys.stdin.read())
        if 'options' in input_json:
            options = input_json['options']
        else:
            options = {}
        results = print_options_method(input_json['cjson'], options)
    elif args['run_workflow']:
        input_json = json.loads(sys.stdin.read())
        if 'options' in input_json:
            options = input_json['options']
        else:
            options = {}
        status, results = run_workflow_method(input_json['cjson'], options)

    sys.stdout.write(json.dumps(results))
    if status:
        sys.exit(status)
