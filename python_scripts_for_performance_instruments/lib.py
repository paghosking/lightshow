#!/usr/bin/python
import chroma

# class for handling color mixing for PERFORMANCE INSTRUMENTS
class MidiColor:
    def __init__(self, no_of_colors):
        # self.output_color = chroma.Color('#000000')
        # self.no_of_colors = 12
        self.lookup_table = {}
        self.channels = []
        self.change_mode(1)
        # for i in range(0,self.no_of_colors):
        # for i in self.lookup_table:
        #     self.lookup_table[i] = chroma.Color('#000000')
        self.color_counts = {}
        # for j in range(0, self.no_of_colors):
        #for j, i in enumerate(self.lookup_table):
        for j in self.channels:
            self.color_counts[j] = [0, 0]
            #print j, self.color_counts[j]
        #print self.color_counts

    # define the different color palette modes
    def change_mode(self, mode):
        self.output_color = chroma.Color('#000000')
        if mode == 1: # drum palette 1 (reds)
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(45/(len(self.channels)))
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')  # C
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A

        elif mode == 2: # drum color palette (greens)
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(45/(len(self.channels)))+90
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')  # C
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 3: # drums color palette (blues)
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(45/(len(self.channels)))+210
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')  # C
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 4: # mode for keyboard (blues)
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(45/(len(self.channels))) + 210
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')  # C
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 5: # mode for keyboard (Greens)
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(45/(len(self.channels))) + 90
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')  # C
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A

        elif mode == 6: # mode for keyboard (reds)
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(45/(len(self.channels)))
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')  # C
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 7: # mode for drums
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(6/(len(self.channels)))
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')  # C
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 8: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 327
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 9: # mode for keyboard (blues)
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 27
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 10: # mode for drums
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 260
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 11: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 293
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 12: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 220
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 13: # mode for drums
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 150
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 14: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 120
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 15: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 180
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A

        elif mode == 16: # mode for drums
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 30
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 17: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 240
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 18: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 140
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A


        elif mode == 19: # mode for drums
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 210
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 20: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels)))
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 21: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(6/(len(self.channels))) + 60
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A

        elif mode == 22: # mode for drums
            self.channels = [33, 43, 47, 48, 31, 51, 46, 49, 42, 85] # in order of basines
            for i in range(0,len(self.channels)):
                hue = i*int(360/(len(self.channels)))
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[0]] = chroma.Color('#ff00ff')  # C
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 23: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(360/(len(self.channels)))
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        elif mode == 24: # mode for keyboard
            self.channels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # in order of basines
            for i in range(0, len(self.channels)):
                hue = i*int(360/(len(self.channels)))
                self.lookup_table[self.channels[i]] = chroma.Color((hue, 1, 1), 'HSV')
            # self.lookup_table[self.channels[1]] = chroma.Color('#ff0000')  # C#
            # self.lookup_table[self.channels[2]] = chroma.Color('#00ffff')  # D
            # self.lookup_table[self.channels[3]] = chroma.Color('#ffff00')  # D#
            # self.lookup_table[self.channels[4]] = chroma.Color('#00ff00')  # E
            # self.lookup_table[self.channels[5]] = chroma.Color('#ff00ff')  # F
            # self.lookup_table[self.channels[6]] = chroma.Color('#00ffff')  # F#
            # self.lookup_table[self.channels[7]] = chroma.Color('#ffff00')  # G
            # self.lookup_table[self.channels[8]] = chroma.Color('#0000ff')  # G#
            # self.lookup_table[self.channels[9]] = chroma.Color('#00ff00')  # A
        self.color_counts = {}
        # for j in range(0, self.no_of_colors):
        #for j, i in enumerate(self.lookup_table):
        for j in self.channels:
            self.color_counts[j] = [0, 0]



    def add_color(self, color_ref, vel, max_vel):
        vel /= float(2 * max_vel)
        vel = self._clamp(vel, 0, 0.5)
        self.color_counts[color_ref][0] += 1
        self.color_counts[color_ref] = [self.color_counts[color_ref][0], vel]
        self.color_counts[color_ref][0] = self._clamp(self.color_counts[color_ref][0], 0, 1)
        self._mix_colors()

    def rem_color(self, color_ref):
        self.color_counts[color_ref][0] -= 1
        self.color_counts[color_ref][0] = self._clamp(self.color_counts[color_ref][0], 0, 1)
        self._mix_colors()

    def _mix_colors(self):
        self.output_color.rgb = (0, 0, 0)
        # for i in range(0, self.no_of_colors):
        #for i, j in enumerate(self.lookup_table):
        for i in self.channels:
            # if self.color_counts[i][0]:
                # self.output_color = self.output_color + self.lookup_table[i]
            # elif self.color_counts[i][1]:
            hue_value = self.lookup_table[i].hsv[0]
            self.output_color = self.output_color + chroma.Color((hue_value,
                                                                  self.lookup_table[i].hsv[1],
                                                                  self.color_counts[i][1]),
                                                                 'HSV')

    def _clamp(self, n, minn, maxn):
        return max(min(maxn, n), minn)

    def update(self):
        # for i in range(0, self.no_of_colors):
        #for i, j in enumerate(self.lookup_table):
        for i in self.channels:
            if self.color_counts[i][0] and self.color_counts[i][1]:
                self.color_counts[i][1] -= 0.002
                self.color_counts[i][1] = self._clamp(self.color_counts[i][1], 0, 1)
                self._mix_colors()
                if self.color_counts[i][1] <= 0:
                    self.color_counts[i][0] = 0
            elif (not self.color_counts[i][0]) and self.color_counts[i][1]:
                self.color_counts[i][1] -= 0.01 * 2
                self.color_counts[i][1] = self._clamp(self.color_counts[i][1], 0, 1)
                self._mix_colors()
