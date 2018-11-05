from bokeh.io import reset_output

################################################

# Import pandas
import pandas as pd

# Read the csv files
player_stats = pd.read_csv('2017-18_playerBoxScore.csv', parse_dates=['gmDate'])
team_stats = pd.read_csv('2017-18_teamBoxScore.csv', parse_dates=['gmDate'])
standings = pd.read_csv('2017-18_standings.csv', parse_dates=['stDate'])

################################################

# Isolate the daily win totals for the Warriors and Rockets
west_top_2 = (standings[(standings['teamAbbr'] == 'HOU')
                      | (standings['teamAbbr'] == 'GS')]
            .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
            .sort_values(['teamAbbr','stDate']))
      
# Preview the DataFrame
west_top_2.head()

################################################

reset_output()

# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource

# Output to file
output_file('west-top-2-standings-race.html', 
	title='Western Conference Top 2 Teams Wins Race')

# Isolate the data for the Rockets and Warriors
rockets_data = west_top_2[west_top_2['teamAbbr'] == 'HOU']
warriors_data = west_top_2[west_top_2['teamAbbr'] == 'GS']

# Create a ColumnDataSource object for each team
rockets_cds = ColumnDataSource(rockets_data)
warriors_cds = ColumnDataSource(warriors_data)

# Create and configure the figure
fig = figure(x_axis_type="datetime",
             plot_height=300,
             plot_width=600,
             title="Western Conference Top 2 Teams Wins Race, 2017-18",
             x_axis_label='Date',
             y_axis_label='Wins',
             toolbar_location=None)

# Render the race as step lines
fig.step('stDate', 'gameWon', color='#CE1141', legend='Rockets', source=rockets_cds)
fig.step('stDate', 'gameWon', color='#006BB6', legend='Warriors', source=warriors_cds)

# Move the legend to the upper left corner
fig.legend.location = "top_left"

# Show the plot
show(fig)

################################################

reset_output()

# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Output to file
output_file('west-top-2-standings-race.html', 
	title='Western Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
west_cds = ColumnDataSource(west_top_2)

# Create views for each team
rockets_view = CDSView(source=west_cds,
                      filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(source=west_cds,
                      filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create and configure the figure
west_fig = figure(x_axis_type="datetime",
                 plot_height=300,
                 plot_width=600,
                 title="Western Conference Top 2 Teams Wins Race, 2017-18",
                 x_axis_label='Date',
                 y_axis_label='Wins',
                 toolbar_location=None)

# Render the race as step lines
west_fig.step('stDate', 'gameWon', color='#CE1141', legend='Rockets',
             source=west_cds, view=rockets_view)
west_fig.step('stDate', 'gameWon', color='#006BB6', legend='Warriors',
             source=west_cds, view=warriors_view)

# Move the legend to the upper left corner
west_fig.legend.location = "top_left"

# Show the plot
show(west_fig)

################################################

reset_output()

# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Output to file
output_file('east-top-2-standings-race.html', 
	title='Eastern Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create views for each team
celtics_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                                           group='BOS')])
raptors_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                                           group='TOR')])

# Create and configure the figure
east_fig = figure(x_axis_type="datetime",
             plot_height=300,
             plot_width=600,
             title="Eastern Conference Top 2 Teams Wins Race, 2017-18",
             x_axis_label='Date',
             y_axis_label='Wins',
             toolbar_location=None)

# Render the race as step lines
east_fig.step('stDate', 'gameWon', 
              color='#007A33', legend='Celtics',
              source=standings_cds, view=celtics_view)
east_fig.step('stDate', 'gameWon', 
              color='#CE1141', legend='Raptors',
              source=standings_cds, view=raptors_view)

# Move the legend to the upper left corner
east_fig.legend.location = "top_left"

# Show the plot
show(east_fig)

################################################

reset_output()

# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import column

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create views for each team
celtics_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                                           group='BOS')])

raptors_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                                           group='TOR')])

rockets_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                      	                   group='HOU')])
warriors_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                      	                   group='GS')])

# Create and configure the figure
east_fig = figure(x_axis_type="datetime",
             plot_height=300,
             plot_width=600,
             title="Eastern Conference Top 2",
             x_axis_label='Date',
             y_axis_label='Wins',
             toolbar_location=None)

west_fig = figure(x_axis_type="datetime",
                 plot_height=300,
                 plot_width=600,
                 title="Western Conference Top 2",
                 x_axis_label='Date',
                 y_axis_label='Wins',
                 toolbar_location=None)


