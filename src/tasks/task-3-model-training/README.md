# Mango Leaf Disease Detection Using Convolutional Neural Networks

This repository contains a comprehensive notebook that outlines a transfer learning approach for Mango Leaf Disease Classification using Convolutional Neural Networks (CNNs).

[Used Notebook: Mango Leaf Disease Detection Using CNN](https://www.kaggle.com/code/vencerlanz09/mango-leaf-disease-detection-using-cnn)

| Models               | Accuracy | Loss   |
|----------------------|----------|--------|
| MobilenetV2          | 97.36    | 0.07412|
| MobilenetV3Small     | 97.36    | 0.07893|
| MobilenetV3Large     | 98.94    | 0.05813|
| EfficientNetB0       | 97.89    | 0.06919|
| EfficientNetB1       | 98.42    | 0.06443|
| EfficientNetB2       | 96.57    | 0.15233|
| EfficientNetB3       | 97.1     | 0.08695|
| EfficientNetB7       | 96.57    | 0.1692 |
| EfficientNetV2B0     | 97.89    | 0.06002|
| EfficientNetV2B1     | 97.89    | 0.07018|
| EfficientNetV2B2     | 98.68    | 0.04708|
| EfficientNetV2B3     | 98.42    | 0.04803|
| EfficientNetV2S      | 98.42    | 0.03933|
| EfficientNetV2M      | 94.99    | 0.155  |
| EfficientNetV2L      | 97.1     | 0.07873|
| ResNet50             | 99.21    | 0.03731|
| ResNet101            | 98.68    | 0.05099|
| VGG16                | 56.2     | 1.10839|
| VGG19                | 84.96    | 2.02759|
| Xception             | 98.68    | 0.07547|
| InceptionV3          | 93.4     | 0.21293|
| InceptionResnetV2    | 93.4     | 0.21928|
| NasNetMobile         | 94.99    | 0.14235|
| NasNetLarge          | 94.46    | 0.16484|
| ResnetRS50           | 98.94    | 0.02524|


## Overview

Mango, known as the 'king of fruits', is a popular and nutritionally rich fruit with a unique flavor, fragrance, and taste. However, mango trees are often subjected to various diseases that can adversely affect fruit yield. Diseases like 'Anthracnose', 'Bacterial Canker', 'Die Back', and 'Powdery Mildew' are common afflictions for mango leaves.

Early detection of these diseases can aid in proper management and ensure high fruit yield. With advancements in technology, using CNNs to detect and classify these diseases in their early stages can be immensely helpful. This project harnesses the power of CNNs for mango leaf disease detection and classification.

## Diseases Detected

- Anthracnose
- Bacterial Canker
- Die Back
- Gall Midge
- Healthy
- Powdary Mildew
- Scooty Mould

## Implementation Details

- **Framework**: TensorFlow
- **Model**: ResNet50 (Transfer Learning)
- **Dataset**: Mango Leaf Disease Dataset
- **Metrics**: Accuracy, F1-Score

## Setup and Usage

1. Clone the repository.
2. Install the necessary libraries and dependencies.
3. Run the Jupyter notebook to train the model and evaluate its performance.

## Results

The model achieved an accuracy of 99.21% and an F1-score of 99.07% on the test dataset.

## Contributing

Feel free to fork or edit the notebook for your own convenience. If you liked the repository, consider starring it. Your support inspires further development and research in this area.

## Author's Note

Ensure to run the cells from top to bottom with a GPU accelerator. Some cells contain Linux commands, so it's important to take this into account. Any suggestions, comments, and recommendations to improve the notebook are highly appreciated.
