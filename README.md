# Sublime Text 3 Plugin, it executes a command on file save

1. set the cammnd base on project, bring up the Command Palette (Command+Shift+P on OS X, Control+Shift+P on Linux/Windows), then input "Project: Edit"
'''js
{
    "folders":
    [
        {
            "follow_symlinks": true,
            "path": "."
        }
    ],
    "settings":
    {
        "build_on_save": "sh onSave.sh"
    }
}
'''
2. run the cammand under project directory, pass the path of the modified file as argument
3. run cammand in background, preventing the Sublime user interface from freezing