# Render the race as step lines
east_fig.step('stDate', 'gameWon', 
              color='#007A33', legend='Celtics',
              source=standings_cds, view=celtics_view)
east_fig.step('stDate', 'gameWon', 
              color='#CE1141', legend='Raptors',
              source=standings_cds, view=raptors_view)

west_fig.step('stDate', 'gameWon', color='#CE1141', legend='Rockets',
             source=standings_cds, view=rockets_view)
west_fig.step('stDate', 'gameWon', color='#006BB6', legend='Warriors',
             source=standings_cds, view=warriors_view)

# Move the legend to the upper left corner
# Move the legend to the upper left corner
east_fig.legend.location = "top_left"
west_fig.legend.location = "top_left"

# Output to file
output_file('east-west-top-2-column.html', 
	title='Conference Top 2 Teams Wins Race')

# Plot the two visualizations in a vertical configuration
show(column(west_fig, east_fig))

################################################

reset_output()

# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import gridplot

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create views for each team
celtics_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                                           group='BOS')])

raptors_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                                           group='TOR')])

rockets_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                      	                   group='HOU')])
warriors_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                      	                   group='GS')])

# Create and configure the figure
east_fig = figure(x_axis_type="datetime",
             plot_height=300,
             plot_width=300,
             title="Eastern Conference Top 2",
             x_axis_label='Date',
             y_axis_label='Wins',
             toolbar_location=None)

west_fig = figure(x_axis_type="datetime",
                 plot_height=300,
                 plot_width=300,
                 title="Western Conference Top 2",
                 x_axis_label='Date',
                 y_axis_label='Wins',
                 toolbar_location=None)


# Render the race as step lines
east_fig.step('stDate', 'gameWon', 
              color='#007A33', legend='Celtics',
              source=standings_cds, view=celtics_view)
east_fig.step('stDate', 'gameWon', 
              color='#CE1141', legend='Raptors',
              source=standings_cds, view=raptors_view)

west_fig.step('stDate', 'gameWon', color='#CE1141', legend='Rockets',
             source=standings_cds, view=rockets_view)
west_fig.step('stDate', 'gameWon', color='#006BB6', legend='Warriors',
             source=standings_cds, view=warriors_view)

# Move the legend to the upper left corner
east_fig.legend.location = "top_left"
west_fig.legend.location = "top_left"

# Output to file
output_file('east-west-top-2-gridplot.html', 
	title='Conference Top 2 Teams Wins Race')

# Reduce the width of both figures
east_fig.plot_width = west_fig.plot_width = 300

# Edit the titles
east_fig.title.text = 'Eastern Conference'
west_fig.title.text = 'Western Conference'

# Configure the gridplot
#east_west_gridplot = gridplot([[west_fig, east_fig]], 
#	                          toolbar_location='right')

east_west_gridplot = gridplot([[west_fig, None], [None, east_fig]], 
	                          toolbar_location='right')

# Plot the two visualizations in a horizontal configuration
show(east_west_gridplot)

################################################

reset_output()

# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.models.widgets import Tabs, Panel

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create views for each team
celtics_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                                           group='BOS')])

raptors_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                                           group='TOR')])

rockets_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                      	                   group='HOU')])
warriors_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr', 
                      	                   group='GS')])

# Create and configure the figure
east_fig = figure(x_axis_type="datetime",
             plot_height=300,
             plot_width=300,
             title="Eastern Conference Top 2",
             x_axis_label='Date',
             y_axis_label='Wins',
             toolbar_location=None)

west_fig = figure(x_axis_type="datetime",
                 plot_height=300,
                 plot_width=300,
                 title="Western Conference Top 2",
                 x_axis_label='Date',
                 y_axis_label='Wins',
                 toolbar_location=None)


# Render the race as step lines
east_fig.step('stDate', 'gameWon', 
              color='#007A33', legend='Celtics',
              source=standings_cds, view=celtics_view)
east_fig.step('stDate', 'gameWon', 
              color='#CE1141', legend='Raptors',
              source=standings_cds, view=raptors_view)

west_fig.step('stDate', 'gameWon', color='#CE1141', legend='Rockets',
             source=standings_cds, view=rockets_view)
west_fig.step('stDate', 'gameWon', color='#006BB6', legend='Warriors',
             source=standings_cds, view=warriors_view)

# Move the legend to the upper left corner
east_fig.legend.location = "top_left"
west_fig.legend.location = "top_left"

# Output to file
output_file('east-west-top-2-gridplot.html', 
	title='Conference Top 2 Teams Wins Race')

# Increase the width of both figures
east_fig.plot_width = west_fig.plot_width = 800

