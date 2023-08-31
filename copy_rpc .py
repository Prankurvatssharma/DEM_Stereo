#! /usr/bin/env python

import sys,os,glob
from osgeo import gdal
from osgeo import gdalconst


input_img = os.path.abspath(sys.argv[1])
output_img = os.path.abspath(sys.argv[2])

rpc_fn = input_img
non_rpc_fn = output_img
rpc_img = gdal.Open(rpc_fn, gdalconst.GA_ReadOnly)
non_rpc_img = gdal.Open(non_rpc_fn, gdalconst.GA_Update)
rpc_data = rpc_img.GetMetadata('RPC')
non_rpc_img.SetMetadata(rpc_data,'RPC')
print("Copying rpc from {} to {}".format(rpc_fn,non_rpc_fn))
del(rpc_img)
del(non_rpc_img)

print("Script is complete!")

