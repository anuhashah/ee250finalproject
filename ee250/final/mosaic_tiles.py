import glob
from PIL import Image
from PIL import ImageFile
from scipy import spatial
import numpy as np
import os

def createPhotomosaic(photo):

    #photo that will become a photo mosaic
    main_photo_path = photo

    #tiles that create the photomosaic
    tile_photos_path = "tiles/*"
    tile_size = (15, 15)

    #Getting all the tiles from their folder
    tile_paths = []
    for file in glob.glob(tile_photos_path):
        tile_paths.append(file)

    tiles = []
    for path in tile_paths:
        tile = Image.open(path)
        tile = tile.resize(tile_size)
        tiles.append(tile)

    #Calculating the dominant color of each of the mosaic tiles
    colors = []
    for tile in tiles:
        dom_color = np.array(tile).mean(axis=0).mean(axis=0)
        colors.append(dom_color)


    #Pixelating the main photo that will be the photomosaic
    main_photo = Image.open(os.path.join(main_photo_path))
    width = int(np.round(main_photo.size[0] / tile_size[0]))
    height = int(np.round(main_photo.size[1] / tile_size[1]))
    resized_photo = main_photo.resize((width, height))

    # Creating  KDTree
    tree = spatial.KDTree(colors)

    # Emptying the integer array then storing the tile indices in there
    closest_tiles = np.zeros((width, height), dtype=np.uint32)

    for i in range(width):
        for j in range(height):
            pixel = resized_photo.getpixel((i,j))
            closest = tree.query(pixel)
            closest_tiles[i,j] = closest[1] 

    # Creating the output image
    output = Image.new('RGB', main_photo.size)

    # Drawing the tiles
    for i in range(width):
        for j in range(height):
            # Offset of tile
            x, y = i*tile_size[0], j*tile_size[1]
            # Index of tile
            index = closest_tiles[i, j]
            # Draw tile
            output.paste(tiles[index], (x, y))

    # Saving output
    output.save("output.jpg")
    output.show()

    