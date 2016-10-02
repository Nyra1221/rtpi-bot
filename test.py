info = {'results': [
            {'route': 1, 'destination': 'DestA', 'duetime': '1'},
            {'route': 2, 'destination': 'DestB', 'duetime': '2'},
            {'route': 3, 'destination': 'DestC', 'duetime': '3'},
            {'route': 4, 'destination': 'DestD', 'duetime': '4'},
            {'route': 5, 'destination': 'DestE', 'duetime': '5'},
            {'route': 6, 'destination': 'DestF', 'duetime': '6'},
            {'route': 7, 'destination': 'DestG', 'duetime': '7'},
            {'route': 8, 'destination': 'DestH', 'duetime': '8'},
            ],
       }

def chunks(info, n):
    for i in range(0, len(info['results']), n):
        chunk = []
        for result in info['results'][i:i+n]:
            chunk.append("Route:" + " " + str(result['route']) + " "
                         + "to" + " " + str(result['destination'])
                         + "\n" + "Due:" + " " + str(result["duetime"])
                         + " " + "minutes." + "\n")
        yield '\n'.join(chunk)

for i, chunk in enumerate(chunks(info, 5), 1):
    print('== CHUNK {} ==\n{}'.format(i, chunk))