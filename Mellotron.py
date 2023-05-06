#!/usr/bin/python3


"""
Application:  Mellotron
Author:  BSFEMA
Note:  I would appreciate it if you kept my attribution as the original author in any fork or remix that is made.
Purpose:  I wanted to see if I could make a Mellotron using pygame.
          From where the Mellotron.py file resides, it will look in the "Mellotron Sound Files" subfolder for subfolders containing the sound files.
          Example:
            Mellotron Sound Files
            \sub1
            \\1.wav
            \\...
            \\35.wav
            \sub2
            ...
          It will sort the subfolders and files, so take that into account when nameing them.
Controls:
          "1"-"0" The first 10 notes
          "Q"-"P" The next 10 notes
          "A"-"L" The next 9 notes
          "Z"-"N" The next 6 notes
          "M" cycles through the various 'Mellotron Sound Files' subfolders
          "<" volume down:  10%
          ">" volume up:  10%
Command Line Parameters:  None
"""


import pygame
import os
import sys


# Globals
pygame.init()  # Initialize pygame
pygame.mixer.init()  # Initialize the pygame audio mixer
dir_path = os.path.join(sys.path[0], "Mellotron Sound Files")  # Path to the "Mellotron Sound Files" subfolder from where the Mellotron.py file is located
folders = []  # Holds the sound set folder names
files = {}  # Holds the paths to all of the sound files
current_sound_set = -1  # Holds the current folders number, which is the loaded sound set
s01=s02=s03=s04=s05=s06=s07=s08=s09=s10=s11=s12=s13=s14=s15=s16=s17=s18=s19=s20=s21=s22=s23=s24=s25=s26=s27=s28=s29=s30=s31=s32=s33=s34=s35 = ""  # Sound files (35 total)
ch_s01=ch_s02=ch_s03=ch_s04=ch_s05=ch_s06=ch_s07=ch_s08=ch_s09=ch_s10=ch_s11=ch_s12=ch_s13=ch_s14=ch_s15=ch_s16=ch_s17=ch_s18=ch_s19=ch_s20=ch_s21=ch_s22=ch_s23=ch_s24=ch_s25=ch_s26=ch_s27=ch_s28=ch_s29=ch_s30=ch_s31=ch_s32=ch_s33=ch_s34=ch_s35 = ""  # Mixer channels (35 total)
snd_s01=snd_s02=snd_s03=snd_s04=snd_s05=snd_s06=snd_s07=snd_s08=snd_s09=snd_s10=snd_s11=snd_s11=snd_s12=snd_s13=snd_s14=snd_s15=snd_s16=snd_s17=snd_s18=snd_s19=snd_s20=snd_s21=snd_s22=snd_s23=snd_s24=snd_s25=snd_s26=snd_s27=snd_s28=snd_s29=snd_s30=snd_s31=snd_s32=snd_s33=snd_s34=snd_s35 = ""  # pygame mixer sounds (35 total)
default_volume = 60


def get_files():  # Gets all of the sound set folders in dir_path, then gets all of the sound files (35)
    global files
    global folders
    global dir_path
    files.clear()
    temp_files = os.listdir(dir_path)
    temp_files.sort()
    for folder in temp_files:
        if os.path.isfile(dir_path + folder):
            print("Removing file:" + folder)
            temp_files.remove(folder)
    folders = temp_files
    for folder in folders:
        temp_files = os.listdir(os.path.join(dir_path, folder))
        temp_files.sort()
        files[folder] = temp_files
        if len(temp_files) != 35:
            print("This folder doesn't have 35 sound files:  " + str(folder))


