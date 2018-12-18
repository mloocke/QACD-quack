import datetime as dt
import matplotlib.cm as cm
import weakref


class DisplayOptions:
    def __init__(self, project):
        self._project = weakref.ref(project)

        # Colourmap options.
        self._valid_colourmap_names = self._determine_valid_colourmap_names()
        self._colourmap_name = 'rainbow'

        # Label options.
        self._valid_scale_bar_locations = \
            ['upper left', 'upper right', 'lower left', 'lower right']
        self._show_ticks_and_labels = True
        self._overall_title = ''
        self._show_project_filename = False
        self._show_date = False

        # Scale options.
        self._valid_units = ['mm', '\u03BCm', 'nm']
        self._valid_scale_bar_colours = ['black', 'white']
        self._use_scale = False
        self._pixel_size = 1.0
        self._units = self._valid_units[1]
        self._show_scale_bar = True
        self._scale_bar_location = 'lower left'
        self._scale_bar_colour = self._valid_scale_bar_colours[0]

        # Histogram options.
        self._use_histogram_bin_count = True
        self._histogram_bin_count = 100
        self._histogram_bin_width = 0.005
        self._histogram_max_bin_count = 200
        self._show_mean_median_std_lines = True

        # Zoom options.
        self._auto_zoom_region = False
        self._zoom_updates_stats = False

        self._listeners = weakref.WeakSet()

    def _determine_valid_colourmap_names(self):
        # Exclude reversed cmaps which have names ending with '_r'.
        all_ = set(filter(lambda s: not s.endswith('_r'), cm.cmap_d.keys()))

        # Exclude qualitative and repeating cmaps, and the deprecated
        # 'spectral' which has been replaced with 'nipy_spectral'.
        exclude = set(['Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2',
                       'Set1', 'Set2', 'Set3', 'Vega10', 'Vega20', 'Vega20b',
                       'Vega20c', 'flag', 'prism', 'spectral', 'tab10',
                       'tab20', 'tab20b', 'tab20c'])
        return sorted(all_.difference(exclude))

    @property
    def auto_zoom_region(self):
        return self._auto_zoom_region

    @property
    def colourmap_name(self):
        return self._colourmap_name

    @colourmap_name.setter
    def colourmap_name(self, colourmap_name):
        name_to_check = colourmap_name
        if name_to_check.endswith('_r'):
            name_to_check = name_to_check[:-2]
        if name_to_check not in self._valid_colourmap_names:
            raise RuntimeError('Not such colourmap: {}'.format(name_to_check))
        self._colourmap_name = colourmap_name

        self._project().save_display_options()

        for listener in self._listeners:
            listener.update_colourmap_name()

    @property
    def date(self):
        return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_next_larger_units(self, units):
        index = self._valid_units.index(units)
        if index == 0:
            return 'm'
        else:
            return self._valid_units[index-1]

    @property
    def histogram_bin_count(self):
        return self._histogram_bin_count

    @property
    def histogram_bin_width(self):
        return self._histogram_bin_width

    @property
    def histogram_max_bin_count(self):
        return self._histogram_max_bin_count

    @property
    def overall_title(self):
        return self._overall_title

    @property
    def project_filename(self):
        return self._project().filename

    @property
    def pixel_size(self):
        return self._pixel_size

    def register_listener(self, listener):
        if listener is not None and listener not in self._listeners:
            self._listeners.add(listener)

    @property
    def scale(self):
        if self._use_scale:
            return self._pixel_size
        else:
            return 1.0

    @property
    def scale_bar_colour(self):
        return self._scale_bar_colour

    @property
    def scale_bar_location(self):
        return self._scale_bar_location

    def set_histogram(self, use_histogram_bin_count, histogram_bin_count,
                histogram_bin_width, histogram_max_bin_count,
                show_mean_median_std_lines, refresh_display=True):
        self._use_histogram_bin_count = use_histogram_bin_count
        self._histogram_bin_count = histogram_bin_count
        self._histogram_bin_width = histogram_bin_width
        self._histogram_max_bin_count = histogram_max_bin_count
        self._show_mean_median_std_lines = show_mean_median_std_lines

        self._project().save_display_options()

        if refresh_display:
            for listener in self._listeners:
                listener.update_histogram_options()

    def set_labels_and_scale(self, show_ticks_and_labels, overall_title,
                             show_project_filename, show_date, use_scale,
                             pixel_size, units, show_scale_bar,
                             scale_bar_location, scale_bar_colour,
                             refresh_display=True):
        # Validation.
        if pixel_size <= 0.0:
            raise RuntimeError('Pixel size must be positive')
        if units not in self.valid_units:
            raise RuntimeError('Unrecognised units {}'.format(units))
        if scale_bar_location not in self._valid_scale_bar_locations:
            raise RuntimeError('Unrecognised scale bar location {}'.format(scale_bar_location))
        if scale_bar_colour not in self._valid_scale_bar_colours:
            raise RuntimeError('Unrecognised scale bar colour {}'.format(scale_bar_colour))

        # Labels.
        self._show_ticks_and_labels = show_ticks_and_labels
        self._overall_title = overall_title
        self._show_project_filename = show_project_filename
        self._show_date = show_date

        # Scale.
        self._use_scale = use_scale
        self._pixel_size = pixel_size
        self._units = units
        self._show_scale_bar = show_scale_bar
        self._scale_bar_location = scale_bar_location
        self._scale_bar_colour = scale_bar_colour

        self._project().save_display_options()

        if refresh_display:
            for listener in self._listeners:
                listener.update_labels_and_scale()

    def set_zoom(self, auto_zoom_region, zoom_updates_stats,
                 refresh_display=True):
        self._auto_zoom_region = auto_zoom_region
        self._zoom_updates_stats = zoom_updates_stats

        self._project().save_display_options()

        if refresh_display:
            for listener in self._listeners:
                listener.update_zoom()

    @property
    def show_date(self):
        return self._show_date

    @property
    def show_mean_median_std_lines(self):
        return self._show_mean_median_std_lines

    @property
    def show_project_filename(self):
        return self._show_project_filename

    @property
    def show_scale_bar(self):
        return self._show_scale_bar

    @property
    def show_ticks_and_labels(self):
        return self._show_ticks_and_labels

    def unregister_listener(self, listener):
        self._listeners.discard(listener)

    @property
    def use_scale(self):
        return self._use_scale

    @property
    def use_histogram_bin_count(self):
        return self._use_histogram_bin_count

    @property
    def units(self):
        return self._units

    @property
    def valid_colourmap_names(self):
        return self._valid_colourmap_names

    @property
    def valid_units(self):
        return self._valid_units

    @property
    def zoom_updates_stats(self):
        return self._zoom_updates_stats
