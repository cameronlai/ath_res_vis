# Athletics Results Visualization

Athletics Results Visualization is a Django app built to visualize athletics results of individual athletes
It curretnly uses data from the [HKSSF]{http://www.hkssf-hk.org.hk/} website.
It uses chart.js as the javascript plotting tool.

## Set up

1. Start Django Project 

  ``` bash
  django-admin startproject ath_res_vis_project
  cd ath_res_vis_project
  ```

2. Clone the git repository

  ``` bash
  git clone https://github.com/cameronlai/ath_res_vis
  ```
  
3. Edit settings.py in your project folder

  ``` bash
  cd ath_res_vis_project
  nano settings.py
  ```

  > Add 'ath_res_vis' in INSTALLED_APPS
  > Add 'ath_res_vis/static/', in STATICFILES_DIR

4. Edit urls.py in your project folder 
  
  ``` bash
  nano urls.py
  ```

  > Add url(r'$^', include('ath_res_vis.urls')), to urlpatterns
  

5. Run migrations with manage.py

  ``` bash
  cd ../
  python manage.py migrate
  ```

6. Dump athletics results data into Database

   - The data used are in PDF formats. They are first converted text files and then parsed into the correct format.
   - Data can be found from this link. http://www.hkssf-hk.org.hk/hk/sec/events/ath.htm
   - You may write your own parser and reuse the web visualization part for other data formats.

## Running Django app

1. Run server

  ``` bash
  python manage.py runserver
  ```

2. Launch web browser, enter correct IP address (Default is 127.0.0.1:8000) and your app is running.

## Database format

   The database is in the following format as in models.py
   | Field Name | Description						|
   | ---------- | ---------------------------------			|
   | Name	| Name of the athelete					|
   | School	| Name of the school the athlete is representing 	|
   | Event	| Name of the event the athelete completed (e.g. 100m)	|
   | Sex	| Sex of the atehlete					|
   | Result	| Results of the athelete (either in seconds or meteres)|
   | Date	| Date of the event completion				|
   | IsTrack	| True = Track event, False = field event		|

## Dependencies

- Chart.js

## License

The app is released under the MIT License and more information can be found in the LICENSE file.

## Contributions

ath_res_vis is a project to help people visualize athletics results more easier, instead of looking up multiple PDF / old text formats.
Contributions for improvements and bug fixes are sincerely welcome!