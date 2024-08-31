import os                          # directory managing
from urllib.request import urlopen # requests managing
from urllib.error import HTTPError # Error handler
from zipfile import ZipFile        # .zip files managing

class WorldClim():
    """Class to get and preprocess World Clim Data"""

    def __init__(self, res = '10', var = 'all'):
        f""" Constructor method

        Receives
        --------

        res : str
            WorldClim data Resolution. Available resolutions
            • 30 (seconds)
            • 2.5 (minutes)
            • 5 (minutes)
            • 10 (minutes)

        var : str
            WorldClim variables to download. Available variables:
            • tmin : minimum temperature (°C)
            • tmax : maximum temperature (°C)
            • tavg : average temperature (°C)
            • prec : precipitation (mm)
            • srad : solar radiation (kJ m-2 day-1)
            • wind : wind speed (m s-1)
            • vapr : water vapor pressure (kPa)
            • all : whole set of previous variables
            • bio : 19 Bioclimatic variables
            • elev : elevation
        """

        self.res = res
        self.var = var
        self.__VARIABLES = ['tmin','tmax','tavg','prec','srad',
                            'wind','vapr','all','bio','elev']
        self.__RESOLUTIONS = ['30','2.5','5','10']

    def url_generation(self):
        f"""Method to download and unzip data from World Clim"""

        url = 'https://geodata.ucdavis.edu/climate/worldclim/2_1/base/wc2.1_'



        if self.var == 'all':

            try:

                for var in tqdm(self.__VARIABLES[0:7]):

                    if self.res == '30':
                        self.__URL = url + self.res + 's_' + var + '.zip'
                    else:
                        self.__URL = url + self.res + 'm_' + var + '.zip'

                    self.download_unzip(url = self.__URL)

            except HTTPError:
                print('URL request failed. Resolution ',self.res,' or variable ', self.var,' non-available')

        else:

            try:

                if self.res == '30':
                    self.__URL = url + self.res + 's_' + self.var + '.zip'
                else:
                    self.__URL = url + self.res + 'm_' + self.var + '.zip'

                self.download_unzip(url = self.__URL)

            except HTTPError:
                print('URL request failed. Resolution ',self.res,' or variable ', self.var,' non-available')


    def download_unzip(self, url : str, extract_to='/'):
        f"""Method to download and unzip data from World Clim

        Receives
        --------

        url : str
            url to get the data

        extract_to : str
            path to save the data

        """

        self.__URL  = url
        self.__path = extract_to
        self.__path_data = os.getcwd() + self.__path + self.__URL[55:-4]

        if os.path.exists(self.__path_data) == False:
            os.mkdir(self.__path_data)

        url_response = urlopen(self.__URL)
        zipfile = ZipFile(BytesIO(url_response.read()))
        zipfile.extractall(path=self.__path_data)