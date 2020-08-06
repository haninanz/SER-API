# SER-API
This API employed Python's Flask as framework to ensure easy navigation and better experience in utilizing the SER model. It accepted an audio file (.wav extension) as input and return the prediction in 2 forms; written in the UI and jsonified.

## Usage
Before running this API, please make sure to pay attention to these few things:
* The audio file you upload must be in **.wav extension**, and contains only utterances to be predicted
* Keep the file to be uploaded in the **same directory** as [API.py](https://github.com/haninanz/SER-API/blob/master/API.py)
* Other than the audio files you want to upload, please don't make any changes in the directory

To use this API, follow these steps below:
1. Open your command prompt.
2. Go to the specific folder the API is located, and run API.py with Python.
3. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser. The page will be as follows: ![Image of SER API](https://github.com/haninanz/SER-API/blob/master/ui1.png)
4. Upload your file and submit it. The predicted emotion will shows up on the UI after a while. To retrieve the jsonified, click on the JSON tab.
