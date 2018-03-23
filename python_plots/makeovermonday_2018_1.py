'''
Dataset taken from makeovermonday Week 1
Data Source: National Chicken Council

'''
import load_data
import plotly
import plotly.graph_objs as go

# url of file path
url_path = "makeovermonday/2018-w-1-u-s-per-capita-consumption-of-poultry-livestock";

data = load_data.load(url_path);
dataset = load_data.select_data(data.dataframes);

def year_consumption():
    # Create a trace
    traces = [];
    col_names = ['beef','pork','broilers','turkey','commercial_fish_shell_fish'];
    for c in col_names:
        traces.append(go.Scatter(
            x = dataset['year'],
            y = dataset[c],
            name=c
        ))
    plotly.offline.plot(traces, filename='diagrams/year_by_consumption_per_poultry.html', auto_open=False);