# Create two panels, one for each conference
east_panel = Panel(child=east_fig, title='Eastern Conference')
west_panel = Panel(child=west_fig, title='Western Conference')

# Assign the panels to Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

# Show the tabbed layout
show(tabs)

################################################

reset_output()

# First, let's find players who took at least 1 three-point shot during the season
three_takers = player_stats[player_stats['play3PA'] > 0]

# First let's clean up the player names, placing them in a single column
three_takers['name'] = [three_takers.iloc[ix]['playFNm'] + ' ' + three_takers.iloc[ix]['playLNm'] 
                        for ix 
                        in range(len(three_takers))]

# Aggregate the total three-point attempts and makes for each player over the course of the season
three_takers = (three_takers.groupby('name')
	                        .sum()
	                        .loc[:,['play3PA', 'play3PM']]
	                        .sort_values('play3PA', ascending=False))

# Filter out anyone who didn't take at least 100 three-point shots
three_takers = three_takers[three_takers['play3PA'] >= 100].reset_index()

# Add a column with a calculated three-point percentage (made/attempted)
three_takers['pct3PM'] = three_takers['play3PM'] / three_takers['play3PA']

""" pycon
>>> # Pull a sample of players 
>>> three_takers.sample(5)
                   name  play3PA  play3PM    pct3PM
229        Corey Brewer      110       31  0.281818
78           Marc Gasol      320      109  0.340625
126      Raymond Felton      230       81  0.352174
127  Kristaps Porziņģis      229       90  0.393013
66      Josh Richardson      336      127  0.377976
"""

################################################

reset_output()

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter

# Output to file
output_file('three-point-att-vs-pct.html',
	        title='Three-Point Attempts vs. Percentage')

# Store the data in a ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)

# Specify the selection tools to be made available
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

# Create the figure
fig = figure(plot_height=400,
             plot_width=600,
             x_axis_label='Three-Point Shots Attempted',
             y_axis_label='Percentage Made',
             title='3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-18',
             toolbar_location='below',
             tools=select_tools)

# Format the y-axis tick labels as percentages
fig.yaxis[0].formatter = NumeralTickFormatter(format="00.0%")

# Add square representing each player
fig.square(x='play3PA',
           y='pct3PM',
           source=three_takers_cds,
           color='royalblue',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=0.3)

# Visualize
show(fig)

################################################

reset_output()

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool

# Output to file
output_file('three-point-att-vs-pct-w-hover.html',
	        title='Three-Point Attempts vs. Percentage')

# Store the data in a ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)

# Specify the selection tools to be made available
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

# Create the figure
fig = figure(plot_height=400,
             plot_width=600,
             x_axis_label='Three-Point Shots Attempted',
             y_axis_label='Percentage Made',
             title='3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-18',
             toolbar_location='below',
             tools=select_tools)

# Format the y-axis tick labels as percentages
fig.yaxis[0].formatter = NumeralTickFormatter(format="00.0%")

# Add square representing each player
fig.square(x='play3PA',
           y='pct3PM',
           source=three_takers_cds,
           color='royalblue',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=0.3)

# Format the tooltip
tooltips = [
            ('Player','@name'),
            ('Three-Pointers Made', '@play3PM'),
            ('Three-Pointers Attempted', '@play3PA'),
            ('Three-Point Percentage','@pct3PM{00.0%}'),
           ]

# Configure a renderer to be used upon hover
hover_glyph = fig.circle(x='play3PA',
                         y='pct3PM',
                         source=three_takers_cds,
                         size=15,
                         alpha=0,
                         hover_fill_color='black',
                         hover_alpha=0.5)

# Add the HoverTool to the figure
fig.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

# Visualize
show(fig)

################################################

reset_output()

# Isolate relevant data
phi_gm_stats = (team_stats[(team_stats['teamAbbr'] == 'PHI') & 
	                       (team_stats['seasTyp'] == 'Regular')]
                .loc[:, ['gmDate', 
                         'teamPTS', 
                         'teamTRB', 
                         'teamAST', 
                         'teamTO', 
                         'opptPTS',]]
                .sort_values('gmDate'))

# Add game number
phi_gm_stats['game_num'] = range(1, len(phi_gm_stats)+1)

# Derive a win_loss column
win_loss = []
for ix in range(len(phi_gm_stats)):
	# If the 76ers score more points, it's a win
    if phi_gm_stats.iloc[ix]['teamPTS'] > phi_gm_stats.iloc[ix]['opptPTS']:
        win_loss.append('W')
    else:
        win_loss.append('L')

# Add the win_loss data to the DataFrame
phi_gm_stats['winLoss'] = win_loss

