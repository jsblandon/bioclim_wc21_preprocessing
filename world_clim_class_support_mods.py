import rioxarray as rxr            # raster managing
from shapely.geometry import mapping, Point, Polygon # for clipping rasters using shapes and geometries managing

def bio_raster_loading(raster_path,shape):
    r''' Function to load and clip bioclimatic rasters

    Receives
    --------

    raster_path : string
        Raster path to retrieve the bioclimatic variable information

    shape : geoDataFrame
        Polygon or Multipolygon data structure to clip the raster

    Returns
    -------

    clp_raster : xarray.DataArray
        clipped raster
    '''
    raster = rxr.open_rasterio(raster_path, masked = True)

    if raster.rio.crs == shape.crs:
        # Clipping bioclim data to the Area Of Interest
        clp_raster = raster.rio.clip(shape.geometry.apply(mapping))
        print('Raster clipping done!')
        return clp_raster

    else:
        print('Both CRS are not the same!')
        return None