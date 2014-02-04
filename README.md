agile-console
=============

### Dependency

agile is a python script file. So you would need Python.


### Installing

Download agile to any folder that you want. The Home folder is usually a good idea.


### Change the CHMOD permissions to give the file execution permissions.

cd into the same directory as the agile script and run the following:

```
chmod +x agile
```


### Adding the script to path

Add this into your .bashrc, .zshrc, or your shell configuration file

```
export PATH=/path/to/directory/applify-dev-console:$PATH
```


### Try it out!

Run the following:

```
agile tasks
```


### Commands


Display current project linked to this repo

```
agile status
```


Shortcut for show all my tasks for this current project

```
agile tasks
```


Display tasks of current user in the current project

```
agile my tasks
```


Display all tasks of all users in all projects

```
agile all tasks
```


Display all tasks of current user in all projects

```
agile all my tasks
```


Start a task that is currently paused or pending, associate a branch with it, and create that branch

```
agile start
```


Start the task associated with the current git branch

```
agile start this
```


Pause a task that has been started

```
agile pause
```


Pause the task associated with the current git branch

```
agile pause this
```


Finish a task that has been started

```
agile finish
```


Finish the task associated with the current git branch

```
agile finish this
```
