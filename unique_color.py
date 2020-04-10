import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


## ref

# https://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa

# https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python

def plot_colortable(colors, title="35 Unique Colors", sort_colors=True):
	"""
	
	copy from https://matplotlib.org/3.1.0/gallery/color/named_colors.html
	
	colors: dict [name] = [hex]
	
	"""
	cell_width = 212
	cell_height = 22
	swatch_width = 48
	margin = 12
	topmargin = 40

	# Sort colors by hue, saturation, value and name.
	if sort_colors is True:
		by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))),
						 name)
						for name, color in colors.items())
		names = [name for hsv, name in by_hsv]
	else:
		names = list(colors)

	n = len(names)
	ncols = 4 
	nrows = n // ncols + int(n % ncols > 0)

	width = cell_width * 4 + 2 * margin
	height = cell_height * nrows + margin + topmargin
	dpi = 72

	fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
	fig.subplots_adjust(margin/width, margin/height,
						(width-margin)/width, (height-topmargin)/height)
	ax.set_xlim(0, cell_width * 4)
	ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
	ax.yaxis.set_visible(False)
	ax.xaxis.set_visible(False)
	ax.set_axis_off()
	ax.set_title(title, fontsize=24, loc="left", pad=10)

	for i, name in enumerate(names):
		row = i % nrows
		col = i // nrows
		y = row * cell_height

		swatch_start_x = cell_width * col
		swatch_end_x = cell_width * col + swatch_width
		text_pos_x = cell_width * col + swatch_width + 7

		ax.text(text_pos_x, y, name, fontsize=14,
				horizontalalignment='left',
				verticalalignment='center')

		ax.hlines(y, swatch_start_x, swatch_end_x,
				  color=colors[name], linewidth=18)

	return fig

def unique_color():
	return ["#ffff00","#00ffff","#7fff00","#ad4545","#c06464","#379e7d","#1c7caf","#cfa345","#99aab5","#bbeaf8","#f19500","#87cefa","#6f1a52","#476aae","#e6521c","#e1609f","#149c98","#b3dd9e","#3b0056","#70867f","#fff2ec","#cae7e7","#daa520","#b6d4d0","#c39797","#660000","#faebd7","#ffe4e1","#bada55","#d0ad8d","#e8def6","#b90702","#b3dd9e","#ffcc00","#4d4238"]

