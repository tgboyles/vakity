# Introduction #

This How-to describes how to deploy the webapp to Google Code. It assumes that you already have the project set up in the Google App Engine Launcher and have the correct credentials for the App Engine console.


# Details #

  * From your local workstation, open your IDE

  * From the PyDev package explorer, open /vakity.trunk/webapp/app.yaml

  * Increment the 'version:' value. For example, if the current value is 'version: 14', make it 'version: 15'. If these don't get incremented, you'll end up overwriting an existing deploy.

  * Save the file.

  * From your local workstation, open the Google App Engine Launcher

  * Select the 'vakity-test-analyzer' project from the project list and click the 'Run' button

  * Click the 'Browse' button. The local version of the app will open in a web browser

  * Test the site using the [Testing](Testing.md) plan

  * If all tests pass, ensure that all changes have been committed to the SCM using the [HowToCommitChangesToSCM](HowToCommitChangesToSCM.md) HowTo

  * Once you've verified that the changes have been committed, return to the Google App Engine Launcher and click the 'Deploy' button

  * You will be presented with a sign-in dialog. Log in with your Google credentials

  * The 'Log Console' dialog will appear. Monitor the log output as it uploads the web-app, paying special attention to any errors or warnings that might appear. Report these immediately to our Dev Ops people. If you don't see any errors, the deployment is successful.

  * From the Google App Engine Launcher, click the 'Dashboard' button or navigate to https://appengine.google.com/dashboard?app_id=vakity-text-analyzer from a web browser

  * From the side navigation bar, under 'Main', select 'Versions'

  * Click on the number link for the latest version. It will open the site in a new tab or window.

  * Test the site using the [Testing](Testing.md) plan.

  * Once all tests have passed, return to the 'Versions' click the select button next to the newly deployed version and click the 'Make Default' button. This will effectively make the new release live and it will be visible to the public.