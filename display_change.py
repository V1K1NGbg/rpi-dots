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

saved = ['','','','']


def draw(num, text, fontxx, draw_func, old = False):
    Himage = Image.new('1', (epd.height, epd.width), 255)
    Himage.paste(Image.open('layout' + str(num) + '.png'))
    draw = ImageDraw.Draw(Himage)
    if old == True:
        text = saved
    for t in range(4):
        saved[t] = text[t]
        if text[t] == '':
            continue
        if draw.textlength(text[t], font=fontxx) > 32.0:
            location = text_locations[t]
            while text[t] != "":
                line = ""
                while text[t] and draw.textlength(line + text[t][0], font=fontxx) <= 32.0:
                    line += text[t][0]
                    text[t] = text[t][1:]
                draw.text(location, line, font=fontxx, fill=0)
                location = (location[0], location[1] + 14)
        else:
            draw.text(text_locations[t], text[t], font=fontxx, fill=0)
    draw_func(draw)
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
    font10 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 10)
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


    # --------------------------------------------


    # if n == 0, loc = (8, 8) else loc = (53, 8) ; (255, 167)
    def draw_booting_screen(draw):
        title = 'Hello There!'
        subtitle = 'Booting...'
        draw.text(((264-draw.textlength(title, font=font24))/2, 70), title, font=font24, fill=0)
        draw.text(((264-draw.textlength(subtitle, font=font18))/2, 100), subtitle, font=font18, fill=0)

    def draw_start_screen(draw):
        title = 'Welcome!'
        draw.text(((264-draw.textlength(title, font=font24) + 53)/2, 70), title, font=font24, fill=0)



    def draw_display_screen(draw):
        title = 'Display'
        draw.text(((264-draw.textlength(title, font=font24) + 53)/2, 70), title, font=font24, fill=0)

    def draw_display_main_screen(draw):
        title = 'Main'
        draw.text(((264-draw.textlength(title, font=font24) + 53)/2, 70), title, font=font24, fill=0)
        
    def draw_display_weather_and_time_screen(draw):
        title = 'w'
        draw.text(((264-draw.textlength(title, font=font24) + 53)/2, 70), title, font=font24, fill=0)

    def draw_display_stats_screen(draw):
        title = 's'
        draw.text(((264-draw.textlength(title, font=font24) + 53)/2, 70), title, font=font24, fill=0)

        

    def draw_docker_screen(draw):
        title = 'Docker'
        draw.text(((264-draw.textlength(title, font=font24) + 53)/2, 70), title, font=font24, fill=0)




    def draw_power_screen(draw):
        title = 'Power'
        draw.text(((264-draw.textlength(title, font=font24) + 53)/2, 70), title, font=font24, fill=0)

    def draw_power_stop_screen(draw):
        title = 'Shutting Down...'
        subtitle = 'press any button to cancel'
        draw.text(((264-draw.textlength(title, font=font24))/2, 70), title, font=font24, fill=0)
        draw.text(((264-draw.textlength(subtitle, font=font12))/2, 100), subtitle, font=font12, fill=0)

    def draw_power_reboot_screen(draw):
        title = 'Rebooting...'
        subtitle = 'press any button to cancel'
        draw.text(((264-draw.textlength(title, font=font24))/2, 70), title, font=font24, fill=0)
        draw.text(((264-draw.textlength(subtitle, font=font12))/2, 100), subtitle, font=font12, fill=0)

    def draw_power_off_screen(draw):
        title = 'Powering Off...'
        subtitle = 'press any button to cancel'
        draw.text(((264-draw.textlength(title, font=font24))/2, 70), title, font=font24, fill=0)
        draw.text(((264-draw.textlength(subtitle, font=font12))/2, 100), subtitle, font=font12, fill=0)

    
    def draw_end_screen():
        Himage = Image.new('1', (epd.height, epd.width), 255)
        Himage.paste(Image.open('rpi.png'))
        epd.display(epd.getbuffer(Himage))


    def main(draw):
        # draw(4, ['Display', 'Vitals', 'Docker', 'Power'], font10, draw_start_screen)
        draw(3, ['Display', 'Docker', '', 'Power'], font10, draw_start_screen)


    draw(0, ['', '', '', ''], font10, draw_booting_screen)

    # time.sleep(3)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    main(draw)


    while True:
        if GPIO.input(5) == False:
            draw(4, ['Back', 'Main', 'Time/Weather', 'Stats'], font10, draw_display_screen)
            while True:
                if GPIO.input(5) == False:
                    main(draw)
                    break
                if GPIO.input(6) == False:
                    draw(4, ['', '', '', ''], font10, draw_display_main_screen, True)
                if GPIO.input(13) == False:
                    draw(4, ['', '', '', ''], font10, draw_display_weather_and_time_screen, True)
                if GPIO.input(19) == False:
                    draw(4, ['', '', '', ''], font10, draw_display_stats_screen, True)



        if GPIO.input(6) == False or GPIO.input(13) == False:
            # draw(4, ['Back', 'CPU', 'Memory', 'Network'], font10, draw_vitals_screen)
            draw(4, ['Back', 'Up', 'Down', 'Start/Stop'], font10, draw_docker_screen)
            while True:
                if GPIO.input(5) == False:
                    main(draw)
                    break



        # if GPIO.input(13) == False:
        #     draw(4, ['Back', 'Up', 'Down', 'Start/Stop'], font10, draw_docker_screen)
        #     while True:
        #         if GPIO.input(5) == False:
        #             main(draw)
        #             break



        if GPIO.input(19) == False:
            draw(4, ['Back', 'Shutdown', 'Restart', 'Power Off'], font10, draw_power_screen)
            while True:
                if GPIO.input(5) == False:
                    main(draw)
                    break
                if GPIO.input(6) == False:
                    draw(0, ['', '', '', ''], font10, draw_power_stop_screen)
                    start_time = time.time()
                    abort = False
                    while time.time() - start_time < 3:
                        if GPIO.input(5) == False or GPIO.input(6) == False or GPIO.input(13) == False or GPIO.input(19) == False:
                            abort = True
                            break
                    if abort:
                        main(draw)
                        break
                    else:
                        draw_end_screen()
                        os.system("sudo shutdown now")
                if GPIO.input(13) == False:
                    draw(0, ['', '', '', ''], font10, draw_power_reboot_screen)
                    start_time = time.time()
                    abort = False
                    while time.time() - start_time < 3:
                        if GPIO.input(5) == False or GPIO.input(6) == False or GPIO.input(13) == False or GPIO.input(19) == False:
                            abort = True
                            break
                    if abort:
                        main(draw)
                        break
                    else:
                        draw_end_screen()
                        os.system("sudo reboot")
                if GPIO.input(19) == False:
                    draw(0, ['', '', '', ''], font10, draw_power_off_screen)
                    start_time = time.time()
                    abort = False
                    while time.time() - start_time < 3:
                        if GPIO.input(5) == False or GPIO.input(6) == False or GPIO.input(13) == False or GPIO.input(19) == False:
                            abort = True
                            break
                    if abort:
                        main(draw)
                        break
                    else:
                        draw_end_screen()
                        os.system("sudo poweroff")


    # --------------------------------------------


    # GPIO.add_event_detect(17, GPIO.FALLING, callback=lambda pin: self.button_pressed(1, button_handler), bouncetime=200)

    # while pressed == False:
    #     if GPIO.input(5) == False:
    #         pressed = True
    #         print("Button Pressed")
    #         break    

    # if n == 0, loc = (8, 8) else loc = (53, 8) ; (255, 167)
    # draw(4, ['Hello000', '', 'World',  '...'], font10, lambda draw: (
    #     # draw.text((53, 8), 'Main box', font=font24, fill=0)
    #     draw.line((53, 8, 255, 167), fill = 0),
    #     draw.line((255, 8, 53, 167), fill = 0)
    # ))

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