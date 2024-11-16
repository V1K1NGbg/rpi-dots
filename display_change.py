#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import subprocess
import logging
import shlex
import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO
import traceback

def draw(num, text):
    Himage = Image.new('1', (epd.height, epd.width), 255)
    Himage.paste(Image.open('layout' + str(num) + '.png'))
    draw = ImageDraw.Draw(Himage)
    for t in range(3):
        if text[t] == '':
            continue
        if draw.textlength(text[t], font=font12) > 32.0:
            location = text_locations[t]
            while text[t] != "":
                line = ""
                while text[t] and draw.textlength(line + text[t][0], font=font12) <= 32.0:
                    line += text[t][0]
                    text[t] = text[t][1:]
                draw.text(location[t], line, font=font12, fill=0)
                location = (location[0], location[1] + 14)
        else:
            draw.text(text_locations[t], text[t], font=font12, fill=0)
    # draw_func(Himage)
    epd.display(epd.getbuffer(Himage))
try:

    # Init
    epd = epd2in7.EPD()
    epd.init()
    epd.Clear(0xFF)

    # Font
    font24 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 24)
    font18 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    font12 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)
    font06 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 6)


    # 176 - 4(offset) / n + 8 = 8, 51, 94, 137
    text_locations = [(8, 8), (8, 51), (8, 94), (8, 137)]

    # Data
    # ip = subprocess.check_output("hostname -I | awk '{print $1;}'", shell=True).decode('utf-8')

    # Create Image
    # Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    # draw = ImageDraw.Draw(Himage)

    # Draw
    # draw.text((0, 0), ip , font = font24, fill = 0)
    # draw.line((20, 50, 70, 100), fill = 0)
    # draw.line((70, 50, 20, 100), fill = 0)
    # draw.rectangle((20, 50, 70, 100), outline = 0)

    # Himage.paste(Image.open('layout0.png'))

    # Display
    # epd.display(epd.getbuffer(Himage))

    pressed = False
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) #5, 6, 13, 19
    # GPIO.add_event_detect(17, GPIO.FALLING, callback=lambda pin: self.button_pressed(1, button_handler), bouncetime=200)

    # while pressed == False:
    #     if GPIO.input(5) == False:
    #         pressed = True
    #         print("Button Pressed")
    #         break

    draw(2, ['Hello000', '', 'World'])

    # Example
    
    # logging.info("epd2in7 Demo")   
    # epd = epd2in7.EPD()
    
    # '''2Gray(Black and white) display'''
    # logging.info("init and Clear")
    # epd.init()
    # epd.Clear(0xFF)
    # font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    # font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    # font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    # # Drawing on the Horizontal image
    # logging.info("1.Drawing on the Horizontal image...")
    # Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    # draw = ImageDraw.Draw(Himage)
    # draw.text((10, 0), 'hello world', font = font24, fill = 0)
    # draw.text((150, 0), u'微雪电子', font = font24, fill = 0)    
    # draw.line((20, 50, 70, 100), fill = 0)
    # draw.line((70, 50, 20, 100), fill = 0)
    # draw.rectangle((20, 50, 70, 100), outline = 0)
    # draw.line((165, 50, 165, 100), fill = 0)
    # draw.line((140, 75, 190, 75), fill = 0)
    # draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    # draw.rectangle((80, 50, 130, 100), fill = 0)
    # draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    # epd.display(epd.getbuffer(Himage))
    # time.sleep(2)
    
    # # Drawing on the Vertical image
    # logging.info("2.Drawing on the Vertical image...")
    # Limage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    # draw = ImageDraw.Draw(Limage)
    # draw.text((2, 0), 'hello world', font = font18, fill = 0)
    # draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
    # draw.line((10, 90, 60, 140), fill = 0)
    # draw.line((60, 90, 10, 140), fill = 0)
    # draw.rectangle((10, 90, 60, 140), outline = 0)
    # draw.line((95, 90, 95, 140), fill = 0)
    # draw.line((70, 115, 120, 115), fill = 0)
    # draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
    # draw.rectangle((10, 150, 60, 200), fill = 0)
    # draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
    # epd.display(epd.getbuffer(Limage))
    # time.sleep(2)
    
    # logging.info("3.read bmp file")
    # Himage = Image.open(os.path.join(picdir, '2in7.bmp'))
    # epd.display(epd.getbuffer(Himage))
    # time.sleep(2)
    
    # logging.info("4.read bmp file on window")
    # Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    # bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    # Himage2.paste(bmp, (50,10))
    # epd.display(epd.getbuffer(Himage2))
    # time.sleep(2)
    
    # '''4Gray display'''
    # logging.info("4Gray display--------------------------------")
    # epd.Init_4Gray()
    
    # Limage = Image.new('L', (epd.width, epd.height), 0)  # 255: clear the frame
    # draw = ImageDraw.Draw(Limage)
    # draw.text((20, 0), u'微雪电子', font = font35, fill = epd.GRAY1)
    # draw.text((20, 35), u'微雪电子', font = font35, fill = epd.GRAY2)
    # draw.text((20, 70), u'微雪电子', font = font35, fill = epd.GRAY3)
    # draw.text((40, 110), 'hello world', font = font18, fill = epd.GRAY1)
    # draw.line((10, 140, 60, 190), fill = epd.GRAY1)
    # draw.line((60, 140, 10, 190), fill = epd.GRAY1)
    # draw.rectangle((10, 140, 60, 190), outline = epd.GRAY1)
    # draw.line((95, 140, 95, 190), fill = epd.GRAY1)
    # draw.line((70, 165, 120, 165), fill = epd.GRAY1)
    # draw.arc((70, 140, 120, 190), 0, 360, fill = epd.GRAY1)
    # draw.rectangle((10, 200, 60, 250), fill = epd.GRAY1)
    # draw.chord((70, 200, 120, 250), 0, 360, fill = epd.GRAY1)
    # epd.display_4Gray(epd.getbuffer_4Gray(Limage))
    # time.sleep(2)
    
    # #display 4Gra bmp
    # Himage = Image.open(os.path.join(picdir, '2in7_Scale.bmp'))
    # epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    # time.sleep(2)

    # logging.info("Clear...")
    # epd.Clear(0xFF)
    # logging.info("Goto Sleep...")
    # epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit(cleanup=True)
    exit()