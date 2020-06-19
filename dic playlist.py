print("Welcome to my playlist")
name = "Terry"
playlist_name = "My rock"
print(f"Created by: {name} Playlist Name: {playlist_name}")

songlist ={ 'song' : [
    {"Song name" : "Baby ko base pasand hai" , "Singer" : ['Vishal Dadlani', 'Shalmali kholgade', 'Badshah'], 'Duration' : 4.13 },
    {"Song name" : "Angrezi beat" , "Singer" : ['Gippy Grewal', 'Yo Yo Honey Singh'], 'Duration' : 3.26 },
    {"Song name" : "Panda" , "Singer" : ['Desiigner'], 'Duration' : 3.46 },
    {"Song name" : "2002" , "Singer" : ['Anne Marie'], 'Duration' : 3.06 },
    {"Song name" : "Bekhayali" , "Singer" : ['Sachet Tondon'], 'Duration' : 6.12 },
    {"Song name" : "Ghungroo" , "Singer" : ['Arijit Singh', 'Shilpa Rao'], 'Duration' : 5.03 }
            ]
}
total_length = 0
for s in songlist['song']:

    total_length += int(s['Duration'])
    print(s["Song name"])
    

print("duration of playlist: ", total_length)