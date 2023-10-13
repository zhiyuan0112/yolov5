#!/usr/bin/env bash

SECONDS=0
python detect_multiprocess.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.1 --source data/test/ffmpeg
duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."


SECONDS=0
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.1 --source data/test/ffmpeg/smoke1
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.1 --source data/test/ffmpeg/smoke2
duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."