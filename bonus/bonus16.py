from modules import functions
import PySimpleGUI as SG

label1 = SG.Text("Select files to compress:")
label2 = SG.Text("Select destination folder:")
input1 = SG.Input()
input2 = SG.Input()
choose_button1 = SG.FilesBrowse("Choose")
choose_button2 = SG.FolderBrowse("Choose")
compress_button = SG.Button("Compress")

window = SG.Window('Compressor', layout=[[label1, input1, choose_button1],
                                         [label2, input2, choose_button2],
                                         [compress_button]])
window.read()
window.close()