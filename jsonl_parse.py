import json
import pandas as pd

#class for parsing jsonl file
class PARSE:
    def __init__(self):
        self.items = list()
    
    def to_list(self, filename):
        #load jsonl file
        with open(filename, 'r') as f:
            #remove newline characters at first and last
            data = f.read()[1:-2]
            #split dicts
            data = data.split('}\n{')

            #load as json   (python dict)
            for item in data:
                item_dict = json.loads('{' + item + '}')
                self.items.append(item_dict)
        
        return self.items   #return as list
    
    def to_df(self, filename):
        item_list = self.to_list(filename)

        #define number of lists as many keys are being parsed
        id_list = []
        type_list = []
        crd_list = []
        for i in item_list:
            i = json.dumps(i, indent=2)
            j = json.loads(i)
            for a in j['annotations']:
                id_list.append(j['id'])
                type_list.append(a['type'])
                crd_list.append(a['coordinates'])
        
        df_dict = {'id': id_list, 'type': type_list, 'coordinate': crd_list}
        df = pd.DataFrame(df_dict)
        return df