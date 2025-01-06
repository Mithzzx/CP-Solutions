import pyautogui as auto
from time import sleep
import sys

x = []

s = '''
 1. “Your beauty is magnetic; it draws me in like the tide to the moon.”
 2. “You have the kind of face that makes memories unforgettable.”
 3. “Your eyes have a depth that feels like falling into a peaceful dream.”
 4. “Every angle of your face is a testament to nature’s genius.”
 5. “Your features are delicate yet strong, like the finest porcelain.”
 6. “Your beauty has a quiet confidence, like it knows it doesn’t need to shout.”
 7. “Your presence feels like standing in a sunbeam, warm and radiant.”
 8. “Your hair flows like a river, smooth and endlessly captivating.”
 9. “You’re graceful in a way that feels effortless, like a bird in flight.”
 10. “Your freckles, if any, are like constellations connecting the universe of you.”
 11. “Your beauty has the richness of velvet—soft, luxurious, and timeless.”
 12. “Your expressions carry an elegance that artists dream of capturing.”
 13. “You glow with a natural light that feels like it comes from within.”
 14. “Your beauty is as serene as a quiet lake at dawn.”
 15. “The way your face lights up when you smile could rival any sunrise.”
 16. “Your beauty is like a whisper—it doesn’t demand attention, but it captivates anyway.”
 17. “There’s something about your face that feels like coming home.”
 18. “Your beauty is untamed, like wildflowers growing in a meadow.”
 19. “Your jawline has the precision of an artist’s perfect stroke.”
 20. “Your cheekbones could tell stories of strength and grace.”
 21. “Your eyes have a warmth that feels like being wrapped in a blanket on a cold day.”
 22. “Your beauty has the sharpness of a blade, cutting straight to my heart.”
 23. “There’s a harmony to your features, like a melody that never gets old.”
 24. “Your beauty is subtle yet powerful, like the pull of a hidden current.”
 25. “You carry yourself like royalty—regal and commanding.”
 26. “Your gaze has the intensity of a storm, wild and unforgettable.”
 27. “Your lips have the softness of silk, inviting and comforting.”
 28. “You’re stunning in a way that feels effortless, like nature just got it right.”
 29. “Your features are sculpted like they were meant to inspire awe.”
 30. “Your face is a perfect blend of strength and tenderness.”
 31. “The way you look at me feels like a secret meant only for us.”
 32. “Your beauty is as rare as a comet streaking across the night sky.”
 33. “Your elegance has a simplicity that makes everything else feel overdone.”
 34. “You have a timeless charm, like a classic film that never fades.”
 35. “Your face has a clarity that feels like fresh air after a storm.”
 36. “Your beauty is as soothing as the sound of rain on a quiet evening.”
 37. “There’s an energy in your features, like they’re alive with purpose.”
 38. “You’re like a piece of modern art—bold, striking, and unforgettable.”
 39. “Your silhouette has the grace of a willow tree swaying in the breeze.”
 40. “Your beauty has a wildness to it, like the untamed ocean.”
 41. “The way your lips curve when you speak is hypnotic.”
 42. “Your eyes have a sparkle that feels like an invitation to adventure.”
 43. “Your beauty has a rhythm, like the steady beat of a perfect song.”
 44. “Your aura carries a lightness that makes everything around you brighter.”
 45. “There’s a natural symmetry to your face that feels calming to look at.”
 46. “Your hands, your gestures, even the smallest movements are poetry in motion.”
 47. “Your beauty is understated, like a treasure waiting to be discovered.”
 48. “You have a glow that feels like it was borrowed from the stars.”
 49. “Your face is like a storybook, every detail worth reading over and over.”
 50. “Your beauty has a quiet strength, like the roots of a tree that hold everything steady.”'''
y= s.split('”')
c=1
for j in y:
    l = 6 if c < 10 else 7
    x.append(j[l:-1])
    c+=1

sleep(3)

l = len(x)
p = 0

c = 0

for i in x:
    auto.write(i)
    auto.press('enter')

    s = str(c) + ":| Line" + str(c + 4) + '\n'
    c = c + 1
    p = c / l * 100
    b = ("Loading.. " + str("%.4f" % p) + '%')
    
    # \r prints a carriage return first, so `b` is printed on top of the previous line.
    sys.stdout.write('\r' + s+b)

    sleep(8)
