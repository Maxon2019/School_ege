w = 60
h = 70

gor = w // 2 * 2 * w
wer = h // 2 * 2 * h

Ggw2 = (w - 2) // 2 * 2 + (h - 1) * (w // 2) * 2 + ((h - 1) // 2) * 2 + (w - 2) * (h // 2) * 2
Wgw2 = (h - 2) // 2 * 2 + (w - 1) * (h // 2) * 2 + ((w - 1) // 2) * 2 + (h - 2) * (w // 2) * 2
print(Ggw2 * gor + Wgw2 * wer)
