## Reproducibility

This project was developed using the following environment:

- Python 3.8.10
- NumPy 1.26.3
- Pandas 1.5.3
- Matplotlib 3.7.1
- Seaborn 0.12.2
- SciPy 1.10.1
- Scikit-learn 1.3.2
- LightGBM 3.3.5
- XGBoost 1.7.5
- CatBoost 1.2.2
- LazyPredict 0.2.12
- MLxtend 0.23.0

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
