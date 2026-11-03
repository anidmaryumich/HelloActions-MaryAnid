# HelloActions-MaryAnid - Lab 11 

# What is the purpose of the on section?: It defines which events start the workflow. Here it's a push to `main` or a manual run.
# What does workflow_dispatch do?: It adds a "Run workflow" button in the Actions tab so the workflow can be started manually.
# What does runs-on specify?: The runner the job runs on and here it's the latest Ubuntu Linux.
# *Why is action/checkout needed?: The runner starts empty and checkout copies the repo's files onto it so it can find `hello.py`.
# *What does the language setup act do?: `actions/setup-python` installs the chosen Python version on the runner.
# What is the difference between compiling and running the program?: Compiling turns source code into something the machine can execute. Running actually executes the program. Python is interpreted, so it has no separate compile step (the "prepare" step only checks for syntax errors).
# Where can you see the program output?: Actions tab -> click the workflow run -> click the job -> expand the "Run the Python program" step.
# What is the difference between a workflow, a job, and a step?: A workflow is the whole automated process. A job is a group of steps that runs on a runner. A step is a single task inside a job, either a command (`run`) or a prebuilt action (`uses`).
