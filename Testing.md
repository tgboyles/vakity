# Regression Testing #

Testing plan for ongoing changes.

## Navigation / Links ##
  1. Enter www.vakity.com (if live testing), or http://localhost:9080/about (local)
  1. Check navigation menu links work: Tool, About, Contact
  1. go to About page: check Learning Styles links to http://en.wikipedia.org/wiki/Learning_styles

## Content ##
  1. Spellcheck content text
  * Menus
  * Buttons
  * Copy

## Layout ##
Check the layout of boxes are aligned neatly
  1. Navigate to **Tool** page
  * Logo & tagline (Centered)
  * Large left side (aligns with Logo box on the left)
  * Small right side (aligns with Logo box on the right)
  * Left & Right sides align along the top and bottom
  * Footer (across entire width of page, sticky to the bottom)

  1. Navigate to **About** Page
  * Logo & tagline (Centered)
  * Small left side (aligns with Logo box on the left)
  * Large right side (aligns with Logo box on the right)
  * Left & Right sides align along the top and bottom
  * Footer (across entire width of page, sticky to the bottom)

  1. Navigate to **Contact** Page
  * Logo & tagline (Centered)
  * Instructions (Centered)
  * Small left side (aligns with Logo box on the left)
  * Large right side (aligns with Logo box on the right)
  * Left & Right sides align along the top and bottom
  * Footer (across entire width of page, sticky to the bottom)


## Functionality ##

  1. Navigate to **Tool** page
  1. Enter "see hear feel". Analyze.
  * Analysis should be one each VAK
  * Percentages should be whole, no decimal, & add to 100
  1. Enter "yesterday I sat"
  * Analysis should be zero each VAK

  1. Navigate to **Contact** Page
  1. Enter contact details and a message (fill all boxes). Hit button to send.
  * Message should be received
  1. Enter partial details (do not fill all boxes). Attempt to send.
  * Message should not be sent
  * User should get error handling