# Python-Plugin-System V1

Hi! :smile:

This project is a sample of **complete plugin system** in python. :seedling:
</br></br>



## Advantage of this system :trophy:

1. Modularity :package:
   * You can easily add a plugin or remove this plugin.
   * You can easily disable or enable a plugin.
2. Error handling :hammer_and_wrench:
   * You can easily check a plugin error. Just one line!
   * If a plugin doesn't work, the program stay alive.
3. Logging :bookmark_tabs:
   * This system generate a logging file to see status of all plugins.
   * All error is printed link indicated.
4. Usage :rose:
   * You just need to set the object **plugin** and calling the function that you want.
   * All the plugin is managed in the background.

# How to start

## Run the example

For launching the process you need to execute the command:
```
./main.py
```
</br>

## Adding plugin :package:
When you want to adding a plugin, you just need to add the plugin's file inside the folder **plugin**.

To add plugin on program append file information to "PLUGIN" inside **plugin.json**:
```json
    {
        "FileName": "new_plugin.py",
        "ClassName": "new_plugin_class",
        "activate": 1 // 0 plugin desactivate / 1 plugin activate 
    }
```
</br>

## Create your type of plugin :notebook_with_decorative_cover:

1. Add your new fonction inside all your plugin's class
2. Add a new fonction inside the class "Plugin" (plugin.py) like sample
3. *(Optional)* Add error handling inside "load_plugin" (plugin.py), if the fonction is necessary.
</br></br>

#
## Futur :rocket:

Don't hesitate to purpose new fonctionality with the issue! :yum:

</br>

> /!\ If you want more details, you can look comments inside the code.
