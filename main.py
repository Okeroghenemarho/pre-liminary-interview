from PIL import Image, ImageColor

COLORS_WORN= ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE",
          "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN", "ASH", "BROWN", "GREEN", "BROWN", "BLUE",
          "BLUE", "BLUE", "PINK", "PINK", "ORANGE","ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE",
          "BLUE","GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE","RED",
          "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN",
          "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE",
          "GREEN","GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED",
          "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]

color_counts = {}
for colors in COLORS_WORN:
    color_counts[colors] = color_counts.get(colors,0)+1
    highest_count = max(color_counts.values())
    lowest_count = min(color_counts.values())
    # to get the variance, highest minus lowest
    variance = highest_count - lowest_count
    # to get the most worn color
    most_worn_color = [colors for colors, count in color_counts.items() if count == highest_count]
# to get the median color. Median element is the element in the middle
median_color = COLORS_WORN[round(len(COLORS_WORN)/2)]
# to get the probability of choosing a red color
red_probability = COLORS_WORN.count("RED")/len(COLORS_WORN)
print(red_probability)
print(median_color)
print(variance)
print(most_worn_color)
print(color_counts)



# the function to get the mean color is not working. There is no rgb value for cream and ash in the getrgb method of ImageColor
# def get_mean_color(colors):
#     red = 0
#     green = 0
#     blue = 0
#
#     for color in colors:
#         rgb = ImageColor.getrgb(color)
#         red += rgb[0]
#         green += rgb[1]
#         blue += rgb[2]
#
#     number_of_colors = len(colors)
#     mean_red = red/number_of_colors
#     mean_green = green/number_of_colors
#     mean_blue = blue/number_of_colors
#
#     mean_color = f"#{mean_blue:02}{mean_green:02}{mean_red:02}"
#     print(mean_color)
#

# get_mean_color(COLORS_WORN)
