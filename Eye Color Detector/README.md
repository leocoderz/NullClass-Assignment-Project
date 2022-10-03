# Eye-Color-detector
Simple Eye Color Detector using Machine Learning

## To simply run this model:
1. Clone this repository
2. Run the [Eye detector model](https://github.com/natarajaiml/Eye-Color-detector/ed1.ipynb) file
3. Upload the image you want to detect
4. Click on detect button
5. View results

## Installation 
#### Clone the project and install requirements
    $ git clone https://github.com/natarajaiml/NullClass-Assignment-Project
    $ cd NullClass-Assignment-Project
    $ sudo pip install -r requirements.txt

    [Note: if you have GPU change tensorflow to tensorflow-gpu in requirements.txt for fast processing]

#### Usage [Image]
    $ python eye-color.py --input_path=sample/2.jpg --input_type=image

**Output:**  

Diminant Eye Color:  Green  

|Color         | Percentage (%)|
|--------------|-----------|
|Blue |  0.0 |
|Blue Gray |  0.0 |
|Brown |  0.0 |
|Brown Gray |  0.0 |
|Brown Black |  0.0 |
|Green |  65.44 |
|Green Gray |  0.0 |
|Other |  34.56 |

<p align="left"><img src="sample/result.jpg" width="640"\></p>

#### Usage [Video/Webcam]
    $ python eye-color.py --input_path=sample/video.mp4 --input_type=video

**Output:**  

Dominant Eye Color:  Green

|Color         | Percentage (%)|
|--------------|-----------|
|Blue |  0.0 |
|Blue Gray |  0.0 |
|Brown |  0.0 |
|Brown Gray |  0.0 |
|Brown Black |  0.0 |
|Green |  18.58 |
|Green Gray |  0.79 |
|Other |  80.63 |

<p align="left"><img src="sample/result_video.jpg" width="640"\></p>

#### References
1. [MTCNN](https://github.com/ipazc/mtcnn)
2. [EYE COLOR](https://www.edow.com/general-eye-care/eyecolor/)
3. [HTML COLOR PICKER](https://www.w3schools.com/colors/colors_picker.asp?colorhex=ffff00)
4. [HSV COLOR MODEL](https://www.lifewire.com/what-is-hsv-in-design-1078068)
5. [RGB TO HSV](https://www.rapidtables.com/convert/color/rgb-to-hsv.html)
6. [EYE COLOR RANGE](https://github.com/jeffreyolchovy/whatismyeyecolor/blob/master/library/src/main/scala)


### Sample
1. [Sample output1](https://github.com/mridulshinghal123/Eye-Color-detector/blob/main/Sample1.png)
2. [Sample output 2](https://github.com/mridulshinghal123/Eye-Color-detector/blob/main/Sample%202.jpg)
