#  ascıı art denen bir yazılım içerisinde sanat var onu yapmanızı isteyeceğiz internetten yardım alabilirsiniz
# elmas yapmanızı istiyoruz
#
# Örnek:
#       *
#      ***
#     *****
#    *******
#   *********
#    *******
#     *****
#      ***
#       *
# şeklinde

size = int(input("Elmasın merkezden itibaren yüksekliğini girin: "))

for i in range(1, size + 1):
    print(" " * (size - i) + "a" * (2 * i - 1))
for i in range(size - 1, 0, -1):
    print(" " * (size - i) + "a" * (2 * i - 1))
