from screeninfo import get_monitors
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from os import path

driver_folder = path.join(path.dirname(path.abspath(__file__)), 'lib', 'webdriver')

width = 0
height = 0
for m in get_monitors():
    if m.is_primary:
        width = m.width/1.5
        height = m.height/1.5

service = Service(executable_path=path.join(driver_folder, 'msedgedriver.exe'))
options = Options()
options.add_argument('-inprivate')

drivers = []
for i in range(20):
    drivers.append(webdriver.Edge(service=service, options=options))
    drivers[i].set_window_size(width/2, height)
    # drivers[i].set_window_position((i%4)*width/2, (i%4)*height/2)
    # tile windows next to eachtoher
    drivers[i].set_window_position((i%2)*width/2, 0)
    drivers[i].get('https://tickets.leedsunited.com/')

input()
