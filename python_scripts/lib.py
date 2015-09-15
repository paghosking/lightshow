#!/usr/bin/python
import chroma

# class for handling color mixing and output
class MidiColor:
    def __init__(self, no_of_colors):
        self.output_color = chroma.Color('#000000')
        self.no_of_colors = 12
        self.lookup_table = {}
        for i in range(0,self.no_of_colors):
            self.lookup_table[i] = chroma.Color('#000000')
        self.color_counts = {}
        for j in range(0, self.no_of_colors):
            self.color_counts[j] = [0, 0]

    # define the different color palette modes
    def change_mode(self, mode):
        self.output_color = chroma.Color('#000000')
        if mode == 1: # mode for color scores
            self.no_of_colors = 12
            self.lookup_table[0] = chroma.Color('#ff0000')  # C RED
            self.lookup_table[1] = chroma.Color('#000000')  # C#
            self.lookup_table[2] = chroma.Color('#ff4400')  # D ORANGE
            self.lookup_table[3] = chroma.Color('#000000')  # D#
            self.lookup_table[4] = chroma.Color('#ff8800')  # E YELLOW
            self.lookup_table[5] = chroma.Color('#00ff00')  # F GREEN
            self.lookup_table[6] = chroma.Color('#000000')  # F#
            self.lookup_table[7] = chroma.Color('#00ffcc')  # G TEAL
            self.lookup_table[8] = chroma.Color('#000000')  # G#
            self.lookup_table[9] = chroma.Color('#0000ff')  # A BLUE
            self.lookup_table[10] = chroma.Color('#000000')  # A#
            self.lookup_table[11] = chroma.Color('#ff00cc')  # B PURPLE
        elif mode == 2:
            self.no_of_colors = 12
            self.lookup_table[0] = chroma.Color('#ff0000')  # C
            self.lookup_table[1] = chroma.Color('#ff0000')  # C#
            self.lookup_table[2] = chroma.Color('#ff0000')  # D
            self.lookup_table[3] = chroma.Color('#ff0000')  # D#
            self.lookup_table[4] = chroma.Color('#ff0000')  # E
            self.lookup_table[5] = chroma.Color('#ff0000')  # F
            self.lookup_table[6] = chroma.Color('#ff0000')  # F#
            self.lookup_table[7] = chroma.Color('#ff0000')  # G
            self.lookup_table[8] = chroma.Color('#ff0000')  # G#
            self.lookup_table[9] = chroma.Color('#ff0000')  # A
            self.lookup_table[10] = chroma.Color('#ff0000')  # A#
            self.lookup_table[11] = chroma.Color('#ff0000')  # B
        elif mode == 3:
            self.no_of_colors = 12
            self.lookup_table[0] = chroma.Color('#000000')  # C
            self.lookup_table[1] = chroma.Color('#00ff00')  # C#
            self.lookup_table[2] = chroma.Color('#00ff00')  # D
            self.lookup_table[3] = chroma.Color('#00ff00')  # D#
            self.lookup_table[4] = chroma.Color('#00ff00')  # E
            self.lookup_table[5] = chroma.Color('#00ff00')  # F
            self.lookup_table[6] = chroma.Color('#00ff00')  # F#
            self.lookup_table[7] = chroma.Color('#00ff00')  # G
            self.lookup_table[8] = chroma.Color('#00ff00')  # G#
            self.lookup_table[9] = chroma.Color('#00ff00')  # A
            self.lookup_table[10] = chroma.Color('#00ff00')  # A#
            self.lookup_table[11] = chroma.Color('#00ff00')  # B
        elif mode == 4:
            self.no_of_colors = 12
            self.lookup_table[0] = chroma.Color('#0000ff')  # C
            self.lookup_table[1] = chroma.Color('#0000ff')  # C#
            self.lookup_table[2] = chroma.Color('#0000ff')  # D
            self.lookup_table[3] = chroma.Color('#0000ff')  # D#
            self.lookup_table[4] = chroma.Color('#0000ff')  # E
            self.lookup_table[5] = chroma.Color('#0000ff')  # F
            self.lookup_table[6] = chroma.Color('#0000ff')  # F#
            self.lookup_table[7] = chroma.Color('#0000ff')  # G
            self.lookup_table[8] = chroma.Color('#0000ff')  # G#
            self.lookup_table[9] = chroma.Color('#0000ff')  # A
            self.lookup_table[10] = chroma.Color('#0000ff')  # A#
            self.lookup_table[11] = chroma.Color('#0000ff')  # B
        else:
            self.no_of_colors = 12
            self.lookup_table[0] = chroma.Color('#28ff00')  # C
            self.lookup_table[1] = chroma.Color('#00ffe8')  # C#
            self.lookup_table[2] = chroma.Color('#007cff')  # D
            self.lookup_table[3] = chroma.Color('#0500ff')  # D#
            self.lookup_table[4] = chroma.Color('#4500ea')  # E
            self.lookup_table[5] = chroma.Color('#57009e')  # F
            self.lookup_table[6] = chroma.Color('#740000')  # F#
            self.lookup_table[7] = chroma.Color('#b30000')  # G
            self.lookup_table[8] = chroma.Color('#ee0000')  # G#
            self.lookup_table[9] = chroma.Color('#ff6300')  # A
            self.lookup_table[10] = chroma.Color('#ffec00')  # A#
            self.lookup_table[11] = chroma.Color('#99ff00')  # B

        self.color_counts = {}
        for j in range(0, self.no_of_colors):
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
        for i in range(0, self.no_of_colors):
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
        for i in range(0, self.no_of_colors):
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