def load_next_sound_set():  # loads the next sound set of audio files
    global current_sound_set
    global files
    global folders
    global dir_path
    global s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35
    global ch_s01, ch_s02, ch_s03, ch_s04, ch_s05, ch_s06, ch_s07, ch_s08, ch_s09, ch_s10, ch_s11, ch_s12, ch_s13, ch_s14, ch_s15, ch_s16, ch_s17, ch_s18, ch_s19, ch_s20, ch_s21, ch_s22, ch_s23, ch_s24, ch_s25, ch_s26, ch_s27, ch_s28, ch_s29, ch_s30, ch_s31, ch_s32, ch_s33, ch_s34, ch_s35
    global snd_s01, snd_s02, snd_s03, snd_s04, snd_s05, snd_s06, snd_s07, snd_s08, snd_s09, snd_s10, snd_s11, snd_s11, snd_s12, snd_s13, snd_s14, snd_s15, snd_s16, snd_s17, snd_s18, snd_s19, snd_s20, snd_s21, snd_s22, snd_s23, snd_s24, snd_s25, snd_s26, snd_s27, snd_s28, snd_s29, snd_s30, snd_s31, snd_s32, snd_s33, snd_s34, snd_s35
    if current_sound_set < (len(folders)-1):
        current_sound_set = current_sound_set + 1
    else:
        current_sound_set = 0
    print("New sound set folder is:  " + str(list(files.keys())[current_sound_set]))
    s01 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][0])
    s02 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][1])
    s03 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][2])
    s04 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][3])
    s05 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][4])
    s06 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][5])
    s07 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][6])
    s08 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][7])
    s09 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][8])
    s10 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][9])
    s11 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][10])
    s12 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][11])
    s13 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][12])
    s14 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][13])
    s15 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][14])
    s16 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][15])
    s17 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][16])
    s18 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][17])
    s19 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][18])
    s20 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][19])
    s21 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][20])
    s22 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][21])
    s23 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][22])
    s24 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][23])
    s25 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][24])
    s26 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][25])
    s27 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][26])
    s28 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][27])
    s29 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][28])
    s30 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][29])
    s31 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][30])
    s32 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][31])
    s33 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][32])
    s34 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][33])
    s35 = os.path.join(dir_path, list(files.keys())[current_sound_set], files[list(files.keys())[current_sound_set]][34])
    pygame.mixer.music.load(s01)
    pygame.mixer.music.load(s02)
    pygame.mixer.music.load(s03)
    pygame.mixer.music.load(s04)
    pygame.mixer.music.load(s05)
    pygame.mixer.music.load(s06)
    pygame.mixer.music.load(s07)
    pygame.mixer.music.load(s08)
    pygame.mixer.music.load(s09)
    pygame.mixer.music.load(s10)
    pygame.mixer.music.load(s11)
    pygame.mixer.music.load(s12)
    pygame.mixer.music.load(s13)
    pygame.mixer.music.load(s14)
    pygame.mixer.music.load(s15)
    pygame.mixer.music.load(s16)
    pygame.mixer.music.load(s17)
    pygame.mixer.music.load(s18)
    pygame.mixer.music.load(s19)
    pygame.mixer.music.load(s20)
    pygame.mixer.music.load(s21)
    pygame.mixer.music.load(s22)
    pygame.mixer.music.load(s23)
    pygame.mixer.music.load(s24)
    pygame.mixer.music.load(s25)
    pygame.mixer.music.load(s26)
    pygame.mixer.music.load(s27)
    pygame.mixer.music.load(s28)
    pygame.mixer.music.load(s29)
    pygame.mixer.music.load(s30)
    pygame.mixer.music.load(s31)
    pygame.mixer.music.load(s32)
    pygame.mixer.music.load(s33)
    pygame.mixer.music.load(s34)
    pygame.mixer.music.load(s35)
    ch_s01 = pygame.mixer.Channel(0)
    ch_s02 = pygame.mixer.Channel(1)
    ch_s03 = pygame.mixer.Channel(2)
    ch_s04 = pygame.mixer.Channel(3)
    ch_s05 = pygame.mixer.Channel(4)
    ch_s06 = pygame.mixer.Channel(5)
    ch_s07 = pygame.mixer.Channel(6)
    ch_s08 = pygame.mixer.Channel(7)
    ch_s09 = pygame.mixer.Channel(8)
    ch_s10 = pygame.mixer.Channel(9)
    ch_s11 = pygame.mixer.Channel(10)
    ch_s12 = pygame.mixer.Channel(11)
    ch_s13 = pygame.mixer.Channel(12)
    ch_s14 = pygame.mixer.Channel(13)
    ch_s15 = pygame.mixer.Channel(14)
    ch_s16 = pygame.mixer.Channel(15)
    ch_s17 = pygame.mixer.Channel(16)
    ch_s18 = pygame.mixer.Channel(17)
    ch_s19 = pygame.mixer.Channel(18)
    ch_s20 = pygame.mixer.Channel(19)
    ch_s21 = pygame.mixer.Channel(20)
    ch_s22 = pygame.mixer.Channel(21)
    ch_s23 = pygame.mixer.Channel(22)
    ch_s24 = pygame.mixer.Channel(23)
    ch_s25 = pygame.mixer.Channel(24)
    ch_s26 = pygame.mixer.Channel(25)
    ch_s27 = pygame.mixer.Channel(26)
    ch_s28 = pygame.mixer.Channel(27)
    ch_s29 = pygame.mixer.Channel(28)
    ch_s30 = pygame.mixer.Channel(29)
    ch_s31 = pygame.mixer.Channel(30)
    ch_s32 = pygame.mixer.Channel(31)
    ch_s33 = pygame.mixer.Channel(32)
    ch_s34 = pygame.mixer.Channel(33)
    ch_s35 = pygame.mixer.Channel(34)
    snd_s01 = pygame.mixer.Sound(s01)
    snd_s02 = pygame.mixer.Sound(s02)
    snd_s03 = pygame.mixer.Sound(s03)
    snd_s04 = pygame.mixer.Sound(s04)
    snd_s05 = pygame.mixer.Sound(s05)
    snd_s06 = pygame.mixer.Sound(s06)
    snd_s07 = pygame.mixer.Sound(s07)
    snd_s08 = pygame.mixer.Sound(s08)
    snd_s09 = pygame.mixer.Sound(s09)
    snd_s10 = pygame.mixer.Sound(s10)
    snd_s11 = pygame.mixer.Sound(s11)
    snd_s11 = pygame.mixer.Sound(s11)
    snd_s12 = pygame.mixer.Sound(s12)
    snd_s13 = pygame.mixer.Sound(s13)
    snd_s14 = pygame.mixer.Sound(s14)
    snd_s15 = pygame.mixer.Sound(s15)
    snd_s16 = pygame.mixer.Sound(s16)
    snd_s17 = pygame.mixer.Sound(s17)
    snd_s18 = pygame.mixer.Sound(s18)
    snd_s19 = pygame.mixer.Sound(s19)
    snd_s20 = pygame.mixer.Sound(s20)
    snd_s21 = pygame.mixer.Sound(s21)
    snd_s22 = pygame.mixer.Sound(s22)
    snd_s23 = pygame.mixer.Sound(s23)
    snd_s24 = pygame.mixer.Sound(s24)
    snd_s25 = pygame.mixer.Sound(s25)
    snd_s26 = pygame.mixer.Sound(s26)
    snd_s27 = pygame.mixer.Sound(s27)
    snd_s28 = pygame.mixer.Sound(s28)
    snd_s29 = pygame.mixer.Sound(s29)
    snd_s30 = pygame.mixer.Sound(s30)
    snd_s31 = pygame.mixer.Sound(s31)
    snd_s32 = pygame.mixer.Sound(s32)
    snd_s33 = pygame.mixer.Sound(s33)
    snd_s34 = pygame.mixer.Sound(s34)
    snd_s35 = pygame.mixer.Sound(s35)