# First five games 
phi_gm_stats.head()


################################################

reset_output()

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, Div
from bokeh.layouts import gridplot, column

# Output to file
output_file('phi-gm-linked-stats.html',
                title='76ers Game Log')

# Store the data in a ColumnDataSource
gm_stats_cds = ColumnDataSource(phi_gm_stats)

# Create a CategoricalColorMapper that assigns specific colors to wins and losses
win_loss_mapper = CategoricalColorMapper(factors = ['W', 'L'], 
	                                     palette=['green', 'red'])

# Create a dict with the stat name and its corresponding column in the data
stat_names = {'Points': 'teamPTS',
              'Assists': 'teamAST',
              'Rebounds': 'teamTRB',
              'Turnovers': 'teamTO',}

# The figure for each stat will be held in this dict
stat_figs = {}

# For each stat in the dict
for stat_label, stat_col in stat_names.items():

	# Create a figure
	fig = figure(y_axis_label=stat_label, 
		         plot_height=200, plot_width=400,
		         x_range=(1, 10), tools=['xpan', 'reset', 'save'])

	# Configure vbar
	fig.vbar(x='game_num', top=stat_col, source=gm_stats_cds, width=0.9, 
		     color=dict(field='winLoss', transform=win_loss_mapper))

	# Add the figure to stat_figs dict
	stat_figs[stat_label] = fig


# Create layout
grid = gridplot([[stat_figs['Points'], stat_figs['Assists']], 
	             [stat_figs['Rebounds'], stat_figs['Turnovers']]])

# Link together the x-axes
stat_figs['Points'].x_range = stat_figs['Assists'].x_range = stat_figs['Rebounds'].x_range = stat_figs['Turnovers'].x_range

# Add a title for the entire visualization using Div
html = """<h3>Philadelphia 76ers Game Log</h3>
<b><i>2017-18 Regular Season</i>
<br>
</b><i>Wins in green, losses in red</i>
"""
supTitle = Div(text=html)

# Visualize
show(column(supTitle, grid))


################################################

reset_output()

# Isolate relevant data
phi_gm_stats_2 = (team_stats[(team_stats['teamAbbr'] == 'PHI') & 
                             (team_stats['seasTyp'] == 'Regular')]
                  .loc[:, ['gmDate', 
                            'team2P%', 
                            'team3P%', 
                            'teamPTS', 
                            'opptPTS']]
                  .sort_values('gmDate'))

# Add game number
phi_gm_stats_2['game_num'] = range(1, len(phi_gm_stats_2) + 1)

# Derive a win_loss column
win_loss = []
for ix in range(len(phi_gm_stats_2)):

	# If the 76ers score more points, it's a win
    if phi_gm_stats_2.iloc[ix]['teamPTS'] > phi_gm_stats_2.iloc[ix]['opptPTS']:
        win_loss.append('W')
    else:
        win_loss.append('L')

# Add the win_loss data to the DataFrame
phi_gm_stats_2['winLoss'] = win_loss

# First five games 
phi_gm_stats_2.head()

################################################

reset_output()

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, NumeralTickFormatter
from bokeh.layouts import gridplot

# Output inline in the notebook
output_file('phi-gm-linked-selections.html',
            title='76ers Percentages vs. Win-Loss')

# Store the data in a ColumnDataSource
gm_stats_cds = ColumnDataSource(phi_gm_stats_2)

# Create a CategoricalColorMapper that assigns specific colors to wins and losses
winLossMapper = CategoricalColorMapper(factors = ['W', 'L'], palette=['Green', 'Red'])

# Specify the tools
toolList = ['lasso_select', 'tap', 'reset', 'save']

# Create a figure relating the percentages
pctFig = figure(title='2PT FG % vs 3PT FG %, 2017-18 Regular Season',
                plot_height=400, plot_width=400, tools=toolList,
                x_axis_label='2PT FG%', y_axis_label='3PT FG%')

# Draw with circle markers
pctFig.circle(x='team2P%', y='team3P%', source=gm_stats_cds, 
	          size=12, color='black')

# Format the y-axis tick labels as percenages
pctFig.xaxis[0].formatter = NumeralTickFormatter(format="00.0%")
pctFig.yaxis[0].formatter = NumeralTickFormatter(format="00.0%")

# Create a figure relating the totals
totFig = figure(title='Team Points vs Opponent Points, 2017-18 Regular Season',
                plot_height=400, plot_width=400, tools=toolList,
                x_axis_label='Team Points', y_axis_label='Opponent Points')

