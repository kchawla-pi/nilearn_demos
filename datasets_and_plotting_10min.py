"""
Plotting brain images with Nilearn
==================================

Nilearn (https://nilearn.github.io/) has fetchers to download online
neuroimaging datasets and many tools to create interactive or
publication-quality visualizations.

"""

######################################################################
import warnings
warnings.simplefilter('ignore')

######################################################################
# Statistical maps
# ================

######################################################################
# Download and plot a group-level statistical map

from nilearn import datasets, plotting, surface
img = datasets.fetch_neurovault_motor_task()['images'][0]
plotting.view_img(img, threshold='95%')

######################################################################
# Plot a figure that can be saved

plotting.plot_stat_map(img, threshold=3)

######################################################################
# Static plots that can be saved in a variety of formats
plotting.plot_stat_map(img, threshold=3, cut_coords=(37, -26, 58))


######################################################################
plotting.plot_stat_map(img, cut_coords=[-18, 64], display_mode='z', threshold=3.)


######################################################################
plotting.plot_glass_brain(img, plot_abs=False, threshold=3.)


######################################################################
# Visualize projections on the cortical surface
# ---------------------------------------------

plotting.view_img_on_surf(img, threshold='95%', surf_mesh='fsaverage')


######################################################################
# Atlases
# =======

destrieux = datasets.fetch_atlas_destrieux_2009()
plotting.view_img(destrieux['maps'],
                  resampling_interpolation='nearest',
                  cmap='gist_ncar', symmetric_cmap=False, colorbar=False)
######################################################################
plotting.plot_roi(destrieux['maps'])

######################################################################
# Plotting a surface atlas
surf_destrieux = datasets.fetch_atlas_surf_destrieux()
fsaverage = datasets.fetch_surf_fsaverage()
plotting.view_surf(fsaverage['pial_left'], surf_destrieux['map_left'],
                   cmap='gist_ncar')
