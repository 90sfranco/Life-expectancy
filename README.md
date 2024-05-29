<p align="center">
  <div style="display: flex; justify-content: center; align-items: center;">
    <img width="180" src="./public/image1.jpg" alt="Life Expectancy">
  </div>
  <h1 align="center">⚙️ Life Expectancy ⚙️</h1>
</p>

Welcome! This repository contains an exercise focused on the analysis of data related to life expectancy in different countries around the world. The challenge is to use a provided dataset to perform cleaning processes and build a unique predictive model. This model will be employed to predict life expectancy based on associated variables, thus providing a deeper understanding of the factors that influence the longevity of populations globally. In addition, the Dash visualization tool will be used to create an interactive dashboard to explore the data and predictions dynamically.


## Project Structure 📃
The structure of the directories and files is as follows:

<pre>

  ├── model
  │ └── random_forest_model.pkl
  ├── notebooks
  │ ├── Life Expectancy Data.csv
  │ └── Migration_EDA.ipynb
  ├── public
  │ └── image1.png
  ├── dashboard_dash.py
  ├── README.md
  └── requirements.txt
</pre>


### Folders 📁
- **model 📑:** This folder stores the predictive model.
- **notebooks 📚:**  Here are the files related to data exploration and analysis. “Life Expectancy Data.csv” is the dataset used, and “Migration_EDA.ipynb” is a Jupyter notebook used to perform exploratory data analysis.

The root contains the following: a script file named “dashboard_dash.py” for the Dash interactive dashboard, an image named “image1.png” and two text files, “README.md” which provides information about the project, and “requirements.txt” which lists the project dependencies.

## Installation Requirements ✔️
To optimize the efficiency of your computer, you can choose to create a virtual environment where you can download the libraries, this is not mandatory and you can create one with this command:

```
python -m venv venv
```

To get inside the virtual environment, use these commands:

```
cd venv
```

```
cd Scripts
```

```
activate
```
Once you have created the virtual environment (or not), execute this command to download the libraries:
```
pip install -r requirements.txt
```
Make sure to be in the proyect root to install de dependecies

## Project Execution 🚀

1. In a terminal, enter in a folder that you want to clone the repository:
    ```
    cd your_folder
    ```

2. Clone the repository using this command:
    ```
    git clone https://github.com/90sfranco/Life-expectancy.git
    ```

3. In the notebooks you can watch the EDA proccess, in the same way, you can watch the code for the visualization with Dash, however, you are free to execute the notebook executing this command
    ```
    cd notebooks
    ```
    ```
    python Migration_EDA.ipynb
    ```

    Also, execute this command to run the Dash service:
    Go to the root(If you ran the notebook how I told you)
    ```
    cd ..
    ```
    And run the service
    ```
    python dashboard_dash.py
    ```

## Contact 📧
If you have any questions or need further assistance, feel free to contact me:
- [david_fel.martinez@uao.edu.co](mailto:david_fel.martinez@uao.edu.co)
- [john_david.franco@uao.edu.co](mailto:john_david.franco@uao.edu.co)