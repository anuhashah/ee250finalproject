def clamp(x): 
  return max(0, min(x, 255))


def hexadecimal(RGB):
  r = clamp(RGB[0])
  g = clamp(RGB[1])
  b = clamp(RGB[2])
  return "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))


data = [73,128,99]
hexa = hexadecimal(data)
print("RGB: ("  + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ") = Hexadecimal: " + hexa)
