#from ../modules import functions
import PySimpleGUI as SG

def konverter(feets, inches):
    return float(feets * 0.3048 + inches * 0.0254)

label1 = SG.Text("Enter feet:")
label2 = SG.Text("Enter inches:")
input_box1 = SG.InputText(tooltip="Enter feet", key="fiti")
input_box2 = SG.InputText(tooltip="Enter inches", key="inci")
convert_button = SG.Button("Convert")
output_label = SG.Text("", key="output")

window = SG.Window('Compressor', layout=[[label1, input_box1],
                                         [label2, input_box2],
                                         [convert_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    feets = float(values["fiti"])
    inches = float(values["inci"])
    window["output"].update(value=f"{konverter(feets,inches)} m", text_color="white")


window.close()

