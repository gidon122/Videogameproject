### Overview
This project analyzes video game sales data to understand patterns in revenue across different regions and countries. It uses a cleaned dataset of sales records and creates visual insights to highlight regional performance and profit distribution.

### Dataset
The project uses the file VideoGamesSales.csv, which contains information about video games including:
- Rank
- Name
- Platform
- Year
- Month
- Genre
- Publisher
- Country
- City
- State
- Region
- National Sales
- Global Sales
- National Profit
- Global Profit

### Objective
The main goal of this project is to:
- explore video game sales trends
- compare performance across regions and countries
- identify top-performing markets
- visualize sales and profit data in a clear and understandable way

### Tools and Libraries
This project is built using Python and common data science libraries:
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Data Cleaning Process
Before analysis, the dataset is cleaned by:
- removing duplicate rows
- filling missing region values
- standardizing country names
- converting sales fields to numeric values
- handling missing values
- reducing extreme outlier values for better visualization

### Visualizations
The notebook includes charts such as:
- National Sales by Region and Country
- Global Sales by Region

These charts help communicate which markets contribute most to overall sales and where revenue is concentrated.

### Project Structure
- `VideoGamesSales.csv` — dataset used for analysis
- `Untitled.ipynb` — notebook containing the full workflow, cleaning, and visualizations

### How to Use
1. Open the notebook in Jupyter or VS Code.
2. Ensure all required libraries are installed.
3. Run the notebook cells in order.
4. Review the cleaned dataset and generated charts.

### Insights
The analysis helps answer questions such as:
- Which region has the highest sales?
- Which countries contribute most to national sales?
- How does global sales compare across regions?
- What patterns emerge in sales by genre, platform, or publisher?

### Conclusion
This project is a practical example of sales data exploration and visualization in Python. It combines data cleaning, transformation, and storytelling through charts to make the business performance of video games easier to understand.

---
