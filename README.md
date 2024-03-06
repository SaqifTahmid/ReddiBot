# ReddiBot

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview
This project implements a Neural Machine Translation (NMT) chatbot capable of handling Reddit conversations. Leveraging Python, TensorFlow, NumPy, and Pandas, the chatbot manages a vast dataset comprising 53 million Reddit comments and replies. The aim is to create an engaging and accurate conversational agent..

### Features

- Sequence-to-sequence NMT model
- Utilized TensorFlow, NumPy, and Pandas
- Dataset: 53 million Reddit comments and replies
- Achieved BLEU score of 23

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SaqifTahmid/ReddiBot
2. Donwload Reddit  DataSet:
   ```bash
   https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/)https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/
3. Download NMT Model:
   ```bash
   git clone https://github.com/daniel-kukiela/nmt-chatbot.git

## Note:
For the NMT Model it is extremely improtant you run the application in Python 3.6 evnironment as Tensorflow 1.X versions have been deprecated  and requires a Python virtual environment to run.

## STEPS:
1. First clone the repository files and download the Reddit dataset.
2. They change the directory of the code to match the location of where the dataset is stored.
3. Run the chat_database.py file
4. Run the traincreation.py file which will produce your test and training data from the created database
5. Before doing anything related to the NMT file it is extremely important that you run a Python 3.6 virtual environment. This can be done directly from Visula Studio Code.
6. Then follow the steams for installation from daniel-kukielas github repo.
7. Make sure CUDA V8 and Cudnn 6 is also installed and added to PATH.
8. Copy Paste your personal train.to and train.from data to the new_data folder in nmt
9. Run prepare_data.py and then run train.py
10. train.py may take close to 10 hours to upto 2 days depending on the month you're using so try to use tensorflow-gpu (if possible)

  # HAPPY CODING !

