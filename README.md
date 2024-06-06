## Reproducibility

This project is a marketing data analysis, the dataset was obtained from: https://www.kaggle.com/datasets/volodymyrgavrysh/bank-marketing-campaigns-dataset 
The goal of this analysis is to find ways to improve campaign targeting. In order to do that, we propose a set of predictive models included in project_file.ipynb.


This project was developed using the following environment:

- Python 3.11.1
- NumPy 1.24.3
- Pandas 1.5.2
- Matplotlib 3.6.3
- Seaborn 0.12.2
- Scikit-learn 1.2.2
- LightGBM 4.2.0
- XGBoost 2.0.1
- CatBoost 1.2.5
- LazyPredict 0.2.12
- MLxtend 0.23.1

All dependencies are listed in the `requirements.txt` file. To recreate the environment, run the following commands:

```sh
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows
myenv\Scripts\activate
# On macOS/Linux
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
