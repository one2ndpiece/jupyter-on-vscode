import ee

# Initialize the Earth Engine library.
ee.Initialize()

# Define the region of interest: around Osaka Castle
roi = ee.Geometry.Point([135.5281, 34.6873])

# Choose the satellite: Landsat 8
dataset = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')

# Filter data
filtered_dataset = dataset.filterBounds(roi).filterDate(ee.Date('2020-01-01'), ee.Date('2020-12-31')).sort('CLOUD_COVER').first()

# Choose bands and create an RGB image
rgb_image = filtered_dataset.select(['B4', 'B3', 'B2'])

# Export the image to Google Drive
task = ee.batch.Export.image.toDrive(
    image=rgb_image,
    description='Osaka_Castle_Landsat_HighRes',
    folder='EarthEngineExports',
    fileNamePrefix='Osaka_Castle_HighRes',
    region=roi.bounds().getInfo()['coordinates'],
    scale=10  # Setting scale to 10 for higher resolution
)

task.start()

# Check task status
print(task.status())
