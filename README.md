# Vision Against Fire

## Getting Started

- First, [access this Google Drive link](https://drive.google.com/drive/folders/1rCaiRYvMJNxwsTDtj7LsTU5xmMMOJY5m?usp=sharing) to download the image files. These are the preprocessed images.
- Next, unzip the file. Each zip file will create `/data/fire` and `/data/nonfire`. Move one subfolder to another so that `fire` and `nonfire` folder are next to each other, under the `/data` folder.
- Now, access `src/firecv.ipynb` file and follow the cells.

## Where can I get the raw dataset?

### First, download all images from:
  
- [Forest Fire Images](https://www.kaggle.com/datasets/mohnishsaiprasad/forest-fire-images)
- [Fire Detection from CCTV](https://www.kaggle.com/datasets/ritupande/fire-detection-from-cctv)
- [Fire Segmentation Image Dataset](https://www.kaggle.com/datasets/diversisai/fire-segmentation-image-dataset)
- [The wildfire dataset](https://www.kaggle.com/datasets/elmadafri/the-wildfire-dataset)
- [Fire Detection Using Surveillance Camera on Roads](https://www.kaggle.com/datasets/tharakan684/urecamain)
- [Forest Fire Dataset](https://www.kaggle.com/datasets/alik05/forest-fire-dataset)
- [Wildfire Detection Image Data](https://www.kaggle.com/datasets/brsdincer/wildfire-detection-image-data)
- [Fire and Smoke dataset](https://www.kaggle.com/datasets/ashutosh69/fire-and-smoke-dataset)
- [Fire Images Database](https://www.kaggle.com/datasets/gondimjoaom/fire-images-database)
- [Forest Fire](https://www.kaggle.com/datasets/arbethi/forest-fire)
- [Fire-Gun](https://www.kaggle.com/datasets/parthmehta15/fire-gun)
- [Fire Detection Dataset](https://www.kaggle.com/datasets/christofel04/fire-detection-dataset)
- [fire and gun dataset](https://www.kaggle.com/datasets/atulyakumar98/fire-and-gun-dataset)
- [wild-fire](https://www.kaggle.com/datasets/ashukr/wildfire)
- [FOREST FIRE IMAGE DATASET](https://www.kaggle.com/datasets/cristiancristancho/forest-fire-image-dataset)
- [WildFire-Smoke-Dataset-Yolo](https://www.kaggle.com/datasets/ahemateja19bec1025/wildfiresmokedatasetyolo)
- [Fire detection dataset](https://www.kaggle.com/datasets/kabilan03/fire-detection-dataset)
- [Fire Detection in YOLO format](https://www.kaggle.com/datasets/ankan1998/fire-detection-in-yolo-format)
- [WildFire-Smoke-Dataset-Tensorflow](https://www.kaggle.com/datasets/ahemateja19bec1025/wildfiresmokedataset)

## Then, run the scripts in the following order.

- Resize and standarize images by running `src/move.py`
- Delete duplicate images by running `src/dedupe.py`
- Remove corrupted images by running `src/delete_if_corrupted.py`
- Augment images by running `src/aug.py`
- Delete duplicate images by running `src/dedupe.py`
- Remove corrupted images by running `src/delete_if_corrupted.py`
- Rename the files by running `rename.py`
- JPGify images by running `src/jpgify.py`
- Remove corrupted images by running `src/delete_if_corrupted.py`
