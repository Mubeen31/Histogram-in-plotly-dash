import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd


player = pd.read_csv('nhl_draft_2013_@thejustinfisher.csv')


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([

    html.Div([
        html.Div([
            html.Div([
                html.H3('Histogram', style = {'margin-bottom': '0px', 'color': 'black'}),
            ])
        ], className = "create_container1 four columns", id = "title"),

    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),


    html.Div([
        html.Div([
             html.P('Select Type', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
             dcc.RadioItems(id = 'radio_items',
                            labelStyle = {"display": "inline-block"},
                            options = [
                                      {'label': 'Histogram (count)', 'value': 'HistCount'},
                                      {'label': 'Histnorm (percent)', 'value': 'HistPerc'},
                                      {'label': 'Histnorm (probability density)', 'value': 'HistPD'},
                                      {'label': 'Histogram (cumulative)', 'value': 'Histogram (cumulative)'},
                                      {'label': 'Histogram (overlay or stack)', 'value': 'Histogram (overlay or stack)'},
                                      {'label': 'Histogram (histfunction)', 'value': 'Histogram (histfunction)'}],
                            value = 'HistCount',
                            style = {'text-align': 'center', 'color': 'black'}, className = 'dcc_compon'),

             ], className = "create_container2 five columns", style = {'margin-bottom': '20px'}),

    ], className = "row flex-display"),



    html.Div([
        html.Div([
            dcc.Graph(id = 'multi_chart',
                      config = {'displayModeBar': 'hover'}),

        ], className = "create_container2 eight columns"),

    ], className = "row flex-display"),

], id= "mainContainer", style={"display": "flex", "flex-direction": "column"})


@app.callback(Output('multi_chart', 'figure'),
              [Input('radio_items', 'value')])
def update_graph(radio_items):




    if radio_items == 'HistCount':



     return {
        'data':[go.Histogram(
                    x = player['Height'],
                    name = 'Height',
                    marker = dict(
                       color = 'rgba(246, 78, 139, 0.4)',
                       line = dict(color = 'black', width = 2)
                                 )
                    # hoverinfo='text',
                    # hovertext=
                    # '<b>Country</b>: ' + terr2['country_txt'].astype(str) + '<br>' +
                    # '<b>Year</b>: ' + terr2['iyear'].astype(str) + '<br>' +
                    # '<b>Height</b>: ' + [f'{x:,.0f}' for x in player['Height']] + '<br>'
              )],


        'layout': go.Layout(
             bargap = 0.01,
             bargroupgap = 0,
             plot_bgcolor='#F2F2F2',
             paper_bgcolor='#F2F2F2',
             title={
                 'text': '<b>Player Height</b>',

                 'y': 0.95,
                 'x': 0.5,
                 'xanchor': 'center',
                 'yanchor': 'top'},
             titlefont={
                        'color': 'black',
                        'size': 15},

             hovermode='closest',
             xaxis=dict(title='<b>Height</b>',
                        color = 'black',
                        showline = True,
                        showgrid = False,
                        showticklabels = True,
                        linecolor = 'black',
                        linewidth = 1,
                        ticks = 'outside',
                        tickfont = dict(
                            family = 'Arial',
                            size = 12,
                            color = 'black'


                )),

             yaxis=dict(title='<b>Count</b>',
                        color = 'black',
                        showline = False,
                        showgrid = True,
                        showticklabels = True,
                        linecolor = 'black',
                        linewidth = 1,
                        ticks = '',
                        tickfont = dict(
                            family = 'Arial',
                            size = 12,
                            color = 'black'
                        )

                ),

            legend = {
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'x': 0.5,
                'y': 1.25,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black',
                 )
        )

    }

    elif radio_items == 'HistPerc':

        return {
            'data': [go.Histogram(
                x = player['Height'],
                histnorm = 'percent',
                name = 'Height',
                marker = dict(
                    color = 'rgba(0, 158, 158, 0.4)',
                    line = dict(color = 'black', width = 2)
                )
                # hoverinfo='text',
                # hovertext=
                # '<b>Country</b>: ' + terr2['country_txt'].astype(str) + '<br>' +
                # '<b>Year</b>: ' + terr2['iyear'].astype(str) + '<br>' +
                # '<b>Height</b>: ' + [f'{x:,.0f}' for x in player['Height']] + '<br>'

            )],

            'layout': go.Layout(
                bargap = 0.01,
                bargroupgap = 0,
                plot_bgcolor = '#F2F2F2',
                paper_bgcolor = '#F2F2F2',
                title = {
                    'text': '<b>Player Height</b>',

                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont = {
                    'color': 'black',
                    'size': 15},

                hovermode = 'closest',
                xaxis = dict(title = '<b>Height</b>',
                             color = 'black',
                             showline = True,
                             showgrid = False,
                             showticklabels = True,
                             linecolor = 'black',
                             linewidth = 1,
                             ticks = 'outside',
                             tickfont = dict(
                                 family = 'Arial',
                                 size = 12,
                                 color = 'black'

                             )),

                yaxis = dict(title = '<b>Count (percent)</b>',
                             color = 'black',
                             showline = False,
                             showgrid = True,
                             showticklabels = True,
                             linecolor = 'black',
                             linewidth = 1,
                             ticks = '',
                             tickfont = dict(
                                 family = 'Arial',
                                 size = 12,
                                 color = 'black'
                             )

                             ),

                legend = {
                    'orientation': 'h',
                    'bgcolor': '#F2F2F2',
                    'x': 0.5,
                    'y': 1.25,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                font = dict(
                    family = "sans-serif",
                    size = 12,
                    color = 'black',
                )
            )

        }

    elif radio_items == 'HistPD':

        return {
            'data': [go.Histogram(
                x = player['Height'],
                histnorm = 'probability density',
                name = 'Height',
                marker = dict(
                    color = 'rgba(122, 69, 209, 0.4)',
                    line = dict(color = 'black', width = 2)
                )
                # hoverinfo='text',
                # hovertext=
                # '<b>Country</b>: ' + terr2['country_txt'].astype(str) + '<br>' +
                # '<b>Year</b>: ' + terr2['iyear'].astype(str) + '<br>' +
                # '<b>Height</b>: ' + [f'{x:,.0f}' for x in player['Height']] + '<br>'

            )],

            'layout': go.Layout(
                bargap = 0.01,
                bargroupgap = 0,
                plot_bgcolor = '#F2F2F2',
                paper_bgcolor = '#F2F2F2',
                title = {
                    'text': '<b>Player Height</b>',

                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont = {
                    'color': 'black',
                    'size': 15},

                hovermode = 'closest',
                xaxis = dict(title = '<b>Height</b>',
                             color = 'black',
                             showline = True,
                             showgrid = False,
                             showticklabels = True,
                             linecolor = 'black',
                             linewidth = 1,
                             ticks = 'outside',
                             tickfont = dict(
                                 family = 'Arial',
                                 size = 12,
                                 color = 'black'

                             )),

                yaxis = dict(title = '<b>Count (probability density)</b>',
                             color = 'black',
                             showline = False,
                             showgrid = True,
                             showticklabels = True,
                             linecolor = 'black',
                             linewidth = 1,
                             ticks = '',
                             tickfont = dict(
                                 family = 'Arial',
                                 size = 12,
                                 color = 'black'
                             )

                             ),

                legend = {
                    'orientation': 'h',
                    'bgcolor': '#F2F2F2',
                    'x': 0.5,
                    'y': 1.25,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                font = dict(
                    family = "sans-serif",
                    size = 12,
                    color = 'black',
                )
            )

        }

    elif radio_items == 'Histogram (cumulative)':



     return {
        'data':[go.Histogram(
                    x = player['Height'],
                    cumulative_enabled=True,
                    name = 'Height',
                    marker = dict(
                       color = 'rgba(69, 209, 118, 0.4)',
                       line = dict(color = 'black', width = 2)
                                 )
                    # hoverinfo='text',
                    # hovertext=
                    # '<b>Country</b>: ' + terr2['country_txt'].astype(str) + '<br>' +
                    # '<b>Year</b>: ' + terr2['iyear'].astype(str) + '<br>' +
                    # '<b>Height</b>: ' + [f'{x:,.0f}' for x in player['Height']] + '<br>'
              )],


        'layout': go.Layout(
             bargap = 0.01,
             bargroupgap = 0,
             plot_bgcolor='#F2F2F2',
             paper_bgcolor='#F2F2F2',
             title={
                 'text': '<b>Player Height</b>',

                 'y': 0.95,
                 'x': 0.5,
                 'xanchor': 'center',
                 'yanchor': 'top'},
             titlefont={
                        'color': 'black',
                        'size': 15},

             hovermode='closest',
             xaxis=dict(title='<b>Height</b>',
                        color = 'black',
                        showline = True,
                        showgrid = False,
                        showticklabels = True,
                        linecolor = 'black',
                        linewidth = 1,
                        ticks = 'outside',
                        tickfont = dict(
                            family = 'Arial',
                            size = 12,
                            color = 'black'


                )),

             yaxis=dict(title='<b>Count</b>',
                        color = 'black',
                        showline = False,
                        showgrid = True,
                        showticklabels = True,
                        linecolor = 'black',
                        linewidth = 1,
                        ticks = '',
                        tickfont = dict(
                            family = 'Arial',
                            size = 12,
                            color = 'black'
                        )

                ),

            legend = {
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'x': 0.5,
                'y': 1.25,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black',
                 )
        )

    }

    elif radio_items == 'Histogram (overlay or stack)':



     return {
        'data':[go.Histogram(
                    x = player['Height'],
                    # name = 'Height',
                    marker = dict(
                       color = 'rgba(246, 78, 139, 0.4)',
                       line = dict(color = 'black', width = 2)
                                 )
                    # hoverinfo='text',
                    # hovertext=
                    # '<b>Country</b>: ' + terr2['country_txt'].astype(str) + '<br>' +
                    # '<b>Year</b>: ' + terr2['iyear'].astype(str) + '<br>' +
                    # '<b>Height</b>: ' + [f'{x:,.0f}' for x in player['Height']] + '<br>'
              ),
            go.Histogram(
                x = player['Height'] + 1,
                # name = 'Height',
                opacity = 0.75,
                marker = dict(
                    color = 'rgba(0, 158, 158, 0.4)',
                    line = dict(color = 'black', width = 2)
                )
                # hoverinfo='text',
                # hovertext=
                # '<b>Country</b>: ' + terr2['country_txt'].astype(str) + '<br>' +
                # '<b>Year</b>: ' + terr2['iyear'].astype(str) + '<br>' +
                # '<b>Height</b>: ' + [f'{x:,.0f}' for x in player['Height']] + '<br>'
            )
        ],


        'layout': go.Layout(
             barmode = 'overlay',
             # barmode = 'stack',
             bargap = 0.01,
             bargroupgap = 0,
             plot_bgcolor='#F2F2F2',
             paper_bgcolor='#F2F2F2',
             title={
                 'text': '<b>Player Height</b>',

                 'y': 0.95,
                 'x': 0.5,
                 'xanchor': 'center',
                 'yanchor': 'top'},
             titlefont={
                        'color': 'black',
                        'size': 15},

             hovermode='closest',
             xaxis=dict(title='<b>Height</b>',
                        color = 'black',
                        showline = True,
                        showgrid = False,
                        showticklabels = True,
                        linecolor = 'black',
                        linewidth = 1,
                        ticks = 'outside',
                        tickfont = dict(
                            family = 'Arial',
                            size = 12,
                            color = 'black'


                )),

             yaxis=dict(title='<b>Count</b>',
                        color = 'black',
                        showline = False,
                        showgrid = True,
                        showticklabels = True,
                        linecolor = 'black',
                        linewidth = 1,
                        ticks = '',
                        tickfont = dict(
                            family = 'Arial',
                            size = 12,
                            color = 'black'
                        )

                ),

            showlegend = False,
            legend = {
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'x': 0.5,
                'y': 1.25,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black',
                 )
        )

    }

    elif radio_items == 'Histogram (histfunction)':



     return {
        'data':[go.Histogram(
                    x = player['Team'],
                    y = player['Round'],
                    histfunc = "sum",
                    name = 'Sum',
                    marker = dict(
                       color = 'rgba(246, 78, 139, 0.4)',
                       line = dict(color = 'black', width = 2)
                                 )
                    # hoverinfo='text',
                    # hovertext=
                    # '<b>Country</b>: ' + terr2['country_txt'].astype(str) + '<br>' +
                    # '<b>Year</b>: ' + terr2['iyear'].astype(str) + '<br>' +
                    # '<b>Height</b>: ' + [f'{x:,.0f}' for x in player['Height']] + '<br>'
              ),
            go.Histogram(
                x = player['Team'],
                y = player['Round'],
                histfunc = "count",
                name = 'Count',
                marker = dict(
                    color = 'rgba(0, 158, 158, 0.4)',
                    line = dict(color = 'black', width = 2)
                )
                # hoverinfo='text',
                # hovertext=
                # '<b>Country</b>: ' + terr2['country_txt'].astype(str) + '<br>' +
                # '<b>Year</b>: ' + terr2['iyear'].astype(str) + '<br>' +
                # '<b>Height</b>: ' + [f'{x:,.0f}' for x in player['Height']] + '<br>'
            )],


        'layout': go.Layout(
             bargap = 0.2,
             bargroupgap = 0,
             plot_bgcolor='#F2F2F2',
             paper_bgcolor='#F2F2F2',
             title={
                 'text': '<b>Player Height</b>',

                 'y': 0.95,
                 'x': 0.5,
                 'xanchor': 'center',
                 'yanchor': 'top'},
             titlefont={
                        'color': 'black',
                        'size': 15},

             # margin = dict(l = 0, r = 0),
             hovermode='closest',
             xaxis=dict(title='<b>Height</b>',
                        color = 'black',
                        showline = True,
                        showgrid = False,
                        showticklabels = True,
                        linecolor = 'black',
                        linewidth = 1,
                        ticks = 'outside',
                        tickfont = dict(
                            family = 'Arial',
                            size = 12,
                            color = 'black'


                )),

             yaxis=dict(title='<b></b>',
                        color = 'black',
                        showline = False,
                        showgrid = True,
                        showticklabels = True,
                        linecolor = 'black',
                        linewidth = 1,
                        ticks = '',
                        tickfont = dict(
                            family = 'Arial',
                            size = 12,
                            color = 'black'
                        )

                ),

            legend = {
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'x': 0.5,
                'y': 1.22,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black',
                 )
        )

    }


if __name__ == '__main__':
    app.run_server(debug=True)