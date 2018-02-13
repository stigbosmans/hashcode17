
file = None


def open_file(filename):
    global file
    file = open(filename, "w")


def write_number_cacheservers(no_cacheservers):
    global file
    file.write(no_cacheservers + '\n')


def write_cache_videos(cacheserver, *videos):
    global file
    string_videos = ""

    for i in videos:
        string_videos = string_videos + str(i) + " "

    file.write(str(cacheserver) + " " + string_videos + '\n')


def close_file():
    global file
    file.close()


"""
Usage:
    
    import FileWriter as writer

    -> Open/make file
    writer.open_file("submission.out")
    
    -> Write the number of used cacheservers
    writer.write_number_cacheservers(str(5))
    
    -> Write the cacheservers (first parameter) + videos on this server (other parameters)
    writer.write_cache_videos(6, 4, 8, 1, 78, 2)
    writer.write_cache_videos(839, 2345, 2345, 2474, 3, 284)
    
    -> Close file
    writer.close_file()
"""