# Draw with square markers
totFig.square(x='teamPTS', y='opptPTS', source=gm_stats_cds, size=10,
              color=dict(field='winLoss', transform=winLossMapper))

# Create layout
grid = gridplot([[pctFig, totFig]])

# Visualize
show(grid)


################################################

reset_output()

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import row

# Output inline in the notebook
output_file('lebron-vs-durant.html',
	        title='LeBron James vs. Kevin Durant')

# Store the data in a ColumnDataSource
player_gm_stats = ColumnDataSource(player_stats)

# Create a view each for each player
lebron_filters = [GroupFilter(column_name='playFNm', group='LeBron'),
                  GroupFilter(column_name='playLNm', group='James')]
lebron_view = CDSView(source=player_gm_stats,
	                  filters=lebron_filters)

durant_filters = [GroupFilter(column_name='playFNm', group='Kevin'),
                  GroupFilter(column_name='playLNm', group='Durant')]
durant_view = CDSView(source=player_gm_stats,
	                  filters=durant_filters)

# Consolidate the common keyword arguments in dictionaries
common_figure_kwargs = {
    'plot_width': 400,
    'x_axis_label': 'Points',
    'toolbar_location': None,
}
common_circle_kwargs = {
    'x': 'playPTS',
    'y': 'playTRB',
    'source': player_gm_stats,
    'size': 12,
    'alpha': 0.7,
}
common_lebron_kwargs = {
    'view': lebron_view,
    'color': '#002859',
    'legend': 'LeBron James'
}
common_durant_kwargs = {
    'view': durant_view,
    'color': '#FFC324',
    'legend': 'Kevin Durant'
}

# Create the two figures and draw the data
hide_fig = figure(**common_figure_kwargs,
                  title='Click Legend to HIDE Data', 
                  y_axis_label='Rebounds')
hide_fig.circle(**common_circle_kwargs, **common_lebron_kwargs)
hide_fig.circle(**common_circle_kwargs, **common_durant_kwargs)

mute_fig = figure(**common_figure_kwargs, title='Click Legend to MUTE Data')
mute_fig.circle(**common_circle_kwargs, **common_lebron_kwargs,
                muted_alpha=0.1)
mute_fig.circle(**common_circle_kwargs, **common_durant_kwargs,
                muted_alpha=0.1)

""" Deprecated version
# Create a scatter plot that compares the players' game-by-game points and rebounds
hide_fig = figure(title='Click Legend to HIDE Data', plot_width=400,
                  x_axis_label='Points', y_axis_label='Rebounds', 
                  toolbar_location=None)
hide_fig.circle(x='playPTS', y='playTRB', 
                source=player_gm_stats, view=lebron_view,
                size=12, alpha=0.7, color='#002859', 
                legend='LeBron James')
hide_fig.circle(x='playPTS', y='playTRB', 
                source=player_gm_stats, view=durant_view,
                size=12, alpha=0.7, color='#FFC324', 
                legend='Kevin Durant')

# Replicate scatter plot in new figure
mute_fig = figure(title='Click Legend to MUTE Data', plot_width=400,
                  x_axis_label='Points', toolbar_location=None)
mute_fig.circle(x='playPTS', y='playTRB', 
                source=player_gm_stats, view=lebron_view,
                size=12, alpha=0.7, color='#002859', 
                legend='LeBron James',
                muted_alpha=0.1)
mute_fig.circle(x='playPTS', y='playTRB', 
                source=player_gm_stats, view=durant_view,
                size=12, alpha=0.7, color='#FFC324', 
                legend='Kevin Durant',
                muted_alpha=0.1)
"""

# Add interactivity to the legend
hide_fig.legend.click_policy = 'hide'
mute_fig.legend.click_policy = 'mute'

# Visualize
show(row(hide_fig, mute_fig))

################################################

reset_output()

# Bokeh Libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# The figure will be right in my Jupyter Notebook
output_file('ugly-figure.html',
	        title='Ugliest Figure Ever!')

# Example figure
fig = figure(background_fill_color='gray',
             background_fill_alpha=0.5,
             border_fill_color='blue',
             border_fill_alpha=0.25,
             plot_height=300,
             plot_width=500,
             h_symmetry=True,
             x_axis_label='X Label',
             x_axis_type='datetime',
             x_axis_location='above',
             x_range=('2018-01-01','2018-06-30'),
             y_axis_label='Y Label',
             y_axis_type='linear',
             y_axis_location='left',
             y_range=(0,100),
             title='Example Figure',
             title_location='right',
             toolbar_location='below',
             tools='save')

# See what it looks like
show(fig)

################################################

reset_output()