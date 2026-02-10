# MSED - Modelación de Socio-Economic Dynamics

A mathematical modeling project for analyzing population dynamics, health sector expenditure, and tourism economics in Chile and Mexico using differential equations and statistical regression.

## Overview

MSED (Modelación de Socio-Economic Dynamics) provides a comprehensive framework for modeling and forecasting demographic and economic trends through:

- **Population Modeling**: Analysis of age-group dynamics (children 0-14, adults 15-64, elderly 65+)
- **Health Sector Analysis**: Healthcare expenditure trend modeling
- **Tourism Economics**: Analysis of tourism arrivals and revenue patterns
- **Numerical Methods**: Runge-Kutta 4th-order (RK4) methods for solving differential equations

## Project Structure

```
MSED/
├── code/                      # Analysis notebooks and scripts
│   ├── poblaciones/          # Population dynamics (Chile & Mexico)
│   ├── sectores_economia/    # Economic sector modeling
│   └── sectores_salud/       # Health sector analysis
├── data/                      # Datasets
│   ├── raw/                  # Original data (Excel/CSV)
│   └── processed/            # Cleaned and processed data
├── documentation/             # Analysis documentation
│   └── Analisis_poblacional/ # LaTeX reports for Chile & Mexico
├── utils/                     # Reusable utilities
│   ├── RK.py                 # Runge-Kutta solver implementation
│   ├── modelacion.py         # Regression + ODE workflow
│   ├── tasas.py              # Exchange rate utilities
│   └── requirements.txt      # Python dependencies
└── archive/                   # Previous deliverables and scripts
```

## Methodology

The project follows a structured workflow for socio-economic modeling:

### 1. Data Collection
- Gather historical data from census, government reports, and economic databases
- Store raw data in `data/raw/` (population, health expenditure, tourism statistics)

### 2. Data Preprocessing
- Normalize European notation and handle missing values
- Clean and structure data for analysis
- Output processed datasets to `data/processed/`

### 3. Statistical Analysis
- Apply linear regression using `statsmodels.OLS` to fit trends
- Extract coefficients to build differential equations
- Validate statistical significance of models

### 4. Differential Equation Construction
- Convert regression models into systems of ordinary differential equations (ODEs)
- Define initial conditions based on historical data
- Specify time periods for prediction

### 5. Numerical Solution
- Implement Runge-Kutta 4th-order (RK4) method for ODE solving
- Generate predictions through specified time periods
- Compare model outputs with actual data

### 6. Visualization & Reporting
- Create graphs and visualizations using matplotlib
- Generate comprehensive reports using LaTeX
- Document findings in Jupyter notebooks

## Technologies

**Python Stack:**
- `pandas` & `numpy` - Data processing and numerical operations
- `statsmodels` & `scipy` - Statistical modeling and optimization
- `matplotlib` - Visualization
- `jupyter` - Interactive notebooks for analysis

**Documentation:**
- LaTeX - Professional report generation
- Markdown - Notebook documentation

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Lunaaaalj/MSED.git
cd MSED
```

2. Install dependencies:
```bash
pip install -r utils/requirements.txt
```

3. Launch Jupyter notebooks:
```bash
jupyter notebook
```

## Usage

### Population Analysis Example

Navigate to population analysis notebooks:
```bash
cd code/poblaciones
jupyter notebook
```

Open the desired notebook (e.g., Chile or Mexico analysis) to:
- Load historical population data
- Run regression analysis on age groups
- Solve population dynamics ODEs using RK4
- Generate forecasts and visualizations

### Health Sector Analysis

Analyze healthcare expenditure trends:
```bash
cd code/sectores_salud
jupyter notebook
```

### Tourism Economics

Study tourism patterns:
```bash
cd code/sectores_economia
jupyter notebook
```

## Key Features

### Runge-Kutta 4th Order Solver
The `utils/RK.py` module provides a custom RK4 implementation for solving systems of ODEs:

```python
from utils.RK import runge_kutta_4
# Solve ODE system with initial conditions and time steps
```

### Modeling Pipeline
The `utils/modelacion.py` module integrates regression and ODE solving:

```python
from utils.modelacion import modelo_poblacion
# Run complete regression → ODE → prediction pipeline
```

## Data Sources

The project analyzes data from:
- **Population**: Census data and demographic projections (2005-2019+)
- **Health**: Government expenditure on healthcare systems
- **Tourism**: Arrival statistics and revenue data with currency conversion
- **Infrastructure**: Supporting economic metrics

## Documentation

Detailed analysis reports are available in `documentation/`:
- `Analisis_poblacional/chile/modelacion_chile.pdf` - Chile population model
- `Analisis_poblacional/mexico/modelacion_mexico.pdf` - Mexico population model

Each notebook contains inline documentation with:
- Markdown explanations of methodology
- Code comments for key operations
- Visualization interpretations

## Contributing

This is an academic research project. For questions or collaborations, please open an issue.

## License

Please refer to the repository license file for usage terms.

## Acknowledgments

This project applies mathematical modeling techniques to real-world socio-economic data for Chile and Mexico, providing insights into demographic shifts, healthcare trends, and tourism economics.
