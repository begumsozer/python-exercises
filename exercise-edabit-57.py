def get_frame(w, h, ch):
  if h <= 2 or w<= 2:
    return "invalid"
  top=[[ch*w]]
  side=[[ch+" "*(w-2)+ch]]*(h-2)
  return top+side+top

print(get_frame(4, 5, "#"))
