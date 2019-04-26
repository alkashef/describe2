
## Project description

An extension to Pandas' describe function. It operates on a Pandas dataframe to produce a dataframe of stats for numerical columns and another dataframe of stats for categorical columns.

Numerical columns are selected using: 

	df.select_dtypes(include=['number'])

While categorical columns are selected using: 

	df.select_dtypes(include=['object'])

See the [numpy dtype hierarchy](https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html).

### Numerical column stats:
- Type 	
- Density 	
- No. of Values 	
- No. of Unique Values 	
- No. of NaN 	
- No. of Zeros 	
- No. of +ve Values 	
- Min 	
- Max 	
- Mean 	
- Std 	
- Median 	
- Mode 	
- Skew 	
- Kurtosis 	
- No. of 3 Sigma Outliers

### Object column stats:
- Type 	
- Density 	
- No. of Values 	
- No. of Unique Values 	No. of NaN

## Project Files

- **datasets**: A folder containing a set of CSV datasets.
- **describe2.py**: Describe2 Python class file.
- **examples.ipynb**: A Jupyter notebook demonstrating Describe2 on sample datasets.
- **README.md**: This file. It contains information about the project.
- **LICENSE.txt**: GNU GPL v3.0 License file. 

## Usage

Import Describe2:

	import Describe2
	describe2 = Describe2.Describe2()

Generate stats for a dataset:

	cars = pd.read_csv('cars.csv')
	num, obj = describe2.d2(cars)

`num` is a dataframe holding the numerical columns stats,
and `obj` is a dataframe holding the categorical columns stats.
 
## License

This is an open source free program provided under Version 3 of the GNU GENERAL PUBLIC LICENSE. A copy of the license is available in LICENSE.txt at the root of the source code. If not, please see <http://www.gnu.org/licenses/>.
