def print_stars(star_count):
    print("Вот ваши звезды :)")
    stars = "".join(["*" for _ in range(star_count)])
    print(stars)


print("Сколько вам звезд на погоны?")
star_count = int(input())
print_stars(star_count)
