import os, cv2
from time import time

# remplacer 'videos/20images.mp4' par le chemin de la vidéo sur votre ordi :
video = cv2.VideoCapture('20images.mp4')

rep_images =  "20images_cv2"
if not os.path.exists(rep_images):
    os.mkdir(rep_images)
else:
    for f in os.listdir(rep_images): os.remove(rep_images+"/"+f)

#
# Extraction des méta-données de la vidéo avec video.get(...) :
#
nb_frame  = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
im_width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
im_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_fps = int(video.get(cv2.CAP_PROP_FPS))
video_dur = nb_frame/video_fps
print("nb_frames  :", nb_frame)
print("image size :",(im_width, im_height))
print("fps        :", video_fps)
print("duration   :", nb_frame/video_fps)

print("\nReady to extract {} frames".format(nb_frame))
i, t0 = 1, time()
ok, frame = video.read()
while ok:
    if i % 10 == 0 : print("{}...".format(i), end="")
    fichier = rep_images+"/image{:03d}.png".format(i)
    cv2.imwrite(fichier,frame)
    ok, frame = video.read()
    i += 1
t1 = time()
video.release() # fermer le fichier video
print("\n{} frames extracted in {:.1f} secondes".format(i-1,(t1-t0)))
