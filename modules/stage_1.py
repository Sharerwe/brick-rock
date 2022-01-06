
import json

def run(**args):
    print('[$] Enter stage 1')
    basic_config =json.dumps([{"module" : "shell_module"}, {"module" : "sleep24h"}])
    return basic_config
                        
