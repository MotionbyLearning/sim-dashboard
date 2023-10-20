import argparse
import os 

import holoviews as hv
import hvplot.xarray
import hvplot.pandas
import panel as pn
import xarray as xr

from typing import Dict, Tuple

from holoviews import opts
from holoviews import streams


hv.extension('bokeh')
opts.defaults(opts.Points(tools=['box_select', 'lasso_select']))


TOO_MANY_POINTS = 10


def parse_args(args: Dict = None) -> Tuple:
    parser = argparse.ArgumentParser(
        description='Start the STM dashboard'
    )
    parser.add_argument('--stm-path', type=str, required=True,
                        help='Path to STM Zarr dataset')
    args = parser.parse_args(args)
    return (args.stm_path, )


def main() -> None:
    # get parameters
    stm_path, = parse_args()

    stm = xr.open_zarr(stm_path)

    # create points plot
    xy = stm[['lat', 'lon']].to_dataframe()
    points = xy.hvplot.points(
        'lon', 
        'lat', 
        geo=True, 
        color='red', 
        tiles='ESRI', 
        frame_width=500, 
        frame_height=500
    )

    # create stream for selection of points
    selection = streams.Selection1D(source=points)
    
    # create variable plots for selection of points
    def plot_variables(index):
        if not index or len(index) > TOO_MANY_POINTS:
            # for no or too many points, plot point 0
            return plot_variables([0])
        else:
            return hv.NdLayout({
                       var: hv.NdOverlay({
                           idx: stm[var].isel(points=idx).hvplot(x='time')
                           for idx in index
                       })
                       for var in ['amplitude', 'phase', ]
            }).cols(1)
    variables = hv.DynamicMap(plot_variables, streams=[selection])
    # fix issue of Layout not being the most external plot instance
    variables = variables.collate()

    # start panel dashboard
    pn.panel(points + variables).show()
    
    
if __name__ == '__main__':
    main()
