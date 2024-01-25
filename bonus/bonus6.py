contents = ['blabla1',
            'albalb1',
            'blabla2',
            'albalb2']

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')              # .. za directory UP   i /files za ulazak u dirctory
