from PIL import Image
import sqlite3


filename_player_skin_ = "photos/skin.png"
filename_yellow_bandage = "bandages/yellow_bandage.png"

filename_pass_ = 'bandages/pyssto.png'


def search_bandages(size, color):
    con = sqlite3.connect('bandages_search.sql')
    cur = con.cursor()

    bandage = cur.execute(f"""SELECT file_name from bandages
    WHERE color = '{color}' and size = '{size}'""").fetchall()

    global filename_yellow_bandage
    filename_yellow_bandage = bandage[0][0]


def bandage_maker(filename_player_skin):
    with Image.open(filename_player_skin) as img_player_skin:
        img_player_skin.load()

    with Image.open(filename_yellow_bandage) as img_yellow_bandage:
        img_yellow_bandage.load()

    img_yellow_bandage.show()

    with Image.open(filename_pass_) as img_pass_:
        img_pass_.load()

    # img_player_skin.paste(
    #     img_pass_, (48, 55))

    img_player_skin.paste(
        img_yellow_bandage, (48, 55))

    img_player_skin.save('photos/you.png')

    img_player_skin.show()


# bandage_maker(filename_player_skin_)