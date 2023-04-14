import pyautogui as pg
from time import sleep

pg.hotkey("alt", "tab")
pg.click(1606, 876)
pg.click(1694, 654)
sleep(0.1)
pg.press("tab")
pg.press("tab")
pg.press("tab")
pg.press("tab")
pg.press("enter")
pg.click(1000, 600)


# pg.hotkey('alt','tab')
# pg.click(1606 , 876)
# pg.click(1694 ,654)
# pg.moveTo(1694 ,654,0.5)
# pg.scroll(-100)
# pg.moveTo( 1000 , 600,0.1)
# pg.click(1632 , 773)
# pg.click(1000 , 600)


# for position in tupla1:
#     if position == (1632, 773):

#         pg.moveTo(position[0], position[1], 0.2)
#         pg.scroll(-100)
#         pg.click()
#     else:
#         pg.click(position)
