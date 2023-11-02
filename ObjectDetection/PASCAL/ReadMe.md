# **VOC2012 Image and Annotation Visualization** Notebook

This repository contains a tool that facilitates the download, extraction, and visualization of the VOC2012 dataset, complete with bounding box annotations extracted from associated XML files.

## **Features**

- **Automated Dataset Download**: Fetches the VOC2012 dataset from Hugging Face's repository in ZIP format.
- **ZIP Extraction**: Conveniently unzips the downloaded dataset to provide access to images and their annotations.
- **Image Visualization**: Displays a select set of images from the dataset for preliminary visualization.
- **XML Annotation Processing**: Reads corresponding XML annotation files for chosen images.
- **Bounding Box Overlay**: Draws bounding boxes around annotated objects on the images, enhancing visualization.
- **Annotation Table Display**: Offers a structured view of extracted details from XML annotations in tabular format.

## **Requirements**

```css
cssCopy code
python [your_script_name].py

```

- **Python**: Version 3.x
- **Libraries**: As specified in **`requirements.txt`**, which includes:
    - requests
    - tqdm
    - pandas
    - matplotlib
    - opencv-python

## **Object Filters for Visualizations**

The tool comes equipped with a specific color mapping that governs the visual representation of certain objects when overlaying bounding box annotations on images. The current mapping is coded as:

```python
color_mapping = {'train': (0, 255, 0), 'person': (0, 0, 255)}
```

This implies:

- 'train' objects are rendered with **green** bounding boxes (RGB: **`(0, 255, 0)`**).
- 'person' objects are visualized with **blue** bounding boxes (RGB: **`(0, 0, 255)`**).

Objects not included in this mapping will not receive bounding boxes during visualization. For incorporating additional object types or altering existing color configurations, users can edit or extend the **`color_mapping`** dictionary. For instance, to visualize 'car' objects in red, an entry **`'car': (255, 0, 0)`** can be added.