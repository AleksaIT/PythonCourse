import PySimpleGUI as SG
from zip_extractor import extract_archive

SG.theme("DarkPurple4")

label1 = SG.Text("Select archive:")
input1 = SG.Input()
choose_button1 = SG.FileBrowse("Choose", key='archive')

label2 = SG.Text("Select dest dir:")
input2 = SG.Input()
choose_button2 = SG.FolderBrowse("Choose", key='folder')

extract_button = SG.Button("Extract")
output_label = SG.Text(key="output", text_color="green")

window = SG.Window('Archive Extractor', layout=[[label1, input1, choose_button1],
                                         [label2, input2, choose_button2],
                                         [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction completed!")

window.close()