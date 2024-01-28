from modules import functions
import PySimpleGUI as SG

label1 = SG.Text("Enter feet:")
label2 = SG.Text("Enter inches:")
input_box1 = SG.InputText(tooltip="Enter feet")
input_box2 = SG.InputText(tooltip="Enter inches")
convert_button = SG.Button("Convert")

window = SG.Window('Compressor', layout=[[label1, input_box1],
                                         [label2, input_box2],
                                         [convert_button]])
window.read()
window.close()