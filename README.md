## Reproducibility

This project was developed using the following environment:

- Python 3.8.10
- NumPy 1.21.0
- Pandas 1.3.0
- Matplotlib 3.4.2
- Seaborn 0.11.1
- SciPy 1.7.0
- Scikit-learn 0.24.2
- LightGBM 3.2.1
- XGBoost 1.4.2
- CatBoost 0.26
- LazyPredict 0.2.9
- MLxtend 0.19.0

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