def set_volume(volume):  # Sets the volume for all (35) audio channels  [volume = 0-100]
    for i in range(0,35):
        pygame.mixer.Channel(i).set_volume(volume / 100)
    print("Volume = " + str(volume) + "%")


def main():
    pygame.mixer.set_num_channels(35)
    print("Audio channel count =", pygame.mixer.get_num_channels())

    pygame.key.set_repeat()
    pygame.display.set_caption("Mellotron")
    size = (600, 100)
    screen = pygame.display.set_mode(size)
    img = pygame.image.load("Mellotron.svg")
    pygame.display.set_icon(img)

    white = (255, 255, 255)
    black = (0, 0, 0)
    font = pygame.freetype.Font("SourceCodePro-Bold.ttf", 24)

    get_files()  # Build the list of folders and sound files
    load_next_sound_set()  # Get the first folder of sounds

    volume = default_volume
    set_volume(volume)

    loop = True
    while loop:
        # Populate screen with information
        screen.fill(white)
        font.render_to(screen, (10, 10), "Music Set [" + str(current_sound_set+1) + "/" + str(len(files.keys())) + "] = " + str(list(files.keys())[current_sound_set]), black)
        font.render_to(screen, (10, 50), "Volume = " + str(volume) + "%", black)
        font.render_to(screen, (600-20, 10), "m", black)
        font.render_to(screen, (600-30, 50), "<>", black)
        # Look for keyboard input
        for event in pygame.event.get():
            ######################################################################
            if event.type == pygame.QUIT:
                loop = False
            ######################################################################
            if event.type == pygame.KEYDOWN:  # KeyDown events
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_1:
                    print("1 down")
                    if (ch_s01): ch_s01.play(snd_s01, 9999)
                if event.key == pygame.K_2:
                    print("2 down")
                    if (ch_s02): ch_s02.play(snd_s02, 9999)
                if event.key == pygame.K_3:
                    print("3 down")
                    if (ch_s03): ch_s03.play(snd_s03, 9999)
                if event.key == pygame.K_4:
                    print("4 down")
                    if (ch_s04): ch_s04.play(snd_s04, 9999)
                if event.key == pygame.K_5:
                    print("5 down")
                    if (ch_s05): ch_s05.play(snd_s05, 9999)
                if event.key == pygame.K_6:
                    print("6 down")
                    if (ch_s06): ch_s06.play(snd_s06, 9999)
                if event.key == pygame.K_7:
                    print("7 down")
                    if (ch_s07): ch_s07.play(snd_s07, 9999)
                if event.key == pygame.K_8:
                    print("8 down")
                    if (ch_s08): ch_s08.play(snd_s08, 9999)
                if event.key == pygame.K_9:
                    print("9 down")
                    if (ch_s09): ch_s09.play(snd_s09, 9999)
                if event.key == pygame.K_0:
                    print("0 down")
                    if (ch_s10): ch_s10.play(snd_s10, 9999)
                if event.key == pygame.K_q:
                    print("q down")
                    if (ch_s11): ch_s11.play(snd_s11, 9999)
                if event.key == pygame.K_w:
                    print("w down")
                    if (ch_s12): ch_s12.play(snd_s12, 9999)
                if event.key == pygame.K_e:
                    print("e down")
                    if (ch_s13): ch_s13.play(snd_s13, 9999)
                if event.key == pygame.K_r:
                    print("r down")
                    if (ch_s14): ch_s14.play(snd_s14, 9999)
                if event.key == pygame.K_t:
                    print("t down")
                    if (ch_s15): ch_s15.play(snd_s15, 9999)
                if event.key == pygame.K_y:
                    print("y down")
                    if (ch_s16): ch_s16.play(snd_s16, 9999)
                if event.key == pygame.K_u:
                    print("u down")
                    if (ch_s17): ch_s17.play(snd_s17, 9999)
                if event.key == pygame.K_i:
                    print("i down")
                    if (ch_s18): ch_s18.play(snd_s18, 9999)
                if event.key == pygame.K_o:
                    print("o down")
                    if (ch_s19): ch_s19.play(snd_s19, 9999)
                if event.key == pygame.K_p:
                    print("p down")
                    if (ch_s20): ch_s20.play(snd_s20, 9999)
                if event.key == pygame.K_a:
                    print("a down")
                    if (ch_s21): ch_s21.play(snd_s21, 9999)
                if event.key == pygame.K_s:
                    print("s down")
                    if (ch_s22): ch_s22.play(snd_s22, 9999)
                if event.key == pygame.K_d:
                    print("d down")
                    if (ch_s23): ch_s23.play(snd_s23, 9999)
                if event.key == pygame.K_f:
                    print("f down")
                    if (ch_s24): ch_s24.play(snd_s24, 9999)
                if event.key == pygame.K_g:
                    print("g down")
                    if (ch_s25): ch_s25.play(snd_s25, 9999)
                if event.key == pygame.K_h:
                    print("h down")
                    if (ch_s26): ch_s26.play(snd_s26, 9999)
                if event.key == pygame.K_j:
                    print("j down")
                    if (ch_s27): ch_s27.play(snd_s27, 9999)
                if event.key == pygame.K_k:
                    print("k down")
                    if (ch_s28): ch_s28.play(snd_s28, 9999)
                if event.key == pygame.K_l:
                    print("l down")
                    if (ch_s29): ch_s29.play(snd_s29, 9999)
                if event.key == pygame.K_z:
                    print("z down")
                    if (ch_s30): ch_s30.play(snd_s30, 9999)
                if event.key == pygame.K_x:
                    print("x down")
                    if (ch_s31): ch_s31.play(snd_s31, 9999)
                if event.key == pygame.K_c:
                    print("c down")
                    if (ch_s32): ch_s32.play(snd_s32, 9999)
                if event.key == pygame.K_v:
                    print("v down")
                    if (ch_s33): ch_s33.play(snd_s33, 9999)
                if event.key == pygame.K_b:
                    print("b down")
                    if (ch_s34): ch_s34.play(snd_s34, 9999)
                if event.key == pygame.K_n:
                    print("n down")
                    if (ch_s35): ch_s35.play(snd_s35, 9999)
                if event.key == pygame.K_m:
                    print("m down = changing sounds folder")
                    load_next_sound_set()
                if event.key == pygame.K_COMMA:
                    print("< down = lowering volume")
                    if volume > 0: volume = volume - 10
                    if volume < 0: volume = 0
                    set_volume(volume)
                if event.key == pygame.K_PERIOD:
                    print("> down = lowering volume")
                    if volume < 100: volume = volume + 10
                    if volume > 100: volume = 100
                    set_volume(volume)
            ######################################################################
            if event.type == pygame.KEYUP:  # KeyUp events
                if event.key == pygame.K_1:
                    print("1 up")
                    if (ch_s01): ch_s01.stop()
                if event.key == pygame.K_2:
                    print("2 up")
                    if (ch_s02): ch_s02.stop()
                if event.key == pygame.K_3:
                    print("3 up")
                    if (ch_s03): ch_s03.stop()
                if event.key == pygame.K_4:
                    print("4 up")
                    if (ch_s04): ch_s04.stop()
                if event.key == pygame.K_5:
                    print("5 up")
                    if (ch_s05): ch_s05.stop()
                if event.key == pygame.K_6:
                    print("6 up")
                    if (ch_s06): ch_s06.stop()
                if event.key == pygame.K_7:
                    print("7 up")
                    if (ch_s07): ch_s07.stop()
                if event.key == pygame.K_8:
                    print("8 up")
                    if (ch_s08): ch_s08.stop()
                if event.key == pygame.K_9:
                    print("9 up")
                    if (ch_s09): ch_s09.stop()
                if event.key == pygame.K_0:
                    print("0 up")
                    if (ch_s10): ch_s10.stop()
                if event.key == pygame.K_q:
                    print("q up")
                    if (ch_s11): ch_s11.stop()
                if event.key == pygame.K_w:
                    print("w up")
                    if (ch_s12): ch_s12.stop()
                if event.key == pygame.K_e:
                    print("e up")
                    if (ch_s13): ch_s13.stop()
                if event.key == pygame.K_r:
                    print("r up")
                    if (ch_s14): ch_s14.stop()
                if event.key == pygame.K_t:
                    print("t up")
                    if (ch_s15): ch_s15.stop()
                if event.key == pygame.K_y:
                    print("y up")
                    if (ch_s16): ch_s16.stop()
                if event.key == pygame.K_u:
                    print("u up")
                    if (ch_s17): ch_s17.stop()
                if event.key == pygame.K_i:
                    print("i up")
                    if (ch_s18): ch_s18.stop()
                if event.key == pygame.K_o:
                    print("o up")
                    if (ch_s19): ch_s19.stop()
                if event.key == pygame.K_p:
                    print("p up")
                    if (ch_s20): ch_s20.stop()
                if event.key == pygame.K_a:
                    print("a up")
                    if (ch_s21): ch_s21.stop()
                if event.key == pygame.K_s:
                    print("s up")
                    if (ch_s22): ch_s22.stop()
                if event.key == pygame.K_d:
                    print("d up")
                    if (ch_s23): ch_s23.stop()
                if event.key == pygame.K_f:
                    print("f up")
                    if (ch_s24): ch_s24.stop()
                if event.key == pygame.K_g:
                    print("g up")
                    if (ch_s25): ch_s25.stop()
                if event.key == pygame.K_h:
                    print("h up")
                    if (ch_s26): ch_s26.stop()
                if event.key == pygame.K_j:
                    print("j up")
                    if (ch_s27): ch_s27.stop()
                if event.key == pygame.K_k:
                    print("k up")
                    if (ch_s28): ch_s28.stop()
                if event.key == pygame.K_l:
                    print("l up")
                    if (ch_s29): ch_s29.stop()
                if event.key == pygame.K_z:
                    print("z up")
                    if (ch_s30): ch_s30.stop()
                if event.key == pygame.K_x:
                    print("x up")
                    if (ch_s31): ch_s31.stop()
                if event.key == pygame.K_c:
                    print("c up")
                    if (ch_s32): ch_s32.stop()
                if event.key == pygame.K_v:
                    print("v up")
                    if (ch_s33): ch_s33.stop()
                if event.key == pygame.K_b:
                    print("b up")
                    if (ch_s34): ch_s34.stop()
                if event.key == pygame.K_n:
                    print("n up")
                    if (ch_s35): ch_s35.stop()
        ######################################################################
        if pygame.key.get_pressed()[pygame.K_BACKSPACE]:  # Not used
            print("Key \"BACKSPACE\" is hold pressed...")
        pygame.display.update()


if __name__ == "__main__":
    main()