#  Kevan Hong-Nhan Nguyen 71632979.  ICS 32 Lab sec 9.  Project #3.
import mapquest
import mapquest_outputs

def _run_user_interface() -> None:
    ''' Runs the entire MapQuest program '''

    locations = _handle_locations_input()
    if len(locations) == 0:
        return
        
    outputs = _handle_outputs_input()
    if len(outputs) == 0:
        return

    json_result = mapquest.get_result(mapquest.build_search_url(locations))
    if _has_route_errors(json_result):
        return

    _display_outputs(json_result, outputs)


def _display_outputs(json_result: 'json', outputs: [str]) -> None:
    ''' Displays the user-specified outputs. If any one of the outputs is
        invalid, the function prints to the console which specific user-inputted
        ouput is causing the error, halting the program from displaying any
        of the outputs (mimicking the working example provided online by the
        professor) '''
    output_types = {'STEPS': mapquest_outputs.Steps(json_result),
                    'TOTALDISTANCE': mapquest_outputs.Distance(json_result),
                    'TOTALTIME': mapquest_outputs.Time(json_result),
                    'LATLONG': mapquest_outputs.Location(json_result)}
    
    for output in outputs:
        if output.upper() not in output_types:
            print('Invalid output type: ' + output)
            return

    for output in outputs:
        output_types[output.upper()].generate()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
            

def _handle_locations_input() -> [str]:
    ''' Handles the locations input. '''
    try:
        locations = []
        num_locations = eval(input())
        if type(num_locations) != int or not num_locations >= 2:
            raise Exception
        for i in range(num_locations):
            locations.append(input().strip())
    except:
        print('The first line must be a positive integer greater than or equal to 2.')
    finally:
        return locations


def _handle_outputs_input() -> [str]:
    ''' Handles the outputs input '''
    try:
        outputs = []
        num_outputs = eval(input())
        if type(num_outputs) != int or not num_outputs >= 1:
            raise Exception
        for i in range(num_outputs):
            outputs.append(input().strip())
    except:
        print('There must be a positive integer number of generators/outputs')
    finally:
        return outputs

def _has_route_errors(json_result: 'json') -> bool:
    ''' Checks to see if there are any errors with user's locations (if any)
        and displays them to the console. Returns True if there are and False if not '''
    if json_result['info']['statuscode'] != 0:
        print('ERROR')
        print('-----')
        for error in json_result['info']['messages']:
            print(error)
        return True
    return False


    
        
if __name__ == '__main__':
    _run_user_interface()
    
