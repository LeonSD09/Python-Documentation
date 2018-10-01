Getting Started with Interactive Data Visualization Using Bokeh

Bokeh prides itself on being a library for _interactive_ data visualization. Unlike popular counterparts in the Python visualization space like ```matplotlib``` and ```seaborn```, Bokeh renders its graphics using HTML and Javascript. While this makes it a great candidate for building web-based dashboards and applications, it is an equally powerful tool for exploring and undersanding your data or creating beautiful custom charts for a project or report.  

Using a number of examples on a real-world dataset, the goal of this tutorial is to get you up and running with Bokeh and by the end you will:

* feel comfortable using Bokeh to go from data to visualization
* be able to create and customize common charts and configure layouts from the ground up
* understand how to leverage Bokeh's ability to add interactive elements to your visualizations

So let's jump in ... 

## From Data to Visualization

The general Bokeh workflow can be outlined as follows:

**Prepare The Data**

Any good data visualization starts with, you guessed it - data. I will assume that you have a basic knowledge of handling data in Python, and if not feel free to check out the [growing number of excellent RealPythoin tutorials on the subject](https://realpython.com/tutorials/data-science/). This step commonly involves data handling libraries like ```pandas``` or ```numpy```  and is all about taking the required steps to transform it into a form that is best suited for the visualization you plan to represent it with. 

**Determine Where The Visualization Will Be Rendered** 

The first step is to determine how you want to generate and ultimately view your visualization. The primary option is to generate an HTML file. However, Bokeh also makes it extremely easy to render your visualization right in a Jupyter notebook.

**Set Up The Figure(s)**

From here you will assemble your figure, preparing the canvas for your visualization. It is this step in which you can customize everything from the titles to the tick marks. Additionally, it is at this step where you can set up a suite of tools that can be leveraged in interacting with your plot - hover actions, selection options, click behaviors, etc. 

**Connect To and Draw Your Data**

Next you will utilize Bokeh's multitude of renderers to give shape to your data. Here you have the flexibility to draw your data from scratch using the many Glyph options - all of which are easily customizable. While drawing visualizations from scratch may sound scary, Bokeh has some built-in functionality for building things like [stacked bar charts](https://bokeh.pydata.org/en/latest/docs/user_guide/categorical.html#stacked) or examples for creating more advanced visualizations like [network graphs](https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html) and [maps](https://bokeh.pydata.org/en/latest/docs/user_guide/geo.html).

**Organize the Layout**

If you need more than one figure to express your data, no big deal. Not only does Bokeh offer the standard grid-like layout options, but also allows you to easily organize your visualizations into a tabbed layout in just a few lines of code. Additionally, your plots can be quickly linked together so a selection on one will be reflected on any combination of the others. 

**Preview and Save Your Beautiful Data Creation**

Finally, it is time to see what you created. At this stage you can take a look at your work, test all of the interactive elements implemented above, and export your new creation to an image file. 

That's it! Those six steps yields a tidy, flexible template for taking your data to from the table to the big screen. The code skeleton will generally look somelike the following, and as I move through the steps in more detail you will see how this skeleton is filled in. 

```python
""" Bokeh Visualization Template

This template is a general outline for turning your data into a 
visualization using Bokeh.
"""
# Data Handling
import pandas as pd
import numpy as np

# Bokeh Libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh. models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

# Prepare the Data

# Determine where the visualization will be rendered
output_file(filename) # Render to static HTML, or 
output_notebook() # Render inline in a Jupyter Notebook

# Set Up the figure(s)
fig = figure() # Instantiate a figure() object

# Connect to and draw the data

# Organize the layout

# Preview and save 
show(fig) # See what I made, and save if I like it
```



## Generating Your First Figure 

The ```bokeh.io``` module offers two options for outputting your visualization:

* **```output_file(filename)```** will write the visualization to a static HTML file
* **```output_notebook()```** will render your visualization directly in a Jupyter notebook

It is important to note that neither function will actually show you the the visualization. That doesn't happen until the ```show()``` function is called. However, they will ensure that when ```show()``` is called the visualization appears where you intend it to.

This is a great opportunity to give you your first glimpse at a default Bokeh ```figure()```. Running the template code from above as will do just this. First using ```output_file()```:

```python
# Bokeh Libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# The figure will be rendered in a static HTML file called output_file_test.html
output_file('output_file_test.html', title='Empty Bokeh Figure')

# Set up a generic figure() object
fig = figure()

# See what it looks like
show(fig)
```

![output_file](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/output_file_example.png) 

As you can see, a new browser window opened with a tab called _Empty Bokeh Figure_ and an empty figure. Not shown is the file generated with the name _output_file_test.html_. This is based on the parameters passed to ```output_file()```.

If I run the same code snippet with ```output_notebook()``` in place out ```output_file()```,  assuming I have a Jupyter Notebook fired up and ready to go I will get the following:

```python
# Bokeh Libraries
from bokeh.io import output_notebook
from bokeh.plotting import figure, show

# The figure will be right in my Jupyter Notebook
output_notebook()

# Set up a generic figure() object
fig = figure()

# See what it looks like
show(fig)
```

![](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/output_notebook_example.png)

Same result, just rendered in a different location. More information about both ```output_file()``` and ```output_notebook()``` can be found in [the Bokeh official docs](https://bokeh.pydata.org/en/latest/docs/reference/io.html#bokeh-io-output).

----

#### TIP: Rendering Multiple Visualizations in the Notebook

Sometimes when rendering multiple visualizations sequentiallyin a Jupyter Notebook you may see that past renders are not being cleared with each execution. If this is a problem, import and run the following between executions:

```python
from bokeh.plotting import reset_output
reset_output()
```

-----

Before moving on, it is worth noting that the default Bokeh figure comes pre-loaded with a toolbar - an important sneak preview into the interactive elements of Bokeh that come right out of the box. You'll find out more about the toolbar and how to configure it in the next section! 



## Getting Your Figure Ready for Data

You now know how to create and view a generic Bokeh figure either in a browser or Jupyter Notebook. But the ```figure()``` object is the canvas for which you will create your data visualization - making configuring it properly essential! Luckily, you will learn how to do that now. 

The ```figure()``` object is not only the foundation of your data visualization. It is also the object that unlocks all of Bokeh's available tools for visualizing data (don't worry, you'll learn about those next). A subclass of [Bokeh's Plot() object](https://bokeh.pydata.org/en/latest/docs/reference/models/plots.html#bokeh.models.plots.Plot), the Bokeh figure inherits all of its attributes. This makes it possible to configure all of the critical aspects of the figure - titles; axis labels, locations, ticks, and types; dimensions; tools and more. 

To show you just a glimpse into the customization options available, I'll make the ugliest figure ever:

```python
# Bokeh Libraries
from bokeh.io import output_notebook
from bokeh.plotting import figure, show

# The figure will be right in my Jupyter Notebook
output_notebook()

# Example figure
fig = figure(
    background_fill_color='gray',
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
```

![](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/example_figure.png)

Once the ```figure()``` object is instantiated, you can still configure it after the fact. 

So if I want to get rid of those gridlines and change the x-axis labels to _linear_ instead of _datetime_ (which is why it is currently shown in microseconds):

```python
# Remove the gridlines from the figure() object
fig.grid.grid_line_color = None

# Change the x-axis type to linear
fig.show()
```

![](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/example_figure_no_gridlines.png)

With so many customizable elements, If you are working in a Notebook or in an IDE with auto-complete - this feature is your friend! Otherwise, doing a quick web search with the keyword _bokeh_ and what you are trying to do will generally point you in the right direction. 

![](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/auto_complete.gif)

There is tons more I could touch on here, but don't feel like you're missing out. I'll make sure to introduce different figure tweaks as the tutorial progresses. Still worried? Check out [the excellent Bokeh User Guide](https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#text-properties) or go straight to the source:

* **[The Bokeh Plot Class](https://bokeh.pydata.org/en/latest/docs/reference/models/plots.html#bokeh.models.plots.Plot)** The superclass of the ```figure()``` object and where figures inherit a lot of their attributes 
* **[The ```figure()``` Method](https://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure.Figure)** Checkout the keywords args towards the top of the page, they should look familiar

Additionally, here are a few specific customization tools worth checking out:

* [**Text Properties**](https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#text-properties) all the attributes related to changing font styles, sizes, colors, etc.
* [**TickFormatters**](https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#tick-label-formats) a built-in object specifically for formatting your axes using Python-like string formatting syntax 



## Drawing Data with Glyphs

Now the fun really begins. But before we jump in, it is probably a good call out to remind you that Bokeh visualizations - unlike those created  ```matplotlib``` and ```seaborn``` - are not ready-made versions of the charts you are used to seeing. That brings us to glyphs, the building blocks of Bokeh visualizations. Glyph is essentially a fancy word for shape, and after you create your figure you are given access to [a bevy of these configurable shapes](https://bokeh.pydata.org/en/latest/docs/reference/plotting.html) to create the visualization of your dreams:

![Glyph options as seen in the Bokeh Reference Guide](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/glyph_options.png)

Now this may sound scary, building everything from scratch, but you will be surprised with the freedom it opens up in making not only the usual charts and graphs but also truly unique and elegant data visualizations.

Let's start with a very basic example. I want to draw some points on an x-y coordinate grid:

```python
reset_output()

# Bokeh Libraries
from bokeh.io import output_notebook
from bokeh.plotting import figure, show

# My x-y coordinate data
x = [1, 2, 1]
y = [1, 1, 2]

# Output the visualization directly in the notebook
output_notebook()

# Create a figure called 'My Coordinates' with no toolbar and axis ranges of [0,3]
fig = figure(
    title='My Coordinates',
    plot_height=300,
    plot_width=300,
    x_range=(0,3),
    y_range=(0,3),
    toolbar_location=None)

# Draw the coordinates as circles
fig.circle(
    x=x,
    y=y,
    color='green',
    size=10,
    alpha=0.5)

# Show plot
show(fig)
```

![](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/first_glyphs.png)

Notice that I hid the toolbar by setting the ```toolbar_location``` property to ```None``` in the figure instantiation. 

```circle()```, along with glyphs like ```diamond()```, ```square()```,``` triangle()```, and ```x()```,  are examples of a scatter markers - as you can image they would be useful in creating scatter plot and bubble charts. Another glyph classication includes single (```line()```), step (```step()```), and multiple (```multi_line()```) lines - all of which are line glyphs - your go to for line charts . Bar/rectangle glyphs (```quad()```, ```vbar()```, ```hbar()```) are the building blocks of histograms, bar/column, waterfall, and even gantt charts. Everything you need to know to familiarize yourself with all of Bokeh's glyph offerings is outlined in [the Reference Guide](https://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html). 

These glyphs can be mix-and-matched to your visualization's needs. Let's say I want to create a visualization that shows how many words I wrote per day to make this tutorial with an trend line of the cumulative words overlaid:

```python
# Pandas and Numpy for generating my dummy data
import pandas as pd
import numpy as np

# Bokeh Libraries
from bokeh.io import output_notebook
from bokeh.plotting import figure, show

# My word count data
dayNum = np.linspace(1,10,10)
dailyWords = [450, 628, 488, 210, 287, 791, 508, 639, 397, 943]
cumWords = np.cumsum(dailyWords)

# Output the visualization directly in the notebook
output_notebook()

# Create a figure with a datetime type x-axis
fig = figure(
    title='My Tutorial Progress',
    plot_height=400,
    plot_width=700,
    x_axis_label='Day Number',
    y_axis_label='Words Written',
    x_minor_ticks=2,
    y_range=(0,6000),
    toolbar_location=None)

# The daily words will be represented as vertical bars (columns)
fig.vbar(
    x=dayNum, 
    bottom=0, 
    top=dailyWords, 
    color='#51B2E8',
    width=0.75,
    legend='Daily')

# The cumulative sum will be a trend line
fig.line(
    x=dayNum,
    y=cumWords, 
    line_width=1,
    color='#23223E',
    legend='Cumulative')

# Put the legend in the upper left corner
fig.legend.location = 'top_left'

# Let's check it out
show(fig)
```

![multi_glyph_example](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/multi_glyph_example.png)

Instead of using explicit color names as in previous examples, this time I took advantage of glyphs being able to interpret [hex color values](https://htmlcolorcodes.com). Also, this is the first time I've shown you how seamlessly a legend can be created by simply setting the ```legend``` property for each glyph. The legend was then moved to the upper left corner of the plot. Much more [detail about styling legends can be found here](https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#legends). Clifferhanger: they will show up again later in the tutorial when we start digging into interactive elements of the visualization. 

## A Quick Aside About Data

Anytime you are exploring a new visualization library, it is a good idea to start with some data for which you have a sense of how you intend to express it visually. The beauty of a package as flexible as Bokeh is that nearly any idea you have should be possible, its just a matter of how you want to leverage the avaialble tools to do so. 

With that said, as I take you through filling out the template above I will be using a subset of a publically-available data from Kaggle that has information about [the National Basketball Association's (NBA) 2017-18 season](https://www.kaggle.com/pablote/nba-enhanced-stats). I will be hopping around between three datasets - one that holds game-by-game snapshots of player statistics, one that holds game-by-game snapshots of team statistics, and one that holds daily team standings and rankings. 

This data has nothing to do with what I do for work, but I love basketball and am always thinking about ways to visualize the ever-growing amount of data associated with it. If you don't have data to play with from school or work, think about something you are interested in and try to find some data for that. It will go a long way in making both the learning and creative process more enjoyable! 



## Using the ColumnDataSource Object

You are ready to get your hands on some real data. The examples above used Python lists and Numpy arrays to represent the data and Bokeh is well equipped to handle these objects. However when it comes to data in Python you are most likely to come across Python dictionaries and Pandas DataFrames, especially if you are reading in data from a file or external data source. As you can imagine, Bokeh is well equipped to work with these more complex data structures and even has built-in functionality to handle them - particularly the ```ColumnDataSource```.

So the first question you may have is - _why use a ```ColumnDataSource``` when Bokeh can interface with other data types directly?_ For one, whether you reference a list, array, dictionary, or DataFrame directly when building your visualization, Bokeh is going to turn it into a ```ColumnDataSource``` behind the scenes anway. More importantly, as you'll see ```ColumnDataSource``` make it much easier to implement the Bokeh's interactive affordances. ****

The ```ColumnDataSource``` is foundational in passing the data to the glyphs you are using to visualize. It's primary functionality is to map names to the arrays within your data. This makes it easier for you to reference elements of your data when building your visualization, and easier for Bokeh to to the same when building your vizualization. 

```ColumnDataSource``` can be passed three forms of data as input parameters:

* **Python ```dict```** where the keys are names associated with the respective value sequences (ie. lists, arrays, etc.)
* **Pandas ```DataFrame```** where the columns of the ```DataFrame``` become the reference names for the ```ColumnDataSource```
* **Pandas ```groupby```** where the columns of the ```ColumnDataSource``` reference the columns as seen by calling ```groupby.describe()```



I want to visualize the race for first place in the NBA's Western Conference in 2017-18 between the defending-champion Golden State Warriors and the challenger Houston Rockets. I have stored the daily win-loss records of these two teams in a ```DataFrame``` named ```westTop2```:

```Python
# Data Handling Libraries
import pandas as pd
import numpy as np

# Read in the standings dataset
standings = pd.read_csv('2017-18_standings.csv')

# Convert stDate column to datetime
standings['stDate'] = pd.to_datetime(standings['stDate'])

# Isolate the daily win totals for the Warriors and Rockets
westTop2 = standings[(standings['teamAbbr'] == 'HOU') | (standings['teamAbbr'] == 'GS')]\
           .loc[:,['stDate', 'teamAbbr', 'gameWon']]\
           .sort_values(['teamAbbr','stDate'])
      
# Preview the DataFrame
westTop2.head()
```

![westTop2_preview](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/westTop2_preview.png)

From here I can load this ```DataFrame``` into a ```ColumnDataSource``` and visualize the race:

```python
# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource

# Output inline in the notebook
output_notebook()

# Create a ColumnDataSource 
rockets = ColumnDataSource(westTop2[westTop2['teamAbbr'] == 'HOU'])
warriors = ColumnDataSource(westTop2[westTop2['teamAbbr'] == 'GS'])

# Create and configure the figure
fig = figure(x_axis_type="datetime", 
             plot_height=300,
             plot_width=600,
             title="Western Conference Top 2 Teams Wins Race, 2017-18",
             toolbar_location=None)

# Add axis labels
fig.xaxis.axis_label = 'Date'
fig.yaxis.axis_label = 'Wins'

# Render the race as step lines
fig.step('stDate', 'gameWon', color='#CC0000', legend='Rockets', source=rockets)
fig.step('stDate', 'gameWon', color='#223E91', legend='Warriors', source=warriors)

# Move the legend to the upper left corner
fig.legend.location = "top_left"

# Show the plot
show(fig)
```

![rockets_v_warriors](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/rockets_v_warriors.png)

I like it! It was definitely a tight race throughout the season, with the Warriors building a pretty big cushion around the middle of the season. However a bit of a late-season slide allowed the Rockets to catch up and ultimately surpass the defending champs to finish the season as the Western Conference number-one seed. 

Notice how the respective ```ColumnDataSource``` objects are referenced when creating the two lines. I simplied passed the original column names as input parameters and specified which ```ColumnDataSource``` to use via the ```source``` property. 

```ColumnDataSource``` objects can do more than just serve as easy way to reference ```DataFrame``` columns. To illustrate another functionality of the ```ColumnDataSource```, I am going to make a small tweak to the code snippet above:

```python
# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Output inline in the notebook
output_notebook()

# Create a ColumnDataSource 
cds = ColumnDataSource(westTop2)

# Create views for each team
rocketsView = CDSView(source=cds, 
                      filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriorsView = CDSView(source=cds, 
                      filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create and configure the figure
westFig = figure(x_axis_type="datetime", 
                 plot_height=300,
                 plot_width=600,
                 title="Western Conference Top 2 Teams Wins Race, 2017-18",
                 toolbar_location=None)

# Add axis labels
westFig.xaxis.axis_label = 'Date'
westFig.yaxis.axis_label = 'Wins'

# Render the race as step lines
westFig.step('stDate', 'gameWon', color='#CC0000', legend='Rockets', 
             source=cds, view=rocketsView)
westFig.step('stDate', 'gameWon', color='#223E91', legend='Warriors', 
             source=cds, view=warriorsView)

# Move the legend to the upper left corner
westFig.legend.location = "top_left"

# Show the plot
show(westFig)
```

![rockets_v_warriors_v2](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/rockets_v_warriors_v2.png)

Different approach, same result. Where in the first example I created two ```ColumnDataSource``` objects, one each with a slice of the ```westTop2``` ```DataFrame```. I actually could have just done that slice with the ```ColumnDataSource``` as illustrated above. 

The ```ColumnDataSource``` object has three built in filters which can be used to create views on your data using a ```CDSView``` object:

* ```GroupFilter``` allows you to select rows from a ```ColumnDataSource``` given a categorical reference value
* ```IndexFilter``` allows you to select rows from a ```ColumnDataSource``` via a list of integer indices
* ```BooleanFilter``` allows you to select rows from a ```ColumnDataSource``` using a list of ```boolean``` values, with ```True``` rows being selected

Well the Western Conference sure was an exciting race, but I forget if the Eastern Conference was the same. I sort of want to view them in a single visualization. A perfect segway to the next topic - layouts. 

If you are still craving more, there is plenty more to chew on related to the  ```ColumnDataSource``` and other source objects offered through Bokeh [here](https://bokeh.pydata.org/en/latest/docs/user_guide/data.html). 



## Organizing Multiple Visualizations with Layouts

The Eastern Conference standings came down to two rivals in the Atlantic Division - the Boston Celtics and the Toronto Raptors. Before I replicate the steps used to create ```westTop2```, I want to try to put the ```ColumnDataSource``` to the test one more time using what you learned above. Can I feed it the entire ```standings``` ```DataFrame``` and then create views for the two teams straight from that?

```python
# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Output inline in the notebook
output_notebook()

# Create a ColumnDataSource 
cds = ColumnDataSource(standings)

# Create views for each team
celticsView = CDSView(source=cds, 
                      filters=[GroupFilter(column_name='teamAbbr', group='BOS')])
raptorsView = CDSView(source=cds, 
                      filters=[GroupFilter(column_name='teamAbbr', group='TOR')])

# Create and configure the figure
eastFig = figure(x_axis_type="datetime", 
             plot_height=300,
             plot_width=600,
             title="Eastern Conference Top 2 Teams Wins Race, 2017-18",
             toolbar_location=None)

# Add axis labels
eastFig.xaxis.axis_label = 'Date'
eastFig.yaxis.axis_label = 'Wins'

# Render the race as step lines
eastFig.step('stDate', 'gameWon', color='#00611B', legend='Celtics', 
             source=cds, view=celticsView)
eastFig.step('stDate', 'gameWon', color='#D50F44', legend='Raptors', 
             source=cds, view=raptorsView)

# Move the legend to the upper left corner
eastFig.legend.location = "top_left"

# Show the plot
show(eastFig)
```

![celtics_v_raptors](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/celtics_v_raptors.png)Not too shabby. The ```ColumnDataSource``` was able to isolate the relevant data within  a 5,040-by-39 ```DataFrame``` without breaking a sweat, saving me a few lines of ```pandas``` code in the process. And what do you know, the Eastern Conference race was no slouch. After the Celtics roared out of the gate, the Raptors clawed all the way back to overtake their division rival and finish the regular season with five more wins. Okay, now that I have my two visualizations it is time to put them together. 

For those familiar with the ```matplotlib``` ```subplot``` paradigm, Bokeh offers the ```colum()```, ```row()```, and ```gridplot()``` functions in its ```bokeh.layouts module```.

The usage is very straightforward. If I want to put my two visualizations in a column-wise configuration I can do so with:

```python
# Bokeh library
from bokeh.layouts import column

# Plot the two visualizations in a column-wise configuration
show(column(eastFig, westFig))
```

![column_layout](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/column_layout.png)

I'll save you the two lines of code, but rest assured swapping ```column``` for ```row``` in the snippet above will similarly configure the two plots in a row-wise configuration. 

The two visualizations above do not have a toolbar, but if they did each figure would have its own. That is one of the main reasons to use ```gridplot()``` instead of either ```row()``` or ```column()```. Syntactically ```gridplot()``` also is slighlty different in that instead of being passed a tuple as input it requires a list of lists, where each list represents a row in the grid:

```python
# Bokeh library
from bokeh.layouts import gridplot

# Add a toolbar to both figures
eastFig.toolbar_location = 'right'
westFig.toolbar_location = 'right'

# Reduce the width of both figures
eastFig.plot_width = 300
westFig.plot_width = 300

# Edit the titles
eastFig.title.text = 'Eastern Conference'
westFig.title.text = 'Western Conference'

# Plot the two visualizations in a row-wise configuration
show(gridplot([[eastFig, westFig]]))
```

![image-20180930194509029](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/gridplot_layout.png)

Lastly on ```gridplot()``` it does allow the passing of ```None``` values, which are interpreted as blank spaces. Therefore if I wanted to leave a placeholder for two additional plots I could use:

```
# Plot the two visualizations with placeholders
show(gridplot([[eastFig, None], [None, westFig]]))
```

![image-20180930194804872](/Users/lsdangio/Desktop/Python/Python-Documentation/Bokeh/RealPython_Tutorial/assets/gridplot_with_nones.png)



## Adding Interaction

### Selection

### Hover and Tooltips

### Linking

### Legends



## Summary and Next Steps