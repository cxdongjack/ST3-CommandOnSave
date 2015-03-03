import sublime, sublime_plugin, os, threading

class BuildonSave(sublime_plugin.EventListener):

    def on_post_save(self, view):
        working_dir = view.window().folders()[0]
        build_command = view.settings().get('build_on_save')

        if build_command:
          SaveAction(build_command, view.file_name(), working_dir).start()
        else:
          print('BuildonSave: Project not configured for build_on_save.  Try setting build_on_save in project settings')


class SaveAction(threading.Thread):

    def __init__(self, command, filename, working_dir):
        self.command = command
        self.filename = filename
        self.working_dir = working_dir
        threading.Thread.__init__(self)
 
    def run(self):
        print('cd %s && %s %s' % (self.working_dir, self.command, self.filename))
        os.chdir(self.working_dir)
        os.system('%s %s' % (self.command, self.filename))
