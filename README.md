# Vakity

## Introduction

Vakity is a web service which provides for an extensible learning style analysis of text along a visual-aural-kinesthetic spectrum. It is based on [Neil Fleming's VAK learning style model](http://en.wikipedia.org/wiki/Learning_styles#Neil_Fleming.27s_VAK.2FVARK_model).

If you are interested in knowing a person's learning style but are not in a position to have them take one of the freely available self-test, this app may be of use to you. You will need a sample of their writing, as from a long email or personal essay.

The application runs it's analysis based on several sets of keywords and looks for their usage in any writing sample. Therefore the larger the sample, the better.

Knowing a person's learning style may benefit you in the following ways: 

1. If your position requires you to transmit information effectively to others, as in training or sales, you can learn to be more efficient in your approach by tailoring your approach to an individual's learning style.

2. You can create more rapport with individuals by seeding your communications with more of "their" key words, be those VISUAL, AUDITORY or KINESTHETIC. 

You can even try it out on yourself by using your own writing sample, although it will be more accurate for you to simple take the test.

## Dictionaries

### Location

- File: Analyze.py 

- Function: process

### Structure

Dictionaries consist of a set of three tuples, one for each of the V-A-K learning styles:

- visual_dictionary

- auditory_dictionary

- kinesthetic_dictionary

Elements in the tuple may be a single word, or a phrase.

## How-Tos

### Deploying The Project

- From your local workstation, open your IDE

- From the PyDev package explorer, open /vakity.trunk/webapp/app.yaml

- Increment the 'version:' value. For example, if the current value is 'version: 14', make it 'version: 15'. If these don't get incremented, you'll end up overwriting an existing deploy.

- Save the file.

- From your local workstation, open the Google App Engine Launcher

- Select the 'vakity-test-analyzer' project from the project list and click the 'Run' button

- Click the 'Browse' button. The local version of the app will open in a web browser

- Test the site using the Testing plan

- If all tests pass, ensure that all changes have been committed to the SCM.

- Once you've verified that the changes have been committed, return to the Google App Engine Launcher and click the 'Deploy' button

- You will be presented with a sign-in dialog. Log in with your Google credentials

- The 'Log Console' dialog will appear. Monitor the log output as it uploads the web-app, paying special attention to any errors or warnings that might appear. Report these immediately to our Dev Ops people. If you don't see any errors, the deployment is successful.

- From the Google App Engine Launcher, click the 'Dashboard' button or navigate to https://appengine.google.com/dashboard?app_id=vakity-text-analyzer from a web browser

- From the side navigation bar, under 'Main', select 'Versions'

- Click on the number link for the latest version. It will open the site in a new tab or window.

- Test the site using the Testing plan.

- Once all tests have passed, return to the 'Versions' click the select button next to the newly deployed version and click the 'Make Default' button. This will effectively make the new release live and it will be visible to the public.
