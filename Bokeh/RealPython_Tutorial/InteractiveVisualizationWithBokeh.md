# Getting Started with Interactive Data Visualization Using Bokeh

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

You are ready to get your hands on some real data. The examples above used Python lists and Numpy arrays to represent the data and Bokeh is well equipped to handle these objects. However when it comes to data in Python you are most likely to come across Python dictionaries and Pandas DataFrames - especially if you are reading in data from a file or external data source. As you can imagine, Bokeh is well equipped to work with these more complex data structures and even has built-in functionality to handle them. For this tutorial I will focus on the most fundamental - the **```ColumnDataSource```**.



## A Quick Aside About Data

Anytime you are exploring a new visualization library, it is a good idea to start with some data for which you already have a sense of how you intend to express it visually. The beauty of a package as flexible as Bokeh is that nearly any idea you have should be possible, its just a matter of how you want to leverage the avaialble tools to do so. 

With that said, as I take you through filling out the template above I will be using a subset of a publically-available datasets from Kaggle that has information about [the National Basketball Association's (NBA) 2017-18 season](https://www.kaggle.com/pablote/nba-enhanced-stats). I will be hopping around between three datasets - one that holds game-by-game snapshots of player statistics, one that holds game-by-game snapshots of team statistics, and one that holds daily team standings and rankings. 

This data has nothing to do with what I do for work, but I love basketball and am always thinking about ways to visualize the ever-growing amount of data associated with it. If you don't have data to play with from school or work, think about something you are interested in and try to find some data for that. It will go a long way in making both the learning and creative processes more enjoyable! 



## Using the ColumnDataSource Object







## Configuring Layouts

### Rows, Columns, and Gridplots

### Tabbed Layouts



## Adding Interaction

### Selection

### Hover and Tooltips

### Linking

### Legends



## Summary and Next Steps