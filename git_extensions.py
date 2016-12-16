import sublime, sublime_plugin
from subprocess import Popen

class git_extensions_browse(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'browse', "%s" % paths[0]]
    Popen(['GitExtensions'] + args)
    return None

class git_extensions_pull(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'pull', "%s" % paths[0],'--merge', '--quiet']
    Popen(['GitExtensions'] + args)
    return None

class git_extensions_commit(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'commit', "%s" % paths[0]]
    Popen(['GitExtensions'] + args)
    return None

class git_extensions_history(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'filehistory', "%s" % paths[0]]
    Popen(['GitExtensions'] + args)
    return None

class git_extensions_checkout(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'checkout', "%s" % paths[0]]
    Popen(['GitExtensions'] + args)
    return None

class git_extensions_merge(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'merge', "%s" % paths[0]]
    Popen(['GitExtensions'] + args)
    return None

class git_extensions_push(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'push', "%s" % paths[0]]
    Popen(['GitExtensions'] + args)
    return None

class git_extensions_branch(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'branch', "%s" % paths[0]]
    Popen(['GitExtensions'] + args)
    return None

class git_extensions_reset(sublime_plugin.WindowCommand):
  def run(self, paths):
    args = [ 'reset', "%s" % paths[0]]
    Popen(['GitExtensions'] + args)
    return None