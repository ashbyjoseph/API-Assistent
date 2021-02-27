#d=[3,4,5]
#print(d)

import wolframalpha
app_id = 'TVEK6R-3YL96P7JVX'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)

#res = client.query('temperature in Washington, DC on October 3, 2012')

#print(next(res.results).text)




import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
sg.theme('DarkPurple')
layout = [  [sg.Text("Enter a question you want to ask Jarvis")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Quit')],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Jarvis', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
while True:
    event, values = window.read()
    if event in (None,'Cancel') :
        break
    res= client.query(values[0])
    sg.Popup(next(res.results).text)

window.close()
