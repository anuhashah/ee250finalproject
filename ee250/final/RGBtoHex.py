def clamp(x): 
  return max(0, min(x, 255))


def hexadecimal(RGB):
  r = clamp(int(RGB[0]))
  g = clamp(int(RGB[1]))
  b = clamp(int(RGB[2]))
  return "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))
