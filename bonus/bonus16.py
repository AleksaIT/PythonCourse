from modules import functions
import PySimpleGUI as SG
from zip_creator import make_archive

label1 = SG.Text("Select files to compress:")
label2 = SG.Text("Select destination folder:")
input1 = SG.Input()
input2 = SG.Input()
choose_button1 = SG.FilesBrowse("Choose", key='files')
choose_button2 = SG.FolderBrowse("Choose", key='folder')
compress_button = SG.Button("Compress")
output_label = SG.Text(key="output", text_color="green")

window = SG.Window('Compressor', layout=[[label1, input1, choose_button1],
                                         [label2, input2, choose_button2],
                                         [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")

window.close()