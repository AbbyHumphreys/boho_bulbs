# Boho Bulbs

![Image showing the Boho Bulbs website on various devices](media/responsive-image.png "Boho Bulbs")

View the deployed site: [Boho Bulbs](https://boho-bulbs-12038623272a.herokuapp.com/)

This is Boho Bulbs, an ecommerce website for users to buy lamps. The website will enable users to browse the products, add them to a shopping and purchase them, as well as to created their own account to keep track of their purchases.

# User Story Testing

A set of user stories were created before creating the site, so guide the design and development of the app. Testing was done during after the site build and the results are as follows:

| | As a / an | I want to be able to… | Achieved by...  | Screenshots |
|----|----|----|----| ---- |
| Viewing and Navigation |   |   |   |
| 1 | Site Visitor | View a list of products                   | Using the 'All Products' nav menu and selecting 'All Products       | [Evidence](media/all-products.png ) |
| 2 | Site Visitor | View a specific category of products      | Using the variety of nav menu filters or drill down filters         | [Evidence](media/filters.png )      |
| 3 | Site Visitor | View individual product details           | Clicking on a product to view details                               | [Evidence](media/individual-product.png )      |
| 4 | Site Visitor | View the total of my shopping bag         | Total seen top right of page at all times                           | [Evidence](media/bag-total.png )    |
| Registration / User Accounts |   |   |   |
| 5 | Site Visitor | Easily register for an account            | Store my personal details and view my purchase history              | [Evidence](media/profile-evidence.png )    |
| 6 | Site Visitor | Easily log in and out                     | Login and out using admin buttons top right of screen               | [Evidence](media/login-out.png )    |
| 7 | Site Visitor | Reset my password                         | Gain access to my account                                           | [Evidence](media/forgot-password.png )    |
| 8 | Site Visitor | Verify my email address after registering | Keep my account secure and know registration was successful         | |
| 9 | Site Visitor | Have a user profile                       | Store my personal details and view my purchase history              | [Evidence](media/profile-evidence.png )    ||
| Sorting / Searching |   |   |   |
| 10 | Site Visitor | Sort the available products               | View the products best suited to my needs and budget                | [Evidence](media/filters.png )      |
| 11 | Site Visitor | Sort by specific category                 | View the products best suited to my needs and budget                | [Evidence](media/filters.png )      |
| 12 | Site Visitor | Sort by multiple categories simultaneously| Narrow down my product list                                         | [Evidence](media/filters.png )      |
| 13 | Site Visitor | Search for a product by name or description| Find a product suited to my needs                                  | [Evidence](media/search-soft.png )  |
| 14 | Site Visitor | Easily see what I have searched for       | See if the product type I want is at the site                       | [Evidence](media/search-soft.png )  |
| Purchasing / Checkout |   |   |   |
| 15 | Site Visitor | Select the quantity of the product        | Select the right amount that I need                                 | [Evidence](media/individual-product.png )      |
| 16 | Site Visitor | View items in my bag to be purchased      | View the total cost of my bag                                       | [Evidence](media/shopping-bag-evidence.png )  |
| 17 | Site Visitor | Adjust the quantity once in the bag       | Easily make changes before checkout                                 | [Evidence](media/shopping-bag-evidence.png )  |
| 18 | Site Visitor | Securely enter payment information        | Checkout safely and securely                                        | [Evidence](media/checkout-evidence.png )  |
| 19 | Site Visitor | View confirmation of a successful order   | Confirm I ordered correctly                                         | [Evidence](media/checkout-success-evidence.png )  |
| 20 | Site Visitor | Receive a confirmation email              | Confirm I ordered correctly and keep a record of them               | [Evidence](media/checkout-email-confirmation.png )  |
| Profile / Product Management |   |   |   |
| 21 | Site Visitor | Add a product                             | Add new products as they come in                                    | [Evidence](media/add-product-evidence.png )  |
| 22 | Site Visitor | Edit a product                            | Update/change product details                                       | [Evidence](media/edit-product-evidence.png )  |
| 23 | Site Visitor | Delete a product                          | Remove products that are no longer available                        | [Evidence](media/delete-product-evidence.png )  |

# Validation Testing

## [HTML Validation](https://validator.w3.org/nu/)

Using my deployed Heroku App, I ran each url of the website through the HTML validator and corrected the following:

- &copy copyright change to &169
- orphan element tags were closed off

## [CSS Validation](https://jigsaw.w3.org/css-validator/)

CSS was directly input to the CSS Validator from each static folder in the app and no errors were found.

## [JS Hint](https://jigsaw.w3.org/css-validator/)

JS Hint was used to validate javascript code and the following errors were corrected:

- missing semi-colons were added



https://pep8ci.herokuapp.